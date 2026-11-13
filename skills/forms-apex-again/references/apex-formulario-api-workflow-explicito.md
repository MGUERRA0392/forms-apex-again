# Patrón APEX para formulario remoto y Workflow explícito

Guía general de construcción para formularios cuyo registro vive detrás de una API, con transiciones de Workflow separadas. Confirma siempre la versión APEX/Universal Theme, los contratos, los permisos y las propiedades disponibles en el destino.

## Composición declarativa

- Usa una página tipo Form con región de datos, items tipados, validaciones, procesos y regiones de pestañas cuando el conjunto de datos lo necesite. Aprovecha templates/Template Options y posiciones existentes del tema; no sustituyas componentes nativos por HTML/CSS dinámico sin una necesidad comprobada.
- Coloca encabezado, breadcrumb y acciones del Hero en la región y slot que el Page Designer de la versión destino reconoce. Verifica posición, botón, template, hot/template options y atributos en Page Designer o export; no infieras que un botón se renderiza por verlo en el árbol.
- Un reporte por estado debe filtrar por estado en servidor y usar una clave de navegación explícita hacia la forma. Conserva claves en session state y revalida autorización al cargar el registro; un filtro visual o parámetro de URL no autoriza acceso.
- En un dashboard, alinea tabla, gráfica, badges y navegación con el mismo contrato de conteos. Estados sin filas se muestran en cero o vacío según el diseño validado; nunca se inventan cifras. Los estados terminales no deben ofrecer acciones de avance.

## Guardar y transicionar son tareas separadas

- Usa DML declarativo de APEX solo cuando la tabla pertenezca al parsing schema y el caso admita ese DML. Para datos remotos, el botón de guardar invoca API de crear/actualizar y lee su respuesta; no configures un Automatic Row Processing contra una tabla remota inexistente.
- Después de un POST confirmado, recupera la clave, instancia y estado inicial con un GET de detalle autoritativo en servidor; no intentes resolver la fila recién creada mediante un GET agregado de etapas.
- El botón Workflow aparece solo después de guardar y recuperar una clave/instancia persistida. Guardar no debe avanzar el flujo automáticamente.
- El botón Workflow abre una página modal. La página consulta acciones permitidas para el estado actual, exige comentarios/fechas/asignación cuando el contrato lo requiera, y presenta el botón Enviar como el único punto de transición explícita.
- Tras enviar, valida HTTP/resultado, recarga estado e historial y conserva actor, fecha y comentario. La autorización de estado/actor debe comprobarse en el servicio; no confiar en valores editables del navegador.
- El modelo de lectura del dashboard y el comando de transición deben pertenecer a contratos separados. Un GET de reporte no habilita ni sustituye un POST de transición.

## Validación y evidencia

Valida en Runtime: crear; comprobar que Workflow no está disponible antes de persistir; guardar y comprobar que no hubo transición; abrir modal; revisar las acciones habilitadas; enviar una acción; verificar estado e historial; confirmar reflejo en reporte/dashboard; comprobar el comportamiento terminal. Prueba además casos sin filas y errores de API. Usa datos sintéticos autorizados y conserva límites de actor/ambiente.

Para cambiar páginas APEX exportadas, realiza backup y trabaja por el canal SQLcl/export/import autorizado para la versión; comprueba versión y destino antes de importar. Una herramienta de despliegue que detecta SQLcl no demuestra que la conexión esté configurada, que la app sea compatible, ni que el ambiente sea seguro para escritura. No eludas las barreras de entorno para desplegar.
