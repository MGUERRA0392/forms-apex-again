# Patrón portable: formularios APEX con Workflow API

## Guardar es distinto de transicionar

Cuando el registro está en otro servicio, usa un formulario APEX y conecta Guardar al API autorizado de creación o actualización. Relee la clave y el estado persistidos. No uses DML local sobre una tabla remota y no hagas que el guardado ejecute una transición.

Muestra `Workflow` solo después de confirmar que existe un registro persistido, un estado válido y que el estado no es terminal. En una cabecera Hero/Breadcrumb, utiliza la posición que ofrezcan el tema y versión de APEX destino. El botón abre un diálogo o página con estado actual, acciones permitidas por el servicio, comentario/motivo requerido e historial disponible. Abrir/cancelar no cambia el estado; solo el envío explícito llama al API de transición. Después, relee estado e historial.

Las condiciones visuales de APEX ayudan a presentar las acciones, pero el servidor debe volver a validar identidad, registro, estado origen y acción. La interfaz no es una barrera de autorización.

## Pantallas estándar

- El dashboard resume el proceso con una gráfica basada en IDs estables, navegación lateral por estados y conteos del mismo conjunto de datos autorizado.
- Cada cola operativa tiene un reporte y un formulario apropiado. Los enlaces preservan clave y contexto; los reportes no ejecutan transiciones.
- Usa componentes nativos y plantillas existentes. Verifica propiedades, atributos, slot, botones y renderizado en Runtime. Page Designer por sí solo no prueba funcionamiento.
- Presenta estados vacíos y errores reales; no inventes datos o métricas.
- Los procesos con varias etapas pueden requerir formularios/reportes por estado, navegación contextual y una página de decisión Workflow; ajusta el número de pantallas a los contratos reales.

## Límites de portabilidad

Este patrón describe mecánicas generales. Nombres de página/API, campos, etiquetas de estado, roles, IDs, hosts, workspaces, usuarios y registros de prueba pertenecen a cada instalación y requieren autorización y read-back local. No incluir secretos ni evidencias empresariales privadas en guías públicas.
