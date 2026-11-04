---
name: iso-bia-continuidad
description: Análisis de Impacto al Negocio (BIA) y construcción de estrategias, planes y ejercicios de continuidad para ISO 22301. Alimenta también los controles A.5.29-A.5.30 de 27001 y la cláusula 8.7.2 de 20000-1.
normas: [22301, 27001, 20000-1]
entrega: BIA (planilla) + estrategias justificadas + planes de continuidad + programa de ejercicios
---

# BIA y continuidad del negocio

## 1. Cuándo usar esta skill

- Implementación de ISO 22301 (cláusula 8.2 en adelante).
- 27001 con los controles `A.5.29` seguridad durante la interrupción y `A.5.30` preparación de las TIC para la continuidad declarados aplicables — que es casi siempre.
- 20000-1 `8.7.2` gestión de la continuidad del servicio.
- Cuando un cliente grande exige un plan de continuidad como condición contractual (motivo real detrás de la mitad de las implementaciones de 22301).

> **Se documenta una vez y se referencia desde las tres normas.** Es el solapamiento más rentable de todo el mapa de integración: un solo trabajo cierra requisitos en tres sistemas.

---

## 2. Qué necesitas antes de empezar

- Alcance con los **productos y servicios** cubiertos (22301 4.3 lo exige explícitamente).
- Mapa de procesos con dueños.
- **Apetito de riesgo** de la dirección (22301 4.1).
- Dependencias: sistemas, proveedores, personas clave, instalaciones, datos.
- Compromisos contractuales de disponibilidad (SLA, penalidades) y obligaciones legales.
- Acceso a las personas que **operan** los procesos. El BIA no se hace desde un escritorio: se hace preguntando.

---

## 3. El método

### Paso 1 — Entender la secuencia. Este es el orden y no es negociable

```
BIA (8.2.2)  →  Apreciación de riesgos (8.2.3)  →  Estrategias (8.3)
     →  Planes (8.4)  →  Ejercicios (8.5)  →  Evaluación (8.6)
```

El **BIA va primero**. Determina *qué* hay que proteger y *en cuánto tiempo*. Recién entonces la apreciación de riesgos pregunta *qué puede interrumpirlo*. Hacerlo al revés lleva a proteger lo que da miedo en vez de lo que importa.

### Paso 2 — El BIA (8.2.2), actividad por actividad

Se analizan **actividades**, no departamentos. Una actividad es algo que produce una salida identificable ("emitir facturas", "atender la mesa de ayuda", "despachar pedidos").

Por cada actividad, cuatro bloques:

**a) Impacto de la interrupción en el tiempo.** La pregunta clave es cómo crece el daño, no cuánto vale hoy. Se evalúa a distintos cortes: 1 h · 4 h · 8 h · 24 h · 72 h · 1 semana. Dimensiones: financiera, legal/regulatoria, contractual, reputacional, de personas.

Casi siempre el impacto no es lineal: hay un punto donde salta. Encontrar ese salto **es** el BIA.

**b) Los tres parámetros.** Que la gente confunde constantemente:

| Sigla | Qué es | Pregunta que responde |
|---|---|---|
| **MTPD/MTPoD** | Período máximo tolerable de interrupción | ¿A partir de cuándo el daño es inaceptable? |
| **RTO** | Objetivo de tiempo de recuperación | ¿En cuánto tiempo me comprometo a recuperar? |
| **RPO** | Objetivo de punto de recuperación | ¿Cuántos datos puedo perder? |

Regla que se viola siempre: **RTO < MTPD.** Si tu RTO es igual al MTPD, no tienes margen y el plan falla la primera vez. Y el RPO manda sobre la frecuencia de respaldo: RPO de 1 hora con respaldo diario es una contradicción escrita.

**c) Dependencias.** Qué necesita esa actividad para funcionar: personas (¿cuántas mínimo? ¿hay una sola que sabe?), sistemas, datos, instalaciones, proveedores, servicios básicos. **Las dependencias cruzadas son lo que hunde los planes**: la actividad A tiene RTO de 4 h pero depende de la actividad B que tiene RTO de 24 h.

**d) Recursos mínimos de operación.** Con cuánto se puede operar en modo degradado. No "todo lo normal": el mínimo viable.

### Paso 3 — Priorizar

Ordenar las actividades por MTPD ascendente. Las de MTPD más corto son las **actividades priorizadas** — el término que usa la norma y el que el auditor espera oír. Todo lo que viene después se hace **solo sobre ellas**. Un BIA que concluye que las 40 actividades son críticas no priorizó nada.

### Paso 4 — Apreciación de riesgos de continuidad (8.2.3)

Sobre las actividades priorizadas: qué escenarios pueden interrumpirlas. Escenarios, no causas exhaustivas — lo que importa es el **efecto**:

- Pérdida de instalaciones (incendio, inundación, sismo, inaccesibilidad)
- Pérdida de sistemas o datos (falla, ciberataque, ransomware, caída de proveedor cloud)
- Pérdida de personas (enfermedad masiva, renuncia de persona clave, huelga)
- Pérdida de proveedores críticos
- Pérdida de servicios básicos (energía, conectividad, agua)

Planificar por efecto y no por causa es lo que hace que un plan sirva para el evento que nadie previó. Usa la metodología única definida en [`iso-apreciacion-riesgos`](../iso-apreciacion-riesgos/SKILL.md).

### Paso 5 — Estrategias y soluciones (8.3)

Por cada actividad priorizada, una estrategia que cumpla su RTO, con **justificación documentada** de por qué esa y no otra — la norma exige la justificación, no solo la elección.

Familias de estrategia: redundancia (activo-activo, activo-pasivo) · sitio alternativo (propio, contratado, remoto) · trabajo manual degradado · tercerización temporal · postergación aceptada · seguros (que **no** son una estrategia de continuidad: transfieren el costo, no recuperan el servicio).

Y por cada estrategia, los **recursos requeridos** (8.3.4): personas, tecnología, información, instalaciones, proveedores, presupuesto. Una estrategia sin presupuesto asignado no es una estrategia; es una intención.

### Paso 6 — Planes de continuidad (8.4)

Un plan **operativo**, no un ensayo. Debe poder ejecutarlo alguien estresado, a las 3 de la mañana, posiblemente sin el titular del cargo. Contenido mínimo:

1. **Criterios y autoridad de activación** — quién declara la contingencia y con qué gatillo objetivo. Sin esto, nadie activa nada por miedo a equivocarse.
2. **Estructura de respuesta (8.4.2)** — roles, no nombres, con al menos un suplente por rol.
3. **Alerta y comunicación (8.4.3)** — a quién se avisa, en qué orden, por qué canal, con qué mensaje. Incluye clientes, proveedores, autoridades y prensa si corresponde. **Con canal alternativo**: si el plan depende del correo corporativo y lo que cayó es el correo, no hay plan.
4. **Procedimientos de recuperación** — pasos concretos, en orden, con tiempos esperados.
5. **Recuperación / vuelta a la normalidad (8.4.5)** — la parte que casi nadie escribe y que el auditor pregunta.
6. **Anexos**: directorio de contactos (actualizado y **accesible fuera de los sistemas de la empresa**), inventario de recursos, formatos de bitácora del incidente.

> Un plan de continuidad guardado solo en el servidor que se cayó es el chiste clásico del rubro. Copia offline, impresa o en dispositivo aparte. El auditor lo pregunta.

### Paso 7 — Ejercicios y pruebas (8.5)

**Es la cláusula donde más se cae 22301.** Un plan nunca probado no cuenta como capacidad de continuidad. Programa anual escalando en realismo:

| Tipo | Esfuerzo | Qué valida |
|---|---|---|
| Revisión de escritorio | Bajo | Que el plan esté completo y coherente |
| Recorrido guiado (walkthrough) | Bajo-medio | Que los roles entiendan qué hacen |
| Simulación de escenario | Medio | Toma de decisiones bajo presión |
| Prueba técnica (restauración, failover) | Medio-alto | Que la tecnología **de verdad** funcione |
| Ejercicio completo | Alto | Todo junto, con interrupción real controlada |

Cada ejercicio produce un **informe con objetivos, qué pasó, qué falló y acciones derivadas**. Un ejercicio donde "todo salió bien" y no generó ninguna acción es sospechoso: no se aprendió nada.

Y lo más importante: **las acciones derivadas se cierran y actualizan el plan.** Ese ciclo cerrado es lo que se audita.

### Paso 8 — Evaluación (8.6)

Revisión periódica de que la documentación y las capacidades siguen siendo adecuadas. Se dispara al menos anualmente y ante cambios: nueva sede, nuevo sistema crítico, cambio de proveedor, reestructuración.

---

## 4. El entregable

| Documento | Cláusula |
|---|---|
| `CON-M-001 Análisis de Impacto al Negocio` (planilla por actividad, con MTPD/RTO/RPO, dependencias y recursos mínimos) | 8.2.2 |
| `CON-M-002 Apreciación de riesgos de continuidad` | 8.2.3 |
| `CON-D-001 Estrategias y soluciones de continuidad` (con justificación y recursos) | 8.3 |
| `CON-PL-001 Plan de continuidad del negocio` (+ planes específicos por escenario si aplica) | 8.4 |
| `CON-PL-002 Programa anual de ejercicios y pruebas` | 8.5 |
| `CON-R-00X Informes de ejercicios` | 8.5 |
| `CON-R-00X Evaluación de documentación y capacidades` | 8.6 |

**Reutilización directa:** el mismo juego cierra `A.5.29` y `A.5.30` de 27001 y `8.7.2` de 20000-1. Regístralo en la columna "cláusulas que cubre" de la lista maestra y no lo escribas tres veces.

---

## 5. Lo que revisa el auditor

- Que el **BIA exista y esté hecho por actividad**, no por departamento.
- **Coherencia RTO < MTPD** y coherencia RPO ↔ frecuencia real de respaldo.
- Que las **estrategias cumplan los RTO declarados** y tengan recursos asignados.
- Que los **planes sean ejecutables**: pide leerlos y a veces le pide a alguien que explique qué haría.
- **Evidencia de ejercicios ejecutados** en el último año, con informe y acciones cerradas.
- **Prueba de restauración de respaldos**, no solo de que el respaldo corre.
- Que el **directorio de contactos esté actualizado** y sea accesible sin los sistemas de la empresa.
- Que el plan se haya **actualizado** tras el último ejercicio o cambio relevante.

---

## 6. Errores que se repiten

- **Saltarse el BIA** e ir directo a escribir planes. Resultado: se protege lo visible, no lo crítico.
- **Todo es crítico.** Si nada se prioriza, nada se protege.
- **RTO = MTPD.** Sin margen, el plan falla al primer contratiempo.
- **RPO incoherente con la frecuencia de respaldo.** El error técnico más frecuente y el más fácil de detectar.
- **Confundir plan de continuidad del negocio con plan de recuperación TI.** El DRP es un subconjunto: recupera sistemas. La continuidad incluye personas, procesos, instalaciones y proveedores.
- **Nunca ejercitar.** La causa número uno de no conformidad mayor en 22301.
- **Plan escrito en prosa.** Nadie lee tres páginas de párrafos en una emergencia. Listas, tablas y diagramas de decisión.
- **Ignorar las dependencias cruzadas** entre actividades con RTO distintos.
- **Plan accesible solo en el sistema que puede caerse.**
- **Contactos desactualizados.** Se revisan al menos dos veces al año; es media hora de trabajo.

---

## 7. Límites

- El BIA requiere **decisiones de negocio de la dirección** (cuánto está dispuesta a perder, cuánto va a invertir). No es un ejercicio técnico y no lo puede resolver el área de TI sola.
- Las estrategias tienen costo real. Un plan sin presupuesto aprobado es un documento, no una capacidad.
- Esta skill no reproduce el texto de 22301.
- Sectores regulados (banca, salud, servicios esenciales, telecomunicaciones) tienen requisitos de continuidad impuestos por el regulador que **mandan sobre** lo que diga la norma.
