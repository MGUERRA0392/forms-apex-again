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

