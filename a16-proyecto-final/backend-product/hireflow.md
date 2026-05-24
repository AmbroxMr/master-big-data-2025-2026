# HireFlow — Pipeline de selección de candidatos

**Campo:** Backend / Product Engineering  
**Tagline:** Visualiza tu funnel de selección y deja de perder candidatos

---

## Contexto

Cuando una empresa abre varias posiciones a la vez, gestionar los candidatos se vuelve caótico rápidamente. Algunos equipos usan hojas de cálculo, otros correos etiquetados, otros herramientas como Notion. El resultado es siempre el mismo: candidatos que se pierden, seguimiento inconsistente y sin visibilidad del estado global del proceso.

Un ATS (Applicant Tracking System) resuelve esto: centraliza las candidaturas, gestiona los estados y genera métricas del proceso de selección. Herramientas como Greenhouse, Lever o Workday hacen esto a escala empresarial. HireFlow es la versión minimalista para equipos pequeños.

---

## Tu misión

Construye el backend de un sistema de gestión de candidatos para procesos de selección.

El sistema debe ser capaz de:

- Gestionar posiciones abiertas con su descripción y departamento
- Recibir candidaturas (nombre, email, posición a la que aplican)
- Mover candidatos a través del pipeline de selección: recibida → revisada → entrevista → oferta → contratado / descartado
- Registrar el motivo cuando un candidato es descartado
- Calcular métricas del funnel: cuántos candidatos hay en cada fase, tasa de conversión entre fases, tiempo medio en cada fase

---

## Pistas técnicas

- El pipeline de selección es una máquina de estados. Las transiciones válidas dependen del estado actual: no puedes pasar de "recibida" a "contratado" directamente. Documenta las transiciones permitidas.
- El historial de cambios de estado es muy valioso: puedes calcular cuánto tiempo lleva un candidato en cada fase y detectar cuellos de botella en el proceso.
- Las métricas del funnel son el diferencial de valor respecto a una hoja de cálculo. Una tasa de conversión del 2% entre revisión y entrevista puede indicar que el criterio de revisión es demasiado exigente, o que se están recibiendo candidatos poco cualificados.
- Añadir notas internas por candidato (que no ve el candidato) es una funcionalidad pequeña que hace el sistema mucho más útil en la práctica.
