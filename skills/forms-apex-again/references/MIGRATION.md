# Forms and Reports to APEX migration playbook

Use this playbook for a new migration or for modernizing an existing APEX application. It describes a repeatable method, not a preconfigured project or a set of assumed business rules.

## 1. Establish scope

- Confirm the requested outcome, business owner, target APEX/Database/ORDS versions, environments, and authorized artifacts.
- Identify Forms modules, libraries, menus, Reports, database objects, external services, and runtime behavior that are in scope.
- Record missing inputs and tool limitations. Do not silently replace missing evidence with a sample application's behavior.
- Preserve source artifacts and calculate hashes when reproducibility matters.

## 2. Inventory and inspect

Build a source inventory with artifact name, format/version, hash, reader/tool, coverage, and limitations. For Forms, inspect supported module, canvas/window, block/item, LOV/record group, trigger/program unit, menu/library, and database-dependency structures. For Reports, inspect query/data model, groups, parameters, formulas, triggers, layout, and output/destination features where available.

Record each finding with a stable source location. Preserve physical identity, duplicate names, parent/owner, null versus empty values, and uncertain links. Separate a parser's structural result from native builder/runtime evidence.

## 3. Recover behavior and rules

For every task, map:

| Source behavior | Rule or requirement | Evidence and confidence | APEX design | Acceptance check |
|---|---|---|---|---|

Review validations, defaults, keyboard/navigation behavior, commit and rollback points, authorization, error messages, queries, parameters, external calls, and report destinations. Mark each rule confirmed, proposed, or unresolved. Do not translate Forms event order mechanically into browser behavior.

## 4. Design the APEX application

For each page, identify purpose, template, heading/breadcrumb, region placement, data source, filters, items, buttons, navigation, and empty/error/success states. Prefer built-in APEX components and the target Universal Theme. Use version-specific documentation for the target release and distinguish available template options from assumptions.

For workflows, provide a dashboard with real counts, a navigation list of states, one queue/report per relevant state, record forms, and an explicit Workflow transition page/dialog. Keep save/update/delete separate from transition. Show transition controls only for persisted records and server-confirmed eligible actions. Preserve history and verify the state after sending.

For Reports, replace output with a suitable APEX report, print/PDF process, or external reporting service based on requirements. Preserve parameters, grouping, calculations, sorting, totals, and output destination; verify each separately.

## 5. Implement safely

- Use local APEX DML only when the application owns the target table. For remotely owned records, use an approved server-side API and explicit create/update/delete operations.
- Validate identity, row scope, permissions, and transition eligibility on the server. Hidden items and client-side conditions are presentation controls, not security boundaries.
- Define transaction ownership, idempotency, retry behavior, timeout handling, and audit/history behavior for remote writes.
- Keep backups and a rollback plan for changes to shared environments. Apply the smallest authorized change.

## 6. Verify and accept

Use behavior-focused tests for create, read, update, cancel/delete semantics, validations, empty queues, each allowed transition, rejected transitions, history, authorization, errors, retries, and responsive layout. Distinguish source inspection, design review, compilation, import, runtime observation, and user acceptance.

Maintain a verification record with target versions, artifacts, test data scope, exact actions, outcomes, defects, fixes, and remaining gaps. A successful parser run or APEX import does not establish functional equivalence. Do not claim completion while required transitions, forms, reports, or acceptance checks remain unverified.

## 7. Reusable learning

Promote only reviewed, portable patterns. Keep project evidence, identifiers, schema details, connection settings, and customer data in the authorized project repository. Review public references for license and version before reusing their code or instructions.

## Comparación crítica de las referencias de extracción

Estas referencias amplían el repertorio de análisis. Son rutas complementarias con distintas capacidades; el agente escoge las que existan y aporten valor al artefacto y a la pregunta concreta. La falta de una herramienta o formato no bloquea el análisis: se continúa con las fuentes disponibles y se explicita qué detalle pudo comprobarse y qué queda incierto.

| Fuente o método | Qué puede aportar | Alcance que conviene confirmar |
| --- | --- | --- |
| [Oracle Forms2XML](https://blogs.oracle.com/apex/forms-to-apex-converting-fmbs-to-xml) ([manual oficial 19.2](https://docs.oracle.com/en/database/oracle/application-express/19.2/aemig/Converting_FormModules_ObjectLibraries_MenuModules_to_XML.html)) | Conversión estructural de FMB a XML por `frmf2xml` o Forms Builder; la familia contempla también módulos de menú y bibliotecas de objetos. Puede hacer más visibles jerarquías y propiedades que una salida textual no muestra. Para el importador APEX documentado, Oracle especifica etiquetas XML en inglés, `USE_PROPERTY_IDS=NO`, no admite bloques basados en sinónimos y permite `DUMP=ALL`. | La herramienta se introdujo en Developer Suite 9i; no asumir que está en Forms 6i ni que acepta cualquier versión antigua. Si está instalada y es compatible, conservar versión/opciones y trabajar sobre una copia. Las restricciones de importación APEX no se deben generalizar a todos los lectores. XML tampoco demuestra ejecución, dependencias resueltas ni equivalencia visual/funcional. Si esta vía no está disponible, continuar por las demás fuentes. |
| [Oracle Forms to APEX Modernization](https://blogs.oracle.com/apex/category/forms-to-apex-modernization) | Orienta el descubrimiento, la arquitectura y el rediseño. Ayuda a elegir entre componentes APEX para datos tabulares —Faceted Search/Smart Filters, Classic Report, Interactive Report, Interactive Grid y Charts— y a separar consulta interactiva de salida impresa. | Es orientación de modernización, no un extractor de módulos. La decisión final depende del objetivo, la versión destino, UX, filtros, permisos, transacciones e impresión del sistema concreto. |
| [Franklin: Oracle Forms Migration](https://github.com/franklingjr/oracle-forms-migration) | Procesa Object List Reports de Forms como TXT UTF-8, individualmente o por lotes. Puede acelerar inventario, búsqueda textual y comparación de vocabulario u objetos en varios módulos. El repositorio declara licencia MIT. | Requiere que el Object List Report esté disponible; no lee el FMB directamente. El reporte es una vista de inventario, no sustituye código, estructura binaria/XML ni inspección visual. Revisar scripts, licencia y efectos antes de reutilizar código o una aplicación demostrativa. Si no se puede generar OLR, el análisis puede continuar con FMB, Builder u otra evidencia accesible. |
| [Silvio: Forms2APEX Migration Playbook](https://github.com/silviosotelo/forms2apex-migration-playbook) | Presenta una secuencia para Forms 6i y Reports RDF y describe una extracción Python estática sin Forms/Java/Forms2XML. Puede servir como segunda lectura de triggers, PL/SQL, SQL y referencias cuando se contrasta con muestras. | Las cifras de coincidencia de triggers del README son resultados reportados por el autor, no reproducidos por este agente. El README también declara que el extractor no recupera propiedades de ítems, canvases ni posiciones. Revisar código, licencia y casos antes de adoptarlo; su disponibilidad no es requisito para usar otras rutas. |
| [Oracle Forum: convertir FMB a TXT](https://forums.oracle.com/ords/apexds/post/converting-fmb-to-txt-6621) | El hilo de 2009 registra la necesidad práctica de buscar e inventariar muchos FMB, y pregunta por automatizar Object List Reports. | Es una pregunta cerrada, no una receta ni prueba de una solución técnica. |

### Escoger y combinar fuentes según lo que esté disponible

1. **FMB:** preservar el original y su hash. Partir de la evidencia que ya exista: lector binario/estático, Forms Builder instalado, Object List Report, XML compatible, o una combinación. Forms Builder puede aportar lectura visual de canvases y propiedades; OLR aporta un índice legible y útil para lotes; XML puede exponer jerarquía y propiedades; un lector estático puede facilitar búsqueda de código. Ninguna ruta es obligatoria ni cubre necesariamente todas las capas. Contrastar sólo cuando la diferencia afecte una decisión; registrar objetos, propiedades o rangos corroborados y los pendientes.
2. **FMX:** tratarlo como salida compilada. Si está disponible el FMB correspondiente, usarlo para el análisis editable y conservar el FMX como evidencia de compilación/runtime. Si sólo se cuenta con FMX, identificar qué lectores o inspecciones compatibles pueden aportar información y describir el límite, sin aplicar comandos FMB→XML no soportados.
3. **PLL/PLD, MMB y OLB:** seguir las referencias y analizar cada artefacto que esté disponible. Si falta una biblioteca, continuar el análisis del módulo principal y marcar las unidades, herencias, menús o recursos que no pudieron resolverse; pedir el artefacto sólo cuando sea necesario para cerrar una dependencia relevante.
4. **Reports:** cuando se disponga de RDF o de una exportación compatible, Reports Builder/rwconverter puede aportar estructura; REP sirve como evidencia compilada, no como sustituto garantizado del diseño fuente. Si esas herramientas no están disponibles, usar el inventario, referencias, consultas, capturas o salidas existentes y separar claramente lo observado de lo inferido. Analizar consultas, grupos, fórmulas, parámetros, triggers, layout, destino y distribución según la evidencia obtenida.
5. **Extensiones no confirmadas (por ejemplo, RCD/RCP):** no inferir el formato sólo por la extensión. Conservar bytes/hash, buscar evidencia del productor o inspeccionar una copia con un lector apropiado disponible. Si no se puede identificar, continuar con los demás artefactos y reportar ese elemento como desconocido.

### Triangular evidencia y orientar la implementación APEX

- Etiquetar hallazgos con **fuente, método, versión si se conoce, hash, objeto/propietario, rango o ruta, grado de interpretación y cobertura**. Distinguir extracción binaria, XML Oracle, Object List Report, lector de terceros, Forms Builder/Reports Builder, diccionario/PLSQL y observación visual.
- Combinar métodos cuando ayude a resolver una duda o a aumentar cobertura, no como una lista de prerrequisitos. Comparar la misma revisión guardada. Una coincidencia corrobora sólo los campos/objetos observados; una diferencia queda como pendiente hasta entenderla. No inferir asociaciones activas a partir de nombres repetidos o coincidencias textuales sin propietario y contexto.
- Priorizar según impacto: reglas y efectos transaccionales/externos; dependencias LOV/record group; navegación y estado; consultas; propiedades y layout. Solicitar otro artefacto o herramienta sólo si resuelve una incertidumbre relevante; entretanto, avanzar con el resto y señalar el alcance parcial.
- Traducir la tarea a componentes APEX apropiados: formularios para captura/edición; reportes clásicos o interactivos, grillas, filtros y gráficos para consulta; diálogos si conservan el contexto. Reutilizar SQL cuando exista y esté autorizado, rediseñando seguridad, variables bind, filtros, paginación, autorización y errores para la versión destino.
- Para Reports, decidir según el uso entre **exploración de datos** (Interactive Report/Grid, Classic Report, búsqueda facetada o gráfico) y **documento imprimible de diseño fijo** (plantilla/motor compatible). Son necesidades distintas; las alternativas dependen de licencia, versión y operación.
- La validación de equivalencia debe cubrir las reglas y dependencias identificadas, con casos discriminantes de alta/edición/cancelación, permisos, filtros, cero/una/muchas filas, errores, impresión o viewports cuando correspondan. Separar la confianza en la extracción de las pruebas de importación, ejecución y presentación APEX.

**Enfoque:** aprovechar la combinación de fuentes que esté a mano y sea útil para cada archivo. El agente no debe exigir Forms2XML, OLR, Forms Builder, Reports Builder ni bibliotecas para comenzar; si una ruta falta, usa otra y deja visible qué pudo obtenerse, con qué confianza y qué detalle quedó pendiente.
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


