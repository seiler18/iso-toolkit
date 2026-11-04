# `datos/` — el catálogo estructurado

Un solo archivo: [`catalogo_normas.json`](catalogo_normas.json). Es el **dato maestro** del toolkit — las skills lo citan, los scripts lo consumen y un futuro servidor MCP lo expondrá como recurso.

---

## Qué contiene

| Bloque | Contenido |
|---|---|
| `normas` | Las 6 normas. Por cada una: cláusulas 4–10 con subapartados, e información documentada obligatoria |
| `anexo_a_27001` | Los 93 controles de la edición 2022, agrupados en 4 temas, con los 11 nuevos marcados |
| `trampas_de_numeracion` | ⭐ Dónde la misma cláusula significa cosas distintas según la norma |

```
9001     28 cláusulas · 17 obligaciones documentales
14001    22 · 15
45001    23 · 17
27001    23 · 15   (+ 93 controles del Anexo A)
22301    26 · 18
20000-1  29 · 25
```

---

## Esquema

### `normas.<clave>`

```jsonc
{
  "designacion": "ISO/IEC 27001:2022",
  "dominio": "Seguridad de la Información",
  "edicion": 2022,
  "sigla_sistema": "SGSI",
  "tiene_anexo_normativo": true,
  "nota_verificacion": "…",          // advertencia sobre ediciones, si aplica
  "clausulas": [
    {
      "num": "6.1",
      "titulo": "Acciones para abordar riesgos y oportunidades",
      "tronco": "propio",             // comun | parcial | propio
      "nota": "…",                    // opcional
      "sub": ["6.1.1 …", "6.1.2 …"]   // opcional
    }
  ],
  "info_documentada": [
    {
      "clausula": "6.1.3 d)",
      "que": "Declaración de Aplicabilidad…",
      "tipo": "D",                    // D documento | R registro | D+R ambos
      "condicional": "…",             // opcional: solo aplica si…
      "estrella": true                // opcional: pieza de alto valor
    }
  ]
}
```

**`tronco`** es la clave de la integración multinorma:

| Valor | Significa |
|---|---|
| `comun` | Se documenta **una sola vez** para todo el SGI |
| `parcial` | Un documento único, con secciones por norma |
| `propio` | Específico de esta norma. No se integra |

### `anexo_a_27001.controles`

```jsonc
{ "id": "A.8.12", "titulo": "Prevención de fuga de datos", "nuevo_2022": true }
```

---

## Cómo se usa

```python
import json
d = json.load(open("catalogo_normas.json", encoding="utf-8"))

# el tronco común de un sistema integrado
comunes = [c for c in d["normas"]["27001"]["clausulas"] if c["tronco"] == "comun"]

# los 11 controles nuevos de 2022
nuevos = [c for c in d["anexo_a_27001"]["controles"] if c.get("nuevo_2022")]
```

O desde la línea de comandos:

```bash
python ../scripts/iso_sgi.py listar --norma 27001
python ../scripts/iso_sgi.py listar --trampas
```

---

## Mantenerlo

**Es la fuente única.** Si actualizas una cláusula en una skill, actualiza también el JSON — y al revés. Cuando cambie una edición de norma:

1. Actualizar `edicion`, `designacion` y las cláusulas afectadas.
2. Añadir o ajustar `nota_verificacion`.
3. Revisar si cambia alguna entrada de `trampas_de_numeracion`.
4. Subir la `version` en `_meta` y la fecha.

---

## ⚖️ Por qué esto es legal

Este archivo **no reproduce el texto de ninguna norma**. Contiene:

- **Identificadores de cláusula y de control** (`8.2.3`, `A.5.30`). Son referencias de uso universal en la industria, no reproducción — la forma en que todo el mundo se refiere a un requisito.
- **Títulos en redacción propia en español.** No se copió la traducción de ningún organismo de normalización: una traducción es en sí misma obra protegida. Por eso hay que **referenciar siempre por el identificador**, que es lo único inequívoco entre traducciones y ediciones.
- **Descripciones originales** de qué debe demostrar la organización, escritas desde el requisito hacia abajo.

Para implementar necesitas la norma oficial, adquirida legalmente: [INN](https://www.inn.cl) en Chile, [ISO Store](https://www.iso.org/store.html) fuera. Ver el [DISCLAIMER](../DISCLAIMER.md).

> ⚠️ **Verifica siempre contra la edición que hayas adquirido.** La numeración cambia entre ediciones, y las versiones chilenizadas (NCh) pueden incluir enmiendas que la edición internacional original no trae — el caso de 27001 y su cláusula 6.3.
