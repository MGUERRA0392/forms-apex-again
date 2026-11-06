---
name: forms-apex-again
description: Analiza Oracle Forms y Reports con evidencia, planea migraciones que preservan el comportamiento y desarrolla aplicaciones Oracle APEX nativas.
---

# Forms APEX Again

Usa esta guía para inspeccionar Oracle Forms o Reports, planear su migración a Oracle APEX, o crear y mantener aplicaciones APEX a partir de requisitos. Es conocimiento portable: no incluye acceso a ambientes, credenciales ni diseños de clientes.

## Selecciona el recorrido

- **Análisis o migración de Forms/Reports:** sigue [las instrucciones de operación](references/INSTRUCTIONS.md), luego el [playbook de migración](references/MIGRATION.md) y la [base de conocimiento](references/KNOWLEDGE.md).
- **Desarrollo APEX sin Forms:** usa los criterios de APEX en `KNOWLEDGE.md` y contrástalos con la documentación de la versión destino.
- **Trabajo combinado:** conecta cada evidencia fuente con páginas, componentes, procesos, APIs y comprobaciones de aceptación. Mantén explícitas las decisiones pendientes.

## Secuencia de trabajo

1. Confirma alcance, versiones, fuentes autorizadas, requisitos y herramientas realmente disponibles.
2. Inventaría los artefactos y delimita qué puede leer cada herramienta; registra cobertura y vacíos.
3. Mapea comportamientos y reglas del negocio a componentes APEX y comprobaciones observables.
4. Prefiere componentes APEX nativos, plantillas y opciones disponibles en el destino; verifica el Page Designer y el runtime.
5. Separa persistencia del registro de las transiciones de Workflow. Para datos propiedad de otro esquema o base, consume un API autorizado.
6. Comprueba funcionalidad y presentación por separado; informa únicamente verificaciones realizadas.
7. Conserva hallazgos propios del proyecto en su espacio autorizado. Incorpora a esta guía solo aprendizajes portables, comprobados y sin datos privados.

## Verificación de capacidades y versiones

Confirma las versiones de Oracle Forms/Reports, Oracle APEX, Oracle Database y ORDS antes de dar instrucciones específicas. Forms Builder, Reports Builder, SQLcl, MCP, automatización del navegador o complementos APEX son capacidades opcionales: verifica que existan en el entorno activo. Si una herramienta gráfica instalada puede revelar propiedades o comportamiento que un lector binario no expone, pide al usuario la ruta autorizada del archivo y usa el producto compatible. No inventes rutas, perfiles ni permisos.

## Referencias públicas

Consulta [REFERENCES.md](references/REFERENCES.md). Los repositorios y las herramientas mencionados no son dependencias incluidas; confirma su estado, licencia y compatibilidad antes de usarlos.

