# LogDrain — Agregador de logs

**Campo:** Data Engineering  
**Tagline:** Centraliza los logs de todas tus aplicaciones en un solo sitio

---

## Contexto

Cuando una empresa tiene varios servicios corriendo en producción, los logs de cada uno viven en sitios distintos: un fichero en el servidor, la salida estándar del contenedor, una herramienta de terceros. Cuando algo falla a las 3 de la mañana, el equipo de guardia tiene que conectarse a cada máquina por separado para buscar el error.

Un agregador de logs resuelve este problema: todas las aplicaciones envían sus logs a un servicio central que los indexa y los hace buscables. Es el problema que resuelven herramientas como Datadog, Elastic Stack o Grafana Loki en empresas reales.

---

## Tu misión

Construye un sistema que reciba logs de múltiples aplicaciones y permita consultarlos de forma centralizada.

El sistema debe ser capaz de:

- Recibir logs desde distintas aplicaciones (con nombre de servicio, nivel y mensaje)
- Almacenarlos con su timestamp e indexarlos para búsqueda
- Exponer una API que permita buscar logs por servicio, nivel y rango de tiempo
- Mostrar métricas básicas: tasa de errores por servicio, picos de actividad

---

## Pistas técnicas

- Los logs llegan rápido y en ráfagas. ¿Cómo evitas que tu backend se convierta en el cuello de botella?
- Un log de nivel `ERROR` es urgente; uno de `DEBUG` es ruido en producción. ¿Cómo modelarías esto en el almacenamiento?
- La búsqueda de texto libre dentro de mensajes de log es un caso de uso clásico de búsqueda full-text. ¿Tu base de datos lo soporta?
- Genera un simulador que imite varios servicios enviando logs con distintos patrones (un servicio que falla periódicamente, otro que solo emite INFO).
