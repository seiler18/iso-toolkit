# Correspondencia por subapartado — 6 normas

**Normas:** ISO 9001:2015 · ISO 14001:2015 · ISO 45001:2018 · ISO/IEC 27001:2022 · ISO 22301:2019 · ISO/IEC 20000-1:2018

> **Para qué sirve:** dado un tema (las partes interesadas, los proveedores, los incidentes…), dice en qué cláusula o control lo trata cada norma. Sirve para armar un sistema integrado sin duplicar documentos y para citar bien en un informe de auditoría.
>
> ⚠️ Material orientativo de autoría propia. **No reproduce el texto de las normas**: solo da referencias. Para implementar necesitas la norma oficial, adquirida legalmente (en Chile, al [INN](https://www.inn.cl)). Lee el [DISCLAIMER](../DISCLAIMER.md).

**Cómo leerla.** Cada celda es la referencia donde la norma trata ese tema; `—` significa que no tiene un apartado para eso. Las referencias `A.x.x` son controles del Anexo A de 27001. La última columna dice si se documenta una sola vez (✅), en un documento con secciones o criterios por norma (⚠️) o por separado (⛔).

La explicación de por qué se integra cada cosa está en el [mapa Anexo SL](00_mapa_anexo_sl.md). Esta tabla es la consulta rápida.

## 4 · Contexto de la organización

| Tema | 9001 | 14001 | 45001 | 27001 | 22301 | 20000-1 | ¿Una vez? |
|---|---|---|---|---|---|---|---|
| Cuestiones internas y externas | 4.1 | 4.1 | 4.1 | 4.1 | 4.1 | 4.1 | ✅ Sí |
| Partes interesadas y sus requisitos | 4.2 | 4.2 | 4.2 | 4.2 | 4.2.1 | 4.2 | ✅ Sí |
| Requisitos legales y otros requisitos | 5.1.2 · 8.2.2 | 6.1.3 | 6.1.3 | 4.2 · A.5.31 | 4.2.2 | 4.2 | ⚠️ Parcial |
| Alcance | 4.3 | 4.3 | 4.3 | 4.3 | 4.3.1 · 4.3.2 | 4.3 | ⚠️ Parcial |
| Procesos del sistema | 4.4.1 · 4.4.2 | 4.4 | 4.4 | 4.4 | 4.4 | 4.4 | ✅ Sí |

- **Cuestiones internas y externas.** 14001 pide las condiciones ambientales y 22301 el apetito de riesgo: van como secciones del mismo análisis. Con las enmiendas de 2024, en las seis el análisis tiene que pronunciarse sobre si el cambio climático afecta a la organización.
- **Partes interesadas y sus requisitos.** En 45001 los trabajadores son parte interesada obligatoria.
- **Requisitos legales y otros requisitos.** Un solo registro legal con una columna de ámbito. En 14001 y 45001, además, se evalúa su cumplimiento (9.1.2).
- **Alcance.** Un documento, pero el alcance de cada certificado puede ser distinto. 22301 nombra los productos y servicios cubiertos; 20000-1, los servicios.
- **Procesos del sistema.** 20000-1 exige gobernar también los procesos que opera un tercero.

## 5 · Liderazgo

| Tema | 9001 | 14001 | 45001 | 27001 | 22301 | 20000-1 | ¿Una vez? |
|---|---|---|---|---|---|---|---|
| Liderazgo y compromiso | 5.1.1 · 5.1.2 | 5.1 | 5.1 | 5.1 | 5.1 | 5.1 | ✅ Sí |
| Política | 5.2.1 · 5.2.2 | 5.2 | 5.2 | 5.2 | 5.2.1 · 5.2.2 | 5.2 | ✅ Sí |
| Roles, responsabilidades y autoridades | 5.3 | 5.3 | 5.3 | 5.3 | 5.3 | 5.3 | ✅ Sí |
| Consulta y participación de los trabajadores | — | — | 5.4 | — | — | — | ⛔ No |

- **Liderazgo y compromiso.** 9001 suma el enfoque al cliente.
- **Política.** Una política integrada con los compromisos de las seis.
- **Consulta y participación de los trabajadores.** Solo existe en 45001. En Chile se apoya en el Comité Paritario.

## 6 · Planificación

| Tema | 9001 | 14001 | 45001 | 27001 | 22301 | 20000-1 | ¿Una vez? |
|---|---|---|---|---|---|---|---|
| Riesgos y oportunidades del sistema | 6.1.1 · 6.1.2 | 6.1.1 | 6.1.1 | 6.1.1 | 6.1.1 · 6.1.2 | 6.1 | ✅ Sí |
| Matriz de riesgos propia del dominio | — | 6.1.2 | 6.1.2 (6.1.2.1–6.1.2.3) | 6.1.2 · 8.2 | 8.2.3 | 6.1 | ⛔ No |
| Planificación de acciones y tratamiento | 6.1.2 | 6.1.4 | 6.1.4 · 8.1.2 | 6.1.3 · 8.3 | 6.1.2 | 6.1 | ⚠️ Parcial |
| Objetivos y su planificación | 6.2.1 · 6.2.2 | 6.2.1 · 6.2.2 | 6.2.1 · 6.2.2 | 6.2 | 6.2.1 · 6.2.2 | 6.2 | ✅ Sí |
| Cambios en el sistema de gestión | 6.3 | — | — | 6.3 | 6.3 | — | ⚠️ Parcial |
| Plan de gestión del servicio | — | — | — | — | — | 6.3 | ⛔ No |

- **Riesgos y oportunidades del sistema.** Una metodología para todo el sistema.
- **Matriz de riesgos propia del dominio.** Aspectos ambientales, peligros de SST, riesgos de la información, de continuidad y de los servicios: registros separados con la misma metodología.
- **Planificación de acciones y tratamiento.** 27001 exige además la Declaración de Aplicabilidad (6.1.3). 45001 obliga a seguir la jerarquía de controles (8.1.2).
- **Objetivos y su planificación.** Un cuadro de objetivos con columna de norma. En 22301 se amarran a los tiempos de recuperación.
- **Cambios en el sistema de gestión.** 14001 y 45001 no tienen este apartado. La 6.3 de 20000-1 es otra cosa: ver la fila siguiente.

## 7 · Apoyo

| Tema | 9001 | 14001 | 45001 | 27001 | 22301 | 20000-1 | ¿Una vez? |
|---|---|---|---|---|---|---|---|
| Recursos | 7.1.1–7.1.4 | 7.1 | 7.1 | 7.1 | 7.1 | 7.1 | ✅ Sí |
| Equipos de seguimiento y medición | 7.1.5 (7.1.5.1 · 7.1.5.2) | 9.1.1 | 9.1.1 | — | — | — | ⚠️ Parcial |
| Conocimiento de la organización | 7.1.6 | — | — | — | — | 7.6 | ✅ Sí |
| Competencia | 7.2 | 7.2 | 7.2 | 7.2 | 7.2 | 7.2 | ✅ Sí |
| Toma de conciencia | 7.3 | 7.3 | 7.3 | 7.3 · A.6.3 | 7.3 | 7.3 | ✅ Sí |
| Comunicación | 7.4 | 7.4.1–7.4.3 | 7.4.1–7.4.3 | 7.4 | 7.4 · 8.4.3 | 7.4 | ✅ Sí |
| Información documentada | 7.5.1–7.5.3 | 7.5.1–7.5.3 | 7.5.1–7.5.3 | 7.5.1–7.5.3 | 7.5.1–7.5.3 | 7.5.1–7.5.4 | ✅ Sí |

- **Equipos de seguimiento y medición.** Un programa de calibración y verificación sirve a las tres.
- **Conocimiento de la organización.** Un solo proceso de gestión del conocimiento.
- **Comunicación.** 22301 agrega la comunicación durante una disrupción (8.4.3).
- **Información documentada.** 20000-1 añade 7.5.4: la lista de documentos propios del sistema de gestión del servicio.

## 8 · Operación

| Tema | 9001 | 14001 | 45001 | 27001 | 22301 | 20000-1 | ¿Una vez? |
|---|---|---|---|---|---|---|---|
| Planificación y control operacional | 8.1 | 8.1 | 8.1.1 | 8.1 | 8.1 | 8.1 | ⛔ No |
| Gestión del cambio operacional | 8.5.6 | 8.1 | 8.1.3 | 8.1 · A.8.32 | — | 8.5.1 | ⚠️ Parcial |
| Proveedores y procesos externos | 8.4.1–8.4.3 | 8.1 | 8.1.4 (8.1.4.1–8.1.4.3) | 8.1 · A.5.19–A.5.22 | 8.3.4 | 8.3.4 | ⚠️ Parcial |
| Requisitos del cliente y acuerdos de servicio | 8.2.1–8.2.4 | — | — | — | — | 8.3.2 · 8.3.3 | ⚠️ Parcial |
| Diseño y transición | 8.3 | — | — | A.8.25 | — | 8.5.2 | ⚠️ Parcial |
| Liberación | 8.6 | — | — | — | — | 8.5.3 | ⚠️ Parcial |
| Inventario de activos y configuración | — | — | — | A.5.9 | — | 8.2.5 · 8.2.6 | ⚠️ Parcial |
| Capacidad y disponibilidad | — | — | — | A.8.6 · A.8.14 | — | 8.4.3 · 8.7.1 | ⚠️ Parcial |
| Incidentes | — | — | 10.2 | A.5.24–A.5.28 | 8.4 | 8.6.1 | ⚠️ Parcial |
| Emergencias y continuidad | — | 8.2 | 8.2 | A.5.29 · A.5.30 | 8.3–8.5 | 8.7.2 | ⚠️ Parcial |
| Análisis de impacto al negocio (BIA) | — | — | — | — | 8.2.2 | — | ⛔ No |
| Ejercicios y evaluación de la continuidad | — | — | — | — | 8.5 · 8.6 | — | ⛔ No |
| Salidas no conformes | 8.7 (8.7.1 · 8.7.2) | — | — | — | — | — | ⛔ No |
| Presupuesto y demanda del servicio | — | — | — | — | — | 8.4.1 · 8.4.2 | ⛔ No |

- **Planificación y control operacional.** Es el núcleo de cada norma: ver la tabla de la cláusula 8 en el mapa.
- **Gestión del cambio operacional.** Un procedimiento de cambios, con los criterios de cada norma como pasos de evaluación.
- **Proveedores y procesos externos.** Una evaluación de proveedores con criterios de calidad, ambiente, SST, seguridad y continuidad.
- **Diseño y transición.** En 9001 es excluible si la organización no diseña.
- **Inventario de activos y configuración.** Un inventario único con los atributos que pide cada una.
- **Incidentes.** Un solo canal de reporte con tipo de incidente; cada tipo sigue su propio tratamiento. En 45001 la investigación vive en la cláusula 10.
- **Emergencias y continuidad.** Un plan de emergencias con capítulo ambiental y de SST. La continuidad se documenta una vez en 22301 y se referencia desde 27001 y 20000-1.

## 9 · Evaluación del desempeño

| Tema | 9001 | 14001 | 45001 | 27001 | 22301 | 20000-1 | ¿Una vez? |
|---|---|---|---|---|---|---|---|
| Seguimiento, medición y análisis | 9.1.1 · 9.1.3 | 9.1.1 | 9.1.1 | 9.1 | 9.1 | 9.1 | ✅ Sí |
| Satisfacción del cliente | 9.1.2 | — | — | — | — | 8.3.2 | ⚠️ Parcial |
| Evaluación del cumplimiento legal | — | 9.1.2 | 9.1.2 | A.5.31 | — | — | ⚠️ Parcial |
| Auditoría interna | 9.2.1 · 9.2.2 | 9.2.1 · 9.2.2 | 9.2.1 · 9.2.2 | 9.2.1 · 9.2.2 | 9.2.1 · 9.2.2 | 9.2 | ✅ Sí |
| Revisión por la dirección | 9.3.1–9.3.3 | 9.3 | 9.3 | 9.3.1–9.3.3 | 9.3.1–9.3.3 | 9.3 | ✅ Sí |
| Informes del servicio | — | — | — | — | — | 9.4 | ⛔ No |

- **Seguimiento, medición y análisis.** Un tablero de indicadores con columna de norma.
- **Evaluación del cumplimiento legal.** Un ejercicio periódico con alcance ambiental y de SST. En 27001 la identificación de requisitos legales es un control del Anexo A.
- **Auditoría interna.** Un programa integrado; la lista de verificación sí va por norma.
- **Revisión por la dirección.** Una sola revisión que cubra las entradas de las seis.

## 10 · Mejora

| Tema | 9001 | 14001 | 45001 | 27001 | 22301 | 20000-1 | ¿Una vez? |
|---|---|---|---|---|---|---|---|
| Generalidades de la mejora | 10.1 | 10.1 | 10.1 | — | — | — | ✅ Sí |
| No conformidad y acción correctiva | 10.2 (10.2.1 · 10.2.2) | 10.2 | 10.2 | 10.2 | 10.1 (10.1.1 · 10.1.2) | 10.1 | ✅ Sí |
| Mejora continua | 10.3 | 10.3 | 10.3 | 10.1 | 10.2 | 10.2 | ✅ Sí |

- **Generalidades de la mejora.** 27001, 22301 y 20000-1 no tienen este apartado: por eso su numeración se corre.
- **No conformidad y acción correctiva.** Un registro único. El número cambia entre normas: es la trampa de cita más frecuente.

---

**Verificación.** Los números de 9001, 45001, 27001 y 22301 están verificados contra el índice de cada norma. Los de 14001 siguen la edición publicada de 2015 y los de 20000-1 salen del catálogo: de esas dos no hay un texto contra el cual comprobarlos.

*Generado con `python scripts/iso_sgi.py correspondencia` a partir de [`datos/catalogo_normas.json`](../datos/catalogo_normas.json): las correcciones van en el catálogo, no en este archivo.*
*Autoría: Jesús Seiler — auditor interno en las seis normas listadas. Material original, no afiliado a ISO ni al INN. Licencia: CC BY-SA 4.0*
