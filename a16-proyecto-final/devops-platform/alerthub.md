# AlertHub — Alertas de infraestructura

**Campo:** DevOps / Platform Engineering  
**Tagline:** Entérate de que algo falla antes de que lo hagan tus usuarios

---

## Contexto

Cuando un servidor se queda sin memoria o un endpoint empieza a responder lento, los usuarios lo notan antes que el equipo técnico. La monitorización proactiva invierte esta situación: el sistema detecta los problemas y avisa al equipo antes de que el impacto llegue a producción.

AlertHub es la versión simplificada de lo que hacen herramientas como PagerDuty, Datadog Monitors o Prometheus Alertmanager: las aplicaciones envían métricas, el sistema las evalúa contra umbrales configurables y dispara alertas cuando algo se sale de rango. Cualquier empresa con infraestructura en producción necesita algo así.

---

## Tu misión

Construye un sistema que reciba métricas de aplicaciones, evalúe umbrales y gestione el ciclo de vida de las alertas.

El sistema debe ser capaz de:

- Recibir métricas de múltiples servicios: CPU, memoria, latencia, tasa de errores
- Gestionar umbrales configurables por servicio y tipo de métrica
- Disparar una alerta cuando una métrica supera su umbral
- Gestionar el ciclo de vida de la alerta: abierta → reconocida → resuelta
- Calcular tiempo de detección (desde que empieza el problema hasta que salta la alerta) y tiempo de resolución

---

## Pistas técnicas

- Una sola lectura anómala puede ser ruido. Considera disparar la alerta solo si el umbral se supera durante N lecturas consecutivas o durante un periodo de tiempo determinado. Esto reduce los falsos positivos.
- El ciclo de vida de la alerta es importante: saber que alguien ha visto el problema (reconocida) es diferente a que el problema esté resuelto. El tiempo entre estas fases es una métrica valiosa.
- Genera un simulador que imite distintos patrones: servicio estable, servicio con degradación gradual, servicio que falla de forma intermitente.
- La configuración de umbrales debería poder cambiarse sin desplegar código nuevo. Piensa dónde y cómo la guardas.
