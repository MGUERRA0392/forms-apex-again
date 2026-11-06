# Conocimiento técnico reutilizable

Esta guía contiene patrones generales. No agregues nombres de clientes, ambientes, esquemas, credenciales, URLs privadas, rutas locales, registros reales ni conclusiones de proyectos sin anonimizar y revisar.

## Niveles de evidencia

Mantén separados estos niveles:

1. **Documentado:** respaldado por documentación oficial citada.
2. **Extraído:** presente en el artefacto mediante lector y ubicación reproducible.
3. **Interpretado:** hipótesis a partir de la extracción; declara alternativas y confianza.
4. **Compilado/importado:** el producto aceptó el artefacto, sin demostrar comportamiento correcto.
5. **Observado en runtime:** reproducido en un entorno autorizado y versionado.
6. **Aceptado:** evidencia cotejada con el requisito esperado.

Un nivel no implica el siguiente. Conserva nombres duplicados, relaciones dudosas e identificadores hasta tener evidencia que los resuelva.

## Lectura Forms y Reports

- Los formatos binarios varían por versión/plataforma. Registra versión, herramienta, hash cuando corresponda, cobertura y limitaciones del lector.
- Contrasta extracción estructural con Builder/runtime nativos cuando estén disponibles. Preserva la identidad original del artefacto.
- Para Forms, revisa lienzos, ventanas, bloques, items, propiedades, navegación, LOVs, grupos de registros, triggers, unidades, menús, bibliotecas y dependencias si la fuente los soporta.
- Un lienzo o preview no revela todo el código de la forma. Anota qué objetos y propiedades se inspeccionaron.
- Para Reports, revisa query/modelo, grupos, columnas, parámetros, fórmulas, triggers, bibliotecas, layout y destinos. No infieras que RDF/RPX/REP representan el mismo nivel de fuente o ejecución.
- Conserva valores nulos frente a cadenas vacías, ámbitos distintos y elementos duplicados.

## APEX declarativo y nativo

- Usa componentes APEX nativos y Universal Theme como base. Escoge plantillas y Template Options disponibles en esa versión/instalación.
- Ubica encabezado y acciones en la zona de breadcrumb/hero prevista; pon contenido, botones y items en el slot definido por la plantilla.
- En regiones, inspecciona tanto Properties como Attributes. La plantilla determina atributos disponibles; cambia una configuración a la vez y verifica el resultado.
- Usa página de reporte/bandeja para lista filtrable y forma nativa para detalle cuando el modelo de datos pertenece a APEX. Verifica enlace de fila, clave primaria, estado, valores enviados y items receptores.
- En formas locales, conserva procesos de Fetch Row y Process Row y botones DML generados por APEX. Adapta condición de creación/edición, botones, template options y slot en lugar de quitar el mecanismo sin necesidad.
- Si la persistencia reside en otro servicio, la forma APEX debe invocar API de manera explícita y no fingir DML sobre una tabla ausente.
- Organiza campos relacionados, usa templates estándar y la cuadrícula real de la región. Region Display Selector debe resolver una navegación útil; no lo agregues solo para imitar un ejemplo.
- Usa CSS/JavaScript a medida solo para una carencia concreta, con escape, accesibilidad y compatibilidad verificada.

## Dashboard y Workflow

- Un dashboard de Workflow normalmente combina título/encabezado con acciones, gráfica por estado, resumen total y panel de navegación por etapas.
- Un estado puede corresponder a un Interactive Report o bandeja, y a una forma enlazada por clave; verifica filtros, enlaces, botones, destinatario y estado transmitido.
- Los estados visibles y el total deben provenir de resultados reales. Una respuesta vacía se representa como “sin datos”; nunca inventes cantidades.
- Separa persistir cambios del registro y moverlo de estado. Guardar no debe disparar transición implícita.
- Muestra Workflow cuando exista instancia guardada y transición autorizada. El botón abre diálogo/página con estado actual, acciones disponibles, comentario/motivo, asignación y tracking.
- La API/servidor valida actor, estado de origen, destino, permisos, comentario y concurrencia. Un item oculto o condición cliente solo controla presentación.
- Tras una transición, vuelve a consultar estado actual e historial. Mantén devoluciones y cancelaciones trazables; identifica explícitamente el estado terminal.

## Datos remotos y contratos API

El contrato del API determina cómo se usan datos remotos. Documenta método, ruta, autenticación, autorización, filtros, entrada/salida, errores, idempotencia, timeout y dueño de la transacción.

Bind cada consulta a una compañía/principal/asignación validada en servidor. El valor del item de página no es control de autorización. Distingue respuesta HTTP exitosa, éxito de la página APEX y commit durable salvo que el contrato pruebe atomicidad.

## Verificación

Usa matriz trazable requisito → componente → evidencia → prueba → resultado. Comprueba casos vacío, éxito, validación, error de servidor/API, no autorizado, reintento y resolución de destino. Registra versiones, entorno, alcance de datos y limitaciones. No declares equivalencia visual sin mirar runtime, ni funcionalidad por solo inspeccionar el código fuente.



## Estándar de construcción APEX para Workflow

- En una pantalla de flujo, usa el encabezado Hero con título y breadcrumb en la zona `Breadcrumb Bar`; coloca acciones del encabezado en el slot `Next` que provee la plantilla. Confirma el nombre del slot en Page Designer y valida que se renderice en runtime.
- Usa botones y Template Options estándar del tema instalado. `Retornar` permanece disponible; diferencia la acción principal con la opción visual estándar adecuada (por ejemplo, `Hot`) y evita CSS para simular plantillas existentes.
- En el dashboard, combina gráfico por estado, resumen con totales reales, contenido descriptivo útil y lista de estados en la columna lateral; cada estado navega a su reporte filtrado por el identificador real de estado. Usa iconos y rótulos legibles, no añadas números de secuencia al nombre del estado.
- Cada bandeja debe ser un reporte con consulta y filtros explícitos por estado, y por usuario/compañía cuando el contrato lo permita. Revisa columnas, orden, búsqueda, paginación, enlace `Editar`, valores enviados y los items de destino de la forma. La forma debe conservar la clave y contexto de estado correctos.
- Una forma API-backed separa `Crear/Guardar` de la transición. El guardado crea o actualiza según la clave persistida; no debe avanzar el flujo automáticamente. Muestra `Workflow` solo con registro e instancia persistidos y mientras haya transición autorizada. Ese botón abre una página/modal de decisión; `Cancelar` no cambia datos y `Enviar` aplica la acción con comentario requerido y vuelve a leer estado e historial.
- En Forms locales sigue usando `Fetch Row`/`Process Row` y DML nativo generado por APEX. Para un origen remoto, usa operaciones API explícitas para alta, edición y cancelación lógica; no crees procesos APEX que aparenten DML sobre tablas que no están en la base del workspace.
- Distribuye campos por grupos funcionales en la cuadrícula de doce columnas de la región. Usa `Optional` para los items y revisa `New Row`, `Column`, `Column Span` y `Label Column Span`; utiliza Region Display Selector cuando ayude a organizar grupos y mantén las propiedades/atributos de región compatibles con la plantilla estándar.
- Antes de exportar, lee de vuelta metadata declarativa: tipo de página, plantilla, posiciones, botones/condiciones, consultas/filtros, items enviados/recibidos y procesos. Luego valida por separado apariencia y comportamiento en runtime.


## Referencias por tema

Para una guía operativa más extensa usa [inspección Forms](forms-inspection.md), [inspección Reports](reports-inspection.md), [formularios y diálogos APEX](apex-forms-and-dialogs.md), [layout/navegación APEX](apex-navigation-and-layout.md) y [reportes/Workflow APEX](apex-reports-and-workflow.md). Estas guías afinan patrones generales; la versión y configuración del destino siguen siendo la autoridad.


## Mapa rápido de referencias profundas

| Tema | Referencia |
|---|---|
| Estructura Forms y límites FMB/FMX | [forms-inspection.md](forms-inspection.md) |
| Semántica de triggers y transacciones | [forms-triggers-and-logic.md](forms-triggers-and-logic.md) |
| Reports RDF/REP y selección del destino | [reports-rdf-rep-a-apex.md](reports-rdf-rep-a-apex.md) |
| Forms, LOVs y modal dialogs | [apex-forms-and-dialogs.md](apex-forms-and-dialogs.md) |
| Componentes declarativos y Page Designer | [apex-componentes-y-patrones.md](apex-componentes-y-patrones.md) |
| Reportes, gráficos y Workflow | [apex-reports-and-workflow.md](apex-reports-and-workflow.md) |
| Pruebas, seguridad y entrega | [apex-validacion-y-entrega.md](apex-validacion-y-entrega.md) |
| Matriz reutilizable | [plantilla-trazabilidad.md](plantilla-trazabilidad.md) |

El repositorio público publica guías portables. Herramientas complementarias como SQLcl, plugins de APEX REST, Forms Builder/Reports Builder, extractores o MCP son opcionales y se instalan/configuran por separado. Verifica versión, licencia, permisos y capacidad activa; nunca dependas de un perfil privado embebido en el agente.
