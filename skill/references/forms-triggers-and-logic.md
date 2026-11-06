# Triggers, unidades y semántica de Oracle Forms

Guía para explicar qué hace una forma y ubicar cada regla en su evento real antes de migrarla. Usa junto a [Inspección de Oracle Forms](forms-inspection.md).

## Inventario ejecutable

Por cada trigger, registra nombre del evento, objeto propietario, nivel (módulo, ventana, bloque o item), orden/secuencia, código disponible, unidades llamadas y evidencia. Distingue trigger de item frente a trigger homónimo de bloque o forma. Registra además program units, PLL/PLX, attached libraries, menús, alertas, built-ins y referencias externas cuando la fuente permita confirmarlos.

Para cada unidad PL/SQL traza:

- tablas/vistas y operaciones de lectura/escritura;
- parámetros de entrada/salida, variables globales y estado de sesión;
- llamadas entre unidades, paquetes, procedimientos remotos y archivos;
- errores, mensajes, excepciones, commits, rollbacks y side effects;
- dependencias no resueltas y diferencias entre código extraído y código invocado en runtime.

No declares que un evento se ejecuta solo por existir en el módulo. Verifica el alcance, la condición, el orden y el camino de ejecución.

## Ciclo de vida y equivalencia

Construye una secuencia temporal con eventos como abrir formulario, consultar registro, entrar/salir de item, validar bloque, insertar/actualizar/borrar, confirmar transacción y cerrar. Usa los nombres reales del módulo y del release. No supongas que una secuencia de triggers se convierte uno a uno en Dynamic Actions.

| Intención observada | Alternativa APEX a evaluar |
|---|---|
| Inicializar contexto o valores | Initialization/render process o default calculado |
| Validar dato al salir/enviar | Validación declarativa o validación de servidor |
| Reaccionar a cambio visual | Dynamic Action si el comportamiento no es regla de seguridad |
| Preparar query y filtrar filas | SQL con bind items y autorización en servidor |
| Guardar fila local | Form nativo con Fetch Row / Process Row |
| Guardar en otro sistema | API explícita con contrato, errores y correlación |
| Navegar a otra ventana/canvas | Página, región, navegación o modal según tarea |
| Confirmar o cancelar decisión | Dialog con submit explícito y cancel sin mutación |
| Transacción de varias operaciones | Paquete PL/SQL/API transaccional; definir propietario de commit |

Esta tabla propone dónde investigar; no declara equivalencia automática. Reglas de integridad y permisos no deben vivir solo en el navegador.

## Validaciones y mensajes

Por cada validación conserva: condición, evento, campo/grupo, mensaje, si impide grabar, excepción y prioridad respecto a otras reglas. Separa obligatoriedad/formato de interfaz, regla de dominio, integridad referencial, autorización del actor y validación de DB/API. Implementa mensajes claros cerca del campo cuando sea posible; repite en servidor las reglas que protegen datos. Prueba vacío, límites, formato inválido, valor de LOV manipulado, concurrencia y error de servicio.

## Transacciones y navegación

Dibuja el límite de commit real: qué operaciones ocurren antes/después de guardar y cuáles se revierten. APEX no debe confirmar una mutación solo porque el usuario abrió una página o modal. Separa guardar de una acción de Workflow. Documenta idempotencia y reintento si interviene un API.

## Checklist de salida

- [ ] Evento y propietario verificados; no se confundió un trigger homónimo.
- [ ] Código completo o límite del lector declarado.
- [ ] Unidades, bibliotecas y dependencias recorridas hasta el nivel acordado.
- [ ] Regla, mensaje, transacción y navegación descritos en orden.
- [ ] Mapeo APEX tiene componente, proceso/servicio, autorización y prueba.
- [ ] Las afirmaciones inferidas están etiquetadas como tales.
