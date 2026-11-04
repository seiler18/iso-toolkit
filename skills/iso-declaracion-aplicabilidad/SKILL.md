---
name: iso-declaracion-aplicabilidad
description: Construye la Declaración de Aplicabilidad (SoA) de ISO/IEC 27001 - los 93 controles del Anexo A, cada uno con decisión de aplicabilidad, justificación, estado de implementación y evidencia. Es el documento obligatorio y exclusivo de 27001, y el que más se cae en auditoría.
normas: [27001]
entrega: Declaración de Aplicabilidad (CSV/planilla + documento de aprobación)
---

# Declaración de Aplicabilidad (SoA)

## 1. Cuándo usar esta skill

Solo en ISO/IEC 27001. Después de la apreciación y el tratamiento de riesgos — **nunca antes**.

Es el documento que el auditor pide primero, en la Fase 1, y con el que decide si la Fase 2 tiene sentido. También es el que revisa el organismo certificador para fijar el alcance del certificado.

---

## 2. Qué necesitas antes de empezar

| Entrada | Por qué es indispensable |
|---|---|
| Alcance del SGSI (4.3) | La aplicabilidad se juzga **dentro** del alcance |
| Matriz de riesgos con propietarios (6.1.2) | Cada control incluido debe rastrearse a un riesgo |
| Plan de tratamiento de riesgos (6.1.3) | La SoA es la contracara del plan |
| Requisitos legales, contractuales y de clientes | Un control puede entrar por contrato aunque no haya riesgo alto |
| Estado real de implementación de cada control | Sin esto la SoA es una lista de deseos |

Si no hay matriz de riesgos, **no empieces**. Una SoA sin riesgos detrás es exactamente el hallazgo que el auditor busca.

---

## 3. El método

### Paso 1 — Cargar los 93 controles

Desde [`../../datos/catalogo_normas.json`](../../datos/catalogo_normas.json) → `anexo_a_27001.controles`. Edición 2022, cuatro temas:

| Tema | Controles | Cantidad |
|---|---|---|
| A.5 Organizacionales | A.5.1 – A.5.37 | 37 |
| A.6 Personas | A.6.1 – A.6.8 | 8 |
| A.7 Físicos | A.7.1 – A.7.14 | 14 |
| A.8 Tecnológicos | A.8.1 – A.8.34 | 34 |

**Los 11 controles nuevos de 2022** son los que más brechas generan y donde el auditor mira con lupa, porque casi nadie los tenía en la edición 2013: `A.5.7` inteligencia de amenazas · `A.5.23` servicios en la nube · `A.5.30` preparación de las TIC para la continuidad · `A.7.4` vigilancia física · `A.8.9` gestión de configuración · `A.8.10` borrado de información · `A.8.11` enmascaramiento de datos · `A.8.12` prevención de fuga de datos · `A.8.16` actividades de monitorización · `A.8.23` filtrado web · `A.8.28` codificación segura.

> Si vienes migrando desde 27001:2013, esos once son tu lista de trabajo real. El resto es en gran parte reagrupación de controles que ya tenías.

### Paso 2 — Decidir aplicabilidad, control por control

Para cada uno, tres preguntas en este orden:

1. **¿Hay un riesgo dentro del alcance que este control trata?** → si sí, aplica.
2. **¿Lo exige una ley, un contrato o un cliente?** → si sí, aplica **aunque el riesgo sea bajo**. Este es el camino que la gente olvida.
3. **¿Hay una razón estructural y verificable para excluirlo?** → única vía a "no aplica".

Exclusiones que un auditor acepta sin discutir:
- `A.8.4` acceso al código fuente, `A.8.25`–`A.8.31` desarrollo → **si la organización no desarrolla software, ni internamente ni tercerizado**.
- `A.6.7` trabajo a distancia → si no existe teletrabajo en ninguna forma.
- `A.7.x` físicos concretos → si la operación es 100 % en nube y no hay instalaciones propias en el alcance.
- `A.5.21` cadena de suministro TIC → si no hay proveedores TIC. Raro, pero pasa.

Exclusiones que **no** pasan nunca: A.5.1 políticas, A.5.9–A.5.14 gestión de activos e información, A.5.15–A.5.18 accesos, A.5.24–A.5.28 incidentes, A.6.3 concienciación, A.8.7 malware, A.8.8 vulnerabilidades, A.8.13 respaldo. Si aparecen como "no aplica", es no conformidad.

> Regla práctica: en una pyme de servicios TI, lo normal es **85-93 controles aplicables**. Una SoA con 60 aplicables levanta sospecha inmediata y garantiza una Fase 1 larga.

### Paso 3 — Escribir justificaciones que sirvan

La justificación es lo que se audita, no la casilla. Debe ser específica y verificable.

| ⛔ No sirve | ✅ Sirve |
|---|---|
| "Aplica" | "Aplica. Trata los riesgos R-012 y R-018 (acceso no autorizado a datos de clientes en la plataforma de producción)." |
| "No aplica, no corresponde" | "No aplica. La organización no realiza desarrollo de software propio ni externalizado; toda la plataforma es SaaS de terceros. Verificable en el inventario de activos y en el mapa de procesos." |
| "Requisito legal" | "Aplica por la Ley 21.719 de protección de datos personales y por la cláusula 8 del contrato marco con <tipo de cliente>." |

Las justificaciones de **inclusión** pueden ser breves si apuntan a un ID de riesgo. Las de **exclusión** tienen que ser argumentadas: son las que se leen con lupa.

### Paso 4 — Declarar el estado de implementación con honestidad

Cuatro estados, sin medias tintas:

| Estado | Significa |
|---|---|
| ✅ Implementado | Operando y con evidencia |
| 🟡 Parcial | Definido pero incompleto, o sin evidencia suficiente |
| 🔵 Planificado | Con fecha y responsable en el plan de tratamiento |
| ⛔ No implementado | Aplica y no hay nada |

**Declarar "implementado" algo que no lo está es el peor error posible.** El auditor va a pedir la evidencia de una muestra de controles; si no aparece, no es una no conformidad por el control — es una no conformidad por la **integridad de la SoA**, que es mucho más grave y pone en duda el documento entero.

Un control 🔵 planificado con fecha y responsable es perfectamente auditable. Uno ✅ falso, no.

### Paso 5 — Enlazar cada control con su evidencia

Columna con el documento, registro o sistema que lo demuestra: `SEG-PR-004`, `Ticket #4471`, `Consola de EDR — reporte mensual`, `Acta CPHS 2026-03`. Esta columna convierte la SoA en el índice de la auditoría y ahorra horas el día de la visita.

### Paso 6 — Aprobar formalmente

La SoA lleva versión, fecha y aprobación de la dirección o del comité de seguridad. Se actualiza cuando cambia el alcance, la matriz de riesgos o el estado de implementación de un control — **como mínimo una vez al año**.

---

## 4. El entregable

Una planilla con estas columnas, más una portada con alcance, versión, aprobación y criterios de decisión:

| Campo | Contenido |
|---|---|
| `id` | A.5.1 … A.8.34 |
| `tema` | Organizacional / Personas / Físico / Tecnológico |
| `control` | Título del control |
| `aplica` | Sí / No |
| `justificacion` | Argumento específico y verificable |
| `origen` | Riesgo / Legal / Contractual / Buena práctica |
| `riesgos_asociados` | R-012, R-018 |
| `estado` | Implementado / Parcial / Planificado / No implementado |
| `evidencia` | Documento, registro o sistema |
| `responsable` | Cargo |
| `fecha_objetivo` | Solo si no está implementado |

Generarla vacía y lista para llenar:

```bash
python scripts/iso_sgi.py soa --formato csv --salida ./SoA_borrador.csv
```

---

## 5. Lo que revisa el auditor

En este orden, casi siempre:

1. Que la SoA **exista, esté aprobada y versionada**.
2. Que estén **los 93 controles**, sin omisiones. Un control que falta en la lista es no conformidad mayor.
3. Las **justificaciones de exclusión**, una por una.
4. **Coherencia SoA ↔ matriz de riesgos ↔ plan de tratamiento.** Un control incluido "por riesgo" que no aparece en la matriz es un problema.
5. Una **muestra de controles marcados como implementados**: pide la evidencia. Suele elegir los nuevos de 2022 y los que más se falsean (A.8.8 vulnerabilidades, A.8.13 respaldo con prueba de restauración, A.5.18 revisión de derechos de acceso).
6. Que la **fecha de última actualización** sea razonable.

---

## 6. Errores que se repiten

- **Hacer la SoA antes que los riesgos.** Se nota siempre.
- **Excluir controles para reducir el trabajo.** Es el atajo que más caro sale.
- **Justificaciones de una palabra.**
- **Declarar implementado lo que no lo está.** Contamina la credibilidad de todo el documento.
- **Copiar una SoA de plantilla sin decidir nada.** Se detecta porque las justificaciones no mencionan ningún riesgo propio.
- **Olvidar los 11 controles nuevos de 2022** al migrar desde 2013.
- **No actualizarla en un año.** Si el sistema está vivo, la SoA cambia.
- **Confundir la SoA con el plan de tratamiento.** Son dos documentos: la SoA dice *qué controles y por qué*; el plan dice *qué se va a hacer, quién y cuándo*.
- Marcar A.8.13 respaldo como implementado **sin prueba de restauración**. Un respaldo que nunca se restauró no está probado, y el auditor lo sabe.

---

## 7. Límites

- Los títulos de control de este toolkit están en redacción propia en español. **Usa siempre el identificador** (`A.8.12`) para referenciar: es lo único inequívoco entre traducciones y ediciones.
- La guía de implementación detallada de cada control está en ISO/IEC 27002:2022, que hay que adquirir aparte. Esta skill no la reproduce.
- La SoA no certifica nada ni garantiza aprobar. Es requisito, no resultado.
