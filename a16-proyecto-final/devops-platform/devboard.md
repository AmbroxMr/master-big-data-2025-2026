# DevBoard — Estado de CI/CD

**Campo:** DevOps / Platform Engineering  
**Tagline:** Visibilidad sobre el estado de tus pipelines de CI/CD

---

## Contexto

Cuando un equipo tiene varios repositorios y pipelines de CI/CD, mantener visibilidad sobre el estado de todo es difícil. ¿Qué ramas están rotas? ¿Cuánto tarda en media el pipeline de producción? ¿Qué repositorio tiene más fallos esta semana? Sin una vista centralizada, cada desarrollador tiene que revisar herramienta por herramienta.

DevBoard agrega esta información: recibe eventos de GitHub, GitLab o cualquier sistema de CI vía webhooks, almacena el historial de builds y calcula métricas de fiabilidad y velocidad del proceso de entrega. Es la versión simplificada de herramientas como LinearB, Datadog CI Visibility o las métricas DORA que usan los equipos más maduros.

---

## Tu misión

Construye un sistema que reciba eventos de pipelines de CI/CD y genere métricas de estado y rendimiento.

El sistema debe ser capaz de:

- Recibir webhooks de eventos de pipeline: iniciado, completado (éxito o fallo), cancelado
- Almacenar el historial de builds por repositorio y rama
- Calcular métricas por repositorio: tasa de éxito, duración media, fallos en las últimas N horas
- Detectar ramas que llevan más de X builds fallidos consecutivos
- Generar un resumen diario del estado de todos los repositorios

---

## Pistas técnicas

- No necesitas integrar con GitHub real desde el principio. Construye un simulador que genere webhooks con el mismo formato que usaría GitHub, y conéctalo al sistema real cuando el backend esté funcionando.
- La tasa de fallo es más útil calculada sobre ventanas temporales (última hora, último día, última semana) que sobre el total histórico. Una rama que falló mucho hace 3 meses pero lleva una semana estable no es un problema.
- Las métricas DORA (Deployment Frequency, Lead Time, Change Failure Rate, Time to Restore) son el estándar de la industria para medir madurez de CI/CD. Implementar aunque sea una de ellas añade mucho valor.
- Un webhook no procesado correctamente es un evento perdido. Considera si necesitas algún mecanismo de garantía de entrega.
