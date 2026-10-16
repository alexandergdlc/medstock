# Casos de uso y recorridos del usuario

**Proyecto:** MedStock · **Versión:** 0.1.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Las políticas PP son propuestas.

## Catálogo y uso

Los criterios principales están en 08; los casos amplían precondiciones, pasos y
alternativas sin duplicar reglas normativas. Todos comparten postcondición mínima:
un rechazo conocido no cambia inventario; un resultado incierto requiere consulta.
Los pasos describen negocio, no contratos API ni clases de implementación.

## CU-001 — Acceder y operar con seguimiento

**Actor:** Usuario.

**Precondiciones:** Cuenta activa; servicio disponible.

**Entrada/disparador:** Credenciales o sesión. **Postcondición:** Acceso autorizado o rechazo informado.

**Requisitos:** RF-001, RF-040.

**Flujo principal:**

1. Identificar usuario.
2. Seleccionar ámbito permitido.
3. Ejecutar operación y conservar referencia de seguimiento.

**Alternativas y errores:**

- Credenciales inválidas: informar sin revelar stock.
- Sesión cerrada/revocada: impedir nueva operación.
- Resultado incierto: ofrecer consulta, no inventar cancelación.

## CU-002 — Administrar identidades y permisos

**Actor:** Administrador.

**Precondiciones:** Permiso administrativo vigente.

**Entrada/disparador:** Alta/cambio de rol o baja de usuario. **Postcondición:** Asignación vigente y evento de auditoría.

**Requisitos:** RF-002, RF-038.

**Flujo principal:**

1. Seleccionar usuario y ámbito.
2. Validar rol y separación de facultades.
3. Confirmar cambio y registrar autor/instante.

**Alternativas y errores:**

- Sin permiso: rechazar.
- Usuario revocado: siguiente operación rechazada.
- Evitar que un cambio administrativo implique facultad clínica no asignada.

## CU-003 — Gestionar establecimientos

**Actor:** Administrador o responsable de sede.

**Precondiciones:** Identidad y permiso de configuración.

**Entrada/disparador:** Nueva sede/ubicación o solicitud de cierre. **Postcondición:** Estructura vigente y referencias conservadas.

**Requisitos:** RF-003, RF-004, RF-036.

**Flujo principal:**

1. Validar código único y zona horaria.
2. Vincular ubicaciones y servicios.
3. Guardar sin crear cantidades de inventario.

**Alternativas y errores:**

- Código duplicado: no crear otra entidad.
- Cierre con stock/tránsito: impedir y listar pendientes.

## CU-004 — Mantener catálogo y políticas

**Actor:** Gestor de catálogo o responsable central.

**Precondiciones:** Permiso específico y unidad definida.

**Entrada/disparador:** Producto, presentación o parámetro. **Postcondición:** Versión utilizable del catálogo.

**Requisitos:** RF-005, RF-006, RF-037.

**Flujo principal:**

1. Identificar producto/fabricante.
2. Definir unidad base y conversiones.
3. Guardar y registrar cambios.

**Alternativas y errores:**

- Factor inválido: rechazar.
- Producto con historia: desactivar, no borrar.
- Cambio no recalcula cantidades históricas.

## CU-005 — Recibir productos por lote

**Actor:** Almacenero autorizado.

**Precondiciones:** Sede/ubicación activa; catálogo y procedencia.

**Entrada/disparador:** Documento, líneas y evaluación física. **Postcondición:** Entrada confirmada y constancia.

**Requisitos:** RF-007, RF-008, RF-009.

**Flujo principal:**

1. Registrar documento y detalle con lotes.
2. Clasificar aceptación u observación.
3. Convertir a unidad base y revisar totales.
4. Confirmar entrada, balances y evento como unidad de negocio.

**Alternativas y errores:**

- Lote contradictorio: revisión, sin confirmar.
- Observado: cuarentena.
- Reintento: recuperar recepción original.
- Fallo anterior a confirmar: sin efecto.

## CU-006 — Consultar stock e historial

**Actor:** Usuario autorizado.

**Precondiciones:** Ámbito autorizado.

**Entrada/disparador:** Filtros y producto/lote. **Postcondición:** Saldo por condición e historial con corte.

**Requisitos:** RF-010, RF-011, RF-012.

**Flujo principal:**

1. Validar ámbito.
2. Aplicar filtros y paginar.
3. Mostrar disponible separado de no disponible.
4. Consultar movimientos del lote.

**Alternativas y errores:**

- Sin permiso: rechazar sin filtrar datos después de entregarlos.
- Saldo puede cambiar: no prometer asignación desde consulta.
- Alertas no generan movimientos.

## CU-007 — Solicitar insumos al servicio

**Actor:** Solicitante.

**Precondiciones:** Servicio de la sede; producto activo.

**Entrada/disparador:** Líneas positivas en unidad base. **Postcondición:** Solicitud enviada o remanente cancelado.

**Requisitos:** RF-013, RF-014.

**Flujo principal:**

1. Crear borrador sin datos personales clínicos.
2. Revisar cantidades y enviar.
3. Consultar avance y cancelar pendiente cuando proceda.

**Alternativas y errores:**

- Enviar no reserva stock en PP-006.
- Línea atendida no se edita ni se cancela retroactivamente.
- Cantidad inválida: corregir antes de enviar.

## CU-008 — Despachar mediante FEFO

**Actor:** Farmacia.

**Precondiciones:** Solicitud enviada y permiso de salida.

**Entrada/disparador:** Identidad de operación, cantidad y aceptación parcial. **Postcondición:** Despacho confirmado con remanente y constancia.

**Requisitos:** RF-015, RF-016, RF-017, RF-018, RF-019.

**Flujo principal:**

1. Revisar servicio, pendiente y elegibilidad.
2. Proponer asignación FEFO de lotes.
3. Registrar aceptación parcial si corresponde.
4. Revalidar permisos, lotes y saldos al confirmar.
5. Confirmar documento, cantidades y auditoría como unidad.
6. Emitir constancia con los lotes realmente entregados.

**Alternativas y errores:**

- Stock cambió: recalcular o rechazar, no usar propuesta obsoleta.
- Bloqueo/vencimiento: excluir.
- Fallo parcial: sin salida confirmada incompleta.
- Respuesta perdida: consultar la misma operación.
- Misma identidad y contenido diferente: rechazar.

## CU-009 — Expedir traslado

**Actor:** Responsable de origen y operador autorizado.

**Precondiciones:** Origen/destino activos distintos.

**Entrada/disparador:** Solicitud, autorización y líneas. **Postcondición:** Unidades en tránsito y salida de origen.

**Requisitos:** RF-020, RF-021.

**Flujo principal:**

1. Registrar demanda y destino.
2. Autorizar en origen.
3. Asignar lotes elegibles y confirmar salida a tránsito.
4. Emitir detalle para recepción.

**Alternativas y errores:**

- Sin stock: no expedir.
- Sin autorización: no confirmar.
- Reintento no duplica tránsito.
- Salida confirmada no se cancela como borrador.

## CU-010 — Recibir y resolver traslado

**Actor:** Receptor de destino y responsable autorizado.

**Precondiciones:** Traslado expedido con cantidades pendientes.

**Entrada/disparador:** Conteo, condición y evidencia. **Postcondición:** Recepción registrada o diferencia pendiente.

**Requisitos:** RF-022, RF-023.

**Flujo principal:**

1. Identificar traslado y lotes.
2. Registrar recibidas aceptadas/observadas.
3. Reducir tránsito por lo efectivamente recibido.
4. Registrar faltantes y resolver con autorización si aplica.

**Alternativas y errores:**

- Nunca recibir más del pendiente.
- Daño recibido: segregar en destino.
- Faltante: sigue pendiente, no ajuste implícito.
- Repetir confirmación devuelve el resultado original.

## CU-011 — Recibir y evaluar devolución

**Actor:** Receptor y responsable farmacéutico.

**Precondiciones:** Despacho identificado y saldo retornable.

**Entrada/disparador:** Cantidad/lote devuelto y evidencia. **Postcondición:** Cuarentena y decisión documentada.

**Requisitos:** RF-024, RF-025.

**Flujo principal:**

1. Verificar relación con despacho original.
2. Registrar devolución física en cuarentena.
3. Evaluar condiciones y vigencia.
4. Liberar lo aprobado o mantener segregado para baja.

**Alternativas y errores:**

- Exceso acumulado: rechazar.
- Lote no coincide: investigar, sin acreditar utilizable.
- Vencido: no liberar.
- No asumir estado clínico desde datos de inventario.

## CU-012 — Contar y ajustar

**Actor:** Operador y aprobador distinto.

**Precondiciones:** Permisos, corte y ámbito definidos.

**Entrada/disparador:** Conteo, motivo y evidencia. **Postcondición:** Ajuste confirmado o rechazado.

**Requisitos:** RF-026, RF-027.

**Flujo principal:**

1. Registrar corte y cantidades físicas.
2. Comparar con saldo y proponer diferencia.
3. Otro usuario revisa evidencia y saldo vigente.
4. Autorizar compensación y registrar el vínculo.

**Alternativas y errores:**

- Autoaprobación: rechazar.
- Saldo cambió: revalidar diferencia, no aplicar delta obsoleto.
- Ajuste negativo excesivo: rechazar.

## CU-013 — Bloquear, liberar o retirar lote

**Actor:** Responsable farmacéutico/central.

**Precondiciones:** Permiso sobre alcance.

**Entrada/disparador:** Lote, motivo, evidencia y sedes afectadas. **Postcondición:** Elegibilidad restringida y seguimiento.

**Requisitos:** RF-028, RF-029.

**Flujo principal:**

1. Identificar lote y ámbito.
2. Registrar bloqueo.
3. Localizar saldo, tránsito y salidas previas.
4. Documentar acciones y eventual liberación permitida.

**Alternativas y errores:**

- Lote ya despachado: mantener historia y localizar, no borrar.
- Propuesta de despacho anterior: revalidar bloqueo.
- Vencido: no liberar para salida ordinaria.

## CU-014 — Registrar baja o compensación

**Actor:** Responsable autorizado.

**Precondiciones:** Documento original/conteo y autorización.

**Entrada/disparador:** Motivo, evidencia, cantidades y condición. **Postcondición:** Movimiento vinculado de salida o corrección.

**Requisitos:** RF-030, RF-031.

**Flujo principal:**

1. Seleccionar origen de la corrección.
2. Revisar efectos posteriores y elegibilidad de cantidades.
3. Autorizar y confirmar movimiento.
4. Conservar historia y evidencia de aprobación.

**Alternativas y errores:**

- No revertir recepción consumida creando negativos.
- No confundir baja informática con destrucción física.
- Reintento produce una sola compensación.

## CU-015 — Auditar, verificar y conciliar

**Actor:** Auditor.

**Precondiciones:** Permiso de lectura y referencia de verificación.

**Entrada/disparador:** Periodo, ámbito y cierre esperado. **Postcondición:** Informe de resultados y anomalías.

**Requisitos:** RF-032, RF-033, RF-039.

**Flujo principal:**

1. Recorrer operaciones y documentos.
2. Comparar saldos con movimientos y tránsito.
3. Verificar historial frente a referencia confiable.
4. Registrar alcance, limitaciones y anomalías.

**Alternativas y errores:**

- Referencia no disponible: resultado incompleto/no concluyente.
- Cadena reescrita sin referencia independiente no prueba integridad.
- No autocorregir discrepancias ni permitir al auditor editar stock.

## CU-016 — Consolidar y exportar

**Actor:** Responsable central o auditor.

**Precondiciones:** Permiso y fecha de corte.

**Entrada/disparador:** Filtros y ámbito. **Postcondición:** Reporte/exportación con corte y permisos.

**Requisitos:** RF-034, RF-035.

**Flujo principal:**

1. Seleccionar sedes permitidas y periodo.
2. Consolidar sin duplicar tránsito.
3. Mostrar filtros, unidades y corte.
4. Exportar el mismo conjunto autorizado.

**Alternativas y errores:**

- No sumar unidades incompatibles como stock único.
- Corte inconsistente: advertir o rechazar reporte, no presentar exactitud falsa.
- Sin permiso de sede: excluir antes de producir salida.

## Relación con historias de usuario

Las historias priorizadas están en la especificación Spec Kit y se prueban con
fixtures controladas de sus dependencias. No se necesita repetir un catálogo completo
de requisitos dentro de cada historia. El mantenimiento del producto requiere seguir
la relación historia → CU → RF → RN → CA de 15.
