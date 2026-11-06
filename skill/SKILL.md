---
name: forms-apex-again
description: Inspecciona Oracle Forms y Reports con evidencia; transforma reglas en un diseño y desarrollo Oracle APEX nativo, verificable y portable.
---

# Forms APEX Again

Agente portable de conocimiento para análisis/migración de Oracle Forms y Reports, y desarrollo Oracle APEX desde cero. No presupongas un cliente, proyecto, esquema, versión, instalación, conexión ni herramienta que no haya confirmado el usuario.

## Enruta la tarea

- **Forms/FMB/FMX:** usa [instrucciones](references/INSTRUCTIONS.md), [inspección Forms](references/forms-inspection.md) y después el [playbook de migración](references/MIGRATION.md).
- **Oracle Reports/RDF/REP:** consulta [inspección de Reports](references/reports-inspection.md); integra parámetros, layout, fórmulas y salida al playbook.
- **Desarrollo APEX sin Forms:** consulta [layout y navegación](references/apex-navigation-and-layout.md), [formularios, LOV y diálogos](references/apex-forms-and-dialogs.md) o [reportes, dashboards y Workflow](references/apex-reports-and-workflow.md), según tarea.
- **Migración más desarrollo:** lee las referencias de origen y destino, y vincula cada regla fuente con un componente y prueba APEX.
- **Conocimiento resumido:** usa [KNOWLEDGE](references/KNOWLEDGE.md); no vuelvas a cargar referencias completas si ya se consultaron en la tarea.

## Método

1. Confirma versiones de Forms, Reports, Database, APEX, Universal Theme y ORDS que sean relevantes; identifica artefactos, permisos, objetivo y límites.
2. Inventaría fuentes y cobertura. Separa lo leído, lo observado en Builder/runtime, lo inferido y lo pendiente; conserva origen y ubicación de cada hallazgo.
3. Modela las reglas de negocio y navegación antes de diseñar páginas. No traduzcas mecánicamente eventos Forms.
4. Prefiere componentes nativos APEX y Universal Theme de la versión real; contrasta las propiedades, Attributes y slots en Page Designer.
5. Implementa o recomienda forma, reporte, LOV, diálogo, dashboard, gráfica y Workflow conforme al contrato de datos; usa API explícito para datos remotos.
6. Verifica fuente, interacción, seguridad, estados vacío/error/éxito y presentación responsive. Declara exactamente qué se probó.
7. Publica solo patrones genéricos, revisados y no identificables. No copies proyectos de muestra, rutas, nombres, IDs, datos ni secretos a este paquete.

## Límites de interpretación

FMB editable, FMX compilado, XML/TXT, capturas, Builder y runtime son fuentes distintas. Acceder a bytes no significa comprender todos los objetos; una extracción parcial no es completa. Consulta [inspección Forms](references/forms-inspection.md) antes de afirmar cobertura. Para Reports, distingue RDF fuente, REP compilado y salida impresa; un PDF no muestra el diseño fuente.

## Estándares APEX

- **Form local:** conserva Fetch Row, Process Row/DML y acciones nativas generadas cuando la página trabaja sobre tabla propia. Ajusta condiciones y apariencia antes de reemplazarlos.
- **Form remoto/API:** usa alta/lectura/actualización/cancelación/transición según contratos del servicio; no simules DML local donde no existe la tabla. Guardar no mueve Workflow automáticamente.
- **Modal:** transfiere clave/contexto, valida al enviar, cancela sin mutación y refresca la región padre al éxito.
- **Reportes:** elige Interactive Report, Classic Report, Interactive Grid o salida documental por tarea; revisa query, filtros, columnas, enlace de edición y valores de destino.
- **UI:** un encabezado estándar con breadcrumb, acciones en slot válido, templates/Template Options existentes, grilla de cada región y revisión de Properties y Attributes. Usa Region Display Selector solo cuando aporte una navegación real.
- **Workflow:** dashboard con gráfica/resumen de datos reales y panel de etapas; reportes filtrados por estado; forma por registro; botón Workflow visible solo para una instancia persistida y elegible; diálogo con acciones, comentario y tracking; el servidor valida actor, origen, destino y permiso.

## Herramientas y credenciales

Una guía no instala Forms Builder, Reports Builder, SQLcl, MCP, navegador ni plugins. Confirma las herramientas activas. El usuario provee acceso local en su ambiente; nunca guardes credenciales, tokens, rutas privadas o perfiles dentro del agente o repo.
