# Reportes, dashboards y Workflow en Oracle APEX

Guía de composición y comportamiento para aplicaciones donde el usuario navega registros por estado. El flujo se define con requisitos y APIs/DB reales; no copies la lógica de otra aplicación.

## Dashboard

Un dashboard de flujo debe responder: cuántos registros existen, en qué estado están y cómo entrar a cada bandeja.

- Encabezado Hero/Breadcrumb con un único título y acciones (por ejemplo, Retornar y Nuevo); botones en el slot permitido por el template, normalmente Next para el Hero.
- Gráfica nativa con query agregada por estado y valores reales. No fabriques 0, porcentajes, estados ni series cuando el contrato no entregó filas; muestra estado vacío legible.
- Resumen textual total y conteos. Alinea la tabla de resumen con la gráfica; la etiqueta debe ser corta, consistente con el menú y sin anotaciones internas.
- Panel lateral Right/Left Column según el diseño establecido, con estado actual/resaltado, icono estándar, label y navegación por estado. No muestres números de secuencia como parte del nombre.
- Cada región tiene su propio layout; inspecciona propiedades y Attributes, no des por hecho que la grilla global aplica a la región.

## Bandeja y Interactive Report

Cada etapa con una bandeja debe filtrar por identificador persistente de estado, WFID/contexto necesario y principal/compañía/asignación que el servidor confirme. El query/API debe respetar alcance por servidor.

Configura y prueba:

- columnas clave para identificar el registro y decidir si abrirlo;
- filtros de estado, contexto y autorización;
- búsqueda, orden, paginación, acciones y mensaje sin datos;
- enlace Editar que envía la PK y contexto exactos al formulario;
- items destino, Clear Cache, checksum/session state y protección contra valores alterados;
- recuentos del panel que usan la misma semántica de filtros y autorización que la bandeja.

Un enlace no es seguro por estar oculto; el endpoint y la página validan permiso y propiedad.

## Workflow desde un formulario

- Guardar crea/actualiza el registro. No cambia de estado.
- Workflow solo aparece cuando el registro y su instancia están persistidos y hay al menos una transición disponible.
- El botón abre página/modal de decisión. Presenta estado actual, acciones válidas, destino, comentario/motivo, destinatario si aplica e historial/tracking.
- Si el destino se calcula después del guardado y se pasa mediante un item de sesión, el Link Builder puede no mostrar una página fija. Inspecciona el export/proceso y confirma en Runtime que el item se resolvió y abrió el destino correcto; metadata configurada no equivale a navegación probada. Revisa también la posición efectiva del botón y su grupo padre; `Invalid Slot [Not Rendered]` significa que la definición debe corregirse antes de evaluar la navegación.
- Cancelar cierra sin mutación. Enviar llama la operación de transición aprobada y explícita.
- El servidor comprueba identidad, registro, estado de origen esperado, acción/destino permitidos, actor/responsable, motivo y concurrencia.
- Después del éxito, relee estado actual, tracking, conteos y bandeja. El estado terminal no se reabre salvo una ruta formal.

No infieras que una etapa es una acción. La definición puede tener estados y varias aristas/pasos entre ellos, incluyendo retornos. Documenta estado, transición, actor, entrada, efecto, rechazo y destino en una tabla.

## APIs y ciclo de vida

Antes de crear páginas, reúne los contratos de lectura, listado, conteos, detalle, alta, actualización, cancelación y transición. Por cada endpoint registra método, ruta, autenticación/autorización, parámetros, respuesta, errores, idempotencia, timeout, logging y propietario de la transacción. Usa alias/perfiles locales del usuario para secretos; nunca incluyas secretos en la aplicación exportada, skill o repo.

## Tipos de reporte

- Interactive Report para búsqueda/ad hoc, filtros/orden y vistas guardadas.
- Classic Report para salida tabular simple y diseño/SQL controlados.
- Interactive Grid para edición tabular multi-fila solo si reglas/validaciones/concurrencia lo permiten.
- Chart para agregados; no sustituye reporte detallado.
- Reporte imprimible para documento paginado/formal.

No conviertas todo a Interactive Report por defecto. Elige según tarea y prueba performance, permisos y exportación.

## Navegación y estado vacío

Los estados y filtros de entrada se conservan conscientemente. Un reporte vacío presenta un mensaje útil y no habilita una transición imposible. El usuario debe poder regresar al dashboard y reconocer el paso por el encabezado y breadcrumb.


## Verificación de un flujo en Runtime

- Crea solo un dato sintético autorizado desde la interfaz y registra la clave de prueba sin incluir información personal.
- Verifica por separado alta/guardado, actualización y transición. Guardar no debe mover el estado; la transición requiere una acción explícita.
- Confirma que el botón Workflow aparece solo con una clave persistida, acciones disponibles y estado no terminal; al abrirlo, revisa origen, destinos, campos obligatorios y confirmación.
- Tras enviar, relee el registro, bandeja, conteos y tracking. Verifica el estado terminal y que no ofrezca una continuación ordinaria.
- Prueba también datos vacíos, validación fallida, rechazo, devolución y error del servicio antes de declarar el flujo listo.
- Distingue la evidencia funcional del recorrido feliz de la paridad visual, seguridad por fila y pruebas de error. Un filtro del reporte o un botón oculto no reemplazan autorización del servidor.

No publiques datos de prueba, IDs, nombres de clientes, endpoints privados ni detalles de ambiente. Conserva en el repositorio únicamente estas prácticas portables.

## Reconstruir el patrón sin una aplicación de muestra

Diseña desde la tarea, la matriz de estados y los contratos disponibles; usa una app existente solo para aprender componentes APEX. No hagas depender el resultado de una aplicación de referencia ni copies sus IDs, rutas, columnas o reglas de negocio.

1. Dashboard inicial: Hero/Breadcrumb con un único título y botones; gráfico APEX nativo por estado; resumen real y panel lateral con etapa activa, icono y enlace. Sin cifras inventadas ni selector para un solo flujo.
2. Una bandeja por estado operativo: reporte nativo adecuado, consulta/filtro por STATUS_ID y autorización validada por servidor; mensaje sin filas y acción Editar que envía PK/contexto exactos a la forma.
3. Forma de detalle: campos agrupados con los templates disponibles en la versión objetivo; botón Retornar y acción de guardado persistente. Si los datos viven en otra base/esquema, los procesos llaman API y no simulan DML local.
4. En cada forma persistida, botón Workflow visible solo si hay clave y transición disponible y el estado no es terminal. Abre la página/modal con estado actual, acciones autorizadas, comentario/motivo, destinatario si corresponde e historial.
5. Cancelar cierra sin cambio; Enviar realiza la transición explícita. Relee por servicio el registro, estado, bandeja, conteos e historial. No cambies de estado al guardar.
6. Usa templates/slots nativos; para Hero, confirma que las acciones estén en Next o la ubicación equivalente ofrecida por la plantilla. Revisa propiedades y Attributes de página/regiones y verifica diseño en runtime ancho/estrecho.

Acepta la solución solo después de inspeccionar el armado en Page Designer y recorrer una instancia sintética desde alta hasta cierre, además de probar edición, estado vacío y errores relevantes. Un recorrido feliz en una app ya creada no certifica que puedas reconstruirla desde cero: esa capacidad requiere una reconstrucción limpia independiente.
