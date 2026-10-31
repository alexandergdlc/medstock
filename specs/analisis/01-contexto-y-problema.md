# Contexto, problema y levantamiento

**Proyecto:** MedStock · **Versión:** 0.3.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Decisiones del propietario aceptadas; detalles operativos pendientes según 14.

## Contexto de negocio

Una cadena reúne establecimientos con servicios y depósitos de medicamentos e
insumos médicos. Las sedes necesitan visibilidad local y supervisión agregada, sin
confundir las existencias de una clínica con las de otra. Auna publica sedes en
varias ciudades y sirve como referencia de organización multisede (FU-003).
No se afirma que MedStock reproduzca su sistema de farmacia.

El manual de oficina farmacéutica aprobado por MINSA y una modificación consultada
reconocen actividades de almacenamiento y dispensación y la trazabilidad de productos
(FU-004, FU-005). El análisis toma ese contexto y propone controles informáticos;
no declara que una lista de pantallas satisfaga todas las obligaciones sanitarias.

## Problema formulado

¿Cómo mantener información verificable de cantidades, lotes y movimientos entre
sedes, priorizando existencias elegibles por vencimiento y evitando salidas duplicadas
cuando varias personas operan sobre el mismo stock?

Las siguientes son hipótesis de riesgo, no incidentes medidos en una clínica:

| Problema potencial | Causa a investigar | Consecuencia | Necesidad |
|---|---|---|---|
| Despachar lote inadecuado | Elegibilidad y orden no comprobados | Merma o entrega no permitida | FEFO y bloqueo |
| Doble descuento/sobreasignación | Confirmaciones concurrentes o reintentos | Inventario inconsistente | Operación indivisible e identidad |
| Pérdida de trazabilidad | Registros editables sin relaciones | No reconstruir un lote | Movimientos vinculados y verificación |
| Doble conteo entre sedes | Traslado sin estado de tránsito | Consolidado incorrecto | Balance de tránsito |
| Acceso fuera de sede | Permisos aplicados solo en pantalla | Exposición o modificación indebida | Autorización en cada operación |
| Lentitud en picos | Carga sin caracterizar y consultas amplias | Retrasos y reintentos | Escenarios y medición |

## Interesados y situación actual

El propietario y desarrollador es Alexander; el docente es evaluador académico.
Los roles operativos se definen en 04, pero aún no se entrevistó a sus equivalentes
reales. No se dispone de inventarios, manuales internos, métricas de merma, tiempos
observados ni volumen de una organización concreta. Por tanto no se dibuja un
AS-IS supuestamente observado: se documentan preguntas y un proceso TO-BE propuesto.

## Técnicas de levantamiento

1. Análisis documental de sílabo, fuentes oficiales y acuerdos del propietario.
2. Modelamiento de procesos y ejemplos para detectar omisiones.
3. Revisión de escenarios con responsable farmacéutico/almacén cuando exista acceso.
4. Validación de requisitos con criterios observables y matriz de trazabilidad.

Preguntas para entrevista futura: ¿dónde termina el stock de farmacia?, ¿quién
libera cuarentena?, ¿qué se registra en un traslado?, ¿cómo se acreditan daños?,
¿qué medicamentos exigen tratamiento especial?, ¿cómo se interpreta el vencimiento?,
¿qué documento autoriza una devolución? No se consignan respuestas inventadas.

## Límites de la investigación

La fuente sanitaria de 2022 se identificó, pero su anexo completo no se extrajo por
el tamaño del archivo. Se consultó el texto accesible de la modificación de 2024 y, en la revisión 0.2.0,
las guías oficiales de inspección identificadas en FU-011/FU-012;
queda pendiente revisión del conjunto normativo aplicable y del personal competente.
Las políticas de detalle de MedStock tienen origen PP, no se atribuyen a una ley.
