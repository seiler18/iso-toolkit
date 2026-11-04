---
name: iso-levantar-sgi
description: Levanta desde cero la arquitectura de un sistema de gestión (una o varias normas) - estructura de carpetas, lista maestra de información documentada, control documental y los documentos base. Es el paso siguiente al diagnóstico de brechas.
normas: [9001, 14001, 45001, 27001, 22301, 20000-1]
entrega: Árbol de carpetas + lista maestra (CSV) + documentos base en Markdown
---

# Levantar un SGI desde cero

> Esta es la skill que el script [`../scripts/iso_sgi.py`](../scripts/iso_sgi.py) automatiza. La skill explica **el criterio**; el script hace **el trabajo mecánico**. Ejecuta el script y después aplica el criterio de aquí para llenarlo.

## 1. Cuándo usar esta skill

Después del diagnóstico, cuando la organización decide implementar. También sirve para **reordenar** un sistema existente que creció sin arquitectura — el síntoma clásico son seis carpetas paralelas, una por norma, con la misma política repetida seis veces y desincronizada.

**Cuándo NO usarla:** si la organización ya tiene un sistema certificado que funciona. Reorganizar la estructura documental de un sistema vivo, sin una razón fuerte, rompe referencias cruzadas y genera no conformidades de control documental. Se hace solo con un plan de migración y actualizando la lista maestra en el mismo movimiento.

---

## 2. Qué necesitas antes de empezar

| Entrada | Obligatoria |
|---|---|
| Normas objetivo y edición | ✅ |
| Alcance del sistema (procesos, sedes, servicios) | ✅ |
| Mapa de procesos, aunque sea un borrador en pizarra | ✅ |
| Organigrama | ✅ |
| Nombre y dominio de la organización (para los encabezados) | ✅ |
| Diagnóstico de brechas | recomendado |
| Documentación existente reutilizable | recomendado |

---

## 3. El método

### Paso 1 — Decidir la arquitectura: tronco + ramas

El principio único del que sale todo lo demás:

> **Todo lo que no dependa de la disciplina específica se documenta UNA vez.**

Según `datos/catalogo_normas.json`, entre el 60 % y el 70 % de las cláusulas de cualquiera de estas seis normas son tronco común. Lo que se ramifica es la cláusula 8 y un puñado de parches.

```
SGI/
├── 00_COMUN/                 ← el tronco. Sirve a TODAS las normas del alcance.
│   ├── 4_CONTEXTO/           FODA · partes interesadas · alcance · mapa de procesos
│   ├── 5_LIDERAZGO/          política integrada · organigrama · RACI
│   ├── 6_PLANIFICACION/      metodología de riesgos · objetivos · gestión del cambio
│   ├── 7_APOYO/              competencias · concienciación · comunicación · control documental
│   ├── 9_EVALUACION/         indicadores · programa de auditoría · revisión por la dirección
│   └── 10_MEJORA/            procedimiento y registro único de NC/AC/OM
│
├── 10_CALIDAD_9001/          ← cláusula 8 + parches propios
├── 20_AMBIENTAL_14001/
├── 30_SST_45001/
├── 40_SEGURIDAD_27001/       (SoA + los 93 controles)
├── 50_CONTINUIDAD_22301/     (BIA + estrategias + planes + ejercicios)
├── 60_SERVICIOS_20000-1/
│
├── 90_REGISTROS/             ← evidencia viva, ordenada por año
│   └── AAAA/
└── 99_OBSOLETOS/             ← versiones retiradas, conservadas y marcadas
```

**Por qué numerado:** fuerza el orden en cualquier explorador, hace las rutas estables aunque cambie el nombre, y el auditor encuentra las cosas solo. Crea únicamente las carpetas de las normas del alcance; carpetas vacías con nombre de norma inducen a error.

**`99_OBSOLETOS/` no es opcional.** La 7.5.3 exige prevenir el uso no intencionado de documentos obsoletos. Borrarlos es peor que archivarlos marcados: te quedas sin trazabilidad de por qué cambió algo.

### Paso 2 — Construir la lista maestra ANTES que los documentos

Este es el paso que casi todos se saltan y es el que ordena el proyecto entero. La lista maestra es una sola planilla con una fila por documento:

| Campo | Ejemplo |
|---|---|
| Código | `COM-P-001` |
| Nombre | Política Integrada de Gestión |
| Tipo | D (documento) / R (registro) |
| Cláusulas que cubre | `9001 5.2 · 14001 5.2 · 45001 5.2 · 27001 5.2 · 22301 5.2 · 20000-1 5.2` |
| Responsable | Gerencia General |
| Versión / fecha | v1 · 2026-08-16 |
| Ubicación | `00_COMUN/5_LIDERAZGO/` |
| Retención | Permanente |
| Estado | Vigente / En elaboración / Obsoleto |

La columna **"cláusulas que cubre"** es la que hace todo el trabajo:
- Se genera sola desde `catalogo_normas.json`, cruzando la información documentada obligatoria de las normas del alcance.
- Le prueba al auditor que cada requisito tiene dueño.
- Detecta duplicación: dos documentos cubriendo la misma cláusula es una alerta.
- Es la base del informe de brechas siguiente.

Nomenclatura sugerida: `<ÁMBITO>-<TIPO>-<NNN>` donde ámbito ∈ {COM, CAL, AMB, SST, SEG, CON, SER}, tipo ∈ {P política, PR procedimiento, IT instructivo, M matriz, F formato, R registro, PL plan}.

### Paso 3 — Escribir el control documental primero (7.5)

Contraintuitivo pero correcto: **el procedimiento de control documental es el primer documento del sistema**, porque define el formato, la codificación, la aprobación y el control de cambios de todos los demás. Escribirlo al final obliga a reformatear todo.

Debe resolver seis cosas, y solo seis:

1. Cómo se **crea y codifica** un documento (plantilla y nomenclatura).
2. Quién **revisa y aprueba**, y cómo consta.
3. Cómo se **distribuye** y dónde vive la versión vigente (una sola ubicación, sin copias en escritorios).
4. Cómo se **controla el cambio** y se numeran las versiones.
5. Qué pasa con los **obsoletos**.
6. Cómo se controlan los documentos **de origen externo** (normas legales, contratos, manuales de proveedor). Este es el que siempre falta.

> Si el sistema vive en SharePoint/Drive/Confluence, el procedimiento debe describir **esa** realidad, no una gestión de papel con firmas azules. Un procedimiento que describe un proceso que nadie sigue es una no conformidad esperando ocurrir.

### Paso 4 — Documentos base del tronco, en este orden

El orden importa: cada uno alimenta al siguiente.

| # | Documento | Alimenta a |
|---|---|---|
| 1 | Procedimiento de control de la información documentada (7.5) | todo |
| 2 | Análisis de contexto — FODA + PESTEL (4.1) | alcance, riesgos |
| 3 | Matriz de partes interesadas y sus requisitos (4.2) | alcance, riesgos, comunicación |
| 4 | **Alcance del sistema (4.3)** | todo lo demás |
| 5 | Mapa de procesos y fichas de proceso (4.4) | riesgos, indicadores, auditoría |
| 6 | **Política integrada (5.2)** | objetivos |
| 7 | Organigrama + matriz RACI (5.3) | competencias, auditoría |
| 8 | Metodología de riesgos y oportunidades (6.1) | todas las matrices |
| 9 | Cuadro de objetivos y planes (6.2) | indicadores |
| 10 | Matriz de competencias y plan de formación (7.2, 7.3) | evidencia de competencia |
| 11 | Matriz de comunicaciones (7.4) | evidencia |
| 12 | Tablero de indicadores (9.1) | revisión por la dirección |
| 13 | Procedimiento y programa de auditoría interna (9.2) | hallazgos |
| 14 | Procedimiento de revisión por la dirección (9.3) | decisiones |
| 15 | Procedimiento y registro único de NC/AC/OM (10) | mejora |

**El alcance (4) es el cuello de botella.** Todo lo posterior depende de él y es donde la gerencia tiene que decidir de verdad. Si se atasca, el proyecto se atasca.

### Paso 5 — La política integrada: una, no seis

Un solo documento, con un compromiso explícito por cada dimensión del alcance. Estructura que funciona:

```
1. Declaración de propósito (2-3 líneas: a qué se dedica la organización)
2. Compromisos comunes
   - cumplir requisitos legales y otros aplicables
   - mejorar continuamente el sistema
   - satisfacer los requisitos de las partes interesadas
3. Compromisos por dimensión (uno por norma del alcance)
   - Calidad ............ satisfacción del cliente
   - Ambiental .......... protección del medio ambiente, prevención de la contaminación
   - SST ................ condiciones seguras, evitar lesiones y daños a la salud,
                          consulta y participación de los trabajadores
   - Seguridad de la información ... confidencialidad, integridad, disponibilidad
   - Continuidad ........ capacidad de seguir entregando productos y servicios
   - Servicios TI ....... cumplir los niveles de servicio acordados
4. Marco para establecer objetivos
5. Aprobación: alta dirección, con nombre, cargo, firma y fecha
6. Comunicación y disponibilidad
```

Cabe en una página. Si pasa de dos, es un manual disfrazado de política.

⚠️ **14001 y 45001 exigen compromisos concretos que el auditor busca literalmente.** No los diluyas en prosa genérica: tienen que estar identificables.

### Paso 6 — Ramas: la cláusula 8 de cada norma

Aquí no hay integración posible, pero sí solapamientos que sí se aprovechan:

| Solapamiento | Cómo se resuelve |
|---|---|
| 14001 8.2 ↔ 45001 8.2 (emergencias) | Un plan de emergencias con capítulo ambiental y capítulo SST |
| 22301 8.4 ↔ 20000-1 8.7.2 ↔ 27001 A.5.29–A.5.30 (continuidad) | Se documenta una vez en 22301 y las otras dos lo referencian |
| 9001 8.4 ↔ 27001 A.5.19–A.5.22 (proveedores) | Un solo proceso de evaluación con criterios de calidad **y** de seguridad |
| 27001 6.1.2–6.1.3 ↔ 8.2–8.3 | Mismo proceso: 6 es el método, 8 es la ejecución. No dupliques el método |
| 45001 8.1.3 ↔ 9001 6.3 ↔ 20000-1 8.5.1 (cambios) | Un procedimiento de gestión del cambio con criterios por dimensión |

### Paso 7 — Preparar la evidencia desde el día uno

`90_REGISTROS/AAAA/` con subcarpetas por cláusula, creadas vacías al inicio. Parece trivial y no lo es: si la carpeta existe, la gente guarda ahí; si no existe, la evidencia termina en correos y carpetas personales, y a los seis meses no hay forma de reconstruirla.

Lo que más se pierde y más se pide: actas de reuniones, registros de capacitación con firma, evidencia de comunicaciones, resultados de mediciones, y en 45001 las actas del CPHS.

---

## 4. El entregable

```
<organizacion>_SGI/
├── 00_LISTA_MAESTRA.csv          ← generado desde catalogo_normas.json
├── 00_COMUN/…                    ← con los 15 documentos base en estado borrador
├── <NN>_<NORMA>/…                ← una por norma del alcance
├── 90_REGISTROS/AAAA/…
└── 99_OBSOLETOS/
```

Cada documento base sale como **stub estructurado**, no en blanco: encabezado con código, versión, cláusulas que cubre y aprobador, más los apartados que el requisito exige y una nota de qué debe contener cada uno. Llenar un stub bien hecho toma una fracción del tiempo de partir de una hoja vacía.

Genera todo esto con:

```bash
python scripts/iso_sgi.py estructura --normas 9001,27001 --org "Mi Empresa" --salida ./SGI
```

---

## 5. Lo que revisa el auditor

- Que la **lista maestra exista, esté actualizada y coincida con la realidad**. Un documento en la carpeta que no está en la lista es hallazgo; uno en la lista que no aparece, también.
- Que la versión que usa la gente sea **la vigente**. El auditor le pide el procedimiento a quien lo ejecuta, no al encargado de calidad.
- Que los **documentos de origen externo** estén identificados y controlados.
- Que la **política esté comunicada** — pregunta a cualquiera, no al gerente.
- Que exista **trazabilidad de aprobación**: quién aprobó qué y cuándo.
- Que los **obsoletos estén identificados** como tales si se conservan.

---

## 6. Errores que se repiten

- **Una carpeta por norma desde el inicio.** Es la decisión que condena al sistema a la duplicación permanente. Tronco primero, siempre.
- **Escribir el control documental al final.** Obliga a reformatear todo.
- **Manual de calidad de 80 páginas.** Desde 2015 no es obligatorio y nadie lo lee. Un mapa de procesos y una lista maestra hacen el mismo trabajo mejor.
- **Copiar plantillas de internet sin adaptarlas.** El auditor detecta en dos minutos un procedimiento que describe una empresa que no es esta. Y si la plantilla venía de otra organización real, además hay un problema de propiedad intelectual.
- **No crear `90_REGISTROS/` al inicio.** La evidencia se pierde y no se recupera.
- **Política de seis páginas** con la misión, la visión y los valores. No es eso.
- **Codificar antes de decidir la nomenclatura.** Renumerar 60 documentos a mitad de proyecto es un día perdido.

---

## 7. Límites

- La estructura no implementa el sistema. Un SGI con todos los documentos y ninguna evidencia de operación **no se certifica**.
- Las plantillas generadas son genéricas por diseño. Adaptarlas al contexto real de la organización es trabajo obligatorio, no opcional.
- Esta skill no reproduce el texto de las normas: describe qué hay que demostrar. Para implementar hay que comprar la norma.
- Si la organización ya está certificada, no reorganices sin plan de migración.
