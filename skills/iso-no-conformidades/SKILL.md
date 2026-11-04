---
name: iso-no-conformidades
description: Gestión del ciclo de no conformidades y acciones correctivas - redacción, corrección inmediata, análisis de causa raíz, acción correctiva, verificación de eficacia y cierre. Un registro único para todo el SGI, filtrable por norma.
normas: [9001, 14001, 45001, 27001, 22301, 20000-1]
entrega: Registro único de NC/AC/OM + procedimiento + fichas de análisis de causa
---

# No conformidades y acciones correctivas

## 1. Cuándo usar esta skill

Cada vez que aparece una desviación, venga de donde venga: auditoría interna o externa, reclamo de cliente, incidente, incumplimiento legal detectado, indicador fuera de meta, error de proceso, hallazgo de la revisión por la dirección.

Es la cláusula 10 de las seis normas y, junto con 9.2 y 9.3, lo que demuestra que el sistema **está vivo**. Un sistema sin ninguna NC registrada en el año no es un sistema perfecto: es un sistema que no se está usando, y el auditor lo lee exactamente así.

---

## 2. Qué necesitas antes de empezar

- Procedimiento de NC/AC definido (o esta skill para escribirlo).
- Registro único, accesible y con dueño.
- Personas capaces de hacer análisis de causa. Es una habilidad que se enseña; no se asume.

⚠️ **Cuidado con la numeración.** El requisito está en cláusulas distintas según la norma:

| Norma | Cláusula de NC/AC |
|---|---|
| ISO 9001:2015 · 14001:2015 | 10.2 No conformidad y acción correctiva |
| ISO 45001:2018 | 10.2 **Incidentes**, no conformidades y acciones correctivas |
| ISO/IEC 27001:2022 | 10.2 No conformidad y acción correctiva (10.1 es Mejora continua) |
| ISO 22301:2019 · ISO/IEC 20000-1:2018 | **10.1** No conformidad y acción correctiva |

---

## 3. El método

### Paso 1 — Un registro único, con columna de norma

No un registro por norma. Uno solo, filtrable. Ahorra trabajo, evita duplicación y le muestra al auditor un sistema integrado de verdad.

| Campo | Nota |
|---|---|
| `id` | NC-2026-001 |
| `fecha_deteccion` | |
| `origen` | Auditoría interna / externa / reclamo / incidente / indicador / observación propia |
| `normas` | 9001, 27001… (puede ser más de una) |
| `clausulas` | Las que se incumplen, bien citadas |
| `proceso` | |
| `descripcion` | Requisito + evidencia + desviación |
| `tipo` | NC mayor / NC menor / Observación / OM |
| `correccion` | Qué se hizo de inmediato |
| `analisis_causa` | Método usado y causa raíz identificada |
| `accion_correctiva` | Qué evita que vuelva a pasar |
| `responsable` · `fecha_compromiso` | |
| `verificacion_eficacia` | Cómo y cuándo se verificó que funcionó |
| `estado` | Abierta / En ejecución / En verificación / Cerrada |
| `fecha_cierre` | |

### Paso 2 — Distinguir corrección de acción correctiva

**La distinción más importante de toda la cláusula 10**, y la que más hallazgos genera.

| | Corrección | Acción correctiva |
|---|---|---|
| Qué hace | Elimina la no conformidad detectada | Elimina la **causa** para que no se repita |
| Ejemplo | Se emite el registro que faltaba | Se cambia el flujo del sistema para que no se pueda avanzar sin ese registro |
| Cuándo | Inmediato | Después del análisis de causa |
| ¿Basta por sí sola? | **No** | Sí, si es eficaz |

Una NC cerrada solo con la corrección es hallazgo garantizado en la siguiente auditoría, y además vuelve a ocurrir. Que es el punto.

**Excepción legítima:** para una NC menor y aislada, la norma permite evaluar si es necesaria una acción correctiva. Si se decide que no, **hay que registrar esa evaluación y su justificación**. La decisión de no actuar es válida; no dejarla escrita, no.

### Paso 3 — Análisis de causa raíz

Elegir el método según el tamaño del problema. Usar los cinco porqués para todo es tan malo como usar Ishikawa para una errata.

| Método | Cuándo | Cómo |
|---|---|---|
| **5 porqués** | NC simples, causa lineal | Preguntar "por qué" hasta llegar a algo que la organización controla |
| **Ishikawa (6M)** | NC con varias causas posibles | Método · Máquina · Mano de obra · Material · Medición · Medio ambiente |
| **Árbol de causas** | Incidentes de SST, incidentes de seguridad | Reconstruir la secuencia y los factores en cada punto |
| **Análisis de barreras** | 27001, 45001 | Qué barrera debía existir, cuál falló y por qué |

**Cómo saber que llegaste a la causa raíz:** tres pruebas.

1. Si eliminas esa causa, ¿el problema deja de ser posible? Si la respuesta es "quizás", sigue.
2. ¿Es algo que la organización **controla**? "El proveedor falló" no es causa raíz: la causa raíz es que no había control de recepción, o que el proveedor no fue evaluado.
3. ¿Deja de ser una persona? **"Falta de atención del operador" nunca es causa raíz.** Es el síntoma. La causa está en la formación, el diseño de la tarea, la carga de trabajo, la falta de verificación o la ausencia de un control. Si el análisis termina en una persona, no terminó.

Y una pregunta que casi nadie hace y que las normas sí piden: **¿existe esta misma no conformidad en otro proceso o área?** Si el análisis reveló una debilidad sistémica, la acción tiene que alcanzar a todos los puntos afectados, no solo al que se detectó.

### Paso 4 — Definir la acción correctiva

Concreta, con responsable y fecha. Y proporcionada a la magnitud del problema — las normas lo dicen explícitamente: no se justifica un proyecto de seis meses por un formulario mal llenado una vez.

Señal de alarma: **si la acción correctiva es "capacitar" o "recordar al personal", casi nunca es suficiente.** La capacitación es válida cuando la causa es realmente falta de competencia; si la causa es un proceso que permite el error, capacitar solo posterga la repetición. La acción robusta cambia el sistema, no la memoria de la gente.

### Paso 5 — Verificar la eficacia

El paso que cierra el ciclo y el que más se omite. Verificar eficacia **no es** confirmar que la acción se ejecutó: es comprobar que **el problema no volvió**.

Necesita:
- Un **criterio** definido de antemano ("cero recurrencias en los próximos 3 meses", "100 % de las órdenes con evaluación previa en la siguiente muestra de 10").
- Un **plazo** razonable: suficiente para que el problema hubiera tenido oportunidad de reaparecer.
- Una **evidencia** de la verificación, con fecha y quién la hizo.

Si la verificación falla, la NC **se reabre** o se abre una nueva con el aprendizaje. Eso no es un fracaso del sistema; es el sistema funcionando.

### Paso 6 — Cerrar y aprender

Cerrar significa: corrección hecha, causa analizada, acción implementada, eficacia verificada, documentado todo.

Y después: ¿hay que **actualizar algo**? La matriz de riesgos, un procedimiento, la matriz de competencias, un indicador. Las normas piden explícitamente que se actualicen los riesgos y oportunidades si es necesario, y que se determinen cambios al sistema. Es la conexión entre 10.2 y 6.1 que casi nadie hace y que le da coherencia real al sistema.

### Paso 7 — Casos especiales

**45001 — investigación de incidentes.** La 10.2 incluye incidentes, no solo NC. Un incidente (con o sin lesión) exige investigación con participación de los trabajadores. Los cuasi-accidentes se registran e investigan igual: son la advertencia gratuita antes del accidente real.

**27001 — incidentes de seguridad.** Van por el proceso de gestión de incidentes (`A.5.24`–`A.5.28`). Los que revelan una debilidad del SGSI **además** entran como NC. `A.5.27` exige aprendizaje a partir de los incidentes: es literalmente esta skill aplicada.

**20000-1 — problemas.** La gestión de problemas (8.6.3) es análisis de causa raíz con otro nombre. Un problema que revela una falla del SGS entra también como NC. No dupliques el análisis: referencia el registro del problema desde la NC.

**14001 / 45001 — incumplimiento legal.** Un incumplimiento detectado en la evaluación de cumplimiento (9.1.2) **es** una no conformidad y se gestiona como tal. Es de las que el auditor busca activamente.

---

## 4. El entregable

| Documento | Cláusula |
|---|---|
| `COM-PR-00X Procedimiento de no conformidades, acciones correctivas y mejora` | 10 |
| `COM-R-001 Registro único de NC/AC/OM` (planilla, con columna de norma) | 10.2 / 10.1 |
| `COM-F-00X Ficha de análisis de causa raíz` | 10.2 / 10.1 |
| `SST-F-00X Ficha de investigación de incidentes` | 45001 10.2 |

---

## 5. Lo que revisa el auditor

- Que el registro **exista y tenga movimiento**. Cero NC en un año es señal roja, no de excelencia.
- Que se distinga **corrección de acción correctiva** en cada caso.
- Que el **análisis de causa sea real** y no termine en "falta de atención del personal".
- Que exista **verificación de eficacia** con criterio, fecha y evidencia — no solo la casilla "cerrado".
- Que las NC de la **auditoría anterior estén cerradas**. Una NC abierta del año pasado escala a mayor.
- Que se haya evaluado si la NC **existe en otras áreas**.
- Que los **plazos comprometidos se cumplan** o que las prórrogas estén justificadas.
- En 45001: evidencia de **participación de los trabajadores** en la investigación de incidentes.

---

## 6. Errores que se repiten

- **Cerrar con la corrección** y llamarla acción correctiva.
- **Causa raíz que termina en una persona.** No es causa, es síntoma.
- **"Capacitar al personal"** como acción correctiva universal.
- **No verificar la eficacia**, o verificarla el mismo día que se implementó la acción.
- **Registros separados por norma.** Multiplica el trabajo y esconde los patrones.
- **Registro vacío.** Interpretado, correctamente, como sistema que no se usa.
- **NC arrastradas** de un año a otro sin justificación.
- **No revisar si el problema existe en otras áreas.**
- **No actualizar la matriz de riesgos** cuando la NC reveló un riesgo no considerado.
- Citar **10.2** en un informe de 22301 o 20000-1 (allí es 10.1).

---

## 7. Límites

- El análisis de causa raíz requiere honestidad organizacional. En una cultura donde la NC se usa para castigar, la gente deja de reportar y el registro se vuelve ficción. Eso no lo arregla un procedimiento: lo arregla la dirección.
- Esta skill no reproduce el texto de las normas.
- Los incidentes de SST tienen obligaciones legales de reporte propias de cada país que **no** se agotan con lo que pide 45001. En Chile, la Ley 16.744 y sus reglamentos mandan sobre esto y tienen plazos propios.
