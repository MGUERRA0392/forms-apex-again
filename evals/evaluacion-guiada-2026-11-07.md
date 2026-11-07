# Evaluación guiada del agente público — 2026-11-07

## Alcance

Se evaluó el paquete público `Forms APEX Again` mediante lectura de sus instrucciones y una simulación manual de dos solicitudes genéricas. El repositorio ofrece skills/referencias, pero esta sesión no dispone de un ejecutor del agente remoto; esto no es una prueba de modelo, extracción binaria, compilación ni despliegue.

## Caso 1: migrar Forms y Reports con evidencia

**Entrada simulada:** migrar un módulo de solicitudes con dos canvases, bloque de base de datos, LOV de sucursal, validación y un RDF con parámetros y totales.

**Ruta observada:** la skill dirige a inspección Forms, lógica/triggers y playbook; para el RDF dirige a inspección Reports y mapeo de salida. Las guías separan FMB editable, FMX compilado, export intermedio y runtime; exigen registrar cobertura, dependencias, consulta, parámetros, layout y diferencias.

**Resultado:** PASS para el método y la delimitación de evidencia. La guía evita afirmar que un FMX o una captura recuperan por completo la lógica. La extracción concreta depende de que el usuario provea artefactos y lector compatible.

## Caso 2: crear APEX desde cero con dashboard, estados y formularios

**Entrada simulada:** construir una aplicación nueva con dashboard, gráfica agregada, navegación lateral por estados, Interactive Report por estado, formulario de alta/edición y acción explícita de Workflow.

**Ruta observada:** la skill dirige a componentes/patrones, layout, formularios y diálogos, reportes/Workflow y validación. La guía distingue formularios vinculados a tabla de formularios respaldados por API; define encabezado Hero, slots de botones, templates/Attributes, filtros por estado, enlace de edición con PK y modal de transición.

**Resultado:** PASS como especificación portable. Exige confirmar versión, tema, contratos, autorización y runtime destino; no autoriza inferir datos ni desplegar por analogía.

## Caso 3: selección de APEXREST para una aplicación APEX 24.2

**Resultado esperado:** reconocer que la guía APEXlang incluida cubre 26.1/26.2, no declarar compatibilidad con 24.2, no clasificar un destino ambiguo como DEV y continuar con el canal compatible documentado.

**Resultado:** PASS. APEXREST figura como adaptador opcional y separado de la inspección Forms/Reports, SQLcl del proyecto y validación de runtime.

## Conclusión

**Apto como guía pública supervisada** para migración Forms/Reports y desarrollo APEX desde cero. Esta evaluación confirma coherencia documental de los dos recorridos; no prueba un agente alojado ni una ejecución contra una base APEX real. Para convertirla en prueba de runtime hace falta un runner/modelo de agente y fixtures públicos sintéticos.
