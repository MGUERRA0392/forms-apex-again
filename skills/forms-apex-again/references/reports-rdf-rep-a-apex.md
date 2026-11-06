# Migrar Oracle Reports a APEX

Usa con [Inspección de Oracle Reports](reports-inspection.md). Primero identifica si el resultado es una bandeja, un análisis o un documento oficial; cada uno necesita un destino distinto.

## Fuente y evidencia

- RDF suele contener el módulo fuente editable; REP suele ser el resultado compilado para ejecutar. Verifica release, cabecera y herramienta antes de clasificar.
- RCP/RCD u otra extensión no estándar: no adivines la expansión. Comprueba formato, versión y lector.
- El PDF/impreso demuestra la salida visible, no la definición de query, fórmulas o triggers.
- Conserva el original y hash. Registra herramienta, release, opciones de exportación, warnings, objetos leídos y limitaciones.

## Extrae el modelo

Crea un inventario por reporte:

| Área | Datos por documentar |
|---|---|
| Queries | SQL, joins, binds, lexical parameters, filtros, orden y dependencias |
| Data model | grupos, relaciones, columnas, summaries, fórmulas y acumulados |
| Parámetros | tipo, formato, default, obligatoriedad, LOV y validación |
| Código | triggers, program units, librerías, subreports y llamadas externas |
| Layout | encabezados, pies, grupos repetidos, saltos, orientación, márgenes, máscaras y paginación |
| Salida | pantalla, archivo, impresión, PDF, canal y permisos |
| Runtime | filtros aplicados, volúmenes, exportación, mensajes y casos sin resultados |

Mantén por separado propiedades extraídas, observación visual, inferencia y pendiente. Un editor compatible es la fuente para propiedades que el parser no expone.

## Elegir destino

| Trabajo del usuario | Destino APEX a evaluar |
|---|---|
| Buscar, filtrar, ordenar, guardar vistas y exportar filas | Interactive Report |
| Lista sencilla con columnas y layout controlados | Classic Report |
| Edición masiva con validaciones por fila y concurrencia definida | Interactive Grid |
| Comparar indicadores agregados | Chart nativo |
| Abrir/editar un registro identificado | Reporte con enlace a Form y transferencia de clave |
| Emitir documento paginado con saltos, firmas o formato oficial | Motor documental/reporting aprobado |
| Consultar varias salidas por sección | Dashboard o páginas agrupadas, no un único reporte gigante |

No afirmes que un Interactive Report reemplaza el PDF: filtros y exportación de filas no reproducen páginas, pies, firmas ni agrupación documental.

## Traslada reglas con trazabilidad

Mapea cada parámetro a un item/bind; filtros a query y autorización de servidor; grupos a agrupación/orden; fórmula a expresión comprobada; totales a agregación con reglas de precisión; enlace a clave primaria y item receptor; máscara a formato APEX. Identifica por separado filtros de UI y seguridad por fila. Nunca confíes autorización a un item oculto.

Para reportes remotos, define el contrato de API que entrega filas, conteos, detalle y acciones. Controla paginación, tamaño de respuesta, orden permitido, filtros admitidos, timeout, errores y credenciales fuera del código/export.

## Comparación

Valida con datos sintéticos o expresamente autorizados: número de filas, grupos, totales, redondeo, nulls, fechas, zona horaria, formato y orden. Para documento, compara número de páginas, encabezados/pies, saltos, orientación y salida. Registra diferencias de propósito, no las ocultes como equivalencias.
