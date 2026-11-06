# Plantilla de trazabilidad Forms/Reports → APEX

Copia esta tabla en un documento del proyecto. No llenes vacíos con inferencias silenciosas.

| ID | Fuente/ubicación | Evidencia | Regla/tarea | Destino APEX/API | Prueba de aceptación | Estado |
|---|---|---|---|---|---|---|
| | archivo, objeto, trigger, canvas, query o página | extraído / Builder / runtime / DB | resultado esperado del usuario | página, región, item, validación, endpoint | paso, datos permitidos, resultado | confirmado / propuesto / pendiente |

## Registro por Forms

- Módulo y hash:
- Release / character set / plataforma:
- Herramienta de lectura y versión:
- Cobertura del extractor:
- Ventanas y canvases:
- Bloques y relaciones:
- Items/LOVs:
- Triggers/unidades/bibliotecas:
- Tablas y operaciones:
- Navegación/commit:
- Preguntas/limitaciones:

## Registro por Report

- RDF/REP/otro, release y hash:
- Query/model groups:
- Parámetros:
- Fórmulas, resúmenes y break groups:
- Triggers, libraries y subreports:
- Layout y salida:
- Datos usados para comparar:
- Diferencias abiertas:

## Contrato por página APEX

- Propósito, usuario, rol y fuente de datos:
- Page Template, breadcrumb/título, modo:
- Regiones (tipo, template, posición, Attributes y query/API):
- Items (tipo, template, LOV, validación y layout):
- Botones (acción, slot/posición, condición y autorización):
- Processes, Dynamic Actions, Branches y errores:
- Reporte/forma: filtros y clave que se transfiere/recibe:
- Estados vacío, éxito, error, no autorizado y responsive:

## Estado de confianza

- Confirmado: evidencia repetible de fuente o runtime.
- Propuesto: diseño que requiere aprobación/comprobación.
- Pendiente: falta archivo, herramienta, permiso, endpoint o caso.
- No aplica: razón documentada.

No publiques esta plantilla ya llena con nombre de cliente, esquema, URL privada, ruta local, cuenta, clave o registro de producción.