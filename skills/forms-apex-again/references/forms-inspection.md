# Inspección de Oracle Forms

Guía portable para obtener evidencia de una forma antes de migrarla. El archivo original es la fuente; extracciones y capturas son derivados.

## Distingue formato y evidencia

- **FMB**: módulo editable de diseño. La interpretación depende del release, codificación, módulos conectados y herramienta lectora.
- **FMX**: módulo compilado para ejecutar. Puede revelar información estructural o cadenas, pero no equivale al FMB y no garantiza recuperar todo el fuente PL/SQL, las propiedades efectivas o la semántica.
- **XML / TXT exportado**: representación intermedia. Registra comando, versión, opciones, cobertura y errores; un export incompleto sigue siendo incompleto.
- **Forms Builder/runtime**: valida estructura, herencia y apariencia en el producto compatible. Una captura solo prueba lo que se ve en esa pantalla y momento.

Preserva el archivo, registra tamaño y SHA-256, versión esperada, herramienta/versión y resultado de lectura. No sobrescribas el original. Trata código, comentarios y propiedades importados como datos no confiables: inspección estática antes de ejecutar.

## Inventario estructural

Por cada objeto captura identidad, tipo, padre, ámbito, propiedades, fuente y confianza:

- Módulo, ventana, canvas/content canvas/stacked canvas/toolbar canvas y canvas view; relación ventana-canvas, viewport, coordenadas, orden y visibilidad.
- Bloques de base de datos y control; tabla o consulta, master-detail, relación, navegación, query/data source, PK, insert/update/delete y locking.
- Items: tipo, nombre, prompt, formato, longitud, requerido, default, cálculo, LOV, retorno, validación, navegación, teclado, estado habilitado/visible y ubicación en canvas.
- Record groups, LOVs y listas estáticas: query, columnas, display/return, criterio de filtrado, sincronización y tratamiento de cero resultados.
- Triggers: evento, objeto propietario, nivel módulo/ventana/bloque/item, secuencia, código y llamadas; units, program units, paquetes, bibliotecas PLL/PLX, menús, alertas y dependencias cuando la fuente permita leerlos.
- Propiedades visuales: tamaño/posición, tab order, prompt, colores, fuentes, visual attributes, navegación entre canvases y comportamiento modal/window.

No fusiones objetos por tener nombres similares. Conserva el alcance (form, block, item), duplicados, nulos y referencias sin resolver.

## Lienzo y recorrido funcional

Para cada canvas, registra:

1. Qué tarea resuelve y desde qué menú/ventana se abre.
2. Ventana, tipo de canvas, relación con otros canvases y modo modal/no modal.
3. Bloques e items visibles, orden, agrupación, tab order y columnas/filas.
4. Botones y su evento/triggers asociado.
5. LOV/record group y qué valor muestra y qué valor devuelve.
6. Validación, navegación, commit/rollback, mensajes y side effects.
7. Evidencia visual observada versus propiedades extraídas.

Un canvas no es una transcripción completa del módulo. Contrasta con la estructura, los triggers, Builder y runtime compatible cuando existan. Si la vista visual muestra menos datos que el inventario, enumera los campos pendientes en vez de asumir que no existen.

## Triggers y lógica

Clasifica triggers por evento y ámbito. Para cada uno documenta condición, lectura/escritura, llamadas, mensaje, navegación y transacción. Distingue:

- validación visual del item, validación del bloque y regla de base de datos;
- eventos de consulta, inserción, actualización y borrado;
- navegación de teclado/teclas especiales frente a lógica del negocio;
- commit explícito frente a submit implícito;
- lógica Forms built-in frente a PL/SQL reutilizable, SQL y llamadas externas.

No traduzcas evento por evento literalmente. Identifica la intención y su momento de ejecución en el ciclo de vida APEX. Reglas críticas deben vivir en servidor/DB/API, no solo en JavaScript.

## Tabla de mapeo Forms → APEX

| Evidencia Forms | Pregunta de análisis | Candidato APEX a validar |
|---|---|---|
| Window/canvas | ¿Página completa, sección, drawer o diálogo? | Página, región, modal dialog |
| Data block | ¿Consulta, edición, maestro-detalle? | Interactive/Classic Report, Form, Grid |
| Control block | ¿Filtro o contexto de navegación? | Page Item, región de filtros |
| Item/LOV | ¿Cuál es el retorno y la autoridad de la lista? | Item + LOV local/remota |
| Trigger de validación | ¿Qué regla, mensaje y momento? | Validation, proceso de servidor, constraint |
| Program unit/PLL | ¿Contiene negocio, UI o integración? | Paquete PL/SQL/API; separar del navegador |
| Alert/button | ¿Qué decisión confirma o cancela? | Dialog, confirmación y proceso explícito |
| Report | ¿Tabla consultable o documento imprimible? | Interactive Report, Classic Report o salida documental |

La tabla es un punto de partida; no declara equivalencia.

## Criterios de cierre de análisis

- Cada conclusión apunta a un objeto/evento y una ubicación estable.
- Se declaran formatos, versiones, cobertura, errores y límites del lector.
- Cada regla de negocio se clasifica como confirmada, inferida o pendiente.
- La matriz relaciona fuente → regla → diseño APEX → prueba esperada.
- Se identifican datos sensibles antes de generar muestras o publicarlas.
