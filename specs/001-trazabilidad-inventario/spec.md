# Feature Specification: Trazabilidad de inventario multisede

**Feature Branch**: `docs/analisis-inicial`

**Created**: 2026-10-15

**Status**: Draft — análisis para revisión; no autoriza implementación.

**Input**: Especificar MedStock para una cadena ampliable de clínicas, medicamentos
e insumos por lote, recepción, solicitudes internas, despacho FEFO, traslados,
devoluciones, ajustes, reservas explícitas, vencimientos, autorizaciones y auditoría verificable. Tres sedes son datos iniciales;
el objetivo de carga es 2 000 usuarios activos simultáneamente. Desarrollo individual.

## User Scenarios & Testing *(mandatory)*

Cada historia tiene una prueba aislable con datos preparados de sus dependencias;
esto no promete que se pueda desplegar sin identidad, catálogo o existencias válidas.
El [dossier](../analisis/00-indice-y-estado.md) contiene el análisis transversal.

### HU-001 — Recibir y conocer existencias confiables (Priority: P1)

Como operador de almacén autorizado quiero recibir productos por lote y consultar su condición para saber qué puede utilizar mi sede.

**Why this priority**: Entrega visibilidad y origen incluso sin el circuito completo de solicitudes.

**Independent Test**: Con catálogo, sede e identidad de ensayo, recibir dos lotes y consultar saldo/historial.

**Acceptance Scenarios**:

- [CA-007](../analisis/08-requisitos-funcionales.md): Registrar procedencias.
- [CA-008](../analisis/08-requisitos-funcionales.md): Preparar recepción.
- [CA-009](../analisis/08-requisitos-funcionales.md): Confirmar recepción.
- [CA-010](../analisis/08-requisitos-funcionales.md): Consultar existencias.
- [CA-011](../analisis/08-requisitos-funcionales.md): Consultar historial por lote.

- [CA-051](../analisis/08-requisitos-funcionales.md): Capturar precisión del vencimiento.

**Flujos:** CU-005, CU-006. Los criterios completos son canónicos en 08 y los casos en 10.

### HU-002 — Solicitar y despachar con FEFO (Priority: P1)

Como farmacia quiero atender demanda interna mediante lotes elegibles, conservando stock y remanentes aun con otras operaciones simultáneas.

**Why this priority**: Evita cantidades imposibles y entrega de lotes no elegibles.

**Independent Test**: Con lotes/solicitudes precargados, ejecutar selección, parcialidad, concurrencia y reintento.

**Acceptance Scenarios**:

- [CA-013](../analisis/08-requisitos-funcionales.md): Crear solicitud interna.
- [CA-014](../analisis/08-requisitos-funcionales.md): Consultar o cancelar solicitud.
- [CA-015](../analisis/08-requisitos-funcionales.md): Evaluar disponibilidad FEFO.
- [CA-016](../analisis/08-requisitos-funcionales.md): Confirmar despacho.
- [CA-017](../analisis/08-requisitos-funcionales.md): Atender parcialmente.
- [CA-018](../analisis/08-requisitos-funcionales.md): Recuperar resultado.
- [CA-019](../analisis/08-requisitos-funcionales.md): Emitir constancia de salida.

- [CA-041](../analisis/08-requisitos-funcionales.md): Registrar consentimiento de entrega parcial.
- [CA-042](../analisis/08-requisitos-funcionales.md): Continuar o cerrar remanentes.
- [CA-043](../analisis/08-requisitos-funcionales.md): Consultar seguimiento de parciales.

**Flujos:** CU-007, CU-008. Los criterios completos son canónicos en 08 y los casos en 10.

### HU-003 — Controlar ámbito y crecimiento (Priority: P1)

Como administrador quiero incorporar nuevas sedes y asignar acceso para ampliar la cadena sin mezclar inventarios.

**Why this priority**: El control por sede y la incorporación de establecimientos son condiciones del negocio.

**Independent Test**: Con tres sedes y usuarios precargados, agregar cuarta sede y ensayar accesos permitidos/denegados.

**Acceptance Scenarios**:

- [CA-001](../analisis/08-requisitos-funcionales.md): Acceder y cerrar sesión.
- [CA-002](../analisis/08-requisitos-funcionales.md): Administrar permisos.
- [CA-003](../analisis/08-requisitos-funcionales.md): Gestionar sedes.
- [CA-004](../analisis/08-requisitos-funcionales.md): Gestionar ubicaciones y servicios.
- [CA-005](../analisis/08-requisitos-funcionales.md): Gestionar catálogo.
- [CA-006](../analisis/08-requisitos-funcionales.md): Definir presentaciones.
- [CA-036](../analisis/08-requisitos-funcionales.md): Desactivar sin borrar.
- [CA-037](../analisis/08-requisitos-funcionales.md): Configurar políticas.
- [CA-038](../analisis/08-requisitos-funcionales.md): Auditar acceso y administración.
- [CA-040](../analisis/08-requisitos-funcionales.md): Mostrar errores y seguimiento.

**Flujos:** CU-001, CU-002, CU-003, CU-004. Los criterios completos son canónicos en 08 y los casos en 10.

### HU-004 — Bloquear y reconstruir un lote (Priority: P1)

Como responsable y auditor quiero impedir salidas de lotes afectados y reconstruir sus movimientos sin editar la historia.

**Why this priority**: La trazabilidad y elegibilidad son controles críticos, no un reporte decorativo.

**Independent Test**: Con movimientos y referencia de cierre de ensayo, bloquear un lote, verificar despacho y detectar alteración.

**Acceptance Scenarios**:

- [CA-028](../analisis/08-requisitos-funcionales.md): Bloquear y liberar lote.
- [CA-029](../analisis/08-requisitos-funcionales.md): Gestionar retiro de lote.
- [CA-032](../analisis/08-requisitos-funcionales.md): Consultar auditoría.
- [CA-033](../analisis/08-requisitos-funcionales.md): Verificar integridad.
- [CA-039](../analisis/08-requisitos-funcionales.md): Reconciliar inventario.

- [CA-052](../analisis/08-requisitos-funcionales.md): Versionar interpretación de fechas.
- [CA-054](../analisis/08-requisitos-funcionales.md): Revalidar fechas al comprometer stock.
- [CA-063](../analisis/08-requisitos-funcionales.md): Consultar decisión y evidencia operativa.

**Flujos:** CU-013, CU-015. Los criterios completos son canónicos en 08 y los casos en 10.

### HU-005 — Trasladar entre sedes (Priority: P2)

Como responsable logístico quiero expedir y recibir por lote, conservando tránsito y diferencias documentadas.

**Why this priority**: Permite operación de cadena sin duplicar stock.

**Independent Test**: Con un lote en origen, expedir ocho, recibir parcialmente y resolver la diferencia de ensayo.

**Acceptance Scenarios**:

- [CA-020](../analisis/08-requisitos-funcionales.md): Solicitar traslado.
- [CA-021](../analisis/08-requisitos-funcionales.md): Autorizar y expedir traslado.
- [CA-022](../analisis/08-requisitos-funcionales.md): Recibir traslado.
- [CA-023](../analisis/08-requisitos-funcionales.md): Resolver diferencia de traslado.

**Flujos:** CU-009, CU-010. Los criterios completos son canónicos en 08 y los casos en 10.

### HU-006 — Controlar retornos y correcciones (Priority: P2)

Como responsable quiero evaluar devoluciones, conteos y bajas sin borrar movimientos ni liberar productos inadecuados.

**Why this priority**: El circuito inverso evita que una corrección se convierta en stock ficticio.

**Independent Test**: Con despacho y conteo de ensayo, devolver a cuarentena, evaluar y autorizar compensación por otro usuario.

**Acceptance Scenarios**:

- [CA-024](../analisis/08-requisitos-funcionales.md): Registrar devolución.
- [CA-025](../analisis/08-requisitos-funcionales.md): Evaluar devolución.
- [CA-026](../analisis/08-requisitos-funcionales.md): Registrar conteo.
- [CA-027](../analisis/08-requisitos-funcionales.md): Autorizar ajuste.
- [CA-030](../analisis/08-requisitos-funcionales.md): Registrar baja.
- [CA-031](../analisis/08-requisitos-funcionales.md): Compensar error.

- [CA-059](../analisis/08-requisitos-funcionales.md): Documentar causas y conservación del retorno.
- [CA-060](../analisis/08-requisitos-funcionales.md): Controlar saldo retornable concurrente.
- [CA-061](../analisis/08-requisitos-funcionales.md): Evaluar retorno por línea.
- [CA-062](../analisis/08-requisitos-funcionales.md): Disponer retorno rechazado.

**Flujos:** CU-011, CU-012, CU-014. Los criterios completos son canónicos en 08 y los casos en 10.

### HU-007 — Supervisar la cadena (Priority: P2)

Como responsable central quiero consultar alertas y reportes por corte y ámbito para supervisar existencias y movimientos.

**Why this priority**: Hace visibles desequilibrios entre sedes sin requerir acceso clínico a pacientes.

**Independent Test**: Con historial precargado de varias sedes, comparar saldo consolidado y exportación autorizada.

**Acceptance Scenarios**:

- [CA-012](../analisis/08-requisitos-funcionales.md): Alertar stock y vencimiento.
- [CA-034](../analisis/08-requisitos-funcionales.md): Consolidar reportes.
- [CA-035](../analisis/08-requisitos-funcionales.md): Exportar resultados.

- [CA-053](../analisis/08-requisitos-funcionales.md): Identificar próximos vencimientos.

**Flujos:** CU-006, CU-016. Los criterios completos son canónicos en 08 y los casos en 10.

### HU-008 — Comprometer y consumir stock mediante reserva (Priority: P2)

Como farmacia quiero apartar cantidades por lote para una solicitud y liberar su remanente por tiempo o cancelación sin alterar el físico incorrectamente.

**Why this priority**: Permite compromisos explícitos y evita sobreasignación entre solicitantes.

**Independent Test**: Con treinta unidades de ensayo, reservar veinte, consumir cinco y cancelar quince; ensayar las carreras de creación/consumo/liberación.

**Acceptance Scenarios**:

- [CA-044](../analisis/08-requisitos-funcionales.md): Crear reserva explícita por lote.
- [CA-045](../analisis/08-requisitos-funcionales.md): Consultar libre y comprometido.
- [CA-046](../analisis/08-requisitos-funcionales.md): Cancelar y liberar reserva.
- [CA-047](../analisis/08-requisitos-funcionales.md): Expirar reserva por tiempo operativo.
- [CA-048](../analisis/08-requisitos-funcionales.md): Consumir reserva al despachar.
- [CA-049](../analisis/08-requisitos-funcionales.md): Invalidar reserva no elegible.
- [CA-050](../analisis/08-requisitos-funcionales.md): Auditar ciclo de reserva.
- [CA-064](../analisis/08-requisitos-funcionales.md): Conciliar compromisos y saldos físicos.

**Flujos:** CU-017, CU-015.

### HU-009 — Decidir autorizaciones sobre contenido vigente (Priority: P2)

Como responsable quiero aprobar o rechazar una operación concreta y asegurar que se ejecute solo sobre su contenido y ámbito válidos.

**Why this priority**: Evita autoaprobación y reutilización de decisiones sobre cantidades o lotes diferentes.

**Independent Test**: Con un ajuste propuesto, probar aprobación válida, cambio de contenido, revocación y rechazo sin efectos.

**Acceptance Scenarios**:

- [CA-055](../analisis/08-requisitos-funcionales.md): Solicitar autorización vinculada.
- [CA-056](../analisis/08-requisitos-funcionales.md): Aprobar o rechazar con alcance.
- [CA-057](../analisis/08-requisitos-funcionales.md): Exigir separación de funciones.
- [CA-058](../analisis/08-requisitos-funcionales.md): Invalidar aprobaciones desactualizadas.

**Flujos:** CU-019.

### Edge Cases

Concurrencia por últimas unidades; respuesta perdida; identidad repetida con contenido
diferente; fallo entre efectos; lote bloqueado o vencido tras consultar; empate FEFO;
traslado parcial con daño y faltante; devolución acumulada concurrente; compensación
sobre stock ya consumido; revocación de permisos; corte de reporte y truncado de
historial. Los resultados esperados están en CA-101 a CA-126 del
[plan de validación](../analisis/15-trazabilidad-y-validacion.md).

## Requirements *(mandatory)*

### Functional Requirements

La definición única de cada RF y su criterio está en el
[catálogo funcional](../analisis/08-requisitos-funcionales.md). Esta especificación
lo incorpora por referencia, evitando dos textos normativos divergentes.

| Historia | Requisitos canónicos |
| --- | --- |
| HU-001 | RF-007, RF-008, RF-009, RF-010, RF-011, RF-051 |
| HU-002 | RF-013, RF-014, RF-015, RF-016, RF-017, RF-018, RF-019, RF-041, RF-042, RF-043 |
| HU-003 | RF-001, RF-002, RF-003, RF-004, RF-005, RF-006, RF-036, RF-037, RF-038, RF-040 |
| HU-004 | RF-028, RF-029, RF-032, RF-033, RF-039, RF-052, RF-054, RF-063 |
| HU-005 | RF-020, RF-021, RF-022, RF-023 |
| HU-006 | RF-024, RF-025, RF-026, RF-027, RF-030, RF-031, RF-059, RF-060, RF-061, RF-062 |
| HU-007 | RF-012, RF-034, RF-035, RF-053 |
| HU-008 | RF-044, RF-045, RF-046, RF-047, RF-048, RF-049, RF-050, RF-064 |
| HU-009 | RF-055, RF-056, RF-057, RF-058 |

### Key Entities

Sede, ubicación, servicio, usuario/asignación, producto/presentación, lote/existencia,
recepción, solicitud/despacho, traslado, devolución, conteo/ajuste, bloqueo y
operación/movimiento/evento de auditoría, reserva/línea, aprobación y política temporal. Las relaciones y significados están en
el [modelo conceptual](../analisis/12-modelo-conceptual.md); no se fija almacenamiento.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: ningún ensayo especificado de concurrencia o reintento deja negativos,
  doble entrega ni movimientos confirmados incompletos.
- **SC-002**: en todos los casos de vencimiento/bloqueo se impide la salida del lote
  no elegible; las asignaciones cumplen el orden FEFO y explican cantidades.
- **SC-003**: agregar la cuarta sede no exige modificar el programa y conserva
  separación de permisos y saldos.
- **SC-004**: todos los movimientos de ensayo permiten reconstruir lote, documento,
  ámbito y autor; la verificación detecta los casos de alteración contra referencia.
- **SC-005**: evaluar un pico de 2 000 usuarios activos bajo el perfil candidato de 16;
  medir errores y tiempos por clase. Candidatos por validar: 95 % de consultas en
  500 ms y movimientos en 1 s, con menos de 1 % de errores técnicos y cero violaciones
  de inventario. No hay medición ni capacidad acreditada todavía.
- **SC-006**: cada uno de los 64 RF tiene criterio, regla, caso de uso y objetivo;
  las políticas aún abiertas se identifican, no se presentan como hechos aprobados.

- **SC-007**: en los escenarios de reserva no se excede el libre elegible ni se consume/libera dos veces; la vigencia se aplica incluso con limpieza retrasada.
- **SC-008**: una autorización no habilita otro contenido o sede; las devoluciones se evalúan por subcantidad con evidencia y sin aumento automático del disponible.

## Clarifications

### Sesión 2026-10-15

Alexander confirmó la inclusión de las cinco capacidades para implementación posterior.
Reservas pasa de evolución fuera de detalle a capacidad analizada en I3. Permanecen
propuestos duración, prioridad FEFO durante compromiso, interpretación temporal y
matriz final de autorizaciones. Scrum/Kanban se comparan como opciones de gestión,
sin alterar los requisitos clínico-logísticos ni declarar adopción automática.

## Assumptions

Una cadena; operación online; identidades y datos de ensayo; cantidades discretas;
solicitudes internas sin pacientes; recepción física revisada por responsable.
Las PP de [14](../analisis/14-supuestos-riesgos-y-pendientes.md) son defaults propuestos
para permitir revisión, no decisiones silenciosas. La normativa aplicable y el
perfil de carga exigen validación. La planificación de cada incremento se hará tras
cerrar sus pendientes críticos. No se requiere completar todo el producto para
revisar esta especificación base.
