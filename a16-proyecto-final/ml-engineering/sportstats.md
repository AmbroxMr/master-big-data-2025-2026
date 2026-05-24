# SportStats — Estadísticas deportivas

**Campo:** ML Engineering  
**Tagline:** Estadísticas reales para ligas amateur

---

## Contexto

Los equipos profesionales tienen analistas y herramientas dedicadas para registrar y analizar cada partido. Las ligas amateur, donde juegan millones de personas, no tienen acceso a nada de eso. El resultado es que los registros se llevan en papel, en hojas de cálculo o directamente no se llevan.

SportStats da a cualquier liga amateur acceso a estadísticas reales: un árbitro o delegado registra los eventos del partido desde una interfaz simple, y el sistema genera automáticamente estadísticas por jugador y por equipo. Es el mismo tipo de sistema que Transfermarkt o SofaScore, pero orientado a ligas locales.

---

## Tu misión

Construye un sistema que registre eventos de partidos y calcule estadísticas sobre ellos.

El sistema debe ser capaz de:

- Registrar eventos durante un partido: gol, asistencia, falta, tarjeta amarilla, tarjeta roja, sustitución
- Asociar cada evento a un jugador, un equipo y un minuto del partido
- Calcular estadísticas por jugador: goles, asistencias, tarjetas, minutos jugados
- Calcular estadísticas por equipo: goles a favor, goles en contra, faltas, posesión (si la registras)
- Generar un resumen del partido al finalizar

---

## Pistas técnicas

- Un partido tiene estados (no iniciado, en curso, en descanso, terminado). Los eventos solo tienen sentido cuando el partido está en curso. ¿Cómo modelas esto?
- Las estadísticas de un jugador son la agregación de sus eventos a lo largo de todos sus partidos. Piensa si las calculas en el momento de la consulta o si las mantienes precalculadas.
- Los goles y asistencias son fáciles de contar. La posesión o el mapa de calor son más complejos — empieza por las métricas simples y añade complejidad si tienes tiempo.
- Añadir una clasificación de liga (puntos, diferencia de goles, partidos jugados) hace el sistema mucho más completo y es un buen ejercicio de agregación.
