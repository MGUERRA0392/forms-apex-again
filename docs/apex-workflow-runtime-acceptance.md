# Criterio reutilizable para Workflow consumido por API en APEX

Esta guía aplica cuando una aplicación APEX presenta un proceso de Workflow que vive en un servicio o motor externo. No prescribe tablas, endpoints, roles, cantidad de estados ni componentes visuales concretos.

## Estructura de la experiencia

- Define primero estados, transiciones, actores, devoluciones, terminales, permisos y datos requeridos.
- Para un único flujo, presenta un dashboard con resumen y visualización de solicitudes por estado; mantén navegación por las etapas en una región lateral o patrón nativo apropiado para la plantilla instalada.
- Provee un reporte por estado que filtre con el identificador estable del estado actual. El enlace de fila pasa las claves necesarias a un formulario o página de detalle.
- Usa componentes APEX y Universal Theme disponibles en la versión destino. Confirma Breadcrumb Bar, Hero, posiciones de botones, templates, Template Options, atributos y grilla desde Page Designer o metadata; no inventes valores ni copies IDs de otra aplicación.
- En formularios extensos, agrupa campos con regiones o Region Display Selector cuando facilite la tarea. Mapea listas de valores y consultas desde fuentes confirmadas.

## Acciones y ciclo de vida

- Mantén Guardar y Workflow como acciones separadas. Guardar llama POST para crear o PUT/PATCH para editar; no transiciona.
- Muestra Workflow solo cuando existe una clave/instancia persistida y el estado permite actuar. El servidor vuelve a validar clave, estado, actor, autorización y destino.
- Workflow abre una página/modal con acciones permitidas, comentario cuando corresponda, actor/asignación si el contrato lo exige, historial, Cancelar y Enviar.
- Cancelar no muta. Enviar solicita una transición explícita y el servicio vuelve a validar sus reglas.
- Los estados terminales no ofrecen transiciones ordinarias. No confíes solo en condiciones de presentación APEX como control de acceso.

## Aceptación en Runtime

Con datos sintéticos autorizados:

1. Crear y guardar; comprobar que no se transicionó automáticamente.
2. Abrir Workflow después del guardado y confirmar que aparecen únicamente las acciones disponibles.
3. Probar al menos un avance y una devolución aprobados, con comentario.
4. Después de cada envío, releer el estado autoritativo y el tracking con actor, fecha y comentario.
5. Confirmar que el estado terminal no permita Enviar.
6. Verificar filtrado del reporte por estado, enlace al formulario, retorno y actualización del dashboard.
7. Separar métricas agregadas de la instancia QA; no atribuir filas anteriores al fixture.

Un endpoint publicado o una respuesta HTTP exitosa aislada no demuestra que la pantalla haya persistido el registro o completado la transición. Registra por separado hechos observados, inferencias y casos no ejecutados, como edición, autorización de distintos actores, reintentos o reconstrucción desde cero.
