# Páginas de forma, LOV y diálogos en Oracle APEX

Patrones de diseño para páginas de alta, edición y consulta. Verifica nombres de propiedades y opciones en la versión y tema instalados.

## Antes de crear la forma

Confirma fuente de verdad, clave primaria, propiedad de datos, modos de alta/edición/consulta, campos editables, reglas, autorizaciones, commit y retorno. Para una página sobre tabla local usa el asistente nativo de Form cuando encaje; para datos remotos define operaciones API. No simules que existe una tabla en el parsing schema si solo se accede por servicio.

## Forma nativa vinculada a tabla/vista

Revisa en Page Designer:

- Automatic Row Fetch / Fetch Row, clave primaria y valores de sesión.
- Automatic Row Processing (DML) / Process Row y manejo de errores.
- Botones generados por el asistente para crear, guardar, borrar y cancelar/retornar.
- Condiciones por modo y clave: acciones de alta cuando no hay PK; actualizar/borrar cuando hay registro y permiso.
- Validaciones APEX, constraints de DB, Lost Update/concurrencia y mensajes.
- Branch de retorno y valores que deben preservarse.

No elimines por defecto los procesos/botones generados. Ajusta condiciones, rótulos, plantilla, posición y apariencia antes de reemplazar el comportamiento nativo.

## Forma respaldada por API

Una API remota requiere un contrato explícito:

- GET de detalle y la clave enviada/recibida.
- POST para crear; PUT/PATCH para actualizar; DELETE físico o cancelación lógica según reglas; el nombre y método deben reflejar lo que realmente hace.
- Respuesta con identificador persistido, estado, errores de campo y correlación.
- Manejo de timeout, reintento, idempotencia, conflicto y límite transaccional.
- Identidad/autorización validadas por el servidor; sesión de APEX y valores de items no son prueba de permisos.

Usa un botón Guardar que invoca el proceso/API apropiado. Distingue modo alta/edición con una clave confiable; vuelve a leer el registro luego de crear/actualizar. Si hay error, conserva lo escrito cuando sea seguro y muestra un mensaje accionable. Guardar no debe ejecutar una transición Workflow implícita.

## Diseño del formulario

- Un encabezado Hero único: breadcrumb, nombre de tarea/registro y acciones en la posición válida del template.
- Agrupa items por significado; usa títulos, regiones o tabs para secciones extensas, no una larga lista sin jerarquía.
- Distribuye items en la grilla real de la región; comprueba Start New Row, columna, span del item y span de la etiqueta.
- Usa templates estándar del tema para items y botones; revisa Template Options, iconos, Required/Optional, formato máscara y altura.
- Los campos no editables deben ser Display Only o Read Only con razón funcional; ocultar no debe ser el único control de seguridad.
- Mensajes de validación junto al campo; labels visibles y accesibles; orden de tab coherente.

## LOV (List of Values)

Define por LOV:

- Display Value y Return Value; llave estable de retorno;
- source estática, query, Shared Component o API; scope y autorización;
- formato de búsqueda, columnas visibles, orden, dependencias/cascada y refresh;
- valor null/placeholder, selección múltiple o única y validación;
- tratamiento de valor histórico que ya no existe en la lista.

Usa Shared LOV cuando varios componentes comparten semántica y autorización. No conviertas una LOV grande en lista estática embebida. Los valores enviados por el navegador se validan nuevamente en servidor.

## Modal Dialog

Úsalo cuando una tarea breve requiere conservar contexto de la página anterior; evita modal para procesos largos o varias etapas complejas.

Comprueba:

1. Page Mode = Modal Dialog y page template/modal settings compatibles.
2. Qué registro/contexto se pasa y qué condiciones reciben sus valores.
3. Botones Submit, Close/Cancel y el proceso que se ejecuta con cada request.
4. Validación y errores dentro del diálogo; Cancel no modifica datos.
5. Cierre exitoso, devolución del estado/clave, refresh de la región padre y retorno de foco al control que abrió el diálogo.

Si una acción es sensible, confirma datos, motivo y alcance antes de enviar. El servidor valida de nuevo estado, actor, permiso y registro. Nunca proceses una mutación en el mero renderizado del modal.

## Comprobación

Prueba alta, edición, consulta, cancelación, errores, clave inválida, valores de LOV manipulados, permisos insuficientes, timeout API, reapertura y viewport estrecho. Inspecciona configuración en Page Designer y resultado en Runtime.


## Formularios nativos y formularios con API

- Si los datos residen en una tabla del parsing schema y el caso requiere DML estándar, usa el asistente de formulario de APEX y conserva sus procesos Fetch Row/Process Row y botones Create, Save/Update, Delete o Cancel que correspondan. Confirma los procesos que genera la versión destino.
- Si los datos residen fuera del parsing schema, conserva los componentes y la experiencia de formulario APEX, pero conecta Guardar a operaciones API explícitas de alta/edición. No simules Automatic Row Processing ni crees procesos DML contra una tabla local inexistente.
- Mantén Guardar independiente de Workflow. Después de persistir la clave, muestra la acción Workflow solo cuando el servidor confirme una transición disponible y no terminal. El botón abre una página/modal; cancelar no cambia estado y enviar invoca la operación de transición.
- Usa condiciones de servidor para presentación y valida de nuevo cada acción en el servidor. Ocultar un botón no autoriza ni protege el endpoint.
- Distingue alta, edición, cancelación lógica y transición en el contrato. “Eliminar” puede significar cancelar y conservar historial; sigue el API y sus reglas, no asumas borrado físico.
