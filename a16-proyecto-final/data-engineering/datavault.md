# DataVault — Catálogo de datasets

**Campo:** Data Engineering  
**Tagline:** Un lugar centralizado para todos los ficheros de datos del equipo

---

## Contexto

En cualquier equipo de datos los ficheros viven dispersos: alguien los sube a Google Drive, otro los manda por Slack, el tercero los tiene en su máquina local. Cuando llega un analista nuevo, no sabe qué datos existen, dónde están ni qué contienen. Esto es un problema real que tienen desde startups hasta grandes empresas.

Un catálogo de datos resuelve esto: una plataforma donde los ficheros se suben, se validan automáticamente, se almacenan de forma organizada y se indexan para que cualquier miembro del equipo pueda encontrarlos y previsualizarlos sin descargarlos. Es la versión simplificada de herramientas como Databricks Unity Catalog o AWS Glue Data Catalog.

---

## Tu misión

Construye un sistema donde los usuarios puedan subir ficheros de datos y el sistema los gestione automáticamente.

El sistema debe ser capaz de:

- Aceptar la subida de ficheros CSV o JSON
- Validar el fichero (está bien formado, tiene al menos una columna, no está vacío)
- Almacenarlo en un sistema de object storage
- Extraer metadatos automáticamente: nombre de columnas, tipos de datos, número de filas, tamaño
- Exponer un catálogo con todos los datasets disponibles y sus metadatos
- Permitir previsualizar las primeras filas de un dataset sin descargarlo

---

## Pistas técnicas

- La validación y extracción de metadatos puede ser costosa para ficheros grandes. ¿La haces de forma síncrona (en la misma petición) o asíncrona (en segundo plano)?
- El object storage y la base de datos de metadatos son dos sistemas distintos con responsabilidades distintas: uno guarda los bytes, el otro guarda la información sobre esos bytes.
- Piensa en qué pasa si alguien sube el mismo fichero dos veces. ¿Lo rechazas, lo sobreescribes o guardas ambas versiones?
- Los metadatos que extraes automáticamente son la base del catálogo. Cuanto más ricos sean, más útil es el sistema.
