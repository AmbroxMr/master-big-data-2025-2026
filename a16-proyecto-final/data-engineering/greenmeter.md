# GreenMeter — Monitor de consumo energético

**Campo:** Data Engineering  
**Tagline:** Convierte lecturas de contador en información útil

---

## Contexto

Las empresas de suministro eléctrico instalan contadores inteligentes que envían lecturas cada pocos minutos. Con esos datos en bruto es posible calcular el consumo real por franja horaria, detectar comportamientos anómalos (un pico de consumo a las 3 de la mañana en una oficina vacía) y proyectar la factura del mes en curso.

Es el mismo tipo de sistema que utilizan compañías como Endesa o Iberdrola para ofrecer informes de consumo a sus clientes. A escala pequeña, cualquier edificio de oficinas o polígono industrial tiene el mismo problema.

---

## Tu misión

Construye un sistema que reciba lecturas periódicas de consumo eléctrico, las procese y genere información útil para el usuario o gestor del edificio.

El sistema debe ser capaz de:

- Recibir lecturas de consumo con timestamp y identificador de contador
- Calcular el consumo agregado por hora y por día
- Detectar lecturas anómalas respecto al patrón habitual del mismo contador
- Proyectar el consumo total del mes en curso basándose en los datos disponibles

---

## Pistas técnicas

- Una "anomalía" puede definirse de muchas formas: desviación estándar, percentil, comparación con la misma hora de días anteriores. No hay una respuesta única, elige la que tenga sentido para tu implementación.
- El consumo eléctrico tiene patrones temporales muy marcados (días laborables vs fines de semana, mañana vs noche). Tenerlos en cuenta mejora mucho la detección de anomalías.
- La proyección mensual es más útil si distingue entre días ya pasados (dato real) y días futuros (estimación basada en media histórica).
- Construye un simulador que genere lecturas con patrones realistas, incluyendo alguna anomalía ocasional.
