# Condiciones de visibilidad de botones Submit en Oracle APEX

APEX evalúa condiciones server-side durante el render. Si la condición usa un item que empieza vacío y se llena después en el navegador, cambiarlo no vuelve a renderizar el botón.

Para una transición de workflow, muestra el botón cuando el servidor conoce una instancia persistida en estado no terminal. Valida nuevamente la acción seleccionada, el comentario requerido, la autorización del actor y el destino permitido en el proceso server-side. La condición de render controla visibilidad; no reemplaza autorización ni validación.

Mantén Guardar y Workflow como acciones separadas cuando la transición sea una decisión explícita del usuario. La aceptación debe cubrir instancia no terminal, estado terminal, campos incompletos y transición autorizada. Distingue la metadata configurada de las pruebas observadas en runtime.
