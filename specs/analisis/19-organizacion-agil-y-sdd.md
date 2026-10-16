# Organización del trabajo: SDD, Scrum y Kanban

**Proyecto:** MedStock · **Versión:** 0.3.0 · **Fecha:** 2026-10-15

**Estado:** borrador para revisión; capacidades incluidas y políticas de detalle identificadas.

## Decisión aceptada

Alexander aceptó **SDD + Kanban** para organizar MedStock. Existe un desarrollador
humano con asistencia de IA; Alexander conserva la responsabilidad de revisar y
aceptar el trabajo. SDD guía las especificaciones y su verificación; Kanban organiza
el flujo de los ítems. El tablero versionado enlaza Issues reales; la vista de GitHub Projects sigue pendiente.

## Scrum y contexto individual

La Guía Scrum define responsabilidades de Product Owner, Scrum Master y Developers,
trabajo en Sprints y artefactos/eventos asociados (FU-013). Usar solo algunas prácticas
no equivale a aplicar íntegramente el marco. Para este proyecto se puede proponer una
adaptación inspirada en Scrum, pero no atribuir responsabilidad humana a Codex ni
crear actas de reuniones que no ocurrieron.

## Enfoque de trabajo elegido

Se adopta **desarrollo iterativo e incremental con SDD y gestión de flujo Kanban**.
Kanban aporta visualización del flujo, control de trabajo en curso y mejora a partir
de medidas (FU-014). Es compatible con un proyecto individual y con el seguimiento
por hitos académicos. Se comprobará su compatibilidad con lo que exija
el docente; esta decisión no modifica por sí sola los requisitos de farmacia.

| Enfoque | Adecuación propuesta | Condición |
|---|---|---|
| Scrum completo | Viable si se organiza un equipo y se cumplen sus responsabilidades/eventos | No afirmar aplicación íntegra por usar sprints o IA |
| Prácticas inspiradas en Scrum | Posibles revisiones periódicas y objetivos cortos en trabajo individual | Documentar adaptación, sin denominarla Scrum completo |
| SDD + Kanban | Elegido por Alexander para este contexto individual | Definir flujo y WIP, registrar evidencia y revisar políticas |

## Flujo inicial aceptado

Pendiente → Preparado → En curso → En revisión → Terminado. Las tarjetas bloqueadas
conservan la causa y cuentan como trabajo iniciado; no se sacan del límite para
ocultar pendientes. Política inicial aceptada: un trabajo principal en curso y no más de dos
iniciados en total contando revisión, ajustable con evidencia.

Cada ítem debe expresar valor, RF/RN involucrados, criterios de aceptación y alcance
acotado. Antes de empezar, cerrar sus PN críticos. Un ítem grande se divide por
comportamiento verificable, no por crear una carpeta sin resultado.

## Relación con SDD y GitHub

1. Seleccionar un resultado de negocio y aclarar la especificación vigente.
2. Preparar el plan técnico cuando corresponda y tareas asociadas al ítem.
3. Trabajar en rama; comprobar los criterios afectados y registrar resultados.
4. Presentar el PR y la evidencia; incorporar observaciones.
5. Integrar por indicación del propietario y revisar lo aprendido.

Una especificación de producto puede abarcar varios ítems; un ítem no necesita
crear otra especificación duplicada. El [tablero de análisis](../../docs/tablero-analisis.md)
es la vista versionada de las Issues. GitHub Projects no está creado: la conexión
disponible permite Issues/PRs pero no administrar Projects. Una vista futura deberá
reflejar las mismas tarjetas, evitando dos estados contradictorios.

## Revisión periódica y terminado

Revisar semanalmente avance, bloqueos y prioridades; registrar una
mejora concreta del proceso. Para documentación: enlaces, trazabilidad, fuentes y
pendientes claros. Para código futuro: criterios funcionales, pruebas pertinentes,
seguridad y documentación actualizada. La aceptación de un requisito y la definición
de terminado cumplen propósitos diferentes.

Las métricas que registraremos desde esta versión son cantidad iniciada, tiempo de ciclo, antigüedad
del trabajo abierto y terminados por periodo. No existe velocidad histórica ni una
fecha estimada fiable por haber añadido más RF. El análisis inicial del curso es una
línea base que se refina por incremento, no una exigencia de congelar el negocio.

## Aplicación durante la fase de análisis

Las tarjetas representan resultados revisables, no un archivo MD por obligación.
Una revisión de reservas puede afectar reglas, RF, casos de uso y criterios sin
crear fuentes duplicadas. Todavía no corresponde implementar código, SQL físico ni
ejecutar `speckit-analyze` sin los documentos técnicos que requiere.

| Estado | Condición de avance en análisis |
|---|---|
| Pendiente | Pregunta o resultado identificado, con dependencias y responsable de resolverlo |
| Preparado | Alcance, documentos afectados y evidencia esperada definidos; si se trata de investigar un pendiente, la pregunta está delimitada |
| En curso | Se consultan fuentes, aclaran decisiones y actualizan especificación y trazabilidad |
| En revisión | PR con cambios coherentes, comprobaciones y decisiones pendientes explícitas para Alexander |
| Terminado | Alexander acepta el resultado y se integra el PR; se cumplen los criterios del ítem |

La línea base 0.2.0 quedó integrada mediante el PR #2. Esta revisión 0.3.0
se gestiona en la Issue #3 y un PR nuevo; la aceptación del método ya está registrada.
Validar la duración de reservas sigue **Pendiente** y no se cierra al integrar la
línea base. Una tarea de documentar una propuesta puede terminar dejando su validación
operativa pendiente, siempre que ese sea su alcance explícito. Una tarea de validar
esa política exige la evidencia correspondiente para terminar.

Para terminar una revisión documental: mantener IDs y enlaces válidos, actualizar
reglas/RF/CU/criterios afectados, registrar fuentes y separar lo aceptado de lo
propuesto. Integrar documentos no acredita validación farmacéutica ni implementación
de las cinco capacidades. Tras integrar la línea base, cada mejora se prepara desde
`main` actualizado en una rama nueva y se revisa mediante otro PR.

## Medición y expectativa inicial

Comenzado significa entrada en En curso; terminado significa aceptación e integración.
En revisión y bloqueados cuentan dentro del WIP máximo de dos iniciados, con un solo
ítem en ejecución activa. Se inicia otro solo si hay capacidad. Registrar fecha de
inicio/fin, bloqueos y vínculos a PR; medir WIP, antigüedad, tiempo de ciclo y terminados
por semana, sin convertir una espera de revisión en trabajo terminado.

SLE provisional para una revisión documental acotada: **85 % en siete días naturales**
desde inicio hasta aceptación/integración. Es una hipótesis de planificación del
asistente, no un rendimiento observado ni un plazo académico acordado. Se revisará
con Alexander y los primeros diez ítems terminados; no hay muestra histórica aún.
