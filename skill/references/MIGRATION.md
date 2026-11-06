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

