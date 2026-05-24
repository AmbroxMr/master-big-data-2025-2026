# PulseCheck — Encuestas de bienestar de equipo

**Campo:** ML Engineering  
**Tagline:** Detecta problemas de equipo antes de que lleguen a recursos humanos

---

## Contexto

El burnout y los problemas de equipo raramente aparecen de golpe. Se acumulan durante semanas o meses antes de que alguien los verbalice. Para cuando llegan a RRHH, el daño ya está hecho.

Las encuestas de pulso semanales son una herramienta que usan cada vez más empresas para detectar estas señales a tiempo: preguntas cortas y anónimas sobre carga de trabajo, ambiente y bloqueos. El sistema agrega las respuestas y detecta tendencias negativas que el manager puede atender antes de que escalen. Herramientas como Officevibe o Leapsome hacen exactamente esto.

---

## Tu misión

Construye un sistema que gestione encuestas periódicas de bienestar y analice las respuestas para detectar tendencias.

El sistema debe ser capaz de:

- Gestionar un banco de preguntas con respuestas en escala 1-5
- Enviar (o simular el envío de) encuestas periódicas a los miembros de un equipo
- Recibir y almacenar respuestas de forma anónima
- Calcular la puntuación media del equipo por categoría (carga de trabajo, ambiente, bloqueos)
- Detectar tendencias: ¿ha bajado la puntuación de una categoría durante N semanas seguidas?
- Generar un informe semanal para el manager con los datos agregados

---

## Pistas técnicas

- El anonimato es fundamental para que las respuestas sean honestas. El sistema no debe permitir saber quién respondió qué, pero sí debe evitar que la misma persona responda varias veces a la misma encuesta.
- Una "tendencia negativa" se puede definir de muchas formas: bajada continua durante N semanas, puntuación por debajo de un umbral, desviación significativa respecto a la media histórica. Elige una y documenta el criterio.
- Los informes para managers son útiles si muestran evolución temporal, no solo el dato de la última semana. Una gráfica de la puntuación a lo largo del tiempo dice mucho más que un número.
- Simula datos de varias semanas con distintos patrones: equipo estable, equipo con caída gradual, equipo con recuperación.
