# Oracle Reports y otros reportes heredados

Analiza el artefacto y la salida antes de decidir cómo representarlo en APEX. Una lista tabular operativa y un documento paginado son tareas distintas.

## Identifica el formato

- **RDF** suele ser fuente editable de Oracle Reports; interpreta solo con herramienta/lector compatible.
- **REP** suele ser artefacto compilado de ejecución y no garantiza recuperar el modelo editable completo.
- Extensiones no estándar o ambiguas (por ejemplo, nombres recordados como RCD/RCP) deben identificarse por cabecera, versión y herramienta, no por su nombre.
- Un PDF/impreso prueba la salida observada, no el SQL, filtros, fórmulas o interacciones que la generaron.

Preserva original y hash. Registra versión de Forms/Reports, base, runtime, lector, opciones, warnings y cobertura.

## Inventario del modelo

Extrae o revisa cuando el formato lo soporte:

1. Data model y query SQL: joins, parámetros bind/lexical, grupos, orden, filtros y dependencias.
2. Columnas de detalle, summary columns, fórmulas, totales, break groups y cálculos.
3. Parámetros de entrada: tipo, default, obligatorio, validación, formato y origen.
4. Triggers de formato/evento, program units, bibliotecas, subreports y llamadas externas.
5. Layout: grupos repetidos, encabezado/pie, páginas, orientación, tamaño, estilos, imágenes, saltos, paginación y formato numérico/fecha.
6. Destinos: pantalla, impresión, PDF/archivo u otros canales, con su configuración permitida.
7. Runtime: comportamiento de filtros, orden, totales, exportación, mensajes y volumen.

Conserva separadas las propiedades extraídas, lo observado en Builder/runtime y las hipótesis. Una captura no sustituye los detalles del data model.

## Elegir la salida APEX

| Necesidad observada | Opción a evaluar |
|---|---|
| Buscar, filtrar, ordenar, guardar vistas y exportar filas | Interactive Report |
| Lista simple con control explícito del SQL/layout | Classic Report |
| Editar varias filas y guardarlas como conjunto | Interactive Grid, si el modelo y permisos lo permiten |
| Comparar indicadores agregados | Chart nativo basado en query agregada |
| Documento con encabezado, saltos, firmas o paginación fija | Generación documental aprobada (por ejemplo, motor de informes disponible); no forzar un IR |
| Resumen navegable con detalle por registro | Dashboard + report enlazado |

Antes de migrar, identifica si el resultado es operativo, analítico o documento oficial. APEX IR no reproduce por sí mismo la paginación ni el diseño impreso de Oracle Reports.

## Mapeo de reportes

Por cada salida conserva:

- parámetros fuente → page items / bind values;
- filtros y seguridad → condiciones del servidor y autorización;
- grupos/order → GROUP BY, orden y rupturas equivalentes;
- fórmulas/totales → expresiones validadas con casos;
- enlaces a detalle → clave primaria enviada y item destino;
- formato → columnas, máscara, etiquetas, formato de fecha/número;
- exportación/impresión → necesidad de negocio y controles autorizados.

Para cualquier SQL generado o recibido desde UI, evita concatenar entrada sin validar. Bind variables para valores; listas permitidas para identificadores o sort expressions; autorización y alcance de datos en servidor.

## Validación comparativa

Utiliza datos sintéticos o expresamente autorizados. Compara filtros, número de grupos, valores, orden, totales, redondeo, fechas, valores nulos, zona horaria y casos límite. Para salida documental compara páginas, encabezados/pies, saltos y archivos generados. Registra diferencias intencionales y no declares equivalencia a partir de una única muestra.
