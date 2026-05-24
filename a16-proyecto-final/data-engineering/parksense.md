# ParkSense — Parking inteligente

**Campo:** Data Engineering  
**Tagline:** Monitorización en tiempo real del estado de un parking

---

## Contexto

Los parkings grandes (centros comerciales, aeropuertos, campus) tienen cientos de plazas repartidas en varias plantas. Hoy en día muchos sistemas siguen contando coches con barreras o sensores magnéticos sin ningún procesamiento central — el responsable del parking no sabe cuántas plazas están libres en cada zona hasta que manda a alguien a mirar.

Un sistema de monitorización en tiempo real resuelve esto: cada sensor de plaza envía su estado continuamente, el backend mantiene el estado global actualizado y genera estadísticas que permiten optimizar la gestión (¿en qué horas se llena más? ¿qué zona se ocupa primero?).

---

## Tu misión

Construye un sistema que reciba el estado de las plazas de un parking en tiempo real y permita consultarlo. Como no tienes sensores físicos, construirás también un simulador que genere el tráfico de datos.

El sistema debe ser capaz de:

- Recibir eventos de cambio de estado de plazas (libre → ocupada, ocupada → libre)
- Mantener el estado actual de cada plaza
- Calcular estadísticas de ocupación por zona y por franja horaria
- Exponer los datos para que un sistema externo (o un dashboard) pueda consultarlos

---

## Pistas técnicas

- Piensa en el volumen: un parking de 500 plazas puede generar cientos de eventos por minuto en hora punta. ¿Cómo afecta esto al diseño?
- El estado actual y el histórico son cosas distintas. ¿Los guardas en el mismo sitio o en sitios diferentes?
- El simulador tiene que poder generar patrones realistas: más tráfico por la mañana y a mediodía, menos de noche.
- ¿Qué pasa si el backend está caído y los sensores siguen enviando datos?
