# Navegación y layout declarativo APEX

## Templates antes que CSS

Usa Page Designer y Universal Theme instalado para seleccionar Page Template, Region Template, Item Template, Button Template y Template Options. Los nombres y propiedades varían por tema, versión y plugins.

- Encabezado estándar con título/breadcrumb; no dupliques títulos en varias regiones.
- En un Hero, ubica acciones donde el template las dibuja (por ejemplo, Next). Un botón en slot inválido puede quedar en Invalid Slot/Not Rendered.
- Reportes y contenido en Body; usa Right Column o Left Column cuando el contenido sea navegación/resumen lateral.
- Para cada región verifica Properties y Attributes: la plantilla puede exponer atributos propios y opciones que no aparecen en otra.
- Aplica template options existentes para iconos, tamaño, posición y estilo. No inventes selectores DOM ni CSS para sustituir una opción nativa.

## Grid de items

En cada región, verifica la cuadrícula disponible (frecuentemente 12 columnas, pero depende del template/layout):

- Start New Row: inicia una nueva fila.
- Column: posición de inicio.
- Column Span: ancho ocupado por control/contenido.
- Label Column Span: ancho de la etiqueta.
- Template: Required, Optional, Hidden u opciones disponibles de la instalación.
- Format Mask, altura, icono, clase y Template Options: aplican según tipo de item.

Calcula la suma de columnas y valida en Runtime, también en ancho reducido. No posiciones a partir de una captura únicamente.

## Region Display Selector

RDS agrupa regiones alternativas como pestañas/selectores. Úsalo si el usuario cambia entre secciones equivalentes y el contenido no debe aparecer simultáneamente. Define una región de selector, regiones asignadas, orden, rótulos, default y persistencia. No uses RDS para esconder datos requeridos de una forma larga sin considerar validación, accesibilidad y navegación directa.

## Accesibilidad y responsive

Comprueba etiqueta, foco, teclado, orden de tab, contraste, mensajes, tamaño de objetivo táctil, tablas anchas y colapso lateral. No fuerces que cada pantalla replique dimensiones exactas de una captura; conserva la misma jerarquía y tarea con el viewport disponible.

## Botones

Documenta label, request, región, Button Position, template, template options, Hot, icono, condition, action/URL, submit behavior, checksum y autorización. Mantén una acción primaria clara y diferencia acciones destructivas. Las condiciones de cliente sirven para presentación; autorización en servidor.
