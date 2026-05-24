# VaultLog — Audit log de accesos a secretos

**Campo:** DevOps / Platform Engineering  
**Tagline:** Sabe quién accedió a qué secreto y cuándo

---

## Contexto

Las credenciales y secretos (contraseñas de bases de datos, API keys, certificados) son el activo más sensible de cualquier sistema. Saber quién tiene acceso a qué, y cuándo accedió, es un requisito básico de seguridad que muchas empresas no cumplen hasta que tienen un incidente.

VaultLog construye esta visibilidad: un sistema donde los secretos se almacenan de forma cifrada y cada acceso queda registrado en un log inmutable. Cuando llega una auditoría de seguridad o un incidente, el equipo puede responder exactamente a "¿quién accedió a la API key de producción el martes pasado?". Es la funcionalidad core de herramientas como HashiCorp Vault o AWS Secrets Manager.

---

## Tu misión

Construye un sistema de gestión de secretos con audit log inmutable.

El sistema debe ser capaz de:

- Almacenar secretos cifrados identificados por nombre y entorno (producción, staging, desarrollo)
- Gestionar usuarios con distintos niveles de acceso (lectura, escritura, admin)
- Registrar en un log inmutable cada operación: quién, qué secreto, qué operación, cuándo
- Consultar el historial de accesos filtrando por usuario, secreto o periodo de tiempo
- Revocar el acceso de un usuario sin eliminar el historial de sus accesos anteriores

---

## Pistas técnicas

- "Inmutable" significa que las entradas del log no se pueden modificar ni eliminar. Un registro de audit que se puede borrar no vale para una auditoría real. Piensa cómo garantizas esto a nivel de datos.
- El cifrado de secretos tiene varios enfoques: cifrar en el cliente antes de enviar, cifrar en el servidor antes de almacenar, usar un KMS externo. Para el MVP, cifrar en el servidor es suficiente; documenta qué algoritmo usas y por qué.
- La diferencia entre "leer el valor de un secreto" y "ver que un secreto existe" es importante para el log. No son la misma operación.
- Añadir expiración automática de secretos (un secreto que caduca después de N días) es una funcionalidad de seguridad muy relevante y relativamente simple de implementar.
