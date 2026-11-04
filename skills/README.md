# Skills — métodos ejecutables de trabajo ISO

Cada carpeta de aquí es una **habilidad**: un método paso a paso, probado, para hacer una pieza concreta de trabajo en un sistema de gestión. Están escritas para servir a dos lectores a la vez:

- **Una persona** que quiere saber cómo se hace algo y qué le van a pedir en la auditoría.
- **Un asistente de IA** (Claude Code) que puede ejecutar el método y producir el entregable.

Por eso cada skill vive en `<nombre>/SKILL.md` con cabecera YAML: es el formato nativo de las *skills* de Claude Code. Si copias la carpeta a `.claude/skills/` de cualquier proyecto, Claude la carga sola.

```bash
# Activarlas en este proyecto (o en el de un cliente)
python ../scripts/iso_sgi.py instalar-skills --destino <ruta>/.claude/skills
```

---

## Las ocho habilidades

| # | Skill | Qué produce | Cuándo se usa |
|---|---|---|---|
| 1 | [`iso-diagnostico-brechas`](iso-diagnostico-brechas/) | Informe de brechas + plan de acción priorizado | **Siempre lo primero.** Antes de escribir un solo documento. |
| 2 | [`iso-levantar-sgi`](iso-levantar-sgi/) | Estructura de carpetas + lista maestra + documentos base | Después del diagnóstico, cuando se decide implementar |
| 3 | [`iso-apreciacion-riesgos`](iso-apreciacion-riesgos/) | Metodología única + las matrices por norma | En cuanto exista el contexto y el alcance |
| 4 | [`iso-declaracion-aplicabilidad`](iso-declaracion-aplicabilidad/) | SoA con los 93 controles justificados | Solo 27001. Es el documento que más se cae en auditoría. |
| 5 | [`iso-bia-continuidad`](iso-bia-continuidad/) | BIA, estrategias y planes de continuidad | Solo 22301 (y alimenta 27001 A.5.29–A.5.30 y 20000-1 8.7.2) |
| 6 | [`iso-auditoria-interna`](iso-auditoria-interna/) | Programa, plan, lista de verificación e informe | Antes de la certificación y todos los años después |
| 7 | [`iso-no-conformidades`](iso-no-conformidades/) | NC redactada, análisis de causa raíz y cierre | Cada vez que aparece un hallazgo |
| 8 | [`iso-revision-direccion`](iso-revision-direccion/) | Acta integrada con las entradas y salidas exigidas | Al menos una vez al año, antes de la auditoría externa |

### El orden real de una implementación

```
1. diagnostico-brechas  ──►  ¿dónde estamos?
2. levantar-sgi         ──►  esqueleto + lista maestra
3. apreciacion-riesgos  ──►  metodología + matrices
4. declaracion-aplicabilidad (si hay 27001)
5. bia-continuidad           (si hay 22301)
        │
        ├─ … se escribe la documentación y se opera 3-6 meses …
        │
6. auditoria-interna    ──►  hallazgos
7. no-conformidades     ──►  se cierran
8. revision-direccion   ──►  la dirección decide
        │
        └──►  auditoría de certificación
```

Sin los pasos 6-7-8 **ejecutados y con evidencia**, ningún organismo certifica. Es el error más caro de las implementaciones apuradas: tener toda la documentación perfecta y cero registros de que el sistema funcionó.

---

## Formato de una skill

```yaml
---
name: iso-nombre-de-la-skill
description: Una línea. Qué hace y cuándo dispararla.
normas: [9001, 14001, 45001, 27001, 22301, 20000-1]   # a cuáles aplica
entrega: Qué artefacto produce
---
```

Y el cuerpo siempre con las mismas secciones:

1. **Cuándo usar esta skill** — y cuándo no.
2. **Qué necesitas antes de empezar** — entradas obligatorias.
3. **El método** — pasos numerados, ejecutables.
4. **El entregable** — estructura exacta de la salida.
5. **Lo que revisa el auditor** — qué mira de verdad y en qué orden.
6. **Errores que se repiten** — los que se ven una y otra vez.
7. **Límites** — lo que esta skill no resuelve.

Si escribes una skill nueva, respeta esas siete secciones. La consistencia es lo que hace que sirvan.

---

## Datos que usan las skills

Todas se apoyan en [`../datos/catalogo_normas.json`](../datos/catalogo_normas.json): cláusulas, información documentada obligatoria, los 93 controles del Anexo A y las trampas de numeración entre normas. Si actualizas una skill porque cambió una cláusula, **actualiza también el JSON** — es la fuente única.

---

## ⚖️ Límite legal, en todas sin excepción

Ninguna skill reproduce el texto de una norma. Describen **qué tiene que demostrar la organización**, con palabras propias. Para implementar necesitas la norma oficial, comprada legalmente ([INN](https://www.inn.cl) en Chile, [ISO Store](https://www.iso.org/store.html) fuera). Ver el [DISCLAIMER](../DISCLAIMER.md).

Ninguna skill certifica nada. Preparan para una auditoría de certificación que hace un organismo acreditado.
