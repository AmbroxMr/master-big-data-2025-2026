# PriceWatch — Monitor de precios

**Campo:** ML Engineering  
**Tagline:** Detecta cuándo un producto está más barato de lo normal

---

## Contexto

Los precios online cambian continuamente. Las tiendas aplican descuentos dinámicos, ajustan precios según la competencia y lanzan promociones flash. Un comprador que no monitoriza activamente puede pagar mucho más de lo necesario por el mismo producto.

PriceWatch automatiza este seguimiento: registra el precio de productos a lo largo del tiempo y avisa cuando el precio baja de un umbral o cuando la bajada es anómala respecto al histórico. Es el mismo problema que resuelven herramientas como Camelcamelcamel para Amazon, o los sistemas de alertas de precio de Skyscanner para vuelos.

---

## Tu misión

Construye un sistema que monitorice el precio de una lista de productos y detecte bajadas de precio relevantes.

El sistema debe ser capaz de:

- Registrar el precio de productos a intervalos regulares (mediante un scraper o un simulador)
- Almacenar el histórico completo de precios por producto
- Calcular el precio mínimo histórico y la media de los últimos N días
- Detectar cuando el precio actual es anómalo respecto al patrón reciente
- Notificar (por log, email, webhook o cualquier mecanismo) cuando se detecta una oportunidad

---

## Pistas técnicas

- Definir "anomalía" es la decisión más importante del proyecto. Una bajada del 5% respecto a la media puede ser irrelevante para un producto de 10€ y muy significativa para uno de 1000€. Piensa en términos relativos o estadísticos (desviación estándar, percentil).
- Un scraper real puede fallar: la página cambia, hay rate limiting, el servidor está caído. Un simulador te libera de estos problemas y te permite controlar los patrones (producto con precio estable, producto con bajadas periódicas, producto con precio volátil).
- El histórico de precios es una serie temporal. Las bases de datos convencionales funcionan, pero piensa si el modelo de datos que eliges facilita o complica las consultas temporales.
- ¿Cada cuánto tiempo tiene sentido comprobar los precios? El sistema debería poder configurarse sin tocar el código.
