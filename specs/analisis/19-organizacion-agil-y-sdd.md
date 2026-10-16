# Organización del trabajo: SDD, Scrum y Kanban

**Proyecto:** MedStock · **Versión:** 0.2.0 · **Fecha:** 2026-10-15

**Estado:** borrador para revisión; capacidades incluidas y políticas de detalle identificadas.

## Decisión aún propuesta

La consulta de Alexander abre la elección del marco de gestión. No se declara
adoptado Scrum ni se inventa un equipo: existe un desarrollador humano y asistencia
con IA. SDD define cómo mantener especificaciones y verificar el resultado; se
puede combinar con una forma de gestionar el trabajo.

## Scrum y contexto individual

La Guía Scrum define responsabilidades de Product Owner, Scrum Master y Developers,
trabajo en Sprints y artefactos/eventos asociados (FU-013). Usar solo algunas prácticas
no equivale a aplicar íntegramente el marco. Para este proyecto se puede proponer una
adaptación inspirada en Scrum, pero no atribuir responsabilidad humana a Codex ni
crear actas de reuniones que no ocurrieron.

## Recomendación para revisión

Proponer **desarrollo iterativo e incremental con SDD y gestión de flujo Kanban**.
Kanban aporta visualización del flujo, control de trabajo en curso y mejora a partir
de medidas (FU-014). Es compatible con un proyecto individual y con el seguimiento
por hitos académicos. La elección final queda a cargo de Alexander y de lo que exija
el docente; no modifica por sí sola los requisitos de farmacia.

| Enfoque | Adecuación propuesta | Condición |
|---|---|---|
| Scrum completo | Viable si se organiza un equipo y se cumplen sus responsabilidades/eventos | No afirmar aplicación íntegra por usar sprints o IA |
| Prácticas inspiradas en Scrum | Posibles revisiones periódicas y objetivos cortos en trabajo individual | Documentar adaptación, sin denominarla Scrum completo |
| SDD + Kanban | Recomendado para este contexto individual | Definir flujo y WIP, registrar evidencia y revisar políticas |

## Flujo propuesto de trabajo

Pendiente → Preparado → En curso → En revisión → Terminado. Las tarjetas bloqueadas
conservan la causa y cuentan como trabajo iniciado; no se sacan del límite para
ocultar pendientes. Propuesta inicial: un trabajo principal en curso y no más de dos
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
crear otra especificación duplicada. Una vez elegido el marco, el tablero podrá
implementarse en GitHub Projects/Issues. En esta revisión no se creó ese tablero
ni se fijó un calendario o capacidad semanal sin consultar a Alexander.

## Revisión periódica y terminado

Como propuesta, revisar semanalmente avance, bloqueos y prioridades; registrar una
mejora concreta del proceso. Para documentación: enlaces, trazabilidad, fuentes y
pendientes claros. Para código futuro: criterios funcionales, pruebas pertinentes,
seguridad y documentación actualizada. La aceptación de un requisito y la definición
de terminado cumplen propósitos diferentes.

Las métricas candidatas del flujo son cantidad iniciada, tiempo de ciclo, antigüedad
del trabajo abierto y terminados por periodo. No existe velocidad histórica ni una
fecha estimada fiable por haber añadido más RF. El análisis inicial del curso es una
línea base que se refina por incremento, no una exigencia de congelar el negocio.
