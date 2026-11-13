# Playbook de migración de Forms y Reports a APEX

Método repetible para iniciar una migración o modernizar una aplicación APEX. No define reglas de negocio ni asume herramientas disponibles.

## 1. Acordar el alcance

- Confirma resultado, propietario funcional, versiones de Forms/Reports, APEX, Database y ORDS, entornos, artefactos autorizados y límites de cambio.
- Identifica módulos Forms, bibliotecas, menús, Reports, objetos de base de datos, servicios externos y ejecución que entran en alcance.
- Registra entradas ausentes y limitaciones de herramientas; no sustituyas evidencia faltante con comportamiento de una aplicación de ejemplo.
- Preserva los originales; calcula hashes cuando la reproducibilidad sea necesaria.

## 2. Inventariar e inspeccionar

Construye un inventario con nombre, formato/versión, hash, herramienta/lector, cobertura y limitaciones. En Forms revisa estructuras soportadas de módulos, ventanas/canvases, bloques/items, LOV/grupos, triggers/unidades, menús/bibliotecas y dependencias. En Reports revisa query/modelo de datos, grupos, parámetros, fórmulas, triggers, layout y destinos.

Registra cada hallazgo con ubicación estable, identidad física, tipo, padre/ámbito y certeza. Conserva duplicados y nulo vs vacío. Separa resultados del parser de evidencia en Builder/runtime.

## 3. Recuperar comportamiento y reglas

| Comportamiento fuente | Regla/requisito | Evidencia y confianza | Diseño APEX | Comprobación de aceptación |
|---|---|---|---|---|

Revisa validaciones, defaults, navegación, commit/rollback, autorización, mensajes de error, queries, parámetros, llamadas externas y destinos de reportes. Marca cada regla confirmada, propuesta o pendiente. No conviertas secuencias de eventos Forms en JavaScript sin entender su intención.

## 4. Diseñar APEX

Define por página propósito, plantilla, encabezado/breadcrumb, posición de regiones, fuente, filtros, items, botones, navegación, estados vacíos/error/éxito y layout adaptable. Prefiere componentes nativos y Universal Theme. Verifica la documentación de la versión objetivo y la lista real de plantillas/opciones.

Para Workflow diseña dashboard con conteos reales, navegación por estados, bandeja/reporte por estado, forma de registro y una interacción Workflow dedicada. Guardar y transicionar son acciones distintas. Enseña la transición solo en registro persistido y elegible; confirma actor, destino y motivo en el servidor; conserva historial y vuelve a leer el resultado.

### Reconstrucción de una aplicación Workflow desde cero

1. Levanta el contrato del motor y del registro de negocio antes de crear páginas: WFID, estados, pasos/acciones, actores, terminales, devoluciones, campos editables por etapa y endpoints de lectura/escritura/transición.
2. Crea una aplicación nueva con ID asignado por el entorno y un backup verificable. Importa o genera la metadata solo tras revisar workspace, versión, ambiente y alcance; nunca reutilices un `install.sql` que borre una aplicación existente sin sustituir y volver a comprobar el ID objetivo.
3. Define el contexto global del flujo cuando sea necesario: Application Item `GLOBAL_ACTUAL_FLOW`, cargado desde el WFID cotejado con el motor y compartido entre páginas. No uses nombres de variables o IDs de ejemplo como autoridad del servidor.
4. Construye el dashboard con Hero/Breadcrumb y botones en el slot válido de la plantilla, gráfica nativa con conteos reales, resumen, rail lateral con iconos y conteo visible. En estado vacío muestra cero/sin datos sin fabricar porcentajes. Conserva el mismo encabezado estándar en dashboard, bandejas y formas.
5. Crea navegación por `STATUS_ID`; cada estado conduce a su Interactive Report filtrado por estado/contexto y a la forma correspondiente mediante una clave estable. Configura query, filtros, enlaces, valores enviados y items destino; verifica tanto el SQL/API fuente como el renderizado y la navegación en Runtime.
6. En las formas, conserva las acciones nativas de retorno y persistencia. Usa Fetch/Process Row para una tabla local propia; para datos remotos usa contratos API explícitos. Muestra `Workflow` solo después de confirmar ID/instancia y estado no terminal. El botón abre una página o diálogo; solo su acción `Enviar` ejecuta la transición.
7. Cierra la prueba en Runtime con un registro sintético no productivo: crear, releer, editar/guardar, abrir/cancelar Workflow, ejecutar transición permitida, releer estado/tracking y comprobar rechazo de actor/estado no autorizado y comportamiento terminal. No declares capacidad de réplica probada con metadata exportada o un ciclo histórico de otra versión.

En cada hito guarda export/backup y un read-back de metadata. Contrasta las posiciones, propiedades y Attributes de Page Designer con el Runtime; una definición presente puede no renderizarse si el slot no es válido.

Para reportes selecciona Interactive Report u otra salida según necesidades. Conserva parámetros, agrupación, cálculos, orden, totales, permisos y destino; prueba cada aspecto.

## 5. Implementar con seguridad

- Usa DML APEX local si la aplicación es propietaria de la tabla. Para datos remotos, usa API aprobado con contratos explícitos de create/read/update/cancel/delete/transition según aplique.
- Valida identidad, alcance del registro, autorización y estado de transición en servidor. Items ocultos y condiciones de cliente no son frontera de seguridad.
- Define propietario transaccional, idempotencia, reintentos, timeout, auditoría e historial para escrituras remotas.
- Mantén backup recuperable, plan de rollback y cambios mínimos en ambientes compartidos.

## 6. Verificar y aceptar

Prueba creación, lectura, actualización, semántica de cancelar/eliminar, validaciones, bandejas vacías, cada transición permitida y rechazada, historial, autorización, errores, reintentos y layout responsive. Distingue revisión de fuente, revisión de diseño, compilación, importación, runtime y aceptación del usuario.

Registra versiones, entorno, alcance de datos de prueba, acciones exactas, resultado, defectos, correcciones y brechas. Parser exitoso o importación APEX no demuestran equivalencia. No declares el trabajo listo si quedan reportes, formas, transiciones o aceptaciones requeridas sin verificar.

## 7. Promover aprendizaje

Publica solo patrones portables que hayan sido revisados. Mantén nombres de proyecto, esquemas, APIs internos, conexión, rutas y datos de negocio en el repositorio privado autorizado. Revisa licencia y versión de las fuentes externas antes de reutilizar material.



## Referencias operativas relacionadas

- [Inspección Forms](forms-inspection.md) cubre lienzos, triggers, LOVs y límites FMB/FMX.
- [Inspección Reports](reports-inspection.md) distingue modelo de datos, salida interactiva y documento paginado.
- [Formularios y diálogos APEX](apex-forms-and-dialogs.md) cubre DML generado, API remoto, modales y retorno.
- [Layout y navegación APEX](apex-navigation-and-layout.md) cubre templates, slots, atributos, RDS y grilla.
- [Reportes y Workflow APEX](apex-reports-and-workflow.md) cubre reportes por estado, dashboard y transiciones seguras.

## Comparación crítica de las referencias de extracción

Las herramientas de estas referencias resuelven problemas distintos; no se deben presentar como convertidores intercambiables ni sumar sus salidas como si fueran una extracción completa.

| Fuente o método | Entrada y valor | Límite que debe conservar el análisis |
| --- | --- | --- |
| [Oracle Forms2XML](https://blogs.oracle.com/apex/forms-to-apex-converting-fmbs-to-xml) | Oracle documenta conversión de FMB a XML desde línea de comandos (`frmf2xml`) o Forms Builder. La familia Forms2XML también contempla módulos de menú y bibliotecas de objetos. El XML estructural permite revisar jerarquías y propiedades que un volcado de texto plano puede perder. | Se introdujo en Developer Suite 9i; no asumir que viene con Forms 6i ni que la versión instalada acepta cualquier archivo antiguo. Registrar versión/opciones y trabajar sobre una copia. Si el módulo requiere actualización de formato para convertir, actualizar solo una copia y conservar el original/hash. XML tampoco prueba ejecución, dependencia resuelta ni paridad visual/funcional. |
| [Oracle Forms to APEX Modernization](https://blogs.oracle.com/apex/category/forms-to-apex-modernization) | La guía de Oracle separa descubrimiento, arquitectura y rediseño; recomienda reutilizar lógica de base de datos cuando es apropiado y construir páginas con componentes APEX. Para datos tabulares propone comparar Faceted Search/Smart Filters, Classic Report, Interactive Report, Interactive Grid y Charts; para salida impresa distingue plantillas y motores. | No existe conversión automática universal. La consulta de origen puede orientar una región APEX, pero filtros, permisos, UX, transacciones y formato de impresión requieren contratos y pruebas del sistema real. Elegir según tarea y versión destino. |
| [Franklin: Oracle Forms Migration](https://github.com/franklingjr/oracle-forms-migration) | Recibe Object List Report de Forms como TXT UTF-8 y permite procesar uno a uno o por lotes. Aporta un método práctico para buscar/inventariar muchos módulos, comparar vocabulario y generar candidatos de lógica. El repositorio declara licencia MIT. | No lee el FMB directamente: depende de que el Object List Report se haya producido. El reporte es una proyección de objetos/propiedades, no reemplaza la estructura binaria/XML, el código completo ni la inspección visual. Los scripts y la aplicación demostrativa no se ejecutan sobre una base del cliente sin revisar código, privilegios, licencia y efectos. |
| [Silvio: Forms2APEX Migration Playbook](https://github.com/silviosotelo/forms2apex-migration-playbook) | Propone una secuencia con compuertas para Forms 6i y Reports RDF, y describe un extractor Python estático sin Forms/Java/Forms2XML. Sus resultados pueden servir como segunda lectura para triggers, PL/SQL, SQL y referencias cuando la herramienta se valida con muestras. | El README reporta coincidencias de triggers entre 20/20 y 54/56 según módulo; son cifras del autor, no reproducidas por este agente ni garantía de cobertura. El mismo README declara que ese extractor no recupera propiedades de ítems, canvases ni posiciones y reserva esas evidencias para exportación estructural. No tratar la salida como árbol completo ni copiar/ejecutar código sin revisar fuente, licencia y casos. |
| [Oracle Forum: convertir FMB a TXT](https://forums.oracle.com/ords/apexds/post/converting-fmb-to-txt-6621) | El hilo de 2009 documenta una necesidad recurrente: inventariar/buscar frases en lotes grandes y pregunta por automatizar Object List Reports. Sirve para identificar el problema operativo y el valor del procesamiento por lotes. | Es una pregunta cerrada, no una receta ni evidencia de que un método concreto funcione. No atribuirle una solución técnica. |

### Elegir evidencia por tipo de artefacto

1. **FMB:** conservar el original y hash; obtener primero inventario/cobertura del lector disponible. Si la versión lo permite, contrastar con Forms2XML; generar Object List Report como índice complementario. Comparar conteos e identidades de ventanas, canvases, bloques, ítems, LOV/record groups, triggers, program units, propiedades y referencias. Registrar diferencias por objeto/rango. Un artefacto puede cubrir código y dejar geometría o propiedades pendientes.
2. **FMX:** es salida compilada, no asumir que conserva una representación editable o toda la metadata del FMB. No aplicar comandos FMB→XML a FMX sin soporte documentado para esa versión; pedir el FMB fuente correspondiente o declarar el límite.
3. **PLL/PLD, MMB y OLB:** inventariarlos por separado y seguir referencias desde Forms. La referencia a biblioteca no entrega su contenido; solicitar la fuente/artefacto exacto para herencia, unidades externas, menús y recursos.
4. **Reports:** identificar RDF como fuente de diseño editable y REP como salida compilada cuando la procedencia esté confirmada. Usar Reports Builder/rwconverter compatible para una lectura estructural; analizar por separado consultas, grupos, fórmulas, parámetros, triggers, layout, destino y distribución. No afirmar que un RDF/XML recrea automáticamente un REP ejecutado.
5. **Extensiones no confirmadas (por ejemplo, RCD/RCP):** no inferir formato por el nombre. Conservar bytes/hash, consultar el productor y probar un lector apropiado en una copia. Informar el resultado como desconocido hasta verificarlo.

### Protocolo de triangulación y conversión a APEX

- Etiquetar cada hecho con **fuente, método, versión, hash, objeto/propietario, rango o ruta, estado de interpretación y cobertura**. Mantener separados: extracción binaria, XML Oracle, Object List Report, lector estático de terceros, Forms Builder/Reports Builder, diccionario/PLSQL de base y observación visual.
- Comparar métodos sobre la misma revisión guardada. Una coincidencia valida solo ese campo/objeto/muestra; una diferencia abre un pendiente, no se resuelve eligiendo la salida más completa por intuición. No promover cadenas, nombres repetidos ni coincidencias de trigger a asociaciones activas sin propietario y contexto.
- Priorizar los huecos por impacto: reglas/validaciones, transacciones y efectos externos; luego dependencias LOV/record group, navegación/estado, consultas y finalmente propiedades/layout. Pedir una nueva exportación solo si cubre un hueco específico.
- Traducir tareas a componentes nativos APEX según el contrato: formularios para captura/edición; reportes clásicos o interactivos, grillas, filtros y gráficos para consulta; diálogos si conservan el contexto de tarea. Reutilizar SQL cuando esté disponible y autorizado, pero volver a definir seguridad, bind variables, filtros de estado, paginación, autorización y tratamiento de errores.
- Resolver salida de reportes en dos decisiones: **exploración de datos** (por ejemplo, Interactive Report/Grid, Classic Report, búsqueda facetada o chart) y **documento imprimible de diseño fijo** (layout/plantilla y motor compatible). El reporte interactivo no es sustituto automático del formulario pixel-perfect; Oracle enumera alternativas de impresión que dependen de licencia, versión y operación.
- Aceptar una migración solo cuando cada regla y dependencia tiene evidencia de origen, componente/consulta destino y casos de prueba discriminantes. Verificar edición/alta/cancelación, permisos, filtros por estado, cero/una/muchas filas, errores, impresión y viewports relevantes según aplique. Separar prueba del extractor, importación APEX, ejecución funcional y revisión visual.

**Conclusión operativa:** usar lectura estática y OLR para amplitud/búsqueda, Forms2XML para contraste estructural cuando sea compatible, y Builder/diccionario para resolver propiedades y dependencias. Ninguna referencia por sí sola garantiza recuperación completa. Registrar explícitamente qué capas faltan antes de afirmar que un módulo está entendido o migrado.
- Mantener perfiles por edición exacta: el diseño común puede dirigirse a 23/24/26, pero [APEXlang y SQLcl](https://docs.oracle.com/en/database/oracle/apex/26.1/apxdc/using-sqlcl-apexlang.html) requieren su perfil 26.1. Validación sintáctica y export/import son etapas distintas de pruebas funcionales. No generar llamadas internas de APEX suponiendo compatibilidad entre versiones.

## Reglas y desarrollo

La matriz debe enlazar **objeto/regla Forms → evidencia/hash/ubicación → regla DB cuando sea visible → implementación APEX → prueba de equivalencia → mejora propuesta y su prueba**. Separar comportamiento existente de cambios acordados.

Antes de adaptar un disparador o program unit, clasificar acceso a datos, validación, transacciones, presentación, navegación, estado y llamadas externas. Revisar parámetros, orden, condiciones y excepciones; una coincidencia léxica no demuestra ejecución. No reemplazar built-ins de Forms mediante búsquedas de texto como si fueran SQL.

Diseñar operaciones PL/SQL reutilizables con contexto explícito, autorización servidor y límites transaccionales. Revisar commit/rollback, excepciones absorbidas, SQL dinámico, secuencias, concurrencia y efectos externos. En APEX, foco y sesión web no reproducen automáticamente el ciclo de eventos Forms. Compartir LOV sólo después de confirmar consultas, filtros, retornos múltiples, NULL, orden y dependencias en cascada.

El FMB puede indicar reglas de DB, pero no contiene necesariamente packages, triggers, constraints, VPD, sinónimos o llamadas remotas. Usar el contrato Oracle MCP/SQLcl del proyecto autorizado cuando exista conexión. Un modelo AI o una conexión MCP no otorgan por sí mismos visibilidad ni validan las reglas. Sin esquema disponible, continuar local y mantener pendiente la prueba DB; no consultar una conexión ajena.

## Criterio de equivalencia funcional

Definir primero qué debe conseguir el usuario y qué invariantes deben conservarse. Las páginas, regiones, disposición visual y organización técnica pueden cambiar. Demostrar por separado que se conservan las reglas y resultados acordados; reproducir el orden de los eventos Forms no basta.

Para cada tarea del módulo, registrar un contrato de aceptación con evidencia del origen y casos concretos:

| Aspecto | Resultado que debe contrastarse |
| --- | --- |
| Selección y captura | Claves, filtros, valores retornados, NULL y listas estáticas correctos |
| Reglas y permisos | Validación y autorización servidor para cada acción, usuario y estado |
| Guardado y cancelación | Efectos persistidos, unidad de trabajo, rollback y borrador descartado |
| Reintentos y concurrencia | Identidad de la operación, conflicto de payload y versión obsoleta; sin duplicar ni sobrescribir indebidamente |
| Integraciones y Reports | Parámetros, resultados y efectos externos, con dependencias explícitas |
| Recuperación y uso | Mensaje comprensible, estado final, navegación y siguiente acción disponibles |

Aplicar solo los aspectos presentes o necesarios en la aplicación. No añadir archivado, aprobaciones ni roles porque existan en una muestra. Una mejora que cambia una regla debe figurar como decisión de negocio pendiente de revisión, con su prueba propia. Si el legado presenta una anomalía, documentar el comportamiento observado y la regla esperada; no conservar ni corregir silenciosamente el posible defecto.

Distinguir evidencia de fuente, prueba de la API, prueba de la interfaz y contraste funcional del módulo. Un laboratorio sintético forma criterio sobre componentes y técnicas; sus resultados no acreditan las reglas del FMB. Si falla una prueba, identificar si el fallo pertenece al arnés, a la implementación o a la expectativa antes de modificar el contrato o repetir una operación con efectos.

## Interfaz, flujo y dimensionamiento

Partir de las tareas y no de las coordenadas: búsqueda/bandeja → detalle → selección → acción → respuesta y recuperación. Evaluar formularios, maestro-detalle, edición por lote, filtros y diálogos según atomicidad, frecuencia, permisos y tamaño medidos. Mantener acceso por teclado, etiquetas, mensajes claros, foco y tamaños de pantalla. Las posiciones del canvas sólo aportan evidencia del contenido.

Proponer menos pasos y menos captura duplicada, defaults justificados, guardado claro y revisión de errores. Una aprobación, automatización, outbox o nueva auditoría son cambios de negocio/arquitectura, no equivalencia automática. Indicar alternativas, impacto en reglas, costo y criterio de decisión.

Dimensionar módulos por reglas, integraciones, Reports, dependencias, datos, permisos y pruebas. Registrar incertidumbres y calibrar horas con un piloto medido. No convertir conteo de ítems en fechas fiables ni inventar usuarios, volúmenes o SLA. Comparar tiempo de tarea, errores, consultas y latencia con una base medida.

## Reports

Para cada invocación documentar report object, archivo RDF/REP/JSP, parámetros de usuario/sistema, contexto, formatos, destino, ejecución síncrona/asíncrona y manejo de estado/error. Distinguir definición de diseño de salida con datos. [rwconverter](https://docs.oracle.com/middleware/12212/formsandreports/use-reports/pbr_cla005.htm) puede convertir RDF a XML; el resultado no compila ni prueba automáticamente la lógica.

Inventariar consultas/grupos/links, columnas fórmula/resumen/placeholder, unidades PL/SQL y triggers de reporte; también marcos repetidos, anclajes, formato condicional, fuentes/imágenes, márgenes, encabezados/pies, totales, saltos y parámetros. Registrar subreportes, librerías, distribución, impresión, NLS y recursos externos. Conservar contenido desconocido, nunca ocultarlo tras un conteo de objetos.

Separar dos decisiones: consulta interactiva en APEX y documento con diseño preciso. Los [reportes APEX](https://docs.oracle.com/en/database/oracle/apex/26.1/htmdb/developing-reports.html) permiten interacción; para [impresión](https://docs.oracle.com/en/database/oracle/apex/24.2/htmdb/printing-report-regions.html), comprobar límites del modo nativo y necesidades de plantilla. FOP, JasperReports, BI Publisher, Document Generator o AOP son opciones a evaluar según requisitos, versión, costo y operación; no son convertidores RDF intercambiables.

Validar con datos sintéticos: vacío/una fila/muchas páginas, totales, NULL, negativos, monedas, fechas, acentos, cadenas largas, imágenes y tamaños de papel. Comparar valores y salida renderizada por separado. No eliminar lógica Reports como “sólo formato” sin revisar efectos laterales. La implementación completa de Reports sigue pendiente de entradas y pruebas, aunque su inventario esté disponible.

## Aprendizaje y dependencias

Registrar hallazgos nuevos como hipótesis con hashes, contraejemplos y límites; promover un patrón sólo con pruebas discriminantes y revisión. Aprendizaje local no entrena automáticamente modelos ni permite transferir datos privados entre clientes.

Si falta un componente necesario, primero preparar la decisión concreta: función requerida, prueba que falta, alternativas existentes, plataforma/versión, origen, licencia, ubicación propuesta y verificación posterior. Pedir sólo la instalación que resuelva esa dependencia. Para Python local no exigir Java, Go, Forms, Reports, DB ni servicios cloud. Para contraste instalado pedir una ruta/versiones solamente cuando toque ejecutar; no repetir solicitudes de entorno ya contestadas.

## Contrato de propiedades del blueprint

Para cada propiedad o regla que se adapte, registrar los siguientes campos como contrato de diseño revisable. Esta plantilla no modifica el modelo extraído ni genera automáticamente APIs APEX:

```json
{
  "source": {"object_id": "...", "owner_id": "...", "property": "...", "stored_value": null, "stored_state": "unknown", "effective_value": null, "effective_state": "unresolved", "origin": "unresolved", "source_sha256": "...", "evidence_location": "..."},
  "target": {"component": "...", "blueprint_property": "...", "proposed_value": null, "value_state": "pending", "apex_release": "unconfirmed", "api_surface": "not_selected"},
  "decision": {"pattern_ids": [], "rationale": "...", "equivalence_or_improvement": "pending", "alternatives": [], "dependencies": []},
  "validation": {"scenarios": [], "documentary_evidence": [], "import_verified": false, "functional_verified": false},
  "status": "proposed_with_gaps"
}
```

`null` con estado `unknown` no significa NULL explícito almacenado. Conservar vacío, NULL, ausencia, defaults y herencia según el método. No sustituir unidades geométricas, built-ins, estado de sesión ni transacciones sin justificar la transformación. Una mejora propuesta debe tener su propia prueba además de equivalencia.

En `decision.rationale`, vincular cada patrón a una decisión y a sus prerrequisitos acreditados; un ID válido sin esa relación no basta. No modificar `source` para hacer coincidir una recomendación. Un valor destino opcional u obligatorio puede proponerse como decisión de negocio pendiente; no se presenta como propiedad efectiva del origen mientras siga sin resolver.

Para LOV y salidas AJAX añadir una matriz de retornos al diseño: expresión/columna de origen con propietario y evidencia → componente destino confirmado o propuesto → mecanismo específico → tipo/NULL/vacío → validación servidor → prueba. El alias identifica una columna del resultado de la consulta, pero no acredita un enlace con un ítem de página o una columna de grid APEX. Un destino o mecanismo sin confirmar permanece pendiente; las propiedades conceptuales del blueprint no generan un enlace ejecutable.

Consultar el tema `apex-patterns` para prerrequisitos y pruebas: tareas/componentes, LOV, sesión/AJAX, autorización, transacciones/concurrencia, integraciones, sincronización, mapeos/reintentos, estado vacío, presentación de payloads, navegación y aprendizaje versionado. Usar claves de blueprint como esquema conceptual; escoger atributos y APIs documentadas después de confirmar la edición destino.

