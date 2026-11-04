# Mapa de integración Anexo SL — 6 normas en un solo sistema

**Normas cubiertas:** ISO 9001:2015 · ISO 14001:2015 · ISO 45001:2018 · ISO/IEC 27001:2022 · ISO 22301:2019 · ISO/IEC 20000-1:2018

> **Para qué sirve:** si tu organización tiene (o quiere) más de una certificación, este mapa te dice **qué puedes documentar una sola vez** y **dónde cada norma te obliga a algo propio**. Es la diferencia entre un sistema integrado y seis carpetas paralelas con el mismo contenido repetido seis veces.
>
> ⚠️ Material orientativo de autoría propia. **No reproduce el texto de las normas** — describe con palabras propias qué exige cada requisito. Para implementar necesitas la norma oficial, que debes adquirir legalmente (en Chile, al [INN](https://www.inn.cl)). Lee el [DISCLAIMER](../DISCLAIMER.md).
>
> ⚠️ Verifica siempre la numeración contra la edición vigente que hayas adquirido: entre ediciones cambia.

---

## La idea en una frase

Desde 2012 las normas de sistemas de gestión comparten una **estructura de alto nivel (Anexo SL)**: las mismas siete cláusulas (4 a 10), en el mismo orden, con el mismo esqueleto. Lo que cambia es el **relleno de la cláusula 8** y un puñado de requisitos propios repartidos en las demás.

**Consecuencia práctica:** entre el **60 % y el 70 %** de la documentación de un sistema integrado puede ser un único juego de documentos que sirve para las seis normas. La cláusula 8 y algunos añadidos son lo que hay que multiplicar.

```
        Cláusula 4 · 5 · 6 · 7 · 9 · 10   →  TRONCO COMÚN (documenta una vez)
        Cláusula 8                        →  RAMA PROPIA de cada norma
        + añadidos específicos            →  parches por norma (ver tablas)
```

---

## Tabla maestra: qué se comparte y qué no

| Cláusula | Requisito troncal (común a las 6) | ¿Se puede documentar una sola vez? |
|---|---|---|
| **4.1** | Cuestiones internas y externas que afectan al sistema | ✅ Sí — un solo análisis de contexto, con secciones por dimensión |
| **4.2** | Partes interesadas y sus requisitos | ✅ Sí — una matriz única con columna "norma aplicable" |
| **4.3** | Alcance del sistema | ⚠️ Parcial — un documento, pero el alcance de cada certificado puede diferir |
| **4.4** | El sistema y sus procesos | ✅ Sí — un mapa de procesos y fichas de proceso únicos |
| **5.1** | Liderazgo y compromiso de la alta dirección | ✅ Sí |
| **5.2** | Política | ✅ Sí — **una Política Integrada** que cubra las seis dimensiones |
| **5.3** | Roles, responsabilidades y autoridades | ✅ Sí — un organigrama + una matriz RACI únicos |
| **6.1** | Acciones para abordar riesgos y oportunidades | ⚠️ Parcial — metodología única, **matrices separadas** (ver abajo) |
| **6.2** | Objetivos y planificación para lograrlos | ✅ Sí — un cuadro de objetivos con columna por norma |
| **6.3** | Planificación de los cambios | ⚠️ **Ojo** — no existe en 14001 ni 45001, y en 20000-1 la 6.3 es otra cosa (ver "trampas") |
| **7.1** | Recursos | ✅ Sí |
| **7.2** | Competencia | ✅ Sí — una matriz de competencias / GAP |
| **7.3** | Toma de conciencia | ✅ Sí — un plan de sensibilización con módulos por norma |
| **7.4** | Comunicación | ✅ Sí — una matriz de comunicaciones |
| **7.5** | Información documentada | ✅ Sí — **un solo** procedimiento de control documental + una Lista Maestra |
| **8** | Operación | ⛔ **No** — es el núcleo propio de cada norma |
| **9.1** | Seguimiento, medición, análisis y evaluación | ✅ Sí — un tablero de indicadores integrado |
| **9.2** | Auditoría interna | ✅ Sí — **un programa anual integrado**, con listas de verificación por norma |
| **9.3** | Revisión por la dirección | ✅ Sí — **una sola revisión** que cubra las entradas de las seis |
| **10** | No conformidades, acciones correctivas y mejora | ✅ Sí — un procedimiento y **un único registro** de NC/AC/OM. ⚠️ pero **la numeración cambia**: ver abajo |

> **El ahorro más grande, en orden:** una sola revisión por la dirección · un solo programa de auditoría interna · un solo control documental · un solo registro de NC/AC · una sola política.

---

## ⚠️ Las cuatro trampas de numeración

Aquí es donde se cae la gente que trabaja con varias normas a la vez. **La misma numeración significa cosas distintas.** Si citas mal la cláusula en un informe de auditoría, le regalas al auditado la excusa perfecta para rechazar el hallazgo.

### 1. La cláusula 10 cambia de orden

| Norma | 10.1 | 10.2 | 10.3 |
|---|---|---|---|
| **9001:2015** · **14001:2015** | Generalidades | No conformidad y acción correctiva | Mejora continua |
| **45001:2018** | Generalidades | **Incidentes**, no conformidades y acciones correctivas | Mejora continua |
| **27001:2022** | **Mejora continua** | No conformidad y acción correctiva | — |
| **22301:2019** · **20000-1:2018** | **No conformidad y acción correctiva** | Mejora continua | — |

Traducido: si en un informe de 22301 escribes "no conformidad respecto de la cláusula 10.2", estás citando *Mejora continua*.

### 2. La 6.3 no es lo mismo en todas

| Norma | 6.3 |
|---|---|
| 9001:2015 | Planificación de los cambios |
| 27001:2022 | Planificación de los cambios *(nueva en la edición 2022)* |
| 22301:2019 | Planificación de cambios en el sistema de gestión |
| **20000-1:2018** | **Planificación del SGS** — ¡otra cosa! Aquí vive el plan de gestión del servicio |
| 14001:2015 | no existe |
| 45001:2018 | no existe — la gestión del cambio está en **8.1.3** |

### 3. La 9.1.2 tiene tres significados

Satisfacción del cliente (**9001**) · Evaluación del cumplimiento legal ambiental (**14001**) · Evaluación del cumplimiento legal de SST (**45001**).

### 4. La 6.1.2 son cuatro matrices distintas

Aspectos ambientales (**14001**) · Identificación de peligros y evaluación de riesgos (**45001**) · Apreciación de riesgos de seguridad de la información (**27001**) · y en **22301** la apreciación de riesgos de continuidad no está en 6.1.2 sino en **8.2.3**.

**No se fusionan.** La metodología sí puede ser una sola; los registros son cuatro.

---

## Los parches: qué añade cada norma fuera de la cláusula 8

Esto es lo que se escapa del tronco común y suele ser lo que se olvida.

### ISO 9001:2015 — Calidad
| Dónde | Qué añade |
|---|---|
| 7.1.5 | Recursos de seguimiento y medición: trazabilidad y calibración de los equipos usados para medir |
| 7.1.6 | Conocimientos de la organización: el saber-hacer necesario para operar, gestionado como un recurso |
| 8.2 | Requisitos para los productos y servicios: comunicación con el cliente, revisión de requisitos |

### ISO 14001:2015 — Ambiental
| Dónde | Qué añade |
|---|---|
| 4.1 | El contexto debe incluir **condiciones ambientales** que afectan o son afectadas por la organización |
| 6.1.2 | **Aspectos ambientales** y determinación de los significativos — matriz propia, no fusionable |
| 6.1.3 | **Requisitos legales** ambientales y otros requisitos |
| 9.1.2 | **Evaluación del cumplimiento legal** ambiental |

### ISO 45001:2018 — Seguridad y Salud en el Trabajo
| Dónde | Qué añade |
|---|---|
| 4.2 | Los **trabajadores** son parte interesada obligatoria |
| **5.4** | **Consulta y participación de los trabajadores** — cláusula que no existe en ninguna otra norma. En Chile se articula con el **CPHS** |
| 6.1.2 | **Identificación de peligros y evaluación de riesgos** para la SST — matriz propia |
| 6.1.3 | Requisitos legales de SST |
| 9.1.2 | Evaluación del cumplimiento legal de SST |
| 10.2 | Incluye explícitamente la **investigación de incidentes**, no solo no conformidades |

### ISO/IEC 27001:2022 — Seguridad de la Información
| Dónde | Qué añade |
|---|---|
| 6.1.2 | **Apreciación de riesgos de seguridad de la información** con metodología definida y criterios de aceptación |
| 6.1.3 | Tratamiento de riesgos + la **Declaración de Aplicabilidad (SoA)** — documento obligatorio y exclusivo de esta norma |
| **Anexo A** | **93 controles** (edición 2022, en 4 temas: organizacional, personas, físico, tecnológico) que hay que justificar uno a uno en la SoA |
| 6.3 | Planificación de cambios (nueva en la edición 2022; no estaba en la 2013) |

> La SoA es la pieza que no se puede integrar ni delegar. Es lo primero que pide el auditor y donde más se cae la gente.

### ISO 22301:2019 — Continuidad del Negocio
| Dónde | Qué añade |
|---|---|
| 4.1 | El contexto debe considerar el **apetito de riesgo** de la organización |
| 4.3 | El alcance debe identificar los **productos y servicios** cubiertos |
| 5.2 | La política debe comprometerse explícitamente con la continuidad |
| 6.2 | Objetivos de continuidad ligados a los tiempos de recuperación |

### ISO/IEC 20000-1:2018 — Gestión de Servicios de TI
| Dónde | Qué añade |
|---|---|
| 4.3 | El alcance debe listar los **servicios** incluidos |
| 4.4 | Gobernanza de **procesos operados por otras partes** — si tercerizas, respondes igual |
| **6.3** | **Plan de gestión del servicio** — vive en "Planificación del SGS", no en 5.3 |
| 7.6 | **Conocimiento** — cláusula propia que no tienen las otras cinco |
| 9.4 | **Informes del servicio** — cláusula propia de evaluación del desempeño |
| 8.x | El catálogo de procesos ITSM más denso de las seis (ver abajo) |

---

## Cláusula 8: dónde cada norma se va por su lado

Esta es la parte que **no se integra**. Un vistazo comparado:

| Norma | Núcleo de la cláusula 8 |
|---|---|
| **9001** | Planificación y control operacional · requisitos para productos y servicios · diseño y desarrollo · control de proveedores externos · producción y provisión · liberación · **control de salidas no conformes** |
| **14001** | Control operacional (incluida la perspectiva de ciclo de vida) · **preparación y respuesta ante emergencias** |
| **45001** | Control operacional con **jerarquía de controles** (eliminar > sustituir > ingeniería > administrativo > EPP) · gestión del cambio · compras, contratistas y subcontratación · **preparación y respuesta ante emergencias** |
| **27001** | Planificación y control operacional · ejecución de la apreciación de riesgos · ejecución del **plan de tratamiento** de riesgos |
| **22301** | **Análisis de Impacto al Negocio (BIA)** y apreciación de riesgos · estrategias y soluciones de continuidad · **planes y procedimientos de continuidad** · programa de **ejercicios y pruebas** · evaluación de la documentación y las capacidades |
| **20000-1** | 8.2 Portafolio de servicios (catálogo, activos, **configuración/CMDB**) · 8.3 Relación y acuerdo (**SLA**, proveedores) · 8.4 Suministro y demanda (presupuesto, demanda, capacidad) · 8.5 Diseño, construcción y transición (cambios, liberación) · 8.6 **Resolución y cumplimiento** (incidentes, peticiones, problemas) · 8.7 **Aseguramiento del servicio** (disponibilidad, continuidad, seguridad) |

> **Solapamientos aprovechables dentro de la cláusula 8:**
> - **14001 8.2 ↔ 45001 8.2** — la preparación ante emergencias puede ser un mismo plan con dos capítulos.
> - **22301 8.4 ↔ 20000-1 continuidad del servicio ↔ 27001 A.5.29–A.5.30** — la continuidad se documenta una vez y se referencia desde las tres.
> - **27001 8.2–8.3 ↔ 6.1.2–6.1.3** — es el mismo proceso de riesgos, ejecutado; no dupliques la metodología.
> - **9001 8.4 ↔ 27001 A.5.19–A.5.22** — la evaluación de proveedores puede ser un solo proceso con criterios de calidad **y** de seguridad.

---

## Cómo usar este mapa (ruta de 5 pasos)

1. **Define el tronco.** Escribe una sola vez las cláusulas 4, 5, 6.2, 6.3, 7, 9 y 10. Un juego de documentos, no seis.
2. **Aplica los parches.** Recorre las tablas de arriba norma por norma y añade lo propio de cada una.
3. **Construye la cláusula 8 por separado.** Aquí no hay atajo. Aprovecha los solapamientos de la nota anterior.
4. **Unifica los registros.** Un solo registro de NC/AC/OM, un solo programa de auditoría, una sola revisión por la dirección. Con columna de "norma" para filtrar.
5. **Prepara la evidencia por cláusula.** El auditor recorre la norma en orden; tu carpeta debería recorrerla igual.

---

## Estructura de carpetas recomendada para un SGI

```
SGI/
├── 00_COMUN/                    ← el tronco: sirve a las 6 normas
│   ├── 4_CONTEXTO/              (FODA · partes interesadas · alcance · mapa de procesos)
│   ├── 5_LIDERAZGO/             (política integrada · organigrama · RACI)
│   ├── 6_PLANIFICACION/         (metodología de riesgos · objetivos · gestión del cambio)
│   ├── 7_APOYO/                 (competencias · concienciación · comunicación · control documental)
│   ├── 9_EVALUACION/            (indicadores · programa de auditoría · revisión por la dirección)
│   └── 10_MEJORA/               (procedimiento y registro único de NC/AC/OM)
│
├── 10_CALIDAD_9001/             ← cláusula 8 + parches propios
├── 20_AMBIENTAL_14001/
├── 30_SST_45001/
├── 40_SEGURIDAD_27001/          (incluye la SoA y los 93 controles)
├── 50_CONTINUIDAD_22301/        (incluye BIA, estrategias, planes y ejercicios)
└── 60_SERVICIOS_20000-1/
```

---

## Herramientas que acompañan a este mapa

Todo lo de arriba está también en formato legible por máquina, y hay scripts que lo convierten en entregables:

```bash
python ../scripts/iso_sgi.py listar --trampas                 # las 4 trampas de numeración
python ../scripts/iso_sgi.py listar --norma 27001             # cláusulas + info documentada obligatoria
python ../scripts/iso_sgi.py estructura --normas 9001,27001 --org "Mi Empresa" --salida ./SGI
python ../scripts/iso_sgi.py checklist --normas todas --salida ./checklist.csv
python ../scripts/iso_sgi.py soa --salida ./soa.csv           # los 93 controles del Anexo A
python ../scripts/iso_sgi.py correspondencia --normas 9001,27001 --formato csv --salida ./cruce.csv
```

- **[`../datos/catalogo_normas.json`](../datos/catalogo_normas.json)** — cláusulas 4–10 de las 6 normas, 107 obligaciones de información documentada, los 93 controles y las trampas de numeración.
- **[`../skills/`](../skills/)** — 8 métodos paso a paso: diagnóstico de brechas, levantar el SGI, riesgos, SoA, BIA, auditoría interna, no conformidades y revisión por la dirección.

---

## Estado de este documento

🚧 **Versión 0.3.** Numeración verificada y trampas documentadas (2026-08-16). La correspondencia al nivel de subapartado, por tema, está en [`01_correspondencia_subapartados.md`](01_correspondencia_subapartados.md) (2026-11-04). Pendiente de desarrollar:

- Mapeo de los 93 controles del Anexo A de 27001 contra las demás normas.
- Ejemplos de política integrada y de matriz de partes interesadas.

⚠️ **Salvedad de 14001:** la numeración de 14001 usada aquí es la de la edición publicada 2015. Si consultas un PDF que dice "6.1.3 Obligaciones de cumplimiento" o "6.1.4 Riesgo asociado con amenazas y oportunidades", **estás mirando un borrador DIS/FDIS, no la norma vigente.**

¿Encontraste un error o falta un cruce? Abre un issue.

---

*Autoría: Jesús Seiler — auditor interno en las seis normas listadas. Material original, no afiliado a ISO ni al INN.*
*Última actualización: 2026-11-04 · Licencia: CC BY-SA 4.0*
