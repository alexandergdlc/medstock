# Análisis de MedStock: índice y estado

**Proyecto:** MedStock · **Versión:** 0.3.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Decisiones del propietario aceptadas; detalles operativos pendientes según 14.

## Propósito y lectura

Este dossier define necesidades, reglas, comportamiento y criterios de evaluación
para el Sistema de Trazabilidad de Inventario Farmacéutico y Médico en una Cadena
de Clínicas. Es la primera versión de análisis, no evidencia de implementación ni
validación en campo. Se preparó con decisiones de Alexander, el sílabo IS-488 y
fuentes primarias identificadas en [referencias](17-fuentes-y-referencias.md).

La organización objetivo es una cadena realista y ampliable, sin atribuir a Auna
procesos internos no publicados. Una organización concreta para validación aún no
está identificada. Tres sedes iniciales y nombres genéricos son datos de ensayo.

## Índice

| Documento | Pregunta que resuelve |
|---|---|
| [01 Contexto](01-contexto-y-problema.md) | ¿Qué problema se aborda y con qué evidencia? |
| [02 Objetivos](02-vision-objetivos-y-exito.md) | ¿Qué resultado se busca y cómo se comprueba? |
| [03 Alcance](03-alcance-y-limites.md) | ¿Qué incluye la solución y sus incrementos? |
| [04 Actores](04-interesados-actores-y-permisos.md) | ¿Quién actúa y con qué autorización? |
| [05 Procesos](05-procesos-del-negocio.md) | ¿Cómo fluye el negocio y sus excepciones? |
| [06 Glosario](06-glosario-del-dominio.md) | ¿Qué significa cada concepto? |
| [07 Reglas](07-reglas-del-negocio.md) | ¿Qué invariantes deben respetarse? |
| [08 Funciones](08-requisitos-funcionales.md) | ¿Qué capacidades se requieren? |
| [09 Calidad](09-requisitos-de-calidad-y-restricciones.md) | ¿Qué cualidades y límites son necesarios? |
| [10 Casos de uso](10-casos-de-uso-e-historias.md) | ¿Qué secuencia sigue cada actor? |
| [11 Información](11-requisitos-de-informacion.md) | ¿Qué información se necesita y valida? |
| [12 Dominio](12-modelo-conceptual.md) | ¿Cómo se relacionan los conceptos? |
| [13 Estados](13-estados-y-eventos.md) | ¿Qué transiciones son válidas? |
| [14 Pendientes](14-supuestos-riesgos-y-pendientes.md) | ¿Qué falta confirmar y qué riesgo implica? |
| [15 Trazabilidad](15-trazabilidad-y-validacion.md) | ¿Cómo se relacionan objetivos y aceptación? |
| [16 Drivers](16-drivers-y-escenarios-de-calidad.md) | ¿Qué condicionará la arquitectura? |
| [17 Fuentes](17-fuentes-y-referencias.md) | ¿Qué se consultó y hasta dónde sustenta? |
| [18 Especialización](18-capacidades-especializadas.md) | ¿Cómo se detallan las cinco capacidades? |
| [19 Trabajo ágil](19-organizacion-agil-y-sdd.md) | ¿Cómo combinar gestión y SDD? |
| [20 Correspondencia sanitaria](20-correspondencia-minsa-digemid.md) | ¿Qué respaldo se verificó y qué es política propia? |
| [21 Actividades por CU](21-diagramas-de-casos-de-uso.md) | ¿Cómo se desarrolla cada uno de los 20 casos? |
| [22 Procesos BPMN](22-diagramas-de-procesos.md) | ¿Cómo participan los responsables en los 14 procesos? |
| [23 Casos de uso UML](23-diagramas-uml-de-casos-de-uso.md) | ¿Qué objetivos tiene cada actor por módulo? |

## Convenciones y autoridad

- `OBJ`: objetivo; `RN`: regla de negocio; `RF`: requisito funcional; `RNF`: calidad.
- `CU`: caso de uso; `CA`: criterio/escenario de aceptación; `DRV`: driver.
- `PP`: política propuesta; `PN`: pendiente; `RSK`: riesgo; `ESC`: escenario de calidad.
- **ACORDADA**: decisión aceptada por Alexander en la conversación. No equivale a
  aprobación de un responsable farmacéutico ni a certificación sanitaria.
- **PROPUESTA**: valor o comportamiento razonable para revisar, claramente identificado.
  Las cinco capacidades están incluidas; sus parámetros de detalle pueden seguir propuestos.
- **PENDIENTE**: decisión sin cierre suficiente para implementar el flujo afectado.
- P1 = imprescindible para integridad/núcleo; P2 = necesaria para alcance completo;
  P3 = evolución opcional. La prioridad no fija una fecha de entrega.

Las reglas normativas están en 07, los requisitos en 08 y los criterios principales
con el RF correspondiente. Los otros documentos los enlazan; no mantienen copias
alternativas. La [especificación Spec Kit](../001-trazabilidad-inventario/spec.md)
resume recorridos de valor y remite al catálogo canónico.

## Flujo SDD aplicado

Se leyó la constitución, se resolvió la plantilla oficial `spec-template` y se creó
una especificación de capacidad junto con su checklist. No hay hooks opcionales
instalados. Las decisiones de negocio se aclaran y versionan antes de generar plan,
contratos técnicos, tareas e implementación. La revisión de este análisis no se
presenta como ejecución de `speckit-analyze`, que necesita spec, plan y tasks.

La primera constitución está en [principios](../../.specify/memory/constitution.md).
Se usó la estructura de `speckit-specify` sin cambiar sus archivos oficiales.

## Estado de validación

La cobertura documental y las referencias cruzadas se revisan en este PR. No existen
entrevistas, mediciones de carga, base de datos ni despliegue funcional de MedStock
en este repositorio. La revisión de políticas, perfil de carga y controles sanitarios
permanece visible en PN. No se autoriza pasar automáticamente a implementación.
