# MetroTrack — Transporte público en tiempo real

**Campo:** ML Engineering  
**Tagline:** Estado en tiempo real de la red y análisis de puntualidad

---

## Contexto

Las aplicaciones de transporte público (Google Maps, Moovit, las apps oficiales de metro) funcionan gracias a feeds de datos en tiempo real: los vehículos publican su posición y estado continuamente, y el sistema calcula retrasos, actualiza horarios estimados y alerta cuando una línea tiene incidencias.

Detrás hay un problema técnico interesante: mucho volumen de datos de posición, necesidad de calcular retrasos en tiempo real comparando contra horarios teóricos, y análisis histórico para detectar qué líneas y franjas horarias son sistemáticamente peor.

---

## Tu misión

Construye un sistema que reciba la posición y estado de vehículos simulados y genere información útil sobre el estado de la red.

El sistema debe ser capaz de:

- Recibir actualizaciones de posición y estado de múltiples vehículos
- Calcular el retraso de cada vehículo respecto a su horario teórico
- Exponer el estado en tiempo real de cada línea
- Almacenar el histórico para analizar puntualidad por línea, hora del día y día de la semana

---

## Pistas técnicas

- El simulador es la pieza más importante: tiene que generar posiciones que sigan una ruta lógica y retrasos que varíen de forma realista (más retraso en hora punta, menos de madrugada).
- "Retraso" es la diferencia entre la hora en que el vehículo debería estar en un punto y la hora real. Para calcularlo necesitas un horario teórico. Puede ser algo muy simple: el vehículo X debe llegar a la parada Y a las HH:MM.
- El estado "en tiempo real" y el histórico tienen requisitos distintos de consulta. El primero necesita ser rápido, el segundo puede ser más lento pero necesita soportar agregaciones.
- Analizar si un retraso es sistemático (siempre tarde en esa línea a esa hora) o puntual (un día concreto) es el núcleo del valor de ML Engineering en este proyecto.
