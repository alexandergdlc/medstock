# Trazabilidad y plan de validación de requisitos

**Proyecto:** MedStock · **Versión:** 0.1.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Las políticas PP son propuestas.

## Matriz funcional completa

Los enlaces canónicos son [RF/CA](08-requisitos-funcionales.md),
[RN](07-reglas-del-negocio.md), [CU](10-casos-de-uso-e-historias.md) y
[OBJ](02-vision-objetivos-y-exito.md). La tabla permite seguir ambas direcciones;
los IDs se mantienen aunque se reordenen archivos. FU-001 origina las capacidades;
las PP se vinculan desde RN y el registro 14.

| Objetivo | RF | Reglas | CU | CA principal | Incremento |
| --- | --- | --- | --- | --- | --- |
| OBJ-004 | RF-001 | RN-002 | CU-001 | CA-001 | I1 |
| OBJ-004 | RF-002 | RN-002, RN-029 | CU-002 | CA-002 | I1 |
| OBJ-001 | RF-003 | RN-001, RN-026 | CU-003 | CA-003 | I1 |
| OBJ-001 | RF-004 | RN-001, RN-002 | CU-003 | CA-004 | I1 |
| OBJ-002 | RF-005 | RN-003, RN-026 | CU-004 | CA-005 | I1 |
| OBJ-002 | RF-006 | RN-004, RN-005 | CU-004 | CA-006 | I1 |
| OBJ-003 | RF-007 | RN-007 | CU-005 | CA-007 | I1 |
| OBJ-003 | RF-008 | RN-006, RN-007, RN-009 | CU-005 | CA-008 | I1 |
| OBJ-003 | RF-009 | RN-007, RN-012, RN-014 | CU-005 | CA-009 | I1 |
| OBJ-002 | RF-010 | RN-002, RN-008 | CU-006 | CA-010 | I1 |
| OBJ-003 | RF-011 | RN-024, RN-033 | CU-006 | CA-011 | I1 |
| OBJ-002 | RF-012 | RN-009, RN-030 | CU-006 | CA-012 | I3 |
| OBJ-002 | RF-013 | RN-017, RN-027, RN-016 | CU-007 | CA-013 | I2 |
| OBJ-002 | RF-014 | RN-015, RN-017 | CU-007 | CA-014 | I2 |
| OBJ-002 | RF-015 | RN-008, RN-009, RN-010, RN-011, RN-032 | CU-008 | CA-015 | I2 |
| OBJ-002 | RF-016 | RN-011, RN-012, RN-013, RN-014 | CU-008 | CA-016 | I2 |
| OBJ-002 | RF-017 | RN-015 | CU-008 | CA-017 | I2 |
| OBJ-003 | RF-018 | RN-014, RN-034 | CU-008 | CA-018 | I2 |
| OBJ-003 | RF-019 | RN-024, RN-035, RN-036 | CU-008 | CA-019 | I2 |
| OBJ-001 | RF-020 | RN-018 | CU-009 | CA-020 | I3 |
| OBJ-001 | RF-021 | RN-010, RN-012, RN-014, RN-018 | CU-009 | CA-021 | I3 |
| OBJ-001 | RF-022 | RN-014, RN-018, RN-019 | CU-010 | CA-022 | I3 |
| OBJ-003 | RF-023 | RN-019, RN-021, RN-031 | CU-010 | CA-023 | I3 |
| OBJ-003 | RF-024 | RN-020 | CU-011 | CA-024 | I3 |
| OBJ-002 | RF-025 | RN-008, RN-020, RN-022 | CU-011 | CA-025 | I3 |
| OBJ-003 | RF-026 | RN-021, RN-031 | CU-012 | CA-026 | I3 |
| OBJ-003 | RF-027 | RN-013, RN-021, RN-023 | CU-012 | CA-027 | I3 |
| OBJ-002 | RF-028 | RN-011, RN-022 | CU-013 | CA-028 | I1 |
| OBJ-003 | RF-029 | RN-022, RN-024 | CU-013 | CA-029 | I3 |
| OBJ-003 | RF-030 | RN-021, RN-022, RN-023 | CU-014 | CA-030 | I3 |
| OBJ-003 | RF-031 | RN-013, RN-020, RN-023 | CU-014 | CA-031 | I3 |
| OBJ-003 | RF-032 | RN-024, RN-033 | CU-015 | CA-032 | I1 |
| OBJ-003 | RF-033 | RN-025 | CU-015 | CA-033 | I2 |
| OBJ-001 | RF-034 | RN-031, RN-033 | CU-016 | CA-034 | I3 |
| OBJ-003 | RF-035 | RN-002, RN-033 | CU-016 | CA-035 | I3 |
| OBJ-003 | RF-036 | RN-026 | CU-003 | CA-036 | I1 |
| OBJ-002 | RF-037 | RN-028, RN-030 | CU-004 | CA-037 | I3 |
| OBJ-004 | RF-038 | RN-024, RN-025, RN-029 | CU-002 | CA-038 | I1 |
| OBJ-003 | RF-039 | RN-012, RN-031 | CU-015 | CA-039 | I2 |
| OBJ-006 | RF-040 | RN-014, RN-034 | CU-001 | CA-040 | I1 |

## Cobertura de reglas

| Regla | Requisitos relacionados |
| --- | --- |
| RN-001 | RF-003, RF-004 |
| RN-002 | RF-001, RF-002, RF-004, RF-010, RF-035 |
| RN-003 | RF-005 |
| RN-004 | RF-006 |
| RN-005 | RF-006 |
| RN-006 | RF-008 |
| RN-007 | RF-007, RF-008, RF-009 |
| RN-008 | RF-010, RF-015, RF-025 |
| RN-009 | RF-008, RF-012, RF-015 |
| RN-010 | RF-015, RF-021 |
| RN-011 | RF-015, RF-016, RF-028 |
| RN-012 | RF-009, RF-016, RF-021, RF-039 |
| RN-013 | RF-016, RF-027, RF-031 |
| RN-014 | RF-009, RF-016, RF-018, RF-021, RF-022, RF-040 |
| RN-015 | RF-014, RF-017 |
| RN-016 | RF-013 |
| RN-017 | RF-013, RF-014 |
| RN-018 | RF-020, RF-021, RF-022 |
| RN-019 | RF-022, RF-023 |
| RN-020 | RF-024, RF-025, RF-031 |
| RN-021 | RF-023, RF-026, RF-027, RF-030 |
| RN-022 | RF-025, RF-028, RF-029, RF-030 |
| RN-023 | RF-027, RF-030, RF-031 |
| RN-024 | RF-011, RF-019, RF-029, RF-032, RF-038 |
| RN-025 | RF-033, RF-038 |
| RN-026 | RF-003, RF-005, RF-036 |
| RN-027 | RF-013 |
| RN-028 | RF-037 |
| RN-029 | RF-002, RF-038 |
| RN-030 | RF-012, RF-037 |
| RN-031 | RF-023, RF-026, RF-034, RF-039 |
| RN-032 | RF-015 |
| RN-033 | RF-011, RF-032, RF-034, RF-035 |
| RN-034 | RF-018, RF-040 |
| RN-035 | RF-019 |
| RN-036 | RF-019 |

## Escenarios adicionales de frontera y fallo

Son especificaciones de pruebas futuras, no resultados ejecutados. Cada ensayo debe
registrar fixture, identidad de operaciones, intercalación/fallo y conciliación final.

| ID | RF | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| CA-101 | RF-016 | Diez unidades y dos operaciones distintas de siete, sin parcial. | Ambas confirman concurrentemente. | Una confirma siete, la otra se rechaza; saldo tres, una salida y auditoría coherente. |
| CA-102 | RF-018 | Una operación de salida ya confirmada cuya respuesta se perdió. | Se repite la misma identidad y contenido. | Se recupera el mismo documento; cantidades y número de movimientos no cambian. |
| CA-103 | RF-018 | Una identidad asociada a cantidad cinco. | Se reenvía esa identidad con cantidad seis. | Conflicto de contenido sin un segundo efecto; el resultado original se conserva. |
| CA-104 | RF-016 | Un despacho de dos lotes listo para confirmar. | Se inyecta fallo antes de completar la unidad de negocio. | No existe salida confirmada parcialmente ni descuento sin documento/evento; el reintento se trata según resultado conocido. |
| CA-105 | RF-028 | Una propuesta FEFO contiene un lote utilizable. | El lote se bloquea antes de confirmar. | No se despacha el lote; se recalcula o rechaza. No se usa la propuesta obsoleta. |
| CA-106 | RF-015 | Dos lotes con vencimiento elegible igual y recepciones distintas. | Se calcula asignación. | Se aplica PP-004 de forma determinista; si también empatan se usa identificador estable. |
| CA-107 | RF-022 | Ocho expedidas, cinco recibidas utilizables y una dañada recibida. | Se registra recepción. | Se descuentan seis del tránsito, cinco pasan a utilizable y una a segregada; dos quedan pendientes, sin pérdida implícita. |
| CA-108 | RF-033 | Copia de ensayo de historial y referencia de cierre independiente. | Se modifica el contenido de un evento sin rehacer enlaces. | La verificación detecta anomalía e identifica el alcance revisado. |
| CA-109 | RF-033 | Cadena válida con referencia independiente al último evento esperado. | Se trunca su final o se recalcula una cadena distinta. | Se detecta divergencia respecto de la referencia; sin esa referencia el resultado se declara limitado, no prueba absoluta. |
| CA-110 | RF-002 | Usuario autorizado solo para sede A. | Manipula la sede a B o utiliza un permiso revocado. | Operación protegida rechazada sin revelar saldos de B ni aplicar cambios. |
| CA-111 | RF-027 | Un ajuste propuesto por usuario U sobre un corte anterior. | U intenta aprobar o el saldo cambió antes de otra aprobación. | Se impide autoaprobación; el segundo caso exige revalidar sin aplicar una diferencia obsoleta. |
| CA-112 | RF-039 | Saldos y movimientos conocidos, incluyendo traslados y compensaciones. | Se introduce diferencia en una copia controlada. | La conciliación informa la discrepancia y no la corrige silenciosamente. |
| CA-113 | RF-015 | La fecha operativa alcanza el vencimiento entre consulta y confirmación. | Se confirma según PP-003. | El lote se excluye al confirmar; no se basa la elegibilidad en la fecha de la pantalla anterior. |
| CA-114 | RF-006 | Dos cajas de veinte unidades recibidas y luego conversión cambiada. | Se consulta la recepción histórica. | La cantidad histórica sigue siendo cuarenta unidades y muestra el factor aplicado. |
| CA-115 | RF-034 | Un usuario tiene acceso a A y otro a toda la cadena. | Consultan/exportan el mismo periodo. | Cada resultado respeta su ámbito, muestra corte y unidades y no duplica tránsito. |
| CA-116 | RF-024 | Despacho con cinco y devolución acumulada de dos. | Dos operaciones diferentes intentan devolver dos cada una a la vez. | La suma aceptada no supera cinco; ninguna carrera crea más cantidad retornada que entregada. |
| CA-117 | RF-021 | Traslado autorizado para ocho unidades y salida ya confirmada. | Se pierde respuesta y se repite la salida. | Se devuelve la expedición original; no se descuentan otras ocho ni se duplican unidades en tránsito. |
| CA-118 | RF-003 | Tres sedes iniciales y permisos segregados. | Se registra una cuarta con sus ubicaciones y usuarios. | Puede operar según permisos sin modificar código y no comparte saldos por defecto. |

## Cobertura de calidad

| Objetivo | RNF | Escenarios |
|---|---|---|
| OBJ-001 | RNF-006 | ESC-004 |
| OBJ-002 | RNF-001 | ESC-001; CA-101/CA-105/CA-113 |
| OBJ-003 | RNF-007, RNF-008 | ESC-005, ESC-006; CA-108/CA-109/CA-112 |
| OBJ-004 | RNF-002 | ESC-003; CA-110 |
| OBJ-005 | RNF-003, RNF-004, RNF-005, RNF-012 | ESC-002, ESC-009 |
| OBJ-006 | RNF-009, RNF-010, RNF-011 | ESC-007, ESC-008 |

## Revisión y evidencias futuras

| Momento | Qué se comprueba | Evidencia |
|---|---|---|
| Análisis | IDs, enlaces, reglas, flujos, estados y pendientes | Informe de revisión documental del PR |
| Diseño | Fuente de verdad, transacción, permisos y recuperación | Prototipos y decisiones justificadas |
| Implementación | CA normales y negativos por incremento | Pruebas y resultados asociados a versión |
| Carga | Perfil medible y conservación del inventario | Resultados crudos, percentiles, errores y conciliación |
| Validación externa | Procesos y políticas operativas | Acta o notas reales, con consentimiento y alcance |

No hay pruebas de aplicación ejecutadas. Integrar este análisis no convierte sus
CA en pruebas pasadas ni elimina PN. Las pruebas manuales y automatizadas futuras
mantendrán los IDs como enlace estable a sus requisitos.
