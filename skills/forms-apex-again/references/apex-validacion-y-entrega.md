# Validación y entrega de aplicaciones APEX

Define una matriz pequeña y repetible antes de considerar terminada una página. La prueba debe observar la interacción esperada, no solo que la aplicación compile.

## Evidencia por nivel

1. Fuente: SQL/export, versión, hash/commit y configuración inspeccionados.
2. Page Designer: componentes, propiedades, Attributes, condiciones y procesos confirmados.
3. Validación APEX: validación/compilación/import completados.
4. Runtime: tarea reproducida en navegador con usuario/rol permitido.
5. Datos: resultado leído desde fuente autorizada y comparado con el comportamiento esperado.
6. Aceptación: criterios cumplidos; diferencias y estados no probados declarados.

No saltes del nivel 1 o 3 al nivel 5. Guarda evidencia con fecha, versión, entorno no secreto y alcance; minimiza o anonimiza datos personales.

## Casos mínimos por patrón

### Forms
Alta, relectura, edición, concurrencia/lost update, cancelación, borrado lógico o físico permitido, clave ausente/inválida, validaciones, LOV nula/alterada y error de servicio.

### Interactive/Classic Reports y Grid
Filtros combinados, usuario/compañía sin datos, búsqueda, sort, paginación, enlaces a forma, valores enviados/recibidos, exportación y autorización del endpoint. Grid: conflicto de edición y validación por fila.

### Dialog
Abrir con clave válida, valores transferidos, submit válido/inválido, Cancel sin mutación, cierre, refresh de padre y foco al control origen.

### Chart/dashboard
Comparar conteos con query fuente, filtro efectivo, etiquetas, combinación de cero/muchos estados, resize y navegación desde leyenda/tarjeta si se ofrece. No uses datos ficticios para ocultar un API sin contrato.

### Workflow
Guardar no transiciona; botón visible solo con instancia persistida/acción disponible; cancelar no cambia estado; enviar valida origen/actor/destino/motivo; rechazo muestra error; éxito relee estado/tracking/conteos; terminal sin rutas no ofrece transiciones. Usa instancia sintética autorizada y no borres auditoría.

## Seguridad y accesibilidad

Prueba identidad/rol permitido y denegado; manipulación de items; URL directa; claves de otro usuario; autorización en servidor; escape de texto; exposición en logs; keyboard/focus, labels y contraste. Condiciones de botón controlan apariencia, nunca autorización.

## Entrega reproducible

1. Confirma target, versión, workspace/esquema y branch/build context.
2. Exporta backup antes de editar.
3. Revisa diff acotado y dependencias afectadas.
4. Importa solo el alcance acordado; captura salida completa y errores.
5. Lee metadata de vuelta; compara componente, procesos y condiciones.
6. Prueba runtime con casos acordados.
7. Adjunta rollback, limitaciones y dueño de seguimiento.

Describe SQLcl como herramienta cuando el proyecto lo exige, pero no incluyas credenciales ni asumas que la conexión local es segura por su alias. Distingue cambios a la aplicación de DDL/DML de base de datos.
