# Uso opcional de APEXREST con Forms APEX Again

APEXREST for Codex and Claude Code puede ayudar a redactar y validar fuentes APEXlang, consultar referencias y metadatos, y gestionar importaciones cuando el proyecto, versión y destino cumplen los requisitos del complemento. Es un adaptador opcional; no forma parte obligatoria de la migración ni reemplaza SQLcl, ORDS o las herramientas de inspección de Forms/Reports.

## Selección por versión y destino

- Confirma la versión real de APEX antes de elegir el flujo. Las guías APEXlang de APEXREST disponibles para este paquete corresponden a 26.1 y 26.2; no supongas compatibilidad con 24.2.
- Para versiones o tareas no cubiertas por APEXREST, utiliza el export/import compatible con la versión y el flujo SQLcl autorizado por el proyecto, y valida el resultado en runtime.
- Antes de cualquier escritura, verifica la identidad efectiva del destino mediante evidencia de conexión. Un alias, nombre DNS o indicación en la interfaz no basta para clasificarlo.
- El complemento limita los despliegues a entornos DEV, QA o TEST. Si el destino figura como producción o la clasificación es ambigua, no configures, reclasifiques ni despliegues con APEXREST.
- La capacidad de ejecutar SQLcl desde WSL no implica que el proceso MCP de APEXREST pueda invocarlo. Trata ambos canales por separado y no dupliques ni copies secretos para salvar una diferencia de permisos.

## Secuencia recomendada

1. Analiza Forms/Reports y registra cobertura, reglas y dependencias.
2. Define el modelo de datos, consultas, seguridad y aceptación APEX.
3. Selecciona componentes declarativos con evidencia del tema, versión y contenedor.
4. Si APEXREST es compatible con la versión y destino, consulta su estado, usa referencias acotadas y valida la fuente antes de importar.
5. Haz la prueba funcional y visual por separado en runtime, con identidad y datos autorizados.
6. Informa qué verificaste, qué no, y el origen de cada evidencia.

No instales dependencias, aceptes licencias, guardes credenciales ni cambies la clasificación del entorno sin autorización específica.