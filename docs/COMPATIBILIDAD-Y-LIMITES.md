# Compatibilidad y límites del paquete Forms APEX Again

Este repositorio **público** distribuye solamente una skill portable con archivos Markdown y manifiestos de plugin. No incluye ejecutables Python, parser binario de Oracle Forms, Forms/Reports Builder, servidor MCP, SQLcl, wallet, credenciales, base de datos ni cliente Oracle APEX.

## Matriz de capacidades

| Capacidad | Skill incluida | Herramienta o comprobación externa |
|---|---|---|
| Guiar inspección de Forms FMB/FMX | Sí, método y límites | Para extraer bytes y objetos se requiere un lector compatible, autorizado y verificado |
| Guiar inspección de Reports RDF/REP | Sí, criterios y mapeo | Extractor/Builder y evidencias según formato/versión |
| Diseñar Forms→APEX y Reports→APEX | Sí, decisiones con trazabilidad | Aceptación funcional, Oracle APEX y requisitos reales fuera de la skill |
| APEX desde cero, UI declarativa y Workflow | Sí, playbooks y reglas | Page Designer/runtime, DB/ORDS y autorización de servidor reales |
| Consultas MCP, SQL, APEXREST y despliegues | No; son capacidades opcionales externas | Configuración y permisos explícitos del usuario en cada cliente |
| Efectuar acciones autónomas o modificar agentes | No | No hay un runtime de orquestación en este paquete |

## Matriz de clientes (estado al 2026-11-13)

| Cliente | Material de integración | Ejecución de la suite de 23 casos |
|---|---|---|
| Codex | Carpeta de skill estándar | **No evaluada en esta auditoría** |
| Claude Code | `.claude-plugin/plugin.json` y skill | **No evaluada en esta auditoría** |
| Gemini CLI | Puede cargar instrucciones cuando soporte un mecanismo compatible; no hay manifiesto nativo en este repo | **No evaluada** |
| Otros clientes | Archivos Markdown trasladables | **No evaluada** |

Un manifiesto existente no demuestra que el cliente haya descubierto el plugin, aplicado la skill, respetado sus límites o producido la respuesta esperada. Documentar por separado instalación, descubrimiento, activación, herramientas disponibles, modelo, pruebas y revisión humana.

## Relación con otras implementaciones

El diseño de esta skill es **instructions-only**. Si el usuario dispone de un extractor local o MCP autorizado, este puede suministrar evidencias a la skill; la guía no lo instala, no lo invoca automáticamente y no certifica resultados. No confundir una recomendación de consultar datos con una operación realizada.

El repositorio público debe contener exclusivamente patrones genéricos y ejemplos sintéticos. No publicar archivos, nombres, endpoints, permisos, capturas, trazas o resultados procedentes de proyectos privados sin permiso y saneamiento explícitos.

## Publicación y licencias

El archivo raíz [`LICENSE`](../LICENSE) declara la licencia MIT para el contenido original de este repositorio. Las fuentes, marcas y materiales de terceros conservan sus propios términos y no quedan relicenciados por el archivo del proyecto. La visibilidad pública por sí sola no determina una licencia.
