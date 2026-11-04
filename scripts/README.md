# Scripts

Utilidades en Python que convierten el catálogo de datos en entregables. Solo biblioteca estándar, sin dependencias. Probado en Python 3.10+.

```bash
python iso_sgi.py --help
```

---

## `iso_sgi.py`

El generador. Cinco subcomandos.

### `listar` — consultar el catálogo

```bash
python iso_sgi.py listar                  # las 6 normas, con recuentos
python iso_sgi.py listar --norma 27001    # cláusulas + información documentada obligatoria
python iso_sgi.py listar --trampas        # ⭐ las trampas de numeración entre normas
```

`--trampas` es lo que más se usa en el día a día: dónde la misma cláusula significa cosas distintas según la norma. Consúltalo **antes** de citar una cláusula en un informe de auditoría de un sistema integrado.

### `estructura` — levantar un SGI completo

```bash
python iso_sgi.py estructura --normas 9001,27001 --org "Mi Empresa" --salida ./SGI
python iso_sgi.py estructura --normas todas --org "Mi Empresa" --salida ./SGI
```

Genera:

- El árbol `00_COMUN/` + una carpeta por norma + `90_REGISTROS/AAAA/` + `99_OBSOLETOS/`.
- **19 documentos base del tronco común** como esqueletos estructurados, con encabezado, cláusulas que cubren, apartados que el requisito exige y notas de criterio.
- Una carpeta por cada cláusula propia de cada norma, con su `_LEEME.md` explicando qué va ahí.
- `00_LISTA_MAESTRA.csv` — el índice del sistema, con la columna "cláusulas que cubre" ya resuelta.
- `README.md` con el orden de trabajo recomendado.

Opciones: `--forzar` para escribir sobre una carpeta que no está vacía.

> Los documentos salen como **esqueletos genéricos**. Adaptarlos al contexto real no es opcional: un documento que describe una empresa que no es esta se detecta en dos minutos de auditoría.

### `checklist` — lista de verificación

```bash
python iso_sgi.py checklist --normas 45001 --salida ./checklist.csv
python iso_sgi.py checklist --normas todas --salida ./checklist_sgi.csv
```

CSV con una fila por cláusula y por obligación de información documentada, con columnas vacías para `estado`, `evidencia_encontrada`, `brecha` y `responsable`.

En sistemas multinorma **agrupa el tronco común una sola vez** en vez de repetirlo por norma — que es lo que hace que estos informes salgan de 300 páginas y nadie los lea.

Sirve tanto para el diagnóstico de brechas como para la lista de verificación de auditoría interna.

### `soa` — Declaración de Aplicabilidad (27001)

```bash
python iso_sgi.py soa --salida ./soa_borrador.csv
```

Los 93 controles del Anexo A con las columnas de decisión: `aplica`, `justificacion`, `origen`, `riesgos_asociados`, `estado`, `evidencia`, `responsable`. Marca los 11 controles nuevos de 2022, que son los que más brechas generan.

⚠️ **Haz primero la matriz de riesgos.** Una SoA sin riesgos detrás es exactamente el hallazgo que busca el auditor.

### `correspondencia` — en qué cláusula trata cada norma cada tema

```bash
python iso_sgi.py correspondencia --salida ../mapeo_integrado/01_correspondencia_subapartados.md
python iso_sgi.py correspondencia --normas 9001,27001 --formato csv --salida ./cruce.csv
```

45 temas (partes interesadas, proveedores, incidentes, cambios…) con la referencia de cada norma al nivel de subapartado y si se documenta una vez o por separado. Con `--normas` quedan solo las columnas pedidas y se descartan los temas que ninguna de ellas trata.

El primer comando es el que genera el `.md` publicado en `mapeo_integrado/`: una corrección va en `correspondencia` del catálogo y después se regenera.

### `instalar-skills` — activar las skills en Claude Code

```bash
python iso_sgi.py instalar-skills --destino ../../.claude/skills
```

Copia las carpetas de `../skills/` a un directorio `.claude/skills`, donde Claude Code las carga automáticamente. Útil para trabajar en el proyecto de un cliente con el método ya cargado.

---

## Los CSV y Excel

Se escriben con `utf-8-sig` y `;` como separador, que es lo que Excel en español espera. Si abres uno y ves `Ã¡` en vez de `á`, revisa que no lo hayas convertido con otra herramienta.

---

## De aquí a un MCP

Este script está escrito con la separación datos / lógica a propósito:

```
datos/catalogo_normas.json   ← el conocimiento estructurado (la parte difícil)
scripts/iso_sgi.py           ← funciones puras que lo transforman
```

Cada subcomando es una función que recibe parámetros y devuelve un artefacto. Convertirlas en herramientas de un servidor MCP es envolverlas, no reescribirlas. Ese es el camino planificado: `listar`, `checklist`, `soa` y `estructura` como *tools*, y `catalogo_normas.json` como *resource*.

---

## ⚖️ Aviso

Estos scripts **no reproducen el texto de ninguna norma ISO**. Trabajan con identificadores de cláusula, títulos en redacción propia y descripciones originales de qué debe demostrar la organización. Para implementar necesitas la norma oficial, adquirida legalmente ([INN](https://www.inn.cl) en Chile, [ISO Store](https://www.iso.org/store.html) fuera). Ver el [DISCLAIMER](../DISCLAIMER.md).
