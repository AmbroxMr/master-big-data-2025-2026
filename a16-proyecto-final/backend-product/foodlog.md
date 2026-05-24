# FoodLog — Gestión de pedidos para food truck

**Campo:** Backend / Product Engineering  
**Tagline:** Del pedido al resumen del día sin papel

---

## Contexto

Un food truck o restaurante pequeño recibe pedidos continuamente, los gestiona de forma manual (papel, pizarra, memoria) y al cerrar no tiene datos claros de cuánto vendió, qué fue más popular o a qué horas tuvo más demanda. Es un problema que tienen miles de negocios de hostelería.

FoodLog digitaliza este flujo: los pedidos entran por una interfaz o API, se encolan y el cocinero los va marcando como completados. Al cierre, el sistema genera un resumen del día con ventas, platos más populares y tiempo medio de preparación. Es el MVP de cualquier POS (Point of Sale) moderno.

---

## Tu misión

Construye el backend de un sistema de gestión de pedidos para un pequeño negocio de hostelería.

El sistema debe ser capaz de:

- Gestionar un menú con platos, descripción y precio
- Recibir pedidos con uno o más platos
- Gestionar el ciclo de vida de un pedido: recibido → en preparación → listo → entregado
- Calcular el tiempo de preparación de cada pedido
- Generar un resumen del día: ingresos totales, platos más vendidos, ticket medio, tiempo medio de preparación

---

## Pistas técnicas

- Un pedido tiene estados. Las transiciones entre estados deben ser válidas: no puedes pasar de "recibido" a "entregado" sin pasar por "en preparación". Piensa cómo implementas esto de forma limpia.
- La cola de pedidos es el corazón del sistema: los pedidos entran en orden y el cocinero los procesa en orden. ¿Usas una cola real (RabbitMQ, Redis) o simulas la cola con una base de datos y estados?
- El tiempo de preparación es la diferencia entre `en_preparacion_desde` y `listo_en`. Guarda los timestamps de cada transición de estado.
- El resumen del día es más útil si puedes filtrarlo por franja horaria (¿a qué horas se vende más?) y por categoría de plato.
