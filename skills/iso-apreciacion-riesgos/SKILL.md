---
name: iso-apreciacion-riesgos
description: Define una metodología única de apreciación de riesgos para todo el SGI y construye las matrices que cada norma exige por separado (aspectos ambientales, peligros SST, riesgos de seguridad de la información, riesgos de continuidad). Una metodología, varias matrices.
normas: [9001, 14001, 45001, 27001, 22301, 20000-1]
entrega: Metodología de riesgos (documento) + matrices por norma (CSV/planilla) + plan de tratamiento
---

# Apreciación de riesgos multinorma

## 1. Cuándo usar esta skill

En cuanto existan el contexto (4.1), las partes interesadas (4.2) y el alcance (4.3). Antes no: un riesgo sin alcance definido es una lista de miedos.

También cuando el sistema existente tiene **cuatro metodologías distintas** porque cada norma la escribió una persona diferente. Es el desorden más común en sistemas integrados y el más fácil de arreglar.

---

## 2. Qué necesitas antes de empezar

- Contexto, partes interesadas y alcance ya escritos.
- Mapa de procesos con dueños.
- Para 14001: qué entra, qué sale y qué se emite en cada proceso.
- Para 45001: las tareas reales, no las del descriptor de cargo. Y el CPHS, si existe.
- Para 27001: inventario de activos de información (o al menos de procesos y sistemas).
- Para 22301: qué productos y servicios son críticos y para quién.
- Apetito de riesgo de la dirección. Si no lo han pensado, hay que hacérselo pensar: sin criterio de aceptación no hay tratamiento posible.

---

## 3. El método

### Paso 1 — Una metodología, cuatro aplicaciones

Lo que **sí** se unifica en un solo documento:

| Elemento | Decisión |
|---|---|
| Escala de probabilidad | 1-5, con definición verbal de cada nivel (no solo el número) |
| Escala de impacto | 1-5, con criterios **por dimensión**: económico, legal, personas, ambiente, información, servicio, reputación |
| Fórmula de nivel de riesgo | Normalmente P × I. Si usas otra, justifícala |
| Bandas y criterio de aceptación | Ej.: 1-4 aceptable · 5-9 tolerable con seguimiento · 10-14 tratar · 15-25 tratar de inmediato |
| Opciones de tratamiento | Evitar · reducir · compartir/transferir · aceptar |
| Frecuencia de revisión | Anual como mínimo, y ante cambios significativos |
| Roles | Quién identifica, quién valora, quién aprueba el riesgo residual |

Lo que **no** se unifica: las matrices. Son cuatro registros distintos porque las cláusulas son distintas (ver `catalogo_normas.json` → `trampas_de_numeracion` → "Cláusula 6.1.2").

> **La escala de impacto es donde se decide todo.** Si "impacto 5" no está definido con criterios concretos por dimensión (ej. "pérdida > X UF", "lesión con tiempo perdido", "indisponibilidad > 8 h", "fuga de datos personales"), cada persona valora distinto y la matriz deja de servir para decidir.

### Paso 2 — Riesgos y oportunidades del sistema (6.1.1) — el nivel que se olvida

Antes de las matrices técnicas, todas las normas piden riesgos y oportunidades **del sistema de gestión**, derivados del contexto y las partes interesadas. No son peligros ni amenazas: son cosas como "rotación del único encargado de calidad", "dependencia de un cliente que representa el 60 % de la facturación", "cambio regulatorio previsto".

Salen directo del FODA: **cada debilidad y cada amenaza es un riesgo candidato; cada fortaleza y cada oportunidad, una oportunidad candidata.** Se registran en una tabla simple con acción, responsable y plazo. Es media jornada de trabajo y cierra una cláusula que se marca ausente en la mitad de los diagnósticos.

### Paso 3 — Las matrices propias

#### 14001 6.1.2 — Aspectos ambientales
Recorrido por proceso: **entradas → actividad → salidas**. Por cada salida, el aspecto (consumo, emisión, vertido, residuo, ruido) y su impacto. Valorar con los criterios de significancia definidos y **declarar cuáles son significativos** — eso es lo que la norma exige documentar.

No olvidar: condiciones **anormales** (mantenimiento, arranque/parada) y **de emergencia** (derrame, incendio). Y la perspectiva de ciclo de vida: qué pasa aguas arriba y aguas abajo de tu proceso, aunque no lo controles.

#### 45001 6.1.2 — Identificación de peligros y evaluación de riesgos
Por **tarea real**, con participación de los trabajadores (5.4 lo exige y el auditor busca la evidencia: firmas, actas del CPHS, registro del taller).

Peligros que se olvidan sistemáticamente: ergonómicos, psicosociales, trabajo en solitario, contratistas y visitas, desplazamientos, y situaciones de emergencia.

El tratamiento **debe seguir la jerarquía de controles** (8.1.2), en este orden: eliminar → sustituir → controles de ingeniería → controles administrativos → EPP. Si la matriz propone EPP para todo, es hallazgo: el EPP es el último recurso, no el primero.

#### 27001 6.1.2 — Riesgos de seguridad de la información
Dos enfoques válidos; elige uno y sé consistente:

- **Por activo**: activo → amenaza → vulnerabilidad → riesgo sobre C/I/D. Más trazable, más pesado.
- **Por escenario**: escenario de riesgo → procesos y activos afectados. Más ágil, mejor para pymes.

Cada riesgo necesita **propietario** (5.3 y 6.1.2 lo exigen explícitamente) y valoración sobre **confidencialidad, integridad y disponibilidad** por separado. El tratamiento se conecta con los controles del Anexo A → alimenta la [SoA](../iso-declaracion-aplicabilidad/SKILL.md).

⚠️ La secuencia correcta es **riesgos → controles → SoA**. Al revés (elegir controles y después inventar riesgos que los justifiquen) se nota y es hallazgo.

#### 22301 8.2.3 — Riesgos de continuidad
Ojo con el número: en 22301 la apreciación de riesgos de continuidad está en **8.2.3**, no en 6.1.2. Se hace **después del BIA** y sobre las actividades priorizadas por él: qué puede interrumpir lo que ya sabemos que es crítico. Ver [`iso-bia-continuidad`](../iso-bia-continuidad/SKILL.md).

#### 20000-1
No exige matriz propia: usa 6.1 con foco en riesgos a los servicios y a los niveles acordados. Se apoya en la de 27001 y en la de continuidad.

### Paso 4 — Plan de tratamiento

Una sola tabla para todas las normas, con columna "norma":

| ID | Norma | Riesgo | P | I | Nivel | Opción | Acción / control | Responsable | Plazo | Riesgo residual | Aprobado por |

El **riesgo residual** y **quién lo aceptó** son las dos columnas que casi nunca están y las dos que el auditor busca. En 27001 la aceptación del riesgo residual por parte del propietario del riesgo es requisito explícito.

### Paso 5 — Cerrar el ciclo

Una matriz que se hizo una vez y nunca se tocó es peor que no tenerla: demuestra que el sistema no está vivo. Define y **cumple** la frecuencia de revisión, y deja rastro de las revisiones aunque no cambie nada ("revisada el 2026-08-16, sin cambios, firma").

---

## 4. El entregable

1. **`COM-PR-00X Metodología de apreciación de riesgos`** — escalas, criterios, bandas, tratamiento, roles, frecuencia. Una sola para todo el SGI.
2. **`COM-M-001 Riesgos y oportunidades del sistema`** (6.1.1) — desde el FODA.
3. **Una matriz por norma aplicable**, cada una con su formato propio.
4. **`COM-M-00X Plan de tratamiento`** — unificado, con columna de norma.
5. **Registro de revisiones** de las matrices.

---

## 5. Lo que revisa el auditor

- Que la metodología esté escrita y que **las matrices la sigan de verdad** (misma escala, mismas bandas). Metodología que dice 1-5 y matriz que usa alto/medio/bajo: hallazgo inmediato.
- Que los criterios de aceptación estén definidos y **aprobados por la dirección**.
- Que cada riesgo tenga **propietario**.
- Que la matriz esté **actualizada** y se vea que sirvió para decidir algo.
- En 45001: evidencia de la **participación de los trabajadores** en la identificación de peligros.
- En 45001: que el tratamiento respete la **jerarquía de controles**.
- En 14001: que los aspectos **significativos** estén declarados como tales y tengan control operacional asociado.
- En 27001: **riesgo residual aceptado formalmente** por el propietario, y coherencia matriz ↔ SoA.

---

## 6. Errores que se repiten

- **Cuatro metodologías distintas** en un mismo sistema integrado.
- **Fusionar las matrices** en una sola. Son cláusulas distintas y el auditor las pide por separado.
- Escala de impacto **sin criterios verbales**. Números sin definición no son medición.
- Matrices donde **todo es riesgo medio**. Señal de que nadie valoró en serio.
- **Copiar la matriz de otra empresa.** Los peligros de una constructora no son los de un software factory. Y si la copia viene de una organización real, hay un problema adicional.
- **45001 sin participación de trabajadores** documentada.
- **27001 al revés**: elegir controles primero y fabricar riesgos que los justifiquen.
- **Sin riesgo residual ni aprobación.** Es la columna que cierra el ciclo.
- Confundir **6.1.1** (riesgos del sistema) con las matrices técnicas. Son cosas distintas y ambas se piden.

---

## 7. Límites

- La metodología es genérica. Sectores regulados (minería, salud, alimentos, banca) tienen metodologías obligatorias por ley que mandan sobre esta.
- No sustituye la evaluación de riesgos exigida por la legislación laboral o ambiental de cada país. En Chile, la matriz de 45001 **no reemplaza** las obligaciones de la Ley 16.744 y su reglamentación.
- No reproduce el texto de las normas.
