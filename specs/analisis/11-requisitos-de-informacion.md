# Información, validaciones e integraciones

**Proyecto:** MedStock · **Versión:** 0.2.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Las políticas PP son propuestas.

## Diccionario conceptual de información

Los campos describen necesidades, no columnas ni tipos físicos. Un identificador
estable se conserva aunque cambie el nombre visible. Los documentos confirmados
mantienen los valores aplicados entonces para no reescribir el pasado.

| Concepto | Información mínima | Validación | Relaciones / sensibilidad |
|---|---|---|---|
| Sede | Código, nombre, zona horaria, estado | Código único; cierre sin pendientes | Ubicaciones y permisos; sin datos clínicos |
| Ubicación | Código, sede, clase, estado | Una sede o ámbito de tránsito definido | Existencias y movimientos |
| Servicio | Código, sede, responsable | Ámbito vigente | Solicitudes; no historia clínica |
| Usuario | Identidad, estado y asignaciones | Activo y permiso por operación | Datos de personal; acceso limitado |
| Producto | Código, descripción, tipo, unidad base, fabricante pertinente | Identidad no ambigua; no confundir DCI y marca | Presentaciones, lotes; catálogo compartido |
| Presentación | Producto, nombre, factor y vigencia | Factor positivo; cantidad base íntegra en PP-001 | Factor histórico en movimientos |
| Lote | Producto, fabricante, código, vencimiento y referencias de origen | Conflictos de fecha no se fusionan | Varios balances en sedes |
| Existencia | Lote, ubicación, condición, cantidad y corte | Cantidad no negativa; condición reconocida | No sumar distintas unidades |
| Procedencia | Proveedor/origen y referencia controlada | Documento identificable | Recepción; evitar datos personales innecesarios |
| Recepción/línea | Número, procedencia, ubicación, lotes, cantidad, evaluación, autor | Total convertido y confirmación coherente | Genera entrada por condición |
| Solicitud/línea | Servicio, solicitante, producto, solicitado, entregado, cancelado y estado | Cantidades consistentes con RN-017 | Uno o varios despachos |
| Despacho/línea | Solicitud, sede, operador, lote, cantidad y destino | Entrega acumulada <= solicitado | Constancia; no pacientes |
| Traslado/línea | Origen, destino, autorización, lote, expedido, recibido y diferencia | Conservación y límite por pendiente | Tránsito y recepciones |
| Devolución/línea | Despacho original, lote, cantidad, evaluación y evaluador | Límite acumulado retornable | Cuarentena y decisión |
| Conteo/ajuste | Corte, físico, saldo, diferencia, motivo, evidencia, solicitante y aprobador | Revalidar al aprobar; aprobador distinto | Compensación vinculada |
| Bloqueo/retiro | Lote, alcance, motivo, referencia, fechas y responsable | Permiso de ámbito y liberación explícita | Afecta elegibilidad; no borra saldo |
| Movimiento | Tipo, documento, operación, autor, instante, lote, unidad base, origen/destino/condición | Inmutable desde operaciones ordinarias | Reconstrucción de custodia |
| Evento de auditoría | Operación, secuencia, contenido significativo y vínculo de integridad | Verificable frente a referencia | No registrar contraseñas ni tokens |
| Resultado de operación | Identidad, ámbito, contenido representado, estado y documento resultante | Mismo contenido reconocido; conflicto rechazado | Recuperación tras respuesta perdida |
| Evidencia | Referencia, tipo, autor y fecha | Acceso autorizado; formato de adjunto aún por diseñar | No exige R2 ni guardar archivos binarios en el primer prototipo |

## Reglas de datos y calidad

RN-004 a RN-009 definen unidades, lotes y fechas. En el prototipo no se acepta
fecha ambigua ni se infiere silenciosamente un día a partir de mes/año. PP-003 debe
resolverlo con validación profesional. Una conversión guardada en un movimiento es
histórica: actualizar la presentación afecta nuevas operaciones.

El corte y la versión de consulta permiten distinguir dato mostrado y estado al
confirmar. No se decide stock basándose en una copia potencialmente antigua.
La identidad de operación se conserva durante la vida del documento; la política
final de retención y archivo queda en PN-006 y no habilita borrar historia.

## Privacidad y clasificación

Catálogo y stock son información operativa de acceso restringido; no son datos
públicos por estar el código en GitHub. Identidad del personal y auditoría requieren
permisos. Historias clínicas, DNI de pacientes y diagnósticos quedan excluidos.
Las semillas y capturas de demostración usan usuarios y documentos sintéticos.
No incluir tokens de sesión en logs ni credenciales en exportaciones.

## Integraciones: necesidad y estado

| Intercambio | Datos | Estado de análisis | Fallo esperado |
|---|---|---|---|
| Navegador a MedStock | Identidad, comandos, consultas | Necesario | Diferenciar rechazo y resultado incierto |
| Recepción desde proveedor | Referencia y líneas | Registro manual en primera versión | Documento incompleto se corrige |
| Reporte/exportación | Filtros, corte, resultados autorizados | Incluido | No producir exportación parcial sin avisar |
| Registro de auditoría | Eventos y referencia verificable | Incluido | No afirmar integridad sin referencia |
| Sistema clínico externo | Recetas/pacientes | Fuera de primera versión | Requiere análisis específico |
| Alertas sanitarias oficiales | Referencia de retiro | Registro manual inicialmente | No afirmar integración automática |

No existe contrato de API externa aceptado. OpenAPI, esquemas físicos, mecanismos
concretos de identidad y gestión de archivos se definen en diseño técnico.

## Información especializada

| Concepto | Datos mínimos adicionales | Control |
|---|---|---|
| Reserva | Solicitud, propietario/ámbito, líneas y lotes, cantidad inicial, consumida, liberada y remanente, inicio/fin y estado | Identidad recuperable; vigencia evaluada con tiempo operativo |
| Aprobación | Tipo, documento/versiones, contenido significativo, solicitante/aprobador, decisión y motivo | No reutilizar sobre contenido distinto; permiso vigente al ejecutar |
| Política temporal | Valor rotulado y precisión, interpretación aprobada, versión y vigencia | No inventar día desde mes/año ni alterar historia |
| Evaluación de retorno | Cantidades por línea aceptada/rechazada/pendiente, causa y evidencia de conservación | Suma de decisiones no supera lo recibido; responsable facultado |

Los compromisos se registran como asignaciones y eventos, no como recepciones físicas.
El detalle temporal de reserva requiere zona/instante inequívoco; el navegador no
es autoridad del tiempo. El almacenamiento de evidencias no obliga a elegir un
servicio concreto en análisis.
