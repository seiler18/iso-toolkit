#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
iso_sgi.py — generador de sistemas de gestion ISO.

Levanta la estructura de un SGI (una o varias normas), la lista maestra de
informacion documentada, listas de verificacion y el esqueleto de la
Declaracion de Aplicabilidad de 27001.

Solo biblioteca estandar. Probado en Python 3.10+.

    python iso_sgi.py listar
    python iso_sgi.py listar --norma 27001
    python iso_sgi.py estructura --normas 9001,27001 --org "Mi Empresa" --salida ./SGI
    python iso_sgi.py checklist --normas 45001 --salida ./checklist.csv
    python iso_sgi.py soa --salida ./soa_borrador.csv
    python iso_sgi.py correspondencia --normas 9001,27001 --formato csv
    python iso_sgi.py instalar-skills --destino ../../.claude/skills

AVISO LEGAL
    Este script NO reproduce el texto de ninguna norma ISO. Trabaja con
    identificadores de clausula, titulos en redaccion propia y descripciones
    originales de que debe demostrar la organizacion. Para implementar
    necesitas la norma oficial, adquirida legalmente (INN en Chile,
    ISO Store fuera). Ver ../DISCLAIMER.md

Autor: Jesus Seiler — Licencia: CC BY-SA 4.0
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ_TOOLKIT = AQUI.parent
DATOS = RAIZ_TOOLKIT / "datos" / "catalogo_normas.json"
SKILLS = RAIZ_TOOLKIT / "skills"

# Prefijo numerico y codigo de carpeta por norma
CARPETAS_NORMA = {
    "9001":    ("10", "CALIDAD",     "CAL"),
    "14001":   ("20", "AMBIENTAL",   "AMB"),
    "45001":   ("30", "SST",         "SST"),
    "27001":   ("40", "SEGURIDAD",   "SEG"),
    "22301":   ("50", "CONTINUIDAD", "CON"),
    "20000-1": ("60", "SERVICIOS",   "SER"),
}

# Documentos base del tronco comun, en orden de dependencia.
# (codigo, nombre, subcarpeta, clausulas_genericas, que_debe_contener)
DOCS_TRONCO = [
    ("COM-PR-001", "Procedimiento de control de la informacion documentada", "7_APOYO", "7.5",
     ["Creacion y codificacion de documentos (plantilla y nomenclatura)",
      "Revision y aprobacion: quien y como consta",
      "Distribucion y ubicacion unica de la version vigente",
      "Control de cambios y numeracion de versiones",
      "Tratamiento de documentos obsoletos",
      "Control de documentos de origen externo (leyes, contratos, manuales de proveedor)"]),
    ("COM-D-001", "Analisis de contexto (FODA / PESTEL)", "4_CONTEXTO", "4.1",
     ["Cuestiones internas: recursos, competencias, cultura, tecnologia, desempeno",
      "Cuestiones externas: legal, tecnologico, competitivo, de mercado, social",
      "Para 14001: condiciones ambientales que afectan o son afectadas por la organizacion",
      "Para 22301: apetito de riesgo de la organizacion",
      "Conclusiones: que de aqui alimenta riesgos, alcance y objetivos"]),
    ("COM-M-001", "Matriz de partes interesadas y sus requisitos", "4_CONTEXTO", "4.2",
     ["Parte interesada / tipo (interna o externa)",
      "Necesidades y expectativas",
      "Cuales se convierten en requisitos legales u otros requisitos",
      "Columna por norma aplicable",
      "Para 45001: los trabajadores son parte interesada obligatoria"]),
    ("COM-D-002", "Alcance del sistema de gestion", "4_CONTEXTO", "4.3",
     ["Procesos, actividades, productos y servicios incluidos",
      "Sedes y ubicaciones fisicas",
      "Exclusiones y su justificacion",
      "Limites organizacionales y de interfaz con terceros",
      "Disponible como informacion documentada para las partes interesadas"]),
    ("COM-D-003", "Mapa de procesos y fichas de proceso", "4_CONTEXTO", "4.4",
     ["Procesos estrategicos, operativos y de apoyo",
      "Secuencia e interaccion entre procesos",
      "Por proceso: dueno, entradas, salidas, indicadores, riesgos, recursos",
      "Criterios y metodos para asegurar operacion y control eficaces"]),
    ("COM-P-001", "Politica integrada de gestion", "5_LIDERAZGO", "5.2",
     ["Declaracion de proposito de la organizacion",
      "Compromisos comunes: cumplir requisitos legales y mejorar continuamente",
      "Un compromiso explicito por cada dimension del alcance",
      "Marco para establecer los objetivos",
      "Aprobacion de la alta direccion: nombre, cargo, firma y fecha",
      "Como se comunica y donde esta disponible",
      "!Cabe en una pagina. Si pasa de dos, es un manual disfrazado."]),
    ("COM-D-004", "Organigrama y matriz RACI", "5_LIDERAZGO", "5.3",
     ["Estructura organizacional vigente",
      "Responsabilidades y autoridades por rol dentro del sistema",
      "Matriz RACI por proceso: responsable, aprobador, consultado, informado",
      "Quien reporta el desempeno del sistema a la alta direccion"]),
    ("COM-PR-002", "Metodologia de apreciacion de riesgos y oportunidades", "6_PLANIFICACION", "6.1",
     ["Escala de probabilidad 1-5 con definicion verbal de cada nivel",
      "Escala de impacto 1-5 con criterios por dimension (economico, legal, personas, ambiente, informacion, servicio, reputacion)",
      "Formula del nivel de riesgo y bandas",
      "Criterios de aceptacion aprobados por la direccion",
      "Opciones de tratamiento: evitar, reducir, compartir, aceptar",
      "Roles: quien identifica, quien valora, quien acepta el riesgo residual",
      "Frecuencia de revision",
      "!UNA metodologia para todo el SGI; las matrices son varias"]),
    ("COM-M-002", "Riesgos y oportunidades del sistema de gestion", "6_PLANIFICACION", "6.1.1",
     ["Derivados del contexto (4.1) y las partes interesadas (4.2)",
      "Cada debilidad y amenaza del FODA es un riesgo candidato",
      "Cada fortaleza y oportunidad es una oportunidad candidata",
      "Accion, responsable, plazo y evaluacion de eficacia",
      "!NO confundir con las matrices tecnicas de 6.1.2"]),
    ("COM-D-005", "Cuadro de objetivos y planificacion para lograrlos", "6_PLANIFICACION", "6.2",
     ["Objetivo medible, coherente con la politica",
      "Columna 'norma' para filtrar en sistemas integrados",
      "Que se hara, con que recursos, quien, cuando, como se evalua",
      "Linea base y meta",
      "Seguimiento periodico con evidencia"]),
    ("COM-PR-003", "Procedimiento de gestion del cambio", "6_PLANIFICACION", "6.3",
     ["Que se considera un cambio significativo",
      "Evaluacion previa de consecuencias por dimension",
      "Integridad del sistema durante el cambio",
      "Recursos y asignacion de responsabilidades",
      "!OJO: en 20000-1 la 6.3 es 'Planificacion del SGS', no gestion del cambio. En 45001 la gestion del cambio esta en 8.1.3"]),
    ("COM-M-003", "Matriz de competencias y plan de formacion", "7_APOYO", "7.2 / 7.3",
     ["Competencia requerida por cargo o rol del sistema",
      "Competencia actual y brecha",
      "Plan de formacion con fechas y responsables",
      "Evidencia de competencia: certificados, evaluaciones, experiencia acreditada",
      "Plan de toma de conciencia: politica, objetivos, contribucion, consecuencias del incumplimiento"]),
    ("COM-M-004", "Matriz de comunicaciones", "7_APOYO", "7.4",
     ["Que se comunica, a quien, cuando, como y quien comunica",
      "Comunicaciones internas y externas por separado",
      "Como se conserva la evidencia de la comunicacion",
      "Para 45001: canales de consulta y participacion de los trabajadores"]),
    ("COM-D-006", "Lista maestra de informacion documentada", "7_APOYO", "7.5",
     ["Una fila por documento y registro del sistema",
      "Codigo, nombre, tipo, version, fecha, responsable, ubicacion, retencion, estado",
      "Columna 'clausulas que cubre' con las normas aplicables",
      "!Es el indice del sistema y lo primero que pide el auditor. Se genera y mantiene con `iso_sgi.py`"]),
    ("COM-D-007", "Tablero de indicadores", "9_EVALUACION", "9.1",
     ["Indicador, formula, fuente del dato, frecuencia, responsable",
      "Linea base, meta y umbral de alerta",
      "Vinculo con el objetivo y con la norma",
      "Analisis y evaluacion de resultados, no solo el numero"]),
    ("COM-PR-004", "Procedimiento y programa anual de auditoria interna", "9_EVALUACION", "9.2",
     ["Criterios de seleccion y perfil de competencia de los auditores",
      "Regla de imparcialidad: nadie audita su propio trabajo",
      "Programa anual que cubra TODAS las clausulas y procesos del alcance",
      "!En sistemas integrados: auditar por proceso, no por norma",
      "Plan de auditoria, listas de verificacion, informe y seguimiento",
      "El informe debe concluir sobre la eficacia del sistema"]),
    ("COM-PR-005", "Procedimiento de revision por la direccion", "9_EVALUACION", "9.3",
     ["Periodicidad y participantes (la alta direccion, no delegados)",
      "Las 12 entradas comunes + las especificas de cada norma del alcance",
      "Salidas obligatorias: oportunidades de mejora, cambios al sistema, necesidades de recursos",
      "Conclusion explicita sobre conveniencia, adecuacion y eficacia continua",
      "Una sola acta para todas las normas",
      "Seguimiento de las decisiones de la revision anterior"]),
    ("COM-PR-006", "Procedimiento de no conformidades, acciones correctivas y mejora", "10_MEJORA", "10",
     ["Distincion explicita entre correccion y accion correctiva",
      "Metodos de analisis de causa raiz y cuando usar cada uno",
      "Criterio y plazo de verificacion de eficacia",
      "Evaluar si la misma NC existe en otras areas",
      "Actualizar riesgos y documentacion cuando corresponda",
      "!OJO con la numeracion: NC/AC es 10.2 en 9001/14001/45001/27001, pero 10.1 en 22301/20000-1"]),
    ("COM-R-001", "Registro unico de NC / AC / OM", "10_MEJORA", "10",
     ["UN registro para todas las normas, con columna 'norma'",
      "Id, fecha, origen, clausulas, proceso, descripcion, tipo",
      "Correccion, analisis de causa, accion correctiva, responsable, plazo",
      "Verificacion de eficacia con criterio, fecha y evidencia",
      "Estado y fecha de cierre",
      "!Un registro vacio se lee como sistema que no se usa"]),
]

SUBCARPETAS_COMUN = [
    ("4_CONTEXTO",      "FODA, partes interesadas, alcance, mapa de procesos"),
    ("5_LIDERAZGO",     "politica integrada, organigrama, RACI"),
    ("6_PLANIFICACION", "metodologia de riesgos, objetivos, gestion del cambio"),
    ("7_APOYO",         "competencias, concienciacion, comunicacion, control documental"),
    ("9_EVALUACION",    "indicadores, programa de auditoria, revision por la direccion"),
    ("10_MEJORA",       "procedimiento y registro unico de NC/AC/OM"),
]


# --------------------------------------------------------------------------
# utilidades
# --------------------------------------------------------------------------

def cargar_datos() -> dict:
    if not DATOS.exists():
        sys.exit(f"ERROR: no encuentro el catalogo de datos en {DATOS}")
    with DATOS.open(encoding="utf-8") as f:
        return json.load(f)


def resolver_normas(datos: dict, texto: str) -> list[str]:
    disponibles = list(datos["normas"].keys())
    if texto.strip().lower() in ("todas", "all", "*"):
        return disponibles
    pedidas = [n.strip() for n in texto.split(",") if n.strip()]
    malas = [n for n in pedidas if n not in disponibles]
    if malas:
        sys.exit(f"ERROR: norma(s) desconocida(s): {', '.join(malas)}\n"
                 f"       disponibles: {', '.join(disponibles)}")
    return pedidas


def escribir_csv(ruta: Path, cabecera: list[str], filas: list[list]) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    # utf-8-sig para que Excel en Windows respete los acentos
    with ruta.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(cabecera)
        w.writerows(filas)


def escribir_texto(ruta: Path, contenido: str) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(contenido, encoding="utf-8")


_PROHIBIDOS = '<>:"/\\|?*'


def slug(texto: str, largo: int = 60) -> str:
    """Convierte un titulo en un nombre de archivo/carpeta valido en Windows."""
    limpio = "".join(" " if ch in _PROHIBIDOS else ch for ch in texto)
    limpio = "_".join(limpio.split())          # colapsa espacios -> _
    limpio = limpio.strip("._")
    return limpio[:largo].rstrip("._") or "sin_nombre"


# --------------------------------------------------------------------------
# comando: listar
# --------------------------------------------------------------------------

def cmd_listar(args, datos: dict) -> None:
    if not args.norma:
        print("\nNormas disponibles en el catalogo:\n")
        for clave, n in datos["normas"].items():
            print(f"  {clave:<9} {n['designacion']:<24} {n['dominio']:<32} "
                  f"({len(n['clausulas'])} clausulas, {len(n['info_documentada'])} doc. obligatorios)")
        print(f"\n  Anexo A de 27001: {len(datos['anexo_a_27001']['controles'])} controles")
        print(f"\n  Trampas de numeracion documentadas: {len(datos['trampas_de_numeracion'])}")
        print("  Ver detalle con:  python iso_sgi.py listar --trampas\n")
        return

    n = datos["normas"].get(args.norma)
    if not n:
        sys.exit(f"ERROR: norma desconocida '{args.norma}'")

    print(f"\n{n['designacion']} — {n['dominio']}  ({n['sigla_sistema']})")
    if n.get("nota_verificacion"):
        print(f"\n  AVISO: {n['nota_verificacion']}")
    print("\n  CLAUSULAS")
    for c in n["clausulas"]:
        marca = {"comun": "[=]", "parcial": "[~]", "propio": "[!]"}[c["tronco"]]
        print(f"    {marca} {c['num']:<7} {c['titulo']}")
        if c.get("nota"):
            print(f"            -> {c['nota']}")
    print("\n    [=] tronco comun   [~] parcialmente integrable   [!] propio de la norma")

    print("\n  INFORMACION DOCUMENTADA OBLIGATORIA")
    for d in n["info_documentada"]:
        est = " *" if d.get("estrella") else "  "
        cond = f"  (condicional: {d['condicional']})" if d.get("condicional") else ""
        print(f"   {est} {d['clausula']:<12} [{d['tipo']:<3}] {d['que']}{cond}")
    print()


def cmd_trampas(datos: dict) -> None:
    print("\nTRAMPAS DE NUMERACION ENTRE NORMAS\n" + "=" * 60)
    for t in datos["trampas_de_numeracion"]:
        print(f"\n{t['tema']}")
        for norma, val in t["detalle"].items():
            if isinstance(val, dict):
                partes = " | ".join(f"{k} {v}" for k, v in val.items())
                print(f"   {norma:<14} {partes}")
            else:
                print(f"   {norma:<14} {val}")
        if t.get("por_que_importa"):
            print(f"   >> {t['por_que_importa']}")
    print()


# --------------------------------------------------------------------------
# comando: estructura
# --------------------------------------------------------------------------

def stub_documento(codigo: str, nombre: str, org: str, clausulas: str,
                   contenido: list[str], hoy: str) -> str:
    # las entradas con "!" al inicio son notas de criterio, no apartados a llenar
    bloques, i = [], 0
    for c in contenido:
        if c.startswith("!"):
            bloques.append(f"> **Nota:** {c[1:].strip()}\n")
        else:
            i += 1
            bloques.append(f"{i}. **{c}**\n\n   _(completar)_\n")
    puntos = "\n".join(bloques)
    return f"""# {nombre}

| | |
|---|---|
| **Codigo** | `{codigo}` |
| **Organizacion** | {org} |
| **Version** | v0 (borrador) |
| **Fecha** | {hoy} |
| **Clausulas que cubre** | {clausulas} |
| **Responsable** | _(definir)_ |
| **Aprobado por** | _(definir)_ |
| **Estado** | En elaboracion |

> Documento generado como esqueleto por `iso_sgi.py`. **Hay que adaptarlo al
> contexto real de la organizacion**: un documento generico que describe una
> empresa que no es esta se detecta en dos minutos de auditoria.

---

## Que debe contener

{puntos}
---

## Control de cambios

| Version | Fecha | Descripcion del cambio | Autor |
|---|---|---|---|
| v0 | {hoy} | Creacion del esqueleto | iso_sgi.py |
"""


def cmd_estructura(args, datos: dict) -> None:
    normas = resolver_normas(datos, args.normas)
    org = args.org
    hoy = date.today().isoformat()
    raiz = Path(args.salida).resolve()

    if raiz.exists() and any(raiz.iterdir()) and not args.forzar:
        sys.exit(f"ERROR: {raiz} ya existe y no esta vacia. Usa --forzar para escribir igual.")

    # etiqueta de clausulas comunes segun las normas del alcance
    etiqueta_comun = " / ".join(normas)

    creadas: list[Path] = []
    lista_maestra: list[list] = []

    # --- tronco comun ---
    for sub, desc in SUBCARPETAS_COMUN:
        d = raiz / "00_COMUN" / sub
        d.mkdir(parents=True, exist_ok=True)
        escribir_texto(d / "_LEEME.md", f"# {sub}\n\n{desc}\n\nTronco comun: sirve a {etiqueta_comun}.\n")
        creadas.append(d)

    for codigo, nombre, sub, clausulas, contenido in DOCS_TRONCO:
        destino = raiz / "00_COMUN" / sub / f"{codigo}_{slug(nombre)}.md"
        cobertura = " · ".join(f"{n} {clausulas}" for n in normas)
        escribir_texto(destino, stub_documento(codigo, nombre, org, cobertura, contenido, hoy))
        lista_maestra.append([
            codigo, nombre, "D" if "-R-" not in codigo else "R", cobertura,
            "(definir)", "v0", hoy, str(destino.relative_to(raiz)).replace("\\", "/"),
            "(definir)", "En elaboracion",
        ])

    # --- ramas por norma ---
    for clave in normas:
        prefijo, etiqueta, cod = CARPETAS_NORMA[clave]
        base = raiz / f"{prefijo}_{etiqueta}_{clave.replace('-', '_')}"
        base.mkdir(parents=True, exist_ok=True)

        n = datos["normas"][clave]
        propias = [c for c in n["clausulas"] if c["tronco"] == "propio"]
        lineas = [f"# {n['designacion']} — {n['dominio']}", "",
                  f"Carpeta de lo **propio** de esta norma. El tronco comun vive en `00_COMUN/`.", ""]
        if n.get("nota_verificacion"):
            lineas += [f"> AVISO: {n['nota_verificacion']}", ""]
        lineas += ["## Clausulas propias de esta norma", ""]
        for c in propias:
            d = base / f"{c['num'].replace('.', '_')}_{slug(c['titulo'], 45)}"
            d.mkdir(parents=True, exist_ok=True)
            creadas.append(d)
            lineas.append(f"- **{c['num']}** {c['titulo']}")
            if c.get("nota"):
                lineas.append(f"  - {c['nota']}")
            for s in c.get("sub", []):
                lineas.append(f"  - {s}")
        lineas += ["", "## Informacion documentada obligatoria de esta norma", "",
                   "| Clausula | Que hay que demostrar | Tipo |", "|---|---|---|"]
        for d_ in n["info_documentada"]:
            cond = f" _(condicional: {d_['condicional']})_" if d_.get("condicional") else ""
            estrella = "* " if d_.get("estrella") else ""
            lineas.append(f"| {d_['clausula']} | {estrella}{d_['que']}{cond} | {d_['tipo']} |")
            lista_maestra.append([
                f"{cod}-?-???", d_["que"][:80], d_["tipo"], f"{clave} {d_['clausula']}",
                "(definir)", "-", "-", str(base.relative_to(raiz)).replace("\\", "/"),
                "(definir)", "Pendiente",
            ])
        escribir_texto(base / "_LEEME.md", "\n".join(lineas) + "\n")

    # --- registros y obsoletos ---
    anio = date.today().year
    reg = raiz / "90_REGISTROS" / str(anio)
    for sub, _ in SUBCARPETAS_COMUN:
        (reg / sub).mkdir(parents=True, exist_ok=True)
    escribir_texto(reg / "_LEEME.md",
                   f"# Registros {anio}\n\nLa evidencia viva del sistema, ordenada por clausula.\n\n"
                   "Si la carpeta existe, la gente guarda aqui. Si no existe, la evidencia\n"
                   "termina en correos y carpetas personales y a los seis meses no hay forma\n"
                   "de reconstruirla.\n")
    obs = raiz / "99_OBSOLETOS"
    obs.mkdir(parents=True, exist_ok=True)
    escribir_texto(obs / "_LEEME.md",
                   "# Obsoletos\n\nVersiones retiradas, conservadas e **identificadas como obsoletas**.\n\n"
                   "La clausula 7.5.3 exige prevenir el uso no intencionado de documentos obsoletos.\n"
                   "Borrarlos es peor que archivarlos marcados: te quedas sin trazabilidad de por que\n"
                   "cambio algo.\n")

    # --- lista maestra ---
    escribir_csv(raiz / "00_LISTA_MAESTRA.csv",
                 ["codigo", "nombre", "tipo", "clausulas_que_cubre", "responsable",
                  "version", "fecha", "ubicacion", "retencion", "estado"],
                 lista_maestra)

    # --- README raiz ---
    escribir_texto(raiz / "README.md", f"""# Sistema de Gestion — {org}

Generado el {hoy} con `iso_sgi.py`.

**Normas del alcance:** {', '.join(datos['normas'][n]['designacion'] for n in normas)}

## Como esta organizado

- `00_COMUN/` — el tronco. Un solo juego de documentos que sirve a **todas** las normas.
- `{'`, `'.join(f"{CARPETAS_NORMA[n][0]}_{CARPETAS_NORMA[n][1]}_{n.replace('-', '_')}/" for n in normas)}` — lo propio de cada norma (clausula 8 y parches).
- `90_REGISTROS/{anio}/` — la evidencia viva.
- `99_OBSOLETOS/` — versiones retiradas, identificadas.
- `00_LISTA_MAESTRA.csv` — el indice del sistema. **Mantenlo actualizado**: es lo primero que pide el auditor.

## Que hacer ahora

1. Completar `COM-PR-001` (control documental) — define el formato de todo lo demas.
2. Completar en orden `COM-D-001` -> `COM-M-001` -> `COM-D-002` (alcance) -> `COM-D-003`.
   El alcance es el cuello de botella: todo lo posterior depende de el.
3. Escribir la politica integrada `COM-P-001`.
4. Metodologia de riesgos `COM-PR-002` y las matrices por norma.
5. Ir marcando el estado en la lista maestra.

Ver el metodo completo en `skills/iso-levantar-sgi/SKILL.md`.

## Aviso

Los documentos son **esqueletos genericos**. Adaptarlos al contexto real de la
organizacion no es opcional. Este material no reproduce el texto de las normas
y no sustituye su adquisicion legal.
""")

    print(f"\nOK — estructura creada en: {raiz}")
    print(f"   normas .............. {', '.join(normas)}")
    print(f"   documentos base ..... {len(DOCS_TRONCO)} esqueletos en 00_COMUN/")
    print(f"   lista maestra ....... {len(lista_maestra)} filas -> 00_LISTA_MAESTRA.csv")
    print(f"   carpetas creadas .... {sum(1 for _ in raiz.rglob('*') if _.is_dir())}")
    print("\n   Siguiente paso: completar COM-PR-001 y despues el alcance (COM-D-002).\n")


# --------------------------------------------------------------------------
# comando: checklist
# --------------------------------------------------------------------------

def cmd_checklist(args, datos: dict) -> None:
    normas = resolver_normas(datos, args.normas)
    salida = Path(args.salida).resolve()

    filas = []
    vistas_comun = set()
    for clave in normas:
        n = datos["normas"][clave]
        for c in n["clausulas"]:
            # el tronco comun se evalua una sola vez para todo el alcance
            if c["tronco"] == "comun" and len(normas) > 1:
                sk = (c["num"], c["titulo"])
                if sk in vistas_comun:
                    continue
                vistas_comun.add(sk)
                ambito = "TRONCO COMUN"
                norma_col = " / ".join(normas)
            else:
                ambito = {"comun": "Tronco comun", "parcial": "Parcial", "propio": "Propio"}[c["tronco"]]
                norma_col = clave
            filas.append([
                ambito, norma_col, c["num"], c["titulo"],
                c.get("nota", ""),
                "", "", "", "",   # estado / evidencia / brecha / responsable
            ])

    # las obligaciones de informacion documentada, aparte
    for clave in normas:
        for d in datos["normas"][clave]["info_documentada"]:
            filas.append([
                "INFO DOCUMENTADA", clave, d["clausula"], d["que"],
                d.get("condicional", ""), "", "", "", "",
            ])

    escribir_csv(salida,
                 ["ambito", "norma", "clausula", "requisito", "nota",
                  "estado", "evidencia_encontrada", "brecha", "responsable"],
                 filas)

    print(f"\nOK — lista de verificacion: {salida}")
    print(f"   normas .... {', '.join(normas)}")
    print(f"   filas ..... {len(filas)}")
    print("\n   Estados sugeridos: Conforme / Parcial / Ausente / No aplica")
    print("   Metodo completo en skills/iso-diagnostico-brechas/SKILL.md\n")


# --------------------------------------------------------------------------
# comando: soa
# --------------------------------------------------------------------------

TEMAS_SOA = {"5": "Organizacional", "6": "Personas", "7": "Fisico", "8": "Tecnologico"}


def cmd_soa(args, datos: dict) -> None:
    salida = Path(args.salida).resolve()
    controles = datos["anexo_a_27001"]["controles"]

    filas = []
    for c in controles:
        tema = TEMAS_SOA[c["id"].split(".")[1]]
        filas.append([
            c["id"], tema, c["titulo"],
            "Si" if c.get("nuevo_2022") else "",
            "", "", "", "", "", "", "",
        ])

    escribir_csv(salida,
                 ["id", "tema", "control", "nuevo_2022", "aplica",
                  "justificacion", "origen", "riesgos_asociados", "estado",
                  "evidencia", "responsable"],
                 filas)

    nuevos = sum(1 for c in controles if c.get("nuevo_2022"))
    print(f"\nOK — esqueleto de Declaracion de Aplicabilidad: {salida}")
    print(f"   controles ......... {len(controles)}")
    print(f"   nuevos de 2022 .... {nuevos}  (los que mas brechas generan)")
    print("\n   origen:  Riesgo / Legal / Contractual / Buena practica")
    print("   estado:  Implementado / Parcial / Planificado / No implementado")
    print("\n   AVISO: haz primero la matriz de riesgos. Una SoA sin riesgos detras")
    print("          es exactamente el hallazgo que busca el auditor.")
    print("   Metodo completo en skills/iso-declaracion-aplicabilidad/SKILL.md\n")


# --------------------------------------------------------------------------
# comando: correspondencia
# --------------------------------------------------------------------------

GRUPOS_ANEXO_SL = {
    "4": "4 · Contexto de la organización",
    "5": "5 · Liderazgo",
    "6": "6 · Planificación",
    "7": "7 · Apoyo",
    "8": "8 · Operación",
    "9": "9 · Evaluación del desempeño",
    "10": "10 · Mejora",
}
MARCA_INTEGRA = {"si": "✅ Sí", "parcial": "⚠️ Parcial", "no": "⛔ No"}

# El .md publicado en mapeo_integrado/ sale de aqui. Si se edita a mano, la
# proxima regeneracion lo pisa: los cambios van en el catalogo o en este texto.
CABECERA_MD = """# Correspondencia por subapartado — 6 normas

**Normas:** {designaciones}

> **Para qué sirve:** dado un tema (las partes interesadas, los proveedores, los incidentes…), dice en qué cláusula o control lo trata cada norma. Sirve para armar un sistema integrado sin duplicar documentos y para citar bien en un informe de auditoría.
>
> ⚠️ Material orientativo de autoría propia. **No reproduce el texto de las normas**: solo da referencias. Para implementar necesitas la norma oficial, adquirida legalmente (en Chile, al [INN](https://www.inn.cl)). Lee el [DISCLAIMER](../DISCLAIMER.md).

**Cómo leerla.** Cada celda es la referencia donde la norma trata ese tema; `—` significa que no tiene un apartado para eso. Las referencias `A.x.x` son controles del Anexo A de 27001. La última columna dice si se documenta una sola vez (✅), en un documento con secciones o criterios por norma (⚠️) o por separado (⛔).

La explicación de por qué se integra cada cosa está en el [mapa Anexo SL](00_mapa_anexo_sl.md). Esta tabla es la consulta rápida.

"""

PIE_MD = """---

**Verificación.** {verificacion}

*Generado con `python scripts/iso_sgi.py correspondencia` a partir de [`datos/catalogo_normas.json`](../datos/catalogo_normas.json): las correcciones van en el catálogo, no en este archivo.*
*Autoría: Jesús Seiler — auditor interno en las seis normas listadas. Material original, no afiliado a ISO ni al INN. Licencia: CC BY-SA 4.0*
"""


def cmd_correspondencia(args, datos: dict) -> None:
    normas = resolver_normas(datos, args.normas)
    bloque = datos["correspondencia"]
    # una fila sin referencia en ninguna de las normas pedidas no aporta nada
    filas = [f for f in bloque["filas"] if any(f["normas"].get(n) for n in normas)]
    salida = Path(args.salida or f"./correspondencia.{args.formato}").resolve()

    if args.formato == "csv":
        escribir_csv(salida,
                     ["grupo", "tema", *normas, "integra", "nota"],
                     [[f["grupo"], f["tema"], *(f["normas"].get(n, "") for n in normas),
                       f["integra"], f.get("nota", "")] for f in filas])
    else:
        designaciones = " · ".join(datos["normas"][n]["designacion"] for n in normas)
        partes = [CABECERA_MD.format(designaciones=designaciones)]
        for grupo, titulo in GRUPOS_ANEXO_SL.items():
            del_grupo = [f for f in filas if f["grupo"] == grupo]
            if not del_grupo:
                continue
            partes.append(f"## {titulo}\n\n")
            partes.append("| Tema | " + " | ".join(normas) + " | ¿Una vez? |\n")
            partes.append("|---|" + "---|" * len(normas) + "---|\n")
            for f in del_grupo:
                celdas = [f["normas"].get(n) or "—" for n in normas]
                partes.append(f"| {f['tema']} | " + " | ".join(celdas)
                              + f" | {MARCA_INTEGRA[f['integra']]} |\n")
            notas = [f for f in del_grupo if f.get("nota")]
            if notas:
                partes.append("\n" + "".join(f"- **{f['tema']}.** {f['nota']}\n" for f in notas))
            partes.append("\n")
        partes.append(PIE_MD.format(verificacion=bloque["verificacion"]))
        escribir_texto(salida, "".join(partes))

    print(f"\nOK — correspondencia por subapartado: {salida}")
    print(f"   normas .... {', '.join(normas)}")
    print(f"   temas ..... {len(filas)}\n")


# --------------------------------------------------------------------------
# comando: instalar-skills
# --------------------------------------------------------------------------

def cmd_instalar_skills(args) -> None:
    destino = Path(args.destino).resolve()
    if not SKILLS.exists():
        sys.exit(f"ERROR: no encuentro las skills en {SKILLS}")

    destino.mkdir(parents=True, exist_ok=True)
    n = 0
    for d in sorted(SKILLS.iterdir()):
        if not d.is_dir() or not (d / "SKILL.md").exists():
            continue
        dst = destino / d.name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(d, dst)
        print(f"   + {d.name}")
        n += 1

    print(f"\nOK — {n} skills instaladas en {destino}")
    print("   Reinicia Claude Code para que las cargue.\n")


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main() -> None:
    p = argparse.ArgumentParser(
        prog="iso_sgi.py",
        description="Generador de sistemas de gestion ISO. No reproduce el texto de las normas.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("AVISO LEGAL")[0].split('"""')[-1],
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    q = sub.add_parser("listar", help="lista normas, clausulas y trampas de numeracion")
    q.add_argument("--norma", help="detalle de una norma (ej. 27001)")
    q.add_argument("--trampas", action="store_true", help="muestra las trampas de numeracion entre normas")

    e = sub.add_parser("estructura", help="genera el arbol del SGI, los documentos base y la lista maestra")
    e.add_argument("--normas", required=True, help="separadas por coma, o 'todas' (ej. 9001,27001)")
    e.add_argument("--org", required=True, help="nombre de la organizacion")
    e.add_argument("--salida", default="./SGI", help="carpeta destino (por defecto ./SGI)")
    e.add_argument("--forzar", action="store_true", help="escribir aunque la carpeta no este vacia")

    c = sub.add_parser("checklist", help="genera la lista de verificacion para diagnostico o auditoria")
    c.add_argument("--normas", required=True, help="separadas por coma, o 'todas'")
    c.add_argument("--salida", default="./checklist.csv")

    s = sub.add_parser("soa", help="genera el esqueleto de la Declaracion de Aplicabilidad (27001)")
    s.add_argument("--salida", default="./soa_borrador.csv")

    r = sub.add_parser("correspondencia", help="tabla de en que clausula trata cada norma cada tema")
    r.add_argument("--normas", default="todas", help="separadas por coma, o 'todas' (por defecto)")
    r.add_argument("--formato", choices=["md", "csv"], default="md")
    r.add_argument("--salida", help="por defecto ./correspondencia.md o .csv, segun --formato")

    i = sub.add_parser("instalar-skills", help="copia las skills a un directorio .claude/skills")
    i.add_argument("--destino", required=True, help="ruta a .claude/skills")

    args = p.parse_args()

    if args.cmd == "instalar-skills":
        cmd_instalar_skills(args)
        return

    datos = cargar_datos()
    if args.cmd == "listar":
        cmd_trampas(datos) if args.trampas else cmd_listar(args, datos)
    elif args.cmd == "estructura":
        cmd_estructura(args, datos)
    elif args.cmd == "checklist":
        cmd_checklist(args, datos)
    elif args.cmd == "soa":
        cmd_soa(args, datos)
    elif args.cmd == "correspondencia":
        cmd_correspondencia(args, datos)


if __name__ == "__main__":
    main()
