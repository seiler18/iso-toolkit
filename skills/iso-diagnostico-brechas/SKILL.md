---
name: iso-diagnostico-brechas
description: Diagnóstico de brechas (gap analysis) contra una o varias normas ISO de sistemas de gestión. Produce un informe con el estado real cláusula por cláusula y un plan de acción priorizado. Úsala SIEMPRE antes de escribir documentación.
normas: [9001, 14001, 45001, 27001, 22301, 20000-1]
entrega: Informe de brechas (Markdown) + plan de acción priorizado (CSV/tabla)
---

# Diagnóstico de brechas

## 1. Cuándo usar esta skill

- Una organización quiere certificarse y no sabe por dónde empezar.
- Ya tiene una certificación y quiere sumar otra (aquí es donde más valor entrega: la mitad del trabajo ya está hecho y nadie lo sabe).
- Va a haber auditoría de vigilancia o recertificación y hay que saber qué falta.
- Cambió la edición de la norma y hay que ver el delta.

**Cuándo NO usarla:** cuando el cliente ya tiene un diagnóstico reciente y lo que necesita es ejecutar. Rehacer el diagnóstico es la forma más elegante de no avanzar.

---

## 2. Qué necesitas antes de empezar

Sin esto el diagnóstico es adivinanza:

| Entrada | Por qué |
|---|---|
| **Normas objetivo** y su edición exacta | La numeración cambia entre ediciones y entre normas (ver `datos/catalogo_normas.json` → `trampas_de_numeracion`) |
| **Alcance pretendido**: qué sedes, qué procesos, qué servicios | Sin alcance no se sabe qué se audita |
| **Tamaño y sector** | Determina la profundidad razonable. Una pyme de 12 personas no necesita el sistema de una minera |
| **Documentación existente**, aunque esté mala o incompleta | El 60 % de las pymes ya tiene algo: manuales, procedimientos, planillas |
| **Si hay certificaciones vigentes** y de qué organismo | Si ya hay una, el tronco común ya existe |
| **Quién es el responsable interno** y cuántas horas tiene | Determina si el plan es de 6 meses o de 18 |

Si falta el alcance, **páralo y pídelo**. Todo lo demás se puede estimar; el alcance no.

---

## 3. El método

### Paso 1 — Cargar la estructura de referencia

Lee de `datos/catalogo_normas.json` las cláusulas 4 a 10 de cada norma objetivo y su lista de información documentada obligatoria. Ese es el eje del diagnóstico: **una fila por cláusula**, no por documento. El auditor recorre la norma en orden; el diagnóstico también.

Si son varias normas, usa la vista integrada: agrupa primero las cláusulas `tronco: comun` (se evalúan una vez para todas) y después las `propio` de cada norma. Evaluar seis veces "¿tienen política?" es lo que hace que estos informes salgan de 300 páginas y nadie los lea.

### Paso 2 — Recolectar evidencia, no opiniones

Para cada cláusula, buscar **el documento o el registro**, no la declaración de intenciones. Tres fuentes, en este orden de confiabilidad:

1. **El registro** (lo que efectivamente pasó: un acta firmada, un ticket cerrado, una medición).
2. **El documento** (lo que dice que va a pasar: un procedimiento, una política).
3. **La entrevista** (lo que la gente cree que pasa). Útil para detectar el hueco entre 1 y 2, nunca como evidencia única.

> Regla práctica: si el responsable tarda más de 5 minutos en encontrarlo, para efectos de auditoría **no existe**. Anótalo como brecha de control documental (7.5) aunque el documento aparezca.

### Paso 3 — Puntuar con una escala corta

Escalas de 1 a 10 producen discusiones inútiles. Usa cuatro estados:

| Estado | Significa | Qué implica |
|---|---|---|
| ✅ **Conforme** | Existe, está implementado y hay evidencia reciente | Nada que hacer |
| 🟡 **Parcial** | Existe pero incompleto, desactualizado o sin evidencia de uso | Corregir, no crear |
| 🔴 **Ausente** | No existe | Crear desde cero |
| ⚪ **No aplica** | Excluido con justificación | **Documentar la justificación**, o el auditor lo convierte en no conformidad |

El ⚪ es el que más se abusa. Solo 9001 8.3 (diseño y desarrollo) admite exclusión limpia; en 27001 la no aplicabilidad de un control va justificada en la SoA. Todo lo demás aplica.

### Paso 4 — Priorizar por riesgo de certificación, no por esfuerzo

Ordena las brechas en tres bandas:

- **🚨 Bloqueante** — sin esto no hay certificación posible. Típicamente: alcance, política, apreciación de riesgos, SoA (27001), auditoría interna ejecutada, revisión por la dirección ejecutada, registro de NC/AC.
- **⚠️ Mayor** — genera no conformidad mayor en auditoría. Un requisito documentado obligatorio ausente, o un proceso completo sin evidencia.
- **📋 Menor** — genera observación u oportunidad de mejora. Formatos, trazabilidad parcial, coherencia entre documentos.

**El criterio de orden es el tiempo de maduración, no la dificultad.** La auditoría interna y la revisión por la dirección exigen que el sistema lleve meses operando: son lo primero que hay que planificar aunque sean lo último que se ejecuta. Un cliente que deja eso para el final se atrasa un trimestre entero, siempre.

### Paso 5 — Estimar y calendarizar

Para cada brecha: esfuerzo en horas-persona, responsable, fecha objetivo. Sin las tres cosas es una lista de deseos.

Referencia realista para una pyme (10-80 personas), una sola norma, un responsable interno con ~10 h/semana:

| Fase | Duración típica |
|---|---|
| Documentación del tronco común | 2-3 meses |
| Documentación específica de la norma | 1-2 meses |
| Operación del sistema generando evidencia | **mínimo 3 meses, y no se puede acelerar** |
| Auditoría interna + acciones correctivas | 1 mes |
| Revisión por la dirección | 2 semanas |
| Auditoría de certificación (Fase 1 + Fase 2) | 1-2 meses según agenda del organismo |

Total honesto: **9 a 14 meses**. Cada norma adicional simultánea suma 2-3 meses, no el doble. Si alguien promete 3 meses, está vendiendo papel, no un sistema.

### Paso 6 — Escribir el informe

Ver estructura abajo. Regla de redacción: **cada brecha se describe por lo que falta demostrar, no por el documento que falta**. "No hay evidencia de que se evalúe el cumplimiento legal ambiental (9.1.2)" es útil. "Falta el procedimiento PR-014" no lo es: presupone una solución.

---

## 4. El entregable

```markdown
# Diagnóstico de brechas — <organización> — <normas> — <fecha>

## 1. Resumen ejecutivo            (1 página, para gerencia)
   - Estado global: X% conforme, Y% parcial, Z% ausente
   - Las 5 brechas bloqueantes
   - Plazo realista estimado hasta estar en condiciones de auditar
   - Esfuerzo total estimado en horas-persona

## 2. Alcance del diagnóstico
   - Qué se evaluó, qué no, y con qué evidencia
   - Personas entrevistadas (cargos, no nombres)
   - Limitaciones del diagnóstico

## 3. Resultados por cláusula
   ### 3.1 Tronco común (aplica a todas las normas del alcance)
   | Cláusula | Requisito | Estado | Evidencia encontrada | Brecha |
   ### 3.2 Específico de <norma>
   | Cláusula | Requisito | Estado | Evidencia encontrada | Brecha |

## 4. Plan de acción priorizado
   | # | Brecha | Banda | Acción | Responsable | Horas | Fecha objetivo | Cláusulas que cierra |

## 5. Quick wins
   Lo que se puede cerrar en menos de 4 horas. Sirve para que el proyecto
   arranque con movimiento visible en la primera semana.

## 6. Anexo: matriz de reaprovechamiento
   Solo si hay más de una norma o ya existe una certificación:
   qué documento existente sirve para qué cláusula de qué norma.
```

El **anexo 6 es el que vende**. Es donde el cliente ve que su segunda certificación no cuesta lo mismo que la primera.

---

## 5. Lo que revisa el auditor

En la auditoría real, el orden de lo que se pide es bastante estable:

1. **Alcance** (4.3) — y si es coherente con lo que la empresa realmente hace.
2. **Política** (5.2) — firmada, vigente, comunicada. Pregunta a un operario si sabe que existe.
3. **Objetivos** (6.2) — medibles y con seguimiento real, no tres frases bonitas.
4. **La matriz de riesgos** propia de la norma (6.1.2) — que exista, que esté actualizada, que se vea que se usó para decidir algo.
5. **Información documentada** (7.5) — la lista maestra, el control de versiones, y que lo publicado sea lo vigente.
6. **La cláusula 8 completa** — con evidencia operativa, no con procedimientos.
7. **Auditoría interna** (9.2) — programa, competencia e imparcialidad del auditor, informe, hallazgos.
8. **Revisión por la dirección** (9.3) — acta con **todas** las entradas exigidas.
9. **NC/AC** (10) — que estén cerradas con análisis de causa y verificación de eficacia.

Ese orden es el guion del diagnóstico también. Si evalúas en ese orden, el informe se lee como se audita.

---

## 6. Errores que se repiten

- **Diagnosticar contra documentos y no contra evidencia.** Tener el procedimiento no es cumplir. La pregunta es "muéstrame la última vez que lo hiciste".
- **Evaluar seis veces lo mismo** en sistemas multinorma. Agrupa el tronco común o el informe se vuelve ilegible.
- **Puntuar con porcentajes falsos.** "Cumplimos al 73 %" no significa nada si el 27 % restante es la SoA.
- **Marcar ⚪ No aplica sin justificación escrita.** Es no conformidad casi garantizada.
- **Olvidar que 9.2 y 9.3 necesitan tiempo, no trabajo.** Se planifican al inicio aunque se ejecuten al final.
- **Confundir el requisito con la solución.** El diagnóstico dice qué falta demostrar; la implementación decide cómo.
- **Citar mal la cláusula en sistemas integrados.** Revisa `trampas_de_numeracion` antes de escribir: la 10.2 no es lo mismo en 9001 que en 22301.

---

## 7. Límites

- Un diagnóstico **no es una auditoría** y no debe llamarse así. Es un servicio de consultoría; una auditoría de certificación la hace un organismo acreditado bajo ISO/IEC 17021-1.
- Quien hace el diagnóstico y luego implementa **no puede después auditar** esa organización. Ni interna ni externamente. Ni gratis.
- El diagnóstico no garantiza la certificación. Reduce sorpresas; no las elimina.
- No sustituye a la norma. Para implementar hay que comprarla.
