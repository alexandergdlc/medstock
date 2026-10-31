# Especialización de las cinco capacidades

**Proyecto:** MedStock · **Versión:** 0.3.0 · **Fecha:** 2026-10-15

**Estado:** borrador para revisión; capacidades incluidas y políticas de detalle identificadas.

## Cambio de alcance confirmado

Alexander pidió incorporar las cinco capacidades para implementación posterior y
mayor precisión de requisitos. Esto confirma su inclusión; no fija todavía duración
de reservas, criterio sanitario de fecha ni todos los niveles de autorización.
La versión 0.2.0 conserva IDs anteriores y añade especializaciones comprobables.

| Capacidad | RF generales conservados | RF especializados | Responsabilidad separada | Reglas principales |
| --- | --- | --- | --- | --- |
| Entregas parciales | RF-014, RF-017 | RF-041, RF-042, RF-043 | Confirmación de cantidad; acumulados; remanente cancelable; seguimiento sin duplicar entregas | RN-015, RN-017 |
| Reservas | RF-010, RF-015, RF-016, RF-018 | RF-044, RF-045, RF-046, RF-047, RF-048, RF-049, RF-050, RF-064 | Asignación FEFO explícita; libre/comprometido; vigencia; consumo y liberación; reconciliación | RN-016, RN-037, RN-038, RN-039, RN-042 |
| Vencimientos | RF-008, RF-012, RF-015, RF-028, RF-037 | RF-051, RF-052, RF-053, RF-054 | Precisión del rótulo; interpretación autorizada; alertas; revalidación temporal | RN-009, RN-028, RN-030, RN-040 |
| Autorizaciones | RF-002, RF-021, RF-027, RF-028, RF-038 | RF-055, RF-056, RF-057, RF-058, RF-063 | Permiso por tipo/sede; contenido aprobado; rechazo; separación de funciones; vigencia al ejecutar | RN-021, RN-029, RN-040 |
| Devoluciones | RF-024, RF-025, RF-030, RF-031 | RF-059, RF-060, RF-061, RF-062, RF-063 | Causa y conservación; límite retornable; evaluación por línea; disposición y evidencia | RN-020, RN-023, RN-041 |

No se busca aumentar el número por tamaño del proyecto. Un RF general define un
contrato agregado; la especialización detalla comportamientos y fronteras. Por ejemplo,
RF-017 mantiene la obligación de atención parcial y RF-041/RF-042 precisan consentimiento
y cierre del remanente; no se construyen dos módulos diferentes para la misma salida.

## Ejemplo integrado de reserva y parcialidad

1. Hay treinta unidades elegibles en una ubicación. Un servicio solicita veinte.
2. Enviar la solicitud no altera libre ni físico.
3. Tras autorizar veinte, una reserva explícita compromete veinte: físico treinta, compromiso veinte, libre diez.
4. Se despachan cinco contra esa reserva: físico veinticinco, compromiso quince, libre diez.
5. Se cancela el resto de la reserva: físico veinticinco, compromiso cero, libre veinticinco.
6. La solicitud conserva quince pendientes, salvo cancelación explícita de esas cantidades.

Cancelar reserva no cancela automáticamente la demanda; cancelar demanda sí debe
liberar su compromiso remanente de forma coherente. Si un lote se bloquea, la liberación
de su reserva no convierte esas unidades en libres elegibles.

## Aprobaciones y fechas

La autorización refiere contenido y versión. Cambiar cantidades o lotes requiere
revisión; incluso sin cambios, al ejecutar se comprueban permisos y stock actuales.
Para vencimientos se conserva la precisión del rótulo: mes/año no se transforma
silenciosamente en un día arbitrario. PP-003 mantiene el corte conservador propuesto,
pendiente de validación profesional, sin atribuirlo a MINSA.

## Retorno y evidencias

Una devolución se identifica contra la salida y lote, conserva causa y evidencia de
conservación y permanece segregada hasta evaluación. Las decisiones pueden ser por
subcantidad; el resto sigue pendiente. Rechazar no elimina unidades físicas: la
salida requiere disposición documentada. El sistema apoya esa decisión, no inspecciona
por sí mismo la calidad física ni firma como profesional sanitario.

## Calidad y secuencia de entrega

RNF-013 a RNF-018 especializan consistencia de compromisos, tiempo efectivo, evidencia,
autorización al ejecutar, corte de consulta y cobertura de las cinco capacidades.
Los objetivos de latencia RNF-003/RNF-004 siguen candidatos: no se multiplican metas
arbitrarias por cada pantalla. I1 prepara datos/fechas, I2 implementaría parciales y
FEFO; I3 incorporaría reservas y decisiones logísticas ampliadas. El diseño de I2
debe considerar la evolución de reservas, sin presumir que ya existe en I1.

## Ejemplo de parcialidad autorizado

Solicitar y autorizar 100, luego entregar 40, deja 60 pendientes autorizadas.
Reservar 30 de esas 60 deja 30 pendientes comprometidas y 30 pendientes sin reserva;
no reduce el pendiente a 30. Cancelar las 60 requiere motivo y libera las 30 reservadas,
sin revertir las 40 entregadas. La solicitud termina cerrada parcialmente.
