# EventMesh — Gestión de eventos y aforo

**Campo:** Backend / Product Engineering  
**Tagline:** Controla el aforo y gestiona la lista de espera automáticamente

---

## Contexto

Organizar un evento con plazas limitadas parece simple hasta que el proceso se hace manual: alguien tiene que llevar la cuenta de cuántas plazas quedan, gestionar las cancelaciones, contactar a las personas en espera... Los organizadores de meetups, talleres y charlas técnicas lo hacen constantemente con herramientas que no están diseñadas para esto.

EventMesh automatiza la gestión de aforo: cuando un evento se llena, los nuevos registros van automáticamente a la lista de espera. Cuando alguien cancela, el siguiente en la lista recibe confirmación automáticamente. Es el mismo mecanismo que usa Eventbrite o Meetup.com, pero construido por ti.

---

## Tu misión

Construye el backend de una plataforma de gestión de eventos con control de aforo y lista de espera.

El sistema debe ser capaz de:

- Crear eventos con fecha, descripción, ubicación y cupo máximo
- Registrar asistentes hasta completar el aforo
- Gestionar la lista de espera automáticamente cuando el evento está lleno
- Procesar cancelaciones: liberar una plaza y confirmar al primero de la lista de espera
- Consultar el estado de un evento: plazas libres, confirmados, en espera

---

## Pistas técnicas

- La concurrencia es el riesgo principal: si dos personas intentan registrarse en el último sitio disponible al mismo tiempo, ¿qué pasa? Necesitas garantizar que el aforo no se sobrepasa aunque lleguen peticiones simultáneas.
- La lista de espera tiene un orden. El primero que se apuntó debe ser el primero en recibir una plaza cuando se libere. ¿Cómo garantizas este orden con concurrencia?
- Un evento puede estar en distintos estados: abierto (quedan plazas), lleno (lista de espera), cancelado. El estado no es un campo que guardas, sino algo que calculas a partir de los datos.
- Las notificaciones (email, webhook) cuando se confirma una plaza desde la lista de espera son la funcionalidad que hace el sistema útil de verdad. Aunque sea un log, implementa el mecanismo.
