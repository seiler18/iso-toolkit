# ISO Toolkit — Sistemas de gestión integrados, en español

**Material práctico y gratuito para implementar sistemas de gestión ISO en pymes de habla hispana.** Escrito por un auditor interno en ejercicio, no por un vendedor de cursos.

> ⚠️ **Esto no es una certificación ni la reemplaza.** Lee el [DISCLAIMER](DISCLAIMER.md) antes de usar nada de aquí.

---

## Qué hay aquí

| Carpeta | Qué contiene |
|---|---|
| [`mapeo_integrado/`](mapeo_integrado/) | ⭐ **El mapa Anexo SL de 6 normas.** Qué documentas una vez y qué te obliga a duplicar cada norma. |
| [`skills/`](skills/) | ⭐ **8 métodos ejecutables**: diagnóstico de brechas, levantar un SGI, riesgos, SoA, BIA, auditoría interna, no conformidades, revisión por la dirección. Cada uno con lo que revisa el auditor y los errores que se repiten. |
| [`datos/`](datos/) | El catálogo estructurado: cláusulas 4–10 de las 6 normas, información documentada obligatoria, los 93 controles del Anexo A y las trampas de numeración. Legible por máquina. |
| [`scripts/`](scripts/) | `iso_sgi.py` — genera la estructura de un SGI, la lista maestra, checklists y el esqueleto de la SoA. Sin dependencias. |
| [`checklists/`](checklists/) | Listas de verificación por norma y por cláusula, para autodiagnóstico y auditoría interna. |
| [`plantillas/`](plantillas/) | Plantillas en Markdown: política integrada, matriz de partes interesadas, RACI, registro de NC/AC, programa de auditoría… |

## Prueba rápida

```bash
git clone <este-repo> && cd iso-toolkit

# ¿En qué se diferencian las cláusulas entre normas? (el error de cita más común)
python scripts/iso_sgi.py listar --trampas

# Levanta el esqueleto de un sistema integrado de calidad + seguridad de la información
python scripts/iso_sgi.py estructura --normas 9001,27001 --org "Mi Empresa" --salida ./SGI

# La Declaración de Aplicabilidad de 27001, con los 93 controles
python scripts/iso_sgi.py soa --salida ./soa.csv
```

Solo necesitas Python 3.10+. No hay dependencias que instalar.

## Normas cubiertas

| Norma | Sistema |
|---|---|
| ISO 9001:2015 | Calidad |
| ISO 14001:2015 | Ambiental |
| ISO 45001:2018 | Seguridad y Salud en el Trabajo |
| ISO/IEC 27001:2022 | Seguridad de la Información |
| ISO 22301:2019 | Continuidad del Negocio |
| ISO/IEC 20000-1:2018 | Gestión de Servicios de TI |

---

## Por qué existe

Casi todo el material serio sobre sistemas de gestión ISO está en inglés y cuesta caro. Lo que hay en español suele ser: un PDF genérico de 2013, un curso de 40 horas, o una consultora cobrando por hora.

Falta lo intermedio: **material concreto, actualizado y gratuito** para la pyme que quiere entender qué le van a pedir antes de contratar a nadie.

Y falta, sobre todo, algo que casi nadie aborda: **cómo integrar varias normas sin triplicar la burocracia**. Una organización con tres certificaciones no necesita tres sistemas de gestión: necesita uno, bien armado. Ese es el foco de este repositorio.

---

## Cómo empezar

1. Lee el [mapa de integración Anexo SL](mapeo_integrado/00_mapa_anexo_sl.md) — entenderás la arquitectura de cualquier norma ISO de sistemas de gestión en 10 minutos.
2. Haz el diagnóstico de brechas siguiendo [`skills/iso-diagnostico-brechas`](skills/iso-diagnostico-brechas/SKILL.md), con el checklist que genera `scripts/iso_sgi.py checklist`.
3. Levanta la estructura con [`skills/iso-levantar-sgi`](skills/iso-levantar-sgi/SKILL.md) y `scripts/iso_sgi.py estructura`.
4. Usa las plantillas del tronco común (`plantillas/`) para lo que te falte.

> **El orden importa.** Diagnosticar antes de documentar te ahorra escribir cosas que ya tenías. Y la auditoría interna y la revisión por la dirección exigen que el sistema lleve meses operando: se planifican al principio aunque se ejecuten al final.

---

## Lo que este repositorio NO hace

- **No reproduce el texto de las normas.** Son obra protegida; hay que comprarlas ([INN](https://www.inn.cl) en Chile, [ISO Store](https://www.iso.org/store.html) fuera).
- **No certifica ni prepara certificados.** Eso lo hacen organismos acreditados.
- **No garantiza que apruebes una auditoría.** Ayuda a que llegues mejor preparado.
- **No contiene información de ninguna empresa real.** Todo es genérico y de autoría propia.

---

## Autor

**Jesús Seiler** — Puerto Montt, Chile. Auditor interno en ISO 9001, 14001, 45001, 27001, 22301 y 20000-1. Analista de sistemas: sistemas de gestión + automatización.

Escribo sobre esto en LinkedIn. Si el material te sirvió, decírmelo es la mejor forma de que siga saliendo.

## Contribuir

Los issues son bienvenidos: errores, cruces que faltan, plantillas que te gustaría ver. Si aportas material, debe ser **de tu autoría** — no se aceptan extractos de normas ni documentos de organizaciones reales.

## Licencia

[CC BY-SA 4.0](LICENSE) — úsalo, adáptalo, aplícalo en tu empresa (también con fines comerciales). Solo dos condiciones: cita la fuente y comparte tus derivados bajo la misma licencia.

## Estado

🚧 **En construcción activa** (iniciado en agosto de 2026). El mapa de integración es lo primero. Si quieres seguir el avance, dale ⭐ al repo.
