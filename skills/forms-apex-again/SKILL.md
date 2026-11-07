---
name: forms-apex-again
description: Inspecciona Oracle Forms y Reports con evidencia; transforma reglas en un diseño y desarrollo Oracle APEX nativo, verificable y portable.
---

# Forms APEX Again

Agente portable de conocimiento para análisis/migración de Oracle Forms y Reports, y desarrollo Oracle APEX desde cero. No presupongas cliente, proyecto, esquema, versión, instalación, conexión ni herramienta que el usuario no haya confirmado.

## Enruta la tarea

- **FMB/FMX y Forms:** [instrucciones](references/INSTRUCTIONS.md), [inspección Forms](references/forms-inspection.md), [triggers/lógica](references/forms-triggers-and-logic.md) y [playbook](references/MIGRATION.md).
- **RDF/REP y Oracle Reports:** [inspección Reports](references/reports-inspection.md), [mapeo a APEX](references/reports-rdf-rep-a-apex.md) y playbook.
- **APEX desde cero:** [componentes y patrones](references/apex-componentes-y-patrones.md), [layout/navegación](references/apex-navigation-and-layout.md), [forms/LOV/dialogs](references/apex-forms-and-dialogs.md).
- **Reportes, dashboards o Workflow:** [reportes y Workflow](references/apex-reports-and-workflow.md).
- **Pruebas/entrega:** [validación y entrega](references/apex-validacion-y-entrega.md); usa también la [plantilla de trazabilidad](references/plantilla-trazabilidad.md).
- **Síntesis rápida:** [KNOWLEDGE](references/KNOWLEDGE.md). No vuelvas a leer referencias completas sin necesidad.

## Método obligatorio

1. Confirma versiones de Forms, Reports, Database, APEX, Universal Theme y ORDS pertinentes; identifica objetivo, permisos, artefactos, fuentes y límites.
2. Inventaría cobertura. Separa extracción, observación en Builder/runtime, inferencia y pendiente; guarda ubicación y origen de cada evidencia.
3. Modela tareas, reglas, navegación, seguridad y transacciones antes de crear páginas. No traduzcas trigger por trigger ni copies aplicaciones de ejemplo.
4. Prefiere componentes declarativos de APEX y Universal Theme de la versión real. Contrasta Properties, Attributes, slots y template options en Page Designer.
5. Relaciona cada regla de origen con página/región/item/proceso/servicio APEX y una prueba de aceptación.
6. Valida fuente, interacción, seguridad, casos vacío/error/éxito y responsive. Declara exactamente qué se comprobó.
7. Publica solo patrones genéricos revisados. Nunca copies proyectos, rutas, nombres, IDs, datos o secretos locales a una edición pública.

## APEXREST opcional

Para autoría APEXlang, referencias, validación o importación con el complemento APEXREST, aplica [límites de versión y destino](references/apexrest-integration.md). No presupongas que el complemento puede acceder a SQLcl/WSL solo porque el usuario sí tenga esa conexión.

## Evidencia y límites

FMB editable, FMX compilado, XML/TXT exportado, Builder y runtime son fuentes distintas. Leer bytes no garantiza interpretar cada objeto, código o propiedad efectiva. Consulta los límites del lector antes de declarar exhaustividad. RDF fuente, REP compilado y salida impresa también son diferentes.

## Estándares APEX

- **Tabla local:** usa Form nativo cuando corresponda; conserva Fetch Row, Process Row/DML y botones generados. Ajusta condición, estilo y posición antes de sustituirlos.
- **Datos remotos:** define GET detalle/listado, POST, PUT/PATCH, cancelación y transición según contrato. No finjas DML local sobre tabla que la aplicación no posee.
- **Form y guardado:** alta/actualización se resuelven con clave y contrato explícitos. Guardar no cambia Workflow por sí mismo.
- **LOV:** display y return values distintos según contrato; el servidor valida de nuevo el retorno y el ámbito.
- **Modal:** transfiere solo clave/contexto necesario; cancelar no muta; submit valida y devuelve resultado para refresh.
- **Reportes:** elige Interactive Report, Classic Report, Interactive Grid, Chart o salida documental por la tarea. Revisa query, filtros, columnas, enlaces y valores enviados/recibidos.
- **UI:** template estándar, un encabezado/breadcrumb coherente, acciones en slot válido, grilla por región y revisión de Properties/Attributes. Usa RDS solo para alternancia funcional real.
- **Workflow:** dashboard con cantidades reales; rail de etapas; bandeja por estado; forma con clave/contexto; botón de Workflow para instancia persistida y elegible; diálogo con acciones, comentario y tracking; validación de actor/origen/destino en servidor.
- **Seguridad:** condiciones de cliente solo cambian presentación. Autorización y alcance de filas viven en servidor/DB/API.

## Herramientas y credenciales

Una guía no instala Forms Builder, Reports Builder, SQLcl, MCP, navegador, plugins ni extractores. Confirma capacidades reales del cliente. El usuario provee herramientas, accesos y permisos; no almacenes credenciales, tokens, perfiles o rutas privadas en el agente.

## Diseño de formularios y Workflow en APEX

Cuando un desarrollo incluya estados y transiciones, propone una experiencia completa: dashboard con conteos/gráfica reales y navegación lateral por estado; reporte interactivo filtrado por estado con enlace de fila al formulario; formulario con retorno y guardado; acción Workflow separada que abre una página modal y muestra solo acciones permitidas. Guardar nunca debe transicionar automáticamente.

Usa componentes del tema instalado: Page Template, región/atributos, Template Options, posiciones de botones y grid de 12 columnas. Inspecciona tanto propiedades como Attributes de regiones. Emplea Hero/breadcrumb y slots estándar del encabezado; no inventes templates ni uses CSS para simular regiones nativas. Para formularios extensos, agrupa secciones con tabs o Region Display Selector y mapea los controles desde evidencia de Forms/contrato.

Distingue una forma local de una forma remota: conserva Fetch/Process Row y acciones DML nativas cuando la fuente pertenece al parsing schema; para datos remotos, presenta una forma APEX normal pero persiste por APIs documentadas. Mantén Crear/Guardar separado de Workflow, y comprueba clave persistida, estado no terminal y autorización del servidor antes de ofrecer la transición. Documenta límites de evidencia: metadata, API, render y recorrido de usuario son verificaciones distintas.
