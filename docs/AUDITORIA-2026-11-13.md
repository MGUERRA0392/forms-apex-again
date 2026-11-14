# Auditoría de Forms APEX Again — corte 2026-11-13

**Fuente:** `MGUERRA0392/forms-apex-again`, repositorio público; rama de referencia inicial `main`, árbol Git `3541347d630e969599d1e280fe210bedb6bd62a7`. **Método:** inspección estática del repositorio y enlaces locales. No se ejecutaron modelos, clientes Codex/Claude/Gemini, Oracle APEX, bases de datos ni extractores Forms/Reports durante el diagnóstico de línea base.

## Inventario verificado

- `skills/forms-apex-again/SKILL.md`: frontmatter con `name`/`description`, routing por tarea, seguridad, versiones y criterios de evidencia.
- 17 referencias técnicas en `skills/forms-apex-again/references/` sobre Forms/Reports/APEX, diseño, workflow y trazabilidad.
- `README.md`, `docs/apex-workflow-runtime-acceptance.md` y `evals/revision-2026-11-07.md` documentan guía y revisión estática, no evaluación funcional de modelos.
- `plugin.json` y `.claude-plugin/plugin.json`: versión `1.0.0`. No existe implementación Python/MCP propia en este repositorio.
- En el árbol de referencia inicial no había `evals/cases.json`, test runner, GitHub Actions ni `LICENSE`. Después, `main` recibió el archivo raíz `LICENSE` con MIT, antes de completar esta rama de revisión.

## Hallazgos

| ID | Prioridad | Hecho comprobado | Riesgo | Tratamiento/estado |
|---|---|---|---|---|
| A-01 | Alta | La revisión documental del 2026-11-07 no incluía respuestas de modelo ni una suite reproducible | Confundir cobertura de texto con eficacia del agente | Se añadieron 23 prompts sintéticos, expectativas y prohibiciones; la semántica del modelo sigue sin evaluarse |
| A-02 | Alta | No había validador de corpus, manifiestos, estructura de skill o enlaces | Errores silenciosos en versiones, referencias y reglas | Se añadió auditor local Python estándar, pruebas unitarias y CI |
| A-03 | Media | La guía puede confundirse con una herramienta de extracción o ejecución | Afirmar capacidades FMB, MCP, SQLcl o APEXREST que el paquete no incluye | Se documentaron capacidad y límites |
| A-04 | Media | Había material portable para Codex y Claude, sin resultados de aceptación por cliente/modelo | Sobreafirmar compatibilidad multi-cliente | La matriz marca las ejecuciones como no evaluadas |
| A-05 | Media | La revisión inicial encontró el repositorio sin licencia; luego `main` incorporó MIT | La nota inicial podía quedar obsoleta en la rama de auditoría | README y compatibilidad de esta rama identifican MIT para el contenido original; materiales de terceros conservan sus términos |
| A-06 | Alta | La publicación de material derivado de proyectos puede exponer datos privados | Riesgo de confidencialidad al reutilizar evidencia | Mantener ejemplos sintéticos y revisar los cambios públicos antes de incorporarlos |

## Evaluación comparativa por tipo de producto

La skill es **instructions-only**. Guía la selección de evidencia y la producción de diseños/planes APEX; no equivale funcionalmente a un parser FMB o servidor MCP. Una guía portátil y una herramienta local pueden tener alcances distintos.

El repositorio no copia implementaciones privadas. El contenido público debe limitarse a patrones genéricos y ejemplos sintéticos; los materiales externos mantienen sus propias licencias.

## Cambios de la rama de auditoría

- Corpus de **23 casos sintéticos** en `evals/cases.json`.
- Validador de estructura, revisiones, referencias, manifiestos/versiones y enlaces locales.
- Pruebas de regresión sin dependencias y CI para Python 3.9/3.11.
- Documentación de evaluación, compatibilidad y límites.

## Puertas pendientes

1. Revisar el diff público completo antes de incorporar la rama y volver a ejecutar CI si cambia.
2. Ejecutar los 23 casos con cada cliente/modelo que se quiera declarar compatible; conservar evidencia saneada en un repositorio privado.
3. Verificar descubrimiento e invocación real del plugin en cada cliente objetivo.
4. Aceptación funcional/visual en Oracle APEX de destino cuando corresponda; el runner sintético no la sustituye.
5. Revisar atribución/licencias de las fuentes de terceros antes de reutilizar contenido sustancial.

**Estado:** validación estructural automatizada en verde para la revisión actual; no certifica seguridad, eficacia semántica del modelo ni compatibilidad universal.
