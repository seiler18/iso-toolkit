# ISO Toolkit

Material abierto para implementar sistemas de gestión ISO en pymes de habla
hispana: catálogo estructurado de 6 normas (`datos/catalogo_normas.json`), 8
skills, el generador `scripts/iso_sgi.py` (Python, solo biblioteca estándar),
el mapa Anexo SL y, más adelante, plantillas y checklists.

**Satélite (nivel B) de [`../organizador-iso`](../organizador-iso/).** Su
memoria, su backlog y sus reglas legales viven allí: los hitos de este repo se
registran en `../organizador-iso/.claude/hitos/` y lo que falta, en
`../organizador-iso/PENDIENTES.md`. La vitrina comercial es
[`../sistemas-gestion`](../sistemas-gestion/).

## Lo vivo

Todo. No hay arqueología: es el producto en construcción.

## La regla de este repo

**Es público** (`seiler18/iso-toolkit`, desde el 2026-11-04). Todo cambio pasa
antes de su push por la skill `chequeo-legal` de `../organizador-iso`: lo que
llega a GitHub queda en el historial aunque después se borre.

- Nunca texto de las normas: se parafrasea y se cita la cláusula.
- Nunca material, nombres ni casos de un empleador ni de ningún cliente. Ni
  siquiera se nombran aquí: la lista de quiénes son vive en `organizador-iso`.
- Nunca «certificar» referido a nosotros.
- El `.gitignore` bloquea PDF y ofimáticos. Los nombres de organizaciones
  reales que no deben entrar van en `.git/info/exclude` (local, no se publica).
  Nada de eso se fuerza con `git add -f`.

`datos/catalogo_normas.json` es la fuente única: si corriges una cláusula en
una skill, corrígela también ahí.

## Comandos

```bash
python scripts/iso_sgi.py listar --trampas        # antes de citar una cláusula
python scripts/iso_sgi.py instalar-skills --destino ../organizador-iso/.claude/skills
```

El resto de subcomandos, en `scripts/README.md`.
