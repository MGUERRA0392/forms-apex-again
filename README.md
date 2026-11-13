# Forms APEX Again

Guía y agente portable en español para analizar Oracle Forms y Reports, recuperar reglas con evidencia y construir aplicaciones Oracle APEX de forma nativa y verificable. Sirve para migraciones y para desarrollo APEX desde cero.

## Contenido

| Necesidad | Recurso |
|---|---|
| Enrutar y ejecutar una tarea | [Skill principal](skills/forms-apex-again/SKILL.md) |
| Método de migración y aceptación | [Playbook](skills/forms-apex-again/references/MIGRATION.md) |
| Evidencia, límites y operación segura | [Instrucciones](skills/forms-apex-again/references/INSTRUCTIONS.md) |
| FMB/FMX, lienzos, bloques, items y LOV | [Inspección Forms](skills/forms-apex-again/references/forms-inspection.md) |
| Triggers, unidades, semántica y transacciones | [Triggers y lógica Forms](skills/forms-apex-again/references/forms-triggers-and-logic.md) |
| RDF/REP, modelo, parámetros y layout | [Inspección Reports](skills/forms-apex-again/references/reports-inspection.md) |
| Salida APEX o documento | [Reports a APEX](skills/forms-apex-again/references/reports-rdf-rep-a-apex.md) |
| Forms, LOV, DML/API y diálogos | [Formularios y diálogos](skills/forms-apex-again/references/apex-forms-and-dialogs.md) |
| Page Designer, templates, grilla y navegación | [Layout y navegación](skills/forms-apex-again/references/apex-navigation-and-layout.md) |
| Formularios, IR, Classic, IG, Charts y RDS | [Componentes APEX](skills/forms-apex-again/references/apex-componentes-y-patrones.md) |
| Dashboard, reportes por estado y Workflow | [Reportes y Workflow](skills/forms-apex-again/references/apex-reports-and-workflow.md) |
| Formulario remoto y transición explícita | [API y Workflow](skills/forms-apex-again/references/apex-formulario-api-workflow-explicito.md) |
| Pruebas y entrega | [Validación y entrega](skills/forms-apex-again/references/apex-validacion-y-entrega.md) |
| Matriz de trazabilidad | [Plantilla](skills/forms-apex-again/references/plantilla-trazabilidad.md) |
| Síntesis de patrones | [KNOWLEDGE](skills/forms-apex-again/references/KNOWLEDGE.md) |
| Fuentes y referencias | [REFERENCES](skills/forms-apex-again/references/REFERENCES.md) |

La guía cubre inspección de canvases, ventanas, bloques, items, LOVs, record groups, triggers y dependencias según la calidad de los artefactos y herramientas disponibles. También orienta la selección entre salida documental y componentes APEX, el desarrollo de formularios y reportes, la navegación y la verificación visual/runtime. Sus conclusiones deben indicar evidencia, cobertura y límites; una lectura parcial nunca demuestra completitud.

## Usar como skill

Copia la carpeta `skills/forms-apex-again` a una ubicación de skills reconocida por tu cliente. Mantén juntos `SKILL.md` y `references/`. Codex y Claude Code pueden usar la carpeta como skill conforme a sus mecanismos de instalación.

## Usar como plugin

El archivo raíz `plugin.json` empaqueta el skill bajo la estructura portable de Agent Plugins. Instala este repositorio o su raíz como plugin en un cliente que admita ese formato. El plugin solo distribuye instrucciones y referencias: no instala Forms Builder, lectores binarios, MCP, conectores ni servicios de runtime.

## Uso responsable

El usuario proporciona sus propios artefactos, permisos y conexiones. No incluyas credenciales en prompts, código cliente o repositorios. Mantén fuentes, datos y evidencia del cliente en ubicaciones autorizadas; publica únicamente material genérico revisado. Revisa licencia y atribución de las fuentes enlazadas antes de reutilizar material sustancial.

## Desarrollo APEX con Workflow

La guía principal incluye criterios de formularios locales y remotos, reportes por estado, navegación, templates/atributos, modal de Workflow y validación por capas. Usa ejemplos propios del proyecto destino y confirma su versión y contrato antes de aplicar el patrón.


## Herramienta opcional y revisión

- Integración segura de APEXREST, límites por versión y destino: [guía de APEXREST](skills/forms-apex-again/references/apexrest-integration.md).
- [Revisión estática del paquete](evals/revision-2026-11-07.md): escenarios de migración, desarrollo APEX y APEXREST; no sustituye una ejecución real del agente.

- [Aceptación Runtime para Workflow en APEX](docs/apex-workflow-runtime-acceptance.md): dashboard, reportes por estado, formularios, botones, transiciones por API y evidencia de tracking.
