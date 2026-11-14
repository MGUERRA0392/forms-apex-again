# Auditoría de Forms APEX Again — corte 2026-11-13

**Fuente:** `MGUERRA0392/forms-apex-again`, repositorio público; rama de referencia `main`, árbol Git `3541347d630e969599d1e280fe210bedb6bd62a7`. **Método:** inspección de fuentes del repositorio y enlaces locales. No se ejecutaron modelos, clientes Codex/Claude/Gemini, APEX, bases de datos ni extractores Forms/Reports durante el diagnóstico de línea base.

## Inventario verificado

- `skills/forms-apex-again/SKILL.md`: frontmatter con `name`/`description`, routing por tarea, seguridad, versiones y criterios de evidencia.
- 18 referencias técnicas en `skills/forms-apex-again/references/` sobre Forms/Reports/APEX, diseño, workflow y trazabilidad.
- `README.md`, `docs/apex-workflow-runtime-acceptance.md` y `evals/revision-2026-11-07.md` muestran guía de uso y tres escenarios de **revisión estática**, no evaluación funcional real.
- `plugin.json` y `.claude-plugin/plugin.json`: versión `1.0.0`. No existe implementación Python/MCP propia en este repositorio y no debe atribuirse ninguna herramienta de otro repositorio a esta skill.
- No había `evals/cases.json`, test runner ni GitHub Actions; tampoco archivo LICENSE. Enlaces internos existentes en la revisión inicial.

## Hallazgos

| ID | Prioridad | Hecho comprobado | Riesgo | Tratamiento |
|---|---|---|---|---|
| A-01 | Alta | Revisión del 2026-11-07 cubre solo tres escenarios documentales, sin respuestas de modelo | Confundir cobertura de texto con eficacia del agente | Suite nueva de **14 prompts sintéticos**, criterios positivos y negativos, documentación de ejecución |
| A-02 | Alta | No había validador de corpus, manifiestos, estructura de skill o enlaces | Errores silenciosos en versiones, referencias y reglas | Auditor local Python estándar, pruebas unitarias y CI |
| A-03 | Media | La guía podría confundirse con una herramienta de extracción/ejecución | Afirmar capacidades de FMB, MCP, SQLcl o APEXREST que el paquete no incluye | Matriz de capacidades y limitaciones explícitas |
| A-04 | Media | Hay material portable para Codex y Claude pero no registro de aceptación de modelo/cliente | Sobreafirmar compatibilidad multi-cliente | Matriz por cliente con `No evaluada` y protocolo repetible |
| A-05 | Media | Repositorio público sin `LICENSE` en `main` | Ambigüedad de permisos de redistribución/contribución | Documentar y proponer elección de licencia; **no** asumir ni insertar licencia unilateralmente |
| A-06 | Alta | Al ser público, una referencia detallada a datos privados puede exponer información no destinada a terceros | Riesgo de confidencialidad al reutilizar documentación | Mantener ejemplos sintéticos, prohibir copiar evidencia privada y revisar diffs antes de publicarlos |

## Evaluación comparativa por tipo de producto

La skill presente es **manual e instructions-only**. Su función es guiar la selección de evidencia y producir diseños/planes APEX; no equivale funcionalmente a un parser FMB o servidor MCP. Es legítimo mantener guías compactas separadas de herramientas locales más extensas.

El repositorio **no se fusiona con ninguna implementación externa**. No se copian archivos de repositorios privados; un futuro handoff se limita a interfaces y evidencias expresamente autorizadas.

## Cambios de la rama de auditoría

- Nuevo corpus de **14 casos** sintéticos en `evals/cases.json`.
- Validador de estructura con registro de revisiones, referencias, manifest/versiones y verificación de ruta.
- Pruebas de regresión sin dependencias y CI para Python 3.9/3.11.
- Documentación de evaluación, compatibilidad y límites, referencias en README y skill.

## Puertas pendientes

1. CI de la rama en verde y revisión del diff público para detectar información sensible.
2. Ejecución real de los 14 casos en cada cliente que se declare compatible; evidencias saneadas, revisión independiente y repetibilidad.
3. Verificar que el plugin sea descubierto realmente por el cliente/versión objetivo.
4. Seleccionar licencia explícita si se quiere ofrecer un proyecto **open source**, en vez de únicamente publicarlo en GitHub.
5. Aceptación funcional/visual en Oracle APEX de destino cuando corresponda; el runner sintético no la sustituye.

**Estado:** auditoría estructural en PR de revisión; no certifica seguridad, funcionalidad de modelos ni compatibilidad universal.
