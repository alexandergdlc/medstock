# Reglas de negocio e invariantes

**Proyecto:** MedStock · **Versión:** 0.2.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Las políticas PP son propuestas.

## Autoridad y estado

Estas son las definiciones normativas de RN para este borrador. ACORDADA significa
aceptación del propietario; las políticas PP son propuestas por revisar, no reglas
atribuidas a DIGEMID ni a una cadena privada. Su detalle y decisión están en 14.
| ID | Regla | Definición | Estado |
| --- | --- | --- | --- |
| RN-001 | Sedes ampliables | Agregar sedes y ubicaciones mediante registros; los identificadores no dependen de nombres fijos ni del número tres. | ACORDADA |
| RN-002 | Ámbito | Toda operación identifica sede y ubicación; el servidor comprueba que el usuario tiene permiso vigente en ese ámbito. | ACORDADA |
| RN-003 | Catálogo común | Un producto comparte identidad en la cadena, pero no mezcla existencias entre ubicaciones. Cambiar su nombre no crea stock. | ACORDADA |
| RN-004 | Unidad base | Cada producto tiene una unidad base; las cantidades de movimientos se expresan en ella y las conversiones se registran con su factor aplicado. | ACORDADA |
| RN-005 | Cantidades | Las cantidades solicitadas y movidas son positivas y enteras para productos discretos. No se permite fraccionar un frasco sellado; productos medidos a granel quedan fuera del primer incremento. | PROPUESTA PP-001 |
| RN-006 | Identidad de lote | Se distingue producto, fabricante y código de lote. El mismo lote puede estar en varias sedes; fechas incompatibles requieren revisión y no se fusionan silenciosamente. | PROPUESTA PP-002 |
| RN-007 | Recepción | Ninguna recepción confirmada incorpora cantidades sin origen, documento, detalle por lote, responsable y resultado de revisión. Lo observado queda en cuarentena. | ACORDADA |
| RN-008 | Disponibilidad | Solo se despacha existencia de condición utilizable y cantidad suficiente. Cuarentena, bloqueo, vencimiento y tránsito no son disponibilidad para solicitudes ordinarias. | ACORDADA |
| RN-009 | Vencimiento | La elegibilidad compara la fecha de vencimiento con la fecha operativa de la sede. Para el prototipo, fecha menor o igual a hoy se excluye. Fechas solo mes/año requieren normalización validada por un responsable. | PROPUESTA PP-003 |
| RN-010 | Orden FEFO | Aplicar FEFO sobre libre elegible al asignar sin reserva o crear una reserva; empate por primera recepción en ubicación de salida y luego ID de lote. Consumir reserva respeta su asignación vigente, revalidando elegibilidad; no reasigna silenciosamente. | ACORDADA; detalle PP-004 y PP-015 |
| RN-011 | Confirmación | La selección mostrada es preliminar: al confirmar se vuelven a comprobar existencia, estado del lote, permisos y cantidad pendiente. | ACORDADA |
| RN-012 | Integridad de operación | Cada recepción, despacho o salida de traslado confirmada une su documento, cambios de existencia y auditoría: se confirman juntos o no producen efecto de negocio. | ACORDADA |
| RN-013 | Sin negativos | Ninguna intercalación de operaciones válidas puede dejar existencia negativa o entregar más unidades que las disponibles. | ACORDADA |
| RN-014 | Reintentos | Una misma operación lógica produce como máximo un efecto: un reintento con el mismo contenido devuelve su resultado; contenido diferente con la misma identidad se rechaza. | ACORDADA |
| RN-015 | Parcialidad | Si no alcanza el stock, se rechaza sin efectos salvo aceptación explícita de una cantidad parcial. La cantidad pendiente se conserva; nunca se marca completada una solicitud incompleta. | PROPUESTA PP-005 |
| RN-016 | Reservas explícitas | Enviar o consultar una solicitud no reserva stock. El alcance incluye una operación explícita de reserva por lote, con vigencia finita, consumo y liberación; su activación está prevista en I3. | CAPACIDAD ACORDADA; detalle PP-006 |
| RN-017 | Solicitud | Solo una solicitud enviada y vigente puede atenderse. Su creador no cambia líneas ya atendidas ni cancela unidades entregadas. | PROPUESTA PP-007 |
| RN-018 | Traslado | El origen y destino son distintos. La salida descuenta origen y crea tránsito; la recepción descuenta tránsito y acredita destino sin duplicar existencia global. | ACORDADA |
| RN-019 | Diferencias | En recepción de traslado, cantidades dañadas quedan segregadas y faltantes permanecen como diferencia pendiente; no se convierte automáticamente un faltante en pérdida aprobada. | PROPUESTA PP-008 |
| RN-020 | Devolución | Una devolución referencia la salida y sus lotes. No puede superar la cantidad entregada menos devoluciones previas; entra a cuarentena hasta evaluación. | ACORDADA |
| RN-021 | Ajustes | Un ajuste requiere motivo, evidencia y autorización de un usuario distinto al solicitante; registra un movimiento compensatorio y no modifica la historia. | ACORDADA; doble intervención PROPUESTA PP-009 |
| RN-022 | Bloqueo | Un lote bloqueado deja de ser elegible en todas las ubicaciones afectadas. Liberarlo requiere responsable autorizado, motivo y evidencia. No se despachan lotes vencidos mediante excepción. | ACORDADA |
| RN-023 | Correcciones | Los movimientos confirmados no se editan ni borran desde funciones ordinarias. Un error se corrige con operación vinculada y comprobación de sus efectos previos. | ACORDADA |
| RN-024 | Auditoría | Toda mutación de negocio conserva autor, fecha, sede, documento, motivo, identidad de operación y cantidades por lote. | ACORDADA |
| RN-025 | Verificación | El registro debe permitir comprobar orden, enlaces y contenido de la cadena de auditoría frente a una referencia confiable; los cambios de permisos también se registran. | ACORDADA |
| RN-026 | Históricos | Sedes, productos y usuarios con movimientos se desactivan sin borrar sus referencias. Una sede con stock o tránsito pendiente no se cierra operativamente. | ACORDADA |
| RN-027 | Datos mínimos | Las solicitudes internas identifican servicio y responsable; no contienen nombres de pacientes, diagnósticos, DNI ni historias clínicas. | ACORDADA |
| RN-028 | Tiempos | Se conserva instante inequívoco del evento y fecha operativa de la sede. El catálogo de sedes registra su zona horaria. | PROPUESTA PP-010 |
| RN-029 | Roles | El administrador técnico no obtiene por defecto facultades de liberar lotes o aprobar ajustes. Los permisos se asignan explícitamente y son revocables. | PROPUESTA PP-011 |
| RN-030 | Reposición | El stock mínimo y el umbral de próximos vencimientos son configurables por sede y producto; una alerta no crea compras ni movimientos automáticamente. | PROPUESTA PP-012 |
| RN-031 | Conservación | Para cada lote, físico en sedes más tránsito debe reconciliarse con saldo inicial, entradas externas, salidas externas y ajustes autorizados. Un traslado interno no cambia ese total. | ACORDADA |
| RN-032 | Producto sin caducidad | Solo categorías con revisión autorizada admiten lote sin fecha; no compiten con lotes caducables en FEFO. Si no se justifica esta categoría, se excluye del prototipo. | PROPUESTA PP-013 |
| RN-033 | Informe | Los resultados indican ámbito, filtros y fecha de corte; los consolidados no exponen sedes fuera de permisos. | ACORDADA |
| RN-034 | Aislamiento de fallos | Un resultado incierto no autoriza repetir con otra identidad: primero se consulta el resultado de la operación original. | ACORDADA |
| RN-035 | Salida a servicio | La entrega a un servicio constituye salida del inventario gestionado. No afirma que el medicamento fue administrado al paciente; el subinventario clínico del servicio es evolución posterior. | PROPUESTA PP-014 |
| RN-036 | Obligaciones separadas | La aplicación apoya registros y controles; el software no acredita inspección física, condiciones de conservación ni certificación sanitaria. | ACORDADA |

## Reglas especializadas de compromiso y decisión

| ID | Regla | Definición | Estado |
| --- | --- | --- | --- |
| RN-037 | Compromisos y libre | En cada corte, libre = utilizable elegible menos compromiso vigente consumible. El compromiso no cambia físico y no supera la cantidad elegible a la que se vincula. | CAPACIDAD ACORDADA; detalle PP-006 |
| RN-038 | Elegibilidad de reserva | Solo se reserva para solicitud vigente, ámbito permitido y lotes elegibles. La reserva se asigna por FEFO y nunca autoriza consumir un lote que después dejó de ser elegible. | ACORDADA; detalle PP-015 |
| RN-039 | Ciclo temporal | Una reserva se cancela, expira o invalida solo por su remanente. A partir del fin T ya no compromete ni autoriza consumo, independientemente de cuándo se actualice su estado materializado. Un lote bloqueado no pasa a libre por liberar la reserva. | CAPACIDAD ACORDADA; plazo PP-016 |
| RN-040 | Decisión ligada al contenido | Aprobaciones e interpretaciones conservan versión, alcance, autor y evidencia. Una aprobación no se reutiliza con cantidades o lotes diferentes ni sustituye revalidar permisos y stock. | PROPUESTA PP-017 |
| RN-041 | Evidencia del retorno | Liberar devolución exige causa, origen y evidencia de conservación revisada por responsable facultado. Rechazarla conserva stock segregado hasta una disposición autorizada. | ACORDADA; procedimiento PP-018 |
| RN-042 | Conservación de reserva | Reservado inicial = consumido + liberado/caducado/invalidado + remanente. Solo consumir genera la salida física correspondiente; cada unidad se consume o libera una sola vez. | ACORDADA |


## Elegibilidad FEFO

Primero filtrar ámbito, producto activo, condición utilizable, ausencia de bloqueo,
fecha y cantidad positiva. Después ordenar los lotes elegibles. La vista preliminar
no garantiza stock; confirmar exige revalidación. No existe una excepción genérica
para despachar vencidos o saltarse bloqueos por urgencia dentro de este alcance.

## Invariantes comprobables

- Cantidad por balance >= 0; pendiente = solicitado - entregado - cancelado >= 0.
- Entregado por solicitud nunca supera lo solicitado sin una nueva solicitud autorizada.
- Devuelto acumulado no supera lo entregado por línea y lote.
- Expedido de traslado = recibido registrado + diferencia en tránsito pendiente +
  resoluciones documentadas; las categorías no se cuentan dos veces.
- Un movimiento confirmado tiene operación, ámbito, autor y contraparte documental.
- Reintentos de la misma identidad y contenido devuelven el resultado previo.
- El total de lote se conserva en traslados internos y cambios de condición.

## Ejemplos de frontera

Recibir de nuevo el mismo lote no crea otra identidad de lote; crea otro movimiento.
Bloquear un lote no elimina unidades físicas. Cancelar una solicitud no revierte una
entrega confirmada. Una baja disminuye custodia con evidencia; cambiar el estado del
lote a vencido no la disminuye. Los factores históricos no se recalculan con cambios
posteriores del catálogo.

## Disponibilidad con reservas

Sin reservas activas, libre coincide con utilizable elegible. Con reservas, las
cantidades comprometidas no están libres para otras solicitudes. La solicitud
propietaria puede consumir su propia asignación vigente y pedir libre adicional
mediante otra asignación válida; no se limita su derecho a su vista de libre ajeno.
Si llega otro lote con vencimiento anterior después de reservar, PP-015 propone
respetar el compromiso original válido; reasignar exige una operación explícita,
no un cambio silencioso. Esta política debe revisarse antes de implementar reservas.
