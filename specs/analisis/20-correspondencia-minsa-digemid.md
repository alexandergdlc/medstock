# Correspondencia con MINSA/DIGEMID y límites de atribución

**Proyecto:** MedStock · **Versión:** 0.2.0 · **Fecha:** 2026-10-15

**Estado:** borrador para revisión; capacidades incluidas y políticas de detalle identificadas.

## Qué se comprobó

Se identificó la RM 554-2022/MINSA que aprueba el manual (FU-004). Su anexo original
completo sigue sin revisión integral. Ahora se consultaron guías oficiales de
inspección publicadas por DIRIS Lima Este y GERESA Arequipa (FU-011/FU-012), y la
modificación RM 810-2024/MINSA (FU-005). Esta es correspondencia documental, no un
pronunciamiento legal ni certificación de cumplimiento del sistema.

| Capacidad | Respaldo identificado | Aplicación y límite en MedStock |
|---|---|---|
| Entrega parcial | FU-011, 7.5.2.27, p. 11 del PDF: registro de entrega parcial de lo prescrito | Se refiere a receta/dispensación. Nuestro remanente de solicitud interna es una política de producto; no sustituye ese registro clínico. |
| Reservas | No se identificó un mandato de reserva informática en las secciones revisadas | Crear, expirar, consumir y liberar compromiso es decisión propia de MedStock. No afirmar que la RM impone duración ni prioridad. |
| Vencimientos | FU-012, 7.5.1.19 y 7.5.1.20, p. 7: identificación de próximos vencimientos y rotación FIFO/FEFO | MedStock elige FEFO. El corte por día y la normalización mes/año siguen PP-003; esos numerales no fijan nuestros parámetros. |
| Autorizaciones | FU-005, 7.1.1.b y 7.2.1: responsabilidades y supervisión; 7.3.6: conservar correcciones identificables | Roles informáticos y doble aprobación de ajustes son controles propios que apoyan responsabilidades; no se atribuye una obligación universal de dos clics o dos aprobadores. |
| Devoluciones | FU-012, 7.5.1.27 a 7.5.1.31, p. 8: procedimiento, registro y evaluación de retorno a disponible | Se propone evidencia y revisión por responsable facultado antes de liberar cantidades. La aplicación no comprueba conservación por sí sola. |

## Interpretación de las referencias

La fuente DIRIS contiene el acta base y hojas modificatorias: se deben contrastar
los numerales afectados con RM 810-2024; no usar una fila antigua como prueba de
vigencia completa. Las páginas indicadas son ordinales del archivo PDF consultado.
FU-012 respalda los numerales citados, no reemplaza el conjunto normativo nacional.

## Uso en requisitos

Los RF especializados 41 a 64 se originan en la decisión del propietario y en el
análisis de controles. La evidencia sanitaria contextualiza solo los temas indicados,
no cada parámetro o solución técnica. RN-009 conserva la política temporal propuesta;
RN-020/RN-041 documentan el retorno; RN-040 es control de versión/aprobación del
producto. Las correspondencias completas se siguen por 18, 08 y 15.

## Antes de operación real

PN-007 mantiene revisión del manual íntegro y sus modificaciones, aplicabilidad por
establecimiento/producto y validación profesional. Si se incorpora dispensación a
pacientes se requerirán análisis clínico, datos y registros adicionales; no se añade
ese alcance por haber encontrado el numeral de entrega parcial. El código abierto
o una cadena de hashes no acreditan habilitación sanitaria ni firma profesional.
