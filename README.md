# Forms APEX Again

Agente portátil, en español, para inspeccionar Oracle Forms y Oracle Reports, planear migraciones con evidencia y desarrollar aplicaciones Oracle APEX nativas.

Este repositorio público se mantiene deliberadamente centrado en instrucciones y referencias reutilizables. No replica el repositorio privado de desarrollo: aquel contiene implementación del agente, paquetes/distribuciones versionadas y validaciones de una instalación concreta. Aquí se publica el núcleo portable para que una persona lo adapte a su entorno.

## Mapa de conocimiento

Empieza por la skill y sigue solo la referencia pertinente:

| Necesidad | Guía |
|---|---|
| Elegir el recorrido y límites de seguridad | [Skill principal](skill/SKILL.md) |
| Método completo de migración y aceptación | [Playbook de migración](skill/references/MIGRATION.md) |
| Cómo inspeccionar FMB, FMX, lienzos, triggers y LOV | [Inspección de Forms](skill/references/forms-inspection.md) |
| Oracle Reports, RDF/REP, modelos, parámetros y salidas | [Inspección de Reports](skill/references/reports-inspection.md) |
| Forms de alta/edición, DML nativo vs API, LOV y modal dialogs | [Formularios y diálogos APEX](skill/references/apex-forms-and-dialogs.md) |
| Interactive/Classic Reports, gráficas, dashboard y Workflow | [Reportes y Workflow APEX](skill/references/apex-reports-and-workflow.md) |
| Page Designer, templates, botones, grilla, RDS y navegación | [Layout y navegación](skill/references/apex-navigation-and-layout.md) |
| Política de evidencia, extracción, APEX y verificación | [Instrucciones operativas](skill/references/INSTRUCTIONS.md) |
| Patrones técnicos sintetizados | [Conocimiento reutilizable](skill/references/KNOWLEDGE.md) |
| Lecturas públicas y documentación Oracle | [Referencias](skill/references/REFERENCES.md) |

## Qué puede hacer el agente

- Inventariar estructura y comportamiento de Forms: ventanas, canvases/lienzos, bloques, items, LOVs, record groups, triggers, unidades y dependencias que la fuente permita leer.
- Distinguir el nivel de evidencia de FMB editable, FMX compilado, XML/TXT, Builder y runtime; declarar cobertura y límites del extractor.
- Analizar Oracle Reports separando query/modelo, grupos, fórmulas, triggers, parámetros, layout y destino de salida.
- Diseñar o implementar páginas APEX: formularios, reportes, páginas modales, navegación, LOVs, gráficas, dashboards y flujos Workflow.
- Preferir componentes nativos del APEX/Universal Theme destino y validar Page Designer y Runtime por separado.
- Entregar una matriz trazable: evidencia fuente → regla → componente/API destino → prueba → resultado.

La presencia de una skill no instala Oracle Forms, APEX, SQLcl, MCP ni plugins. El usuario proporciona sus propios artefactos, conexiones, herramientas y permisos. El agente no contiene credenciales.

## Instalación y uso

Carga skill/SKILL.md con el mecanismo de skills que soporte tu cliente de Codex/Claude Code. Si ese cliente no descubre el directorio del repositorio automáticamente, copia la carpeta skill a su ubicación de skills de usuario y conserva juntas las referencias bajo skill/references. Confirma en el cliente qué capacidades están realmente activas antes de iniciar análisis.

Para una tarea concreta entrega versiones y artefactos autorizados, objetivo, límites, fuentes disponibles y resultado esperado. No incluyas secretos en prompts, repositorios ni exports.

## Privacidad, licencia y contribuciones

El contenido es genérico y no incluye artefactos, esquemas, URLs privadas, nombres de clientes, rutas locales ni datos reales de la empresa. Antes de contribuir, anonimiza ejemplos y verifica que el material pueda publicarse.

La visibilidad pública permite consultar el contenido, pero el repositorio no declara todavía una licencia de reutilización. No supongas que se pueden redistribuir textos o código de terceros. Las fuentes externas enlazadas son independientes; revisa su licencia antes de reutilizar contenido sustancial.
