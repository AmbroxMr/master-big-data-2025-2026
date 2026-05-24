# QuizArena — Trivial en tiempo real

**Campo:** Backend / Product Engineering  
**Tagline:** Crea salas de juego y compite con el ranking en vivo

---

## Contexto

Las dinámicas de grupo interactivas son mucho más efectivas que las presentaciones pasivas, tanto en formación como en eventos de empresa. Herramientas como Kahoot o Mentimeter lo han demostrado: cuando hay un componente competitivo y en tiempo real, la participación se dispara.

QuizArena es la versión backend-first de estas herramientas: el valor técnico está en la gestión de salas concurrentes, la sincronización del estado del juego entre múltiples participantes y la actualización del ranking en tiempo real.

---

## Tu misión

Construye el backend de una plataforma de trivial multijugador en tiempo real.

El sistema debe ser capaz de:

- Crear salas de juego con un código de acceso único
- Gestionar el ciclo completo de una partida: sala abierta → pregunta activa → tiempo → siguiente pregunta → fin
- Recibir respuestas de múltiples jugadores simultáneamente con su timestamp
- Calcular puntuaciones (la velocidad de respuesta puede contar)
- Actualizar el ranking en tiempo real conforme llegan respuestas
- Gestionar un banco de preguntas con sus respuestas correctas

---

## Pistas técnicas

- Una sala de juego es una máquina de estados: abierta, en curso (con una pregunta activa), entre preguntas, terminada. Los eventos permitidos dependen del estado actual.
- El tiempo real puede implementarse de varias formas: WebSockets, Server-Sent Events, polling agresivo. Cada una tiene sus tradeoffs de complejidad y escalabilidad.
- La concurrencia es el reto principal: múltiples jugadores respondiendo a la vez. Asegúrate de que el sistema gestiona bien las respuestas simultáneas sin condiciones de carrera.
- Empieza con un solo anfitrión que controla el ritmo (avanza las preguntas manualmente). El temporizador automático es una capa de complejidad que puedes añadir después.
