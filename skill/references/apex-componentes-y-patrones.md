# Guía integral de componentes y construcción Oracle APEX

Aplica al release y tema realmente instalados. APEX cambia propiedades y capacidades; confirma cada opción en la ayuda oficial de esa versión y en Page Designer.

## Preparar la aplicación

Antes de crear páginas, fija: tarea y actores, fuente de datos, clave, seguridad, navegación, versión APEX/Universal Theme, responsive, reglas y aceptación. Define Shared Components necesarios: navegación, listas LOV reutilizables, autenticación/autorización, mensajes, build options, archivos estáticos y configuración de APIs. No codifiques secretos ni valores de un ambiente en la exportación.

## Componentes por tarea

| Tarea | Componente que se debe evaluar |
|---|---|
| Alta/edición/consulta de un registro | Form nativo local o form API-backed |
| Búsqueda operativa con filtros y vistas | Interactive Report |
| Tabla sencilla con SQL/layout definidos | Classic Report |
| Edición de varias filas | Interactive Grid, con modelo de validación/concurrencia claro |
| Indicador agregado | Chart |
| Alternar regiones relacionadas | Region Display Selector |
| Elección por catálogo | LOV local, Shared LOV o LOV remota |
| Captura de pasos o datos agrupados | Wizard/regiones por tarea, con estado persistido |
| Acción secundaria contextual | Botón en región/posición válida o menú contextual |
| Decisión que necesita contexto breve | Modal Dialog |

El componente se elige por tarea y release, no porque aparezca en la aplicación de referencia.

## Page Designer: inspección obligatoria

Por página verifica identificación, alias/título, modo, autenticación, template, navegación, regiones, items, botones, dynamic actions, validaciones, computations, processes, branches, autorizaciones y condiciones. Por región inspecciona Properties y Attributes: el Region Type/Template puede cambiar los atributos disponibles. Anota template, display position, parent region, source, order y el slot esperado.

Distingue la definición guardada del render runtime. Una pantalla que compila o una metadata que dice Next no prueba que el botón se vea o que su submit funcione.

## Plantillas y layout

Usa Page Template, Region Template, Item Template, Button Template y Template Options ya instalados. Evita inventar clases CSS para imitar un patrón que el tema ya ofrece.

- Un encabezado Hero mantiene un título/breadcrumb coherente y acciones en un slot válido de esa plantilla (comúnmente Next, verificar instalación).
- Coloca el encabezado en Breadcrumb Bar cuando ese sea el patrón del tema; no dupliques títulos en otra región.
- Ubica navegación/resumen en Left/Right Column si el page template ofrece esa columna.
- Mide la grilla dentro de cada región. No asumas que la grilla global y la regional son iguales.
- Items: Start New Row, columna, Column Span, ancho de label, template (Optional/Required/Hidden según el tema), máscara, altura e icono.
- Revisa orden de tab, labels, Required, mensajes, contraste, teclado y ancho estrecho.
- En botones define label, request, slot/posición, template/opciones, icono, Hot, condición, submit/redirect y autorización. Un slot inválido puede aparecer como Invalid Slot/Not Rendered.

## Formularios

### Tabla local

Usa wizard Form on Table/View o el patrón nativo adecuado. Conserva y configura Fetch Row, Process Row/DML y los botones generados para Create/Save/Delete/Cancel. Revisa primary key, protección de lost update, validations, branching, condiciones por modo y mensajes. No reemplaces esos procesos por SQL manual sin motivo y revisión de impacto.

### Servicio/API

Mapea GET detalle, POST alta, PUT/PATCH actualización, cancelación lógica o DELETE permitido, y transición de Workflow como operaciones separadas. Un solo botón Guardar puede crear o actualizar si el contrato lo define claramente; relee el registro y conserva su identificador tras alta. Guardar nunca debe transicionar implícitamente. El servidor comprueba identidad, ownership, estado y valores; errores deben preservar entrada cuando sea seguro.

### LOVs

Define valor visible y valor retornado, llave estable, query/source, filtros, cascada y refresh, nulos, selección, búsqueda, autorización y respuesta vacía. Una Shared LOV debe representar la misma semántica y seguridad. Los valores seleccionados por el cliente se vuelven a validar en servidor.

### Dialogs

Define página origen, valores enviados, items destino, checksum/session state, modo modal y retorno. Cancelar no muta. Submit ejecuta la acción explícita, muestra validación y, al éxito, cierra el diálogo y refresca la región origen. Prueba tab/foco/escape conforme a política y release.

## Reportes, charts y navegación

Un Interactive Report debe explicitar query, columnas visibles, búsqueda, filtros, orden, paginación, acciones y enlace a forma; valida qué clave/contexto envía y qué items reciben. Classic Report es apropiado cuando el diseño/SQL es fijo. Interactive Grid requiere permisos y concurrencia por fila. Chart usa agregaciones de datos reales, labels legibles, series con color consistente y estado vacío; no inventes conteos.

Para navegación, define lista, menú, breadcrumb, retorno y sesión. El destino recibe únicamente los valores necesarios; protege contra manipulaciones. Usa RDS si de verdad permite alternar contenido afín, con orden/default accesibles, no como contenedor arbitrario.

## Desarrollo seguro y versionado

Separa lectura, escritura y transición; no hagas DML local a tablas remotas que APEX no posee. API requiere contrato, perfil del usuario fuera del agente, autorización en servidor, timeout, logging sin secretos y estrategia de errores/reintentos. Usa SQLcl/APEX export/import cuando el equipo lo haya definido; backup, target identity check, diff/metadata read-back y validación antes/después. No despliegues sobre un ambiente cuyo nombre/rol no se haya confirmado.
