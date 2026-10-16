# Mapa del próximo entregable de análisis

Este mapa organizó el entregable preparado en `specs/analisis/`. Los documentos
están redactados como borrador para revisión; sus políticas PP requieren validación.
Consultar el [índice del análisis](../specs/analisis/00-indice-y-estado.md).

| Archivo previsto | Contenido |
|---|---|
| `00-indice-y-estado.md` | Orden de lectura, responsables, estado y convenciones |
| `01-contexto-y-problema.md` | Contexto de cadena de clínicas, problema y fuentes |
| `02-vision-objetivos-y-exito.md` | Objetivos y criterios de éxito |
| `03-alcance-y-limites.md` | Alcance completo y primera entrega funcional |
| `04-interesados-actores-y-permisos.md` | Responsabilidades y permisos por sede |
| `05-procesos-del-negocio.md` | Procesos propuestos, alternativas y excepciones |
| `06-glosario-del-dominio.md` | Términos y unidades de inventario |
| `07-reglas-del-negocio.md` | FEFO, vencimientos, stock, traslados y correcciones |
| `08-requisitos-funcionales.md` | Requisitos con ID, prioridad y origen |
| `09-requisitos-de-calidad-y-restricciones.md` | Seguridad, operación y límites |
| `10-casos-de-uso-e-historias.md` | Interacciones y criterios de aceptación |
| `11-requisitos-de-informacion.md` | Datos necesarios y significado |
| `12-modelo-conceptual.md` | Conceptos y relaciones, sin SQL físico |
| `13-estados-y-eventos.md` | Ciclos de vida y transiciones |
| `14-supuestos-riesgos-y-pendientes.md` | Incertidumbres e impactos |
| `15-trazabilidad-y-validacion.md` | Necesidad, objetivo, regla, requisito y aceptación |
| `16-drivers-y-escenarios-de-calidad.md` | Drivers priorizados y escenarios medibles |
| `17-fuentes-y-referencias.md` | Fuentes oficiales, alcance y referencias bibliográficas |
| `18-capacidades-especializadas.md` | Parcialidad, reservas, fechas, autorizaciones y retornos |
| `19-organizacion-agil-y-sdd.md` | Comparación de gestión ágil y propuesta SDD/Kanban |
| `20-correspondencia-minsa-digemid.md` | Numerales verificados y límites de atribución |

Los modelos editables se incluirán mediante Mermaid o fuentes asociadas. No se
inventará un proceso actual observado si no se dispone de entrevistas o documentos.
La información pública de redes como Auna contextualiza la organización, no valida
sus procesos internos. Se revisarán fuentes MINSA/DIGEMID y sus modificaciones.

## Decisiones aceptadas

- Una cadena ampliable; tres sedes iniciales como demostración.
- Catálogo compartido; existencias por sede, ubicación y lote.
- Solicitudes internas y validación/confirmación de farmacia.
- Unidad base por producto y conversiones explícitas desde presentaciones.
- Recepción, FEFO, traslados con tránsito y recepción, devoluciones con evaluación,
  ajustes autorizados, bloqueo/retiro de lotes y auditoría verificable.
- Desarrollo individual y Cloudflare como plataforma prioritaria.
- Objetivo de 2 000 usuarios activos simultáneos; falta perfil de carga.

## Pendientes por proceso

Desempate FEFO, reservas y su vencimiento, despacho parcial, días de alerta de
vencimiento, condiciones de devolución, matriz final de autorización, volumen de
datos y perfil de carga. Se propondrán políticas con fundamento y se marcarán como
propuestas hasta su revisión. También se debe identificar el contexto institucional
concreto si se desea afirmar validación con una cadena real.

## Criterio de cierre del análisis

Requisitos identificados y verificables; procesos normales y alternativos; modelos
consistentes; permisos explícitos; drivers priorizados; trazabilidad y pendientes
con impacto conocido. Los bloqueos críticos del negocio deberán resolverse antes
de diseñar su funcionalidad. No se requiere cerrar toda tecnología para describir
el problema, las reglas y los resultados esperados.
