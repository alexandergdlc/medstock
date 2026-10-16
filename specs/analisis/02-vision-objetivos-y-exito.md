# Visión, objetivos y resultados esperados

**Proyecto:** MedStock · **Versión:** 0.3.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Decisiones del propietario aceptadas; detalles operativos pendientes según 14.

## Visión

Que la administración de una cadena conozca qué productos y lotes tiene, dónde están,
por qué se movieron y quién intervino, mientras farmacia atiende solicitudes con
control de elegibilidad y concurrencia. El valor inicial es inventario confiable;
las funciones clínicas completas y la inteligencia artificial no son precondiciones.

## Objetivo general

Especificar y posteriormente construir una solución web multisede de trazabilidad
que preserve integridad de inventario, selección FEFO y evidencia de movimientos,
con crecimiento configurable y evaluación explícita de carga.

| ID | Objetivo específico | Evidencia de éxito futura |
|---|---|---|
| OBJ-001 | Gestionar y ampliar una cadena sin fijar tres sedes | Alta de cuarta sede y balances segregados; traslado sin doble conteo |
| OBJ-002 | Controlar disponibilidad y priorizar lotes elegibles | Casos FEFO, vencimiento, bloqueo y parcialidad con resultados esperados |
| OBJ-003 | Reconstruir y verificar cada movimiento | Historial por lote, compensaciones, reintentos y detección de anomalías |
| OBJ-004 | Limitar acceso según responsabilidades | Casos negativos de permiso, revocación y separación entre sedes |
| OBJ-005 | Evaluar comportamiento bajo un pico de 2 000 usuarios activos | Informe con perfil, duración, latencias, errores y conciliación |
| OBJ-006 | Hacer la operación comprensible y el análisis verificable | Errores con seguimiento, recorridos reproducibles y enlaces de requisitos |

## Criterios de éxito del análisis

El 100 % de RF debe tener actor, prioridad, criterio principal, CU, regla y objetivo;
los RNF deben tener método de verificación. Los procesos críticos incluyen alternativas
y errores; las decisiones abiertas tienen responsable y momento de cierre. El dossier
se puede revisar sin depender de un chat previo.

## Criterios de éxito del producto

Se aspira a cero saldos negativos y cero efectos duplicados en los escenarios
controlados; un movimiento confirmado tiene autor, ámbito y detalle reconstruible.
Agregar sedes no exige código específico por sede. Para carga se usará el perfil
propuesto ESC-002, sin declarar aprobado el objetivo hasta medirlo.

Los p95 candidatos de 500 ms/1 s se aplican a respuestas operativas según 16; los
reportes grandes tienen otra categoría. Son metas de ingeniería pendientes, no
promesas comerciales. No se afirma una reducción porcentual de merma o ahorro
porque no existe línea base de una organización real.

## Evaluación de optimización

OBJ-002 se complementa con RF-067/RF-068: identificar sobrestock, faltantes y riesgo
de vencimiento con corte y parámetros explícitos. Se observarán cantidad no atendida,
merma por causa, antigüedad y cobertura por producto/ubicación. No se fija aún un
porcentaje de reducción sin línea base. Un aumento de traslados no demuestra mejora;
se compararán disponibilidad y pérdida evitable, sin incentivar consumo clínico.
