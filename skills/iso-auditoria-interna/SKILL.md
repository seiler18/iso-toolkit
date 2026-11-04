---
name: iso-auditoria-interna
description: Ciclo completo de auditoría interna para una o varias normas - programa anual, plan de auditoría, listas de verificación por cláusula, ejecución, redacción de hallazgos e informe. Un solo programa integrado para todo el SGI.
normas: [9001, 14001, 45001, 27001, 22301, 20000-1]
entrega: Programa anual + plan por auditoría + listas de verificación + informe con hallazgos
---

# Auditoría interna

## 1. Cuándo usar esta skill

- Al planificar el año del sistema de gestión (el programa se arma en enero, no en octubre).
- Antes de una auditoría de certificación, vigilancia o recertificación. **Es requisito**: sin auditoría interna ejecutada y con evidencia, no hay certificación.
- Cuando la organización quiere saber, sin presión externa, cómo está de verdad.

> El requisito 9.2 no se cumple con una auditoría hecha la semana anterior a la externa. El auditor mira las fechas y saca sus conclusiones.

---

## 2. Qué necesitas antes de empezar

- Normas del alcance y su edición.
- Mapa de procesos con dueños.
- Resultados de la auditoría anterior y estado de sus hallazgos.
- Estado del sistema: matrices, indicadores, NC abiertas.
- **Auditores internos competentes e imparciales.** Sin esto no se puede empezar. Ver Paso 2.

---

## 3. El método

### Paso 1 — El programa anual (9.2.2): uno solo para todas las normas

El programa es plurianual o anual y cubre **todo el sistema**, no una norma a la vez. Debe considerar:

- La **importancia de los procesos** — los críticos se auditan con más frecuencia.
- Los **cambios** desde la última auditoría — proceso nuevo, sede nueva, sistema nuevo, reestructuración.
- Los **resultados anteriores** — donde hubo hallazgos, se vuelve antes.

Formato mínimo:

| Nº | Proceso / área | Normas y cláusulas | Fecha planificada | Auditor | Auditado | Estado |

**Cobertura obligatoria:** todas las cláusulas de todas las normas del alcance, en todos los procesos aplicables, **dentro del ciclo del programa** (normalmente 1 año, 3 como máximo si está justificado). Un hueco de cobertura es hallazgo automático: el auditor externo cruza el programa contra la norma y ve qué falta.

**Truco de eficiencia real:** audita **por proceso, no por norma**. En una visita al área de operaciones se cubre 9001 8.5, 14001 8.1, 45001 8.1, 27001 A.8.x y 20000-1 8.6 con las mismas preguntas. Auditar seis veces la misma área, una por norma, es lo que hace que nadie quiera recibir al auditor interno.

### Paso 2 — Auditores: competencia e imparcialidad

Los dos requisitos que más se incumplen en pymes, y los dos que se revisan primero.

**Competencia**: formación en la norma y en técnicas de auditoría (referencia: ISO 19011), más conocimiento suficiente del proceso. Se evidencia con certificados y con un perfil de auditor definido.

**Imparcialidad**: `un auditor no audita su propio trabajo`. Sin excepciones. En una empresa de 15 personas esto se resuelve con:
- Auditoría cruzada entre áreas (el de operaciones audita administración y viceversa).
- Un auditor externo contratado **solo para la auditoría interna** — es legítimo y frecuente.
- Un equipo mixto: alguien de fuera lidera, alguien de dentro acompaña.

⚠️ **Límite de este proyecto:** quien implementó o asesoró el sistema **no puede auditarlo**, ni siquiera como auditor interno contratado. Es un conflicto de interés bajo ISO/IEC 17021-1 y es motivo de cuestionamiento del certificado.

### Paso 3 — El plan de cada auditoría

Se envía al auditado **con anticipación** (una o dos semanas). Contiene: objetivo, alcance, criterios (normas y cláusulas, documentos internos, requisitos legales), fechas y horarios por área, auditores, y método (entrevista, observación, revisión documental, muestreo).

Nada de auditorías sorpresa en el sistema de gestión. La sorpresa es para el fraude, no para la mejora.

### Paso 4 — Listas de verificación

Se generan desde [`../../datos/catalogo_normas.json`](../../datos/catalogo_normas.json), una fila por cláusula:

| Cláusula | Qué debe demostrar | Pregunta de auditoría | Evidencia solicitada | Resultado | Observaciones |

**Cómo se escribe una buena pregunta de auditoría:**

| ⛔ Cerrada e inútil | ✅ Abierta y verificable |
|---|---|
| "¿Tienen procedimiento de compras?" | "Muéstrame cómo evaluaron al último proveedor que incorporaron." |
| "¿Se hacen las capacitaciones?" | "¿Cómo sabes que esta persona es competente para esta tarea? Muéstrame." |
| "¿Conocen la política?" | "¿Qué parte de la política se aplica a lo que tú haces?" |
| "¿Se respaldan los datos?" | "¿Cuándo fue la última restauración de prueba y qué resultado dio?" |

La regla es siempre la misma: **pedir la evidencia, no la afirmación.** Y elegir la muestra tú, no aceptar la que te ofrecen.

Genera la base con:
```bash
python scripts/iso_sgi.py checklist --normas 9001,14001,45001 --salida ./checklist.csv
```

### Paso 5 — Ejecutar

- **Reunión de apertura**: confirmar plan, alcance, horarios, criterios de hallazgo y confidencialidad. 15 minutos.
- **Recolección**: entrevistar a quien hace el trabajo, no solo al jefe. Observar la operación real. Revisar registros por muestreo. Anotar la evidencia con identificación precisa (documento, código, fecha, número de registro) — sin eso el hallazgo no se sostiene después.
- **Verificar contra el criterio**, no contra tu opinión de cómo debería hacerse. Un proceso que no te gusta pero cumple el requisito **es conforme**. Este es el error más común del auditor novato y el que destruye la relación con las áreas.
- **Reunión de cierre**: presentar los hallazgos ese mismo día, sin sorpresas posteriores. Confirmar que el auditado entiende cada uno. No negociar la existencia del hallazgo; sí aclarar la redacción.

### Paso 6 — Redactar hallazgos con la fórmula de tres partes

Todo hallazgo tiene exactamente tres componentes. Si falta uno, no se sostiene:

```
REQUISITO  — qué exige la norma o el documento interno (cláusula citada)
EVIDENCIA  — qué se observó, con identificación precisa
DESVIACIÓN — por qué lo observado no cumple el requisito
```

**Ejemplo:**
> **Requisito:** ISO 9001:2015, 8.4.1 — la organización debe conservar información documentada de la evaluación y reevaluación de los proveedores externos.
> **Evidencia:** en la muestra de tres proveedores incorporados en 2026 (PRV-041, PRV-043, PRV-047), no se encontró registro de evaluación previa. El procedimiento COM-PR-008 v2 exige ficha de evaluación firmada antes de la primera orden de compra.
> **Desviación:** se incorporaron proveedores sin la evaluación previa exigida por el propio procedimiento y por la cláusula 8.4.1.

Clasificación:

| Tipo | Criterio |
|---|---|
| **No conformidad mayor** | Ausencia total de un requisito · falla sistémica · falla que afecta la capacidad del sistema de lograr resultados · varias menores del mismo requisito |
| **No conformidad menor** | Falla puntual y aislada que no compromete el sistema |
| **Observación** | Cumple, pero hay riesgo de dejar de cumplir |
| **Oportunidad de mejora** | Cumple; se puede hacer mejor. **No es obligatoria de atender** — y hay que decirlo, o se convierte en una carga inventada |

⚠️ **Cita bien la cláusula.** En sistemas integrados, "10.2 no conformidades" es correcto en 9001, 14001, 45001 y 27001, pero en 22301 y 20000-1 la 10.2 es "Mejora continua". Consulta `trampas_de_numeracion` en el JSON antes de escribir. Una cita errada le da al auditado la excusa perfecta para rechazar el hallazgo.

### Paso 7 — El informe

```
1. Datos: fechas, alcance, criterios, auditores, auditados
2. Resumen ejecutivo: cuántos hallazgos, de qué tipo, la conclusión en un párrafo
3. Conclusión sobre la eficacia del sistema  ← entrada obligatoria de 9.3
4. Hallazgos detallados (los tres componentes, uno por uno)
5. Fortalezas observadas   ← no es adorno: sostiene la credibilidad del informe
6. Estado de los hallazgos de la auditoría anterior
7. Anexo: listas de verificación completadas
```

El punto 3 es el que se olvida y el que la revisión por la dirección necesita. No es "se encontraron 7 hallazgos": es "el sistema es eficaz / es parcialmente eficaz / no es eficaz para lograr los resultados previstos, porque…".

### Paso 8 — Seguimiento

Los hallazgos entran al registro único de NC/AC — ver [`iso-no-conformidades`](../iso-no-conformidades/SKILL.md). La auditoría no termina con el informe: termina cuando los hallazgos están **cerrados y verificados**.

---

## 4. El entregable

| Documento | Cláusula |
|---|---|
| `COM-PR-00X Procedimiento de auditoría interna` | 9.2 |
| `COM-PL-001 Programa anual de auditorías` | 9.2.2 |
| `COM-F-00X Plan de auditoría` (uno por auditoría) | 9.2.2 |
| `COM-F-00X Listas de verificación` por norma/proceso | 9.2.2 |
| `COM-R-00X Informe de auditoría interna` | 9.2.2 |
| Registros de competencia de los auditores | 7.2 |

---

## 5. Lo que revisa el auditor externo

1. Que el **programa cubra todas las cláusulas y procesos** del alcance dentro del ciclo.
2. **Competencia de los auditores internos** — pide los certificados.
3. **Imparcialidad** — pregunta directamente quién auditó qué y si audita su propia área.
4. Que las **listas de verificación estén completadas de verdad**, no todas con ✅ y sin una nota.
5. Que los **hallazgos estén bien redactados** y con evidencia identificable.
6. Que el informe incluya la **conclusión sobre la eficacia**.
7. Que los hallazgos estén **cerrados con verificación de eficacia**, no solo "corregido".
8. Que las **fechas sean creíbles**: un programa anual ejecutado íntegramente en tres días la semana previa a la externa es una señal roja.

---

## 6. Errores que se repiten

- **Auditoría interna la semana antes de la externa.** Se nota en las fechas y desacredita todo el sistema.
- **Auditar la propia área.** Incumplimiento directo de 9.2.
- **Listas de verificación todas en verde**, sin una sola observación. Nadie tiene un sistema perfecto; significa que no se auditó.
- **Hallazgos sin evidencia identificable.** "Se observan debilidades en compras" no es un hallazgo, es una opinión.
- **Auditar contra la opinión del auditor** en vez de contra el criterio.
- **Citar mal la cláusula** en sistemas integrados.
- **No cerrar los hallazgos** o cerrarlos con la corrección sin análisis de causa.
- **Seis auditorías separadas, una por norma.** Agota a la organización y multiplica el costo sin agregar valor.
- **Informe sin conclusión sobre la eficacia** — deja coja la revisión por la dirección.
- **Convertir las oportunidades de mejora en obligaciones.** Genera resistencia y no aporta nada.

---

## 7. Límites

- La auditoría interna **no certifica**. La de certificación la hace un organismo acreditado bajo ISO/IEC 17021-1.
- **Quien implementó o asesoró no puede auditar** esa organización. Ni interna ni externamente, ni gratis.
- Esta skill se apoya en los principios de ISO 19011 (directrices para auditoría de sistemas de gestión) pero **no reproduce su texto**. Si vas a formalizar el proceso, adquiérela.
- Una auditoría interna impecable no garantiza aprobar la externa. Reduce mucho las sorpresas.
