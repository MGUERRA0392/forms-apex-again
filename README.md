# Forms APEX Again

Agente portable de conocimiento, en español, para analizar Oracle Forms y Reports, transformar reglas con evidencia y desarrollar Oracle APEX de forma nativa y verificable.

## Por qué esta edición pública es más pequeña que la privada

Este repositorio contiene el manual y la skill reutilizable. El repositorio privado también contiene implementación del agente, plugins, scripts, pruebas, recursos, distribuciones versionadas y validaciones ligadas a una instalación. Esos componentes no son necesarios para enseñar el método y podrían incluir dependencias o contexto local. La edición pública amplía el conocimiento sin replicar esa implementación, secretos, conexiones ni datos de empresa.

La guía sí incluye rutas completas y matrices para aplicar a artefactos propios. No incluye extractores binarios ni promete recuperar por completo lógica no presente en el FMB/FMX/RDF/REP entregado.

## Mapa de conocimiento

| Necesidad | Guía |
|---|---|
| Iniciar y enrutar una tarea | [Skill principal](skill/SKILL.md) |
| Método de migración y aceptación | [Playbook](skill/references/MIGRATION.md) |
| Evidencia, límites y operación segura | [Instrucciones](skill/references/INSTRUCTIONS.md) |
| Estructura de FMB/FMX, lienzos, bloques, items, LOV | [Inspección Forms](skill/references/forms-inspection.md) |
| Triggers, unidades, semántica y transacciones | [Triggers y lógica Forms](skill/references/forms-triggers-and-logic.md) |
| RDF/REP, modelo, parámetros y layout | [Inspección Reports](skill/references/reports-inspection.md) |
| Decidir entre salida APEX y documento | [Reports a APEX](skill/references/reports-rdf-rep-a-apex.md) |
| Forms, LOVs, DML local/API y diálogos | [Formularios y diálogos](skill/references/apex-forms-and-dialogs.md) |
| Page Designer, templates, grilla y navegación | [Layout y navegación](skill/references/apex-navigation-and-layout.md) |
| Componentes APEX: Form, IR, Classic, IG, Chart, RDS | [Componentes y patrones](skill/references/apex-componentes-y-patrones.md) |
| Dashboard, bandejas y Workflow | [Reportes y Workflow](skill/references/apex-reports-and-workflow.md) |
| Casos de prueba, seguridad y entrega | [Validación y entrega](skill/references/apex-validacion-y-entrega.md) |
| Matriz práctica de requisitos a implementación | [Plantilla de trazabilidad](skill/references/plantilla-trazabilidad.md) |
| Resumen de patrones | [KNOWLEDGE](skill/references/KNOWLEDGE.md) |
| Playbooks comunitarios y documentación Oracle | [Referencias](skill/references/REFERENCES.md) |

## Qué cubre

- Inspección estructural y funcional de módulos Forms: ventanas, canvas/lienzos, vistas, bloques, items, propiedades, LOVs, record groups, triggers, unidades y dependencias según la fuente y el lector.
- Diferencia entre FMB editable, FMX compilado, export intermedio, Builder y runtime; cobertura, confianza y límites explícitos.
- Oracle Reports: queries, data model, grupos, fórmulas, triggers, parámetros, bibliotecas, layout, paginación y destinos.
- Desarrollo APEX desde cero y migración: Forms, diálogos, reportes interactivos/clásicos, Interactive Grid, charts, LOVs, navegación, RDS y Workflow.
- DML nativo cuando la tabla pertenece al parsing schema y operaciones API cuando los datos están remotos, sin fingir que son el mismo patrón.
- Criterios de Page Designer, templates/Template Options, Properties/Attributes, posiciones de botones y grilla real.
- Matriz trazable: evidencia de origen → regla → componente/API → prueba → resultado o brecha.

## Instalar y usar

Carga la carpeta skill con el mecanismo de skills disponible en Codex, Claude Code u otro cliente compatible. Si el cliente no descubre el repositorio directamente, copia la carpeta skill completa a la ubicación de skills de usuario y conserva juntos SKILL.md y references. Consulta README/SKILL del cliente para confirmar esa ruta. La documentación no instala el runtime ni los lectores.

Para comenzar, entrega versiones, objetivo, fuentes autorizadas, herramientas disponibles y límites. El usuario proporciona sus propios artefactos, conexiones y permisos; el agente no contiene credenciales.

## Privacidad, licencia y contribuciones

El contenido publicado es genérico: no incluye artefactos, esquemas, URLs privadas, nombres de clientes, rutas locales ni datos reales de empresa. Revisa y anonimiza cualquier contribución.

El repositorio no declara aún una licencia de reutilización. La visibilidad pública no concede automáticamente permiso para copiar material de terceros. Revisa licencia y atribución de las fuentes enlazadas antes de reutilizar contenido sustancial.
