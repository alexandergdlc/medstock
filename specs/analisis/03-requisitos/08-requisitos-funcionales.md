# Requisitos funcionales y aceptación principal

**Proyecto:** MedStock · **Versión:** 0.3.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Decisiones del propietario aceptadas; detalles operativos pendientes según 14.

## Convenciones del catálogo

Cada RF tiene un criterio principal CA con el mismo número; CA-101 y siguientes
amplían concurrencia y fallos en 15. P1/P2 indican prioridad. I1/I2/I3 son incrementos
propuestos, no autorizaciones de implementación. El origen general es FU-001
(acuerdos de Alexander); las reglas enlazadas indican cualquier política PP pendiente.
La inclusión de las cinco capacidades fue confirmada por Alexander. Los valores
operativos de detalle y su aplicación profesional siguen sujetos a validación.
RF-041 a RF-064 especializan las capacidades generales sin renumerar RF existentes.
La correspondencia padre/especialización se registra en 18; no representa duplicar
implementaciones ni contar dos veces el mismo valor de negocio.

| ID | Capacidad | Prioridad | Incremento | Actor | CU |
| --- | --- | --- | --- | --- | --- |
| RF-001 | Acceder y cerrar sesión | P1 | I1 | Usuario | CU-001 |
| RF-002 | Administrar permisos | P1 | I1 | Administrador | CU-002 |
| RF-003 | Gestionar sedes | P1 | I1 | Administrador | CU-003 |
| RF-004 | Gestionar ubicaciones y servicios | P1 | I1 | Responsable de sede | CU-003 |
| RF-005 | Gestionar catálogo | P1 | I1 | Gestor de catálogo | CU-004 |
| RF-006 | Definir presentaciones | P1 | I1 | Gestor de catálogo | CU-004 |
| RF-007 | Registrar procedencias | P1 | I1 | Almacenero | CU-005 |
| RF-008 | Preparar recepción | P1 | I1 | Almacenero | CU-005 |
| RF-009 | Confirmar recepción | P1 | I1 | Almacenero autorizado | CU-005 |
| RF-010 | Consultar existencias | P1 | I1 | Usuario autorizado | CU-006 |
| RF-011 | Consultar historial por lote | P1 | I1 | Auditor o farmacia | CU-006 |
| RF-012 | Alertar stock y vencimiento | P2 | I3 | Farmacia | CU-006 |
| RF-013 | Crear solicitud interna | P1 | I2 | Solicitante | CU-007 |
| RF-014 | Consultar o cancelar solicitud | P1 | I2 | Solicitante | CU-007 |
| RF-015 | Evaluar disponibilidad FEFO | P1 | I2 | Farmacia | CU-008 |
| RF-016 | Confirmar despacho | P1 | I2 | Farmacia | CU-008 |
| RF-017 | Atender parcialmente | P1 | I2 | Farmacia | CU-008 |
| RF-018 | Recuperar resultado | P1 | I2 | Usuario que opera | CU-008 |
| RF-019 | Emitir constancia de salida | P1 | I2 | Farmacia | CU-008 |
| RF-020 | Solicitar traslado | P2 | I3 | Responsable de sede | CU-009 |
| RF-021 | Autorizar y expedir traslado | P2 | I3 | Responsable de origen | CU-009 |
| RF-022 | Recibir traslado | P2 | I3 | Receptor de destino | CU-010 |
| RF-023 | Resolver diferencia de traslado | P2 | I3 | Responsable autorizado | CU-010 |
| RF-024 | Registrar devolución | P2 | I3 | Receptor de farmacia | CU-011 |
| RF-025 | Evaluar devolución | P2 | I3 | Responsable farmacéutico | CU-011 |
| RF-026 | Registrar conteo | P2 | I3 | Almacenero | CU-012 |
| RF-027 | Autorizar ajuste | P2 | I3 | Responsable autorizado | CU-012 |
| RF-028 | Bloquear y liberar lote | P1 | I1 | Responsable farmacéutico | CU-013 |
| RF-029 | Gestionar retiro de lote | P2 | I3 | Responsable central | CU-013 |
| RF-030 | Registrar baja | P2 | I3 | Responsable autorizado | CU-014 |
| RF-031 | Compensar error | P2 | I3 | Responsable autorizado | CU-014 |
| RF-032 | Consultar auditoría | P1 | I1 | Auditor | CU-015 |
| RF-033 | Verificar integridad | P1 | I2 | Auditor | CU-015 |
| RF-034 | Consolidar reportes | P2 | I3 | Responsable central | CU-016 |
| RF-035 | Exportar resultados | P2 | I3 | Auditor o responsable | CU-016 |
| RF-036 | Desactivar sin borrar | P1 | I1 | Administrador autorizado | CU-003 |
| RF-037 | Configurar políticas | P2 | I3 | Responsable central | CU-004 |
| RF-038 | Auditar acceso y administración | P1 | I1 | Administrador y auditor | CU-002 |
| RF-039 | Reconciliar inventario | P1 | I2 | Auditor o responsable | CU-015 |
| RF-040 | Mostrar errores y seguimiento | P1 | I1 | Usuario | CU-001 |
| RF-041 | Registrar consentimiento de entrega parcial | P1 | I2 | Farmacia | CU-008 |
| RF-042 | Continuar o cerrar remanentes | P1 | I2 | Solicitante y farmacia | CU-007 |
| RF-043 | Consultar seguimiento de parciales | P1 | I2 | Solicitante | CU-007 |
| RF-044 | Crear reserva explícita por lote | P2 | I3 | Farmacia autorizada | CU-017 |
| RF-045 | Consultar libre y comprometido | P2 | I3 | Usuario autorizado | CU-017 |
| RF-046 | Cancelar y liberar reserva | P2 | I3 | Farmacia autorizada | CU-017 |
| RF-047 | Expirar reserva por tiempo operativo | P2 | I3 | Farmacia con vencimiento temporal automático | CU-017 |
| RF-048 | Consumir reserva al despachar | P2 | I3 | Farmacia | CU-017 |
| RF-049 | Invalidar reserva no elegible | P2 | I3 | Responsable farmacéutico | CU-017 |
| RF-050 | Auditar ciclo de reserva | P2 | I3 | Auditor y farmacia | CU-017 |
| RF-051 | Capturar precisión del vencimiento | P1 | I1 | Almacenero | CU-018 |
| RF-052 | Versionar interpretación de fechas | P1 | I1 | Responsable farmacéutico | CU-018 |
| RF-053 | Identificar próximos vencimientos | P2 | I3 | Responsable de farmacia | CU-018 |
| RF-054 | Revalidar fechas al comprometer stock | P1 | I2 | Farmacia | CU-018 |
| RF-055 | Solicitar autorización vinculada | P2 | I3 | Operador habilitado | CU-019 |
| RF-056 | Aprobar o rechazar con alcance | P2 | I3 | Responsable autorizado | CU-019 |
| RF-057 | Exigir separación de funciones | P2 | I3 | Responsable autorizado | CU-019 |
| RF-058 | Invalidar aprobaciones desactualizadas | P2 | I3 | Responsable y operador | CU-019 |
| RF-059 | Documentar causas y conservación del retorno | P2 | I3 | Receptor de farmacia | CU-011 |
| RF-060 | Controlar saldo retornable concurrente | P2 | I3 | Receptor de farmacia | CU-011 |
| RF-061 | Evaluar retorno por línea | P2 | I3 | Responsable farmacéutico | CU-011 |
| RF-062 | Disponer retorno rechazado | P2 | I3 | Responsable autorizado | CU-014 |
| RF-063 | Consultar decisión y evidencia operativa | P2 | I3 | Auditor | CU-015 |
| RF-064 | Conciliar compromisos y saldos físicos | P2 | I3 | Auditor o responsable | CU-015 |
| RF-065 | Configurar la red de custodia | P1 | I1 | Administrador | CU-003 |
| RF-066 | Autorizar cantidades de solicitud | P1 | I2 | Farmacia o responsable facultado | CU-019 |
| RF-067 | Analizar cobertura y riesgo de merma | P2 | I3 | Responsable de farmacia o cadena | CU-020 |
| RF-068 | Evaluar redistribución preventiva | P2 | I3 | Responsable de cadena | CU-020 |

## RF-001 — Acceder y cerrar sesión

**Actor:** Usuario. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-004. **Caso:** CU-001. **Reglas:** RN-002.

El sistema debe: Identificar usuarios y permitir cierre de sesión, sin aceptar acceso anónimo a inventario.

**CA-001 — Aceptación principal:** Dadas credenciales inválidas, el acceso falla sin mostrar existencias; al cerrar sesión no se admiten nuevas operaciones protegidas con esa sesión.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-002 — Administrar permisos

**Actor:** Administrador. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-004. **Caso:** CU-002. **Reglas:** RN-002, RN-029.

El sistema debe: Asignar y revocar roles por sede a usuarios activos, registrando quién cambió el permiso.

**CA-002 — Aceptación principal:** Revocado el permiso de una sede, la siguiente operación protegida en esa sede se rechaza y el cambio queda auditado.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-003 — Gestionar sedes

**Actor:** Administrador. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-001. **Caso:** CU-003. **Reglas:** RN-001, RN-026.

El sistema debe: Registrar, modificar y desactivar establecimientos mediante configuración y código único.

**CA-003 — Aceptación principal:** Con tres sedes existentes se registra una cuarta con otro código, sin cambiar ni desplegar el programa.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-004 — Gestionar ubicaciones y servicios

**Actor:** Responsable de sede. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-001. **Caso:** CU-003. **Reglas:** RN-001, RN-002.

El sistema debe: Registrar almacenes, farmacias y servicios solicitantes, vinculados a una sede.

**CA-004 — Aceptación principal:** Una ubicación de la sede A no puede utilizarse como ubicación de salida de la sede B.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-005 — Gestionar catálogo

**Actor:** Gestor de catálogo. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-002. **Caso:** CU-004. **Reglas:** RN-003, RN-026.

El sistema debe: Registrar productos con tipo, descripción, unidad base, fabricante y datos de identificación pertinentes.

**CA-005 — Aceptación principal:** Desactivar un producto con movimientos impide nuevas operaciones ordinarias sin eliminar sus registros históricos.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-006 — Definir presentaciones

**Actor:** Gestor de catálogo. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-002. **Caso:** CU-004. **Reglas:** RN-004, RN-005.

El sistema debe: Registrar factores positivos de conversión a unidad base y conservar el factor aplicado en cada movimiento.

**CA-006 — Aceptación principal:** Dos cajas de veinte unidades generan cuarenta unidades base; cambiar después la presentación no altera el movimiento anterior.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-007 — Registrar procedencias

**Actor:** Almacenero. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-005. **Reglas:** RN-007.

El sistema debe: Registrar proveedor o procedencia y referencia documental para una recepción.

**CA-007 — Aceptación principal:** No se confirma recepción sin procedencia identificable y documento con número o referencia controlada.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-008 — Preparar recepción

**Actor:** Almacenero. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-005. **Reglas:** RN-006, RN-007, RN-009.

El sistema debe: Capturar líneas recibidas, presentación, cantidad base, lote, fecha y evaluación inicial.

**CA-008 — Aceptación principal:** Una línea con cantidad cero o lote contradictorio queda sin confirmar y muestra la causa.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-009 — Confirmar recepción

**Actor:** Almacenero autorizado. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-005. **Reglas:** RN-007, RN-012, RN-014.

El sistema debe: Confirmar recepción y clasificar cantidades utilizables u observadas de forma trazable.

**CA-009 — Aceptación principal:** Confirmar dos veces la misma recepción produce una sola entrada y un único resultado de operación.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-010 — Consultar existencias

**Actor:** Usuario autorizado. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-002. **Caso:** CU-006. **Reglas:** RN-002, RN-008.

El sistema debe: Consultar saldos por sede, ubicación, producto, lote y condición, distinguiendo disponible y no disponible.

**CA-010 — Aceptación principal:** Cinco unidades en cuarentena aparecen separadas y no aumentan el saldo despachable.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-011 — Consultar historial por lote

**Actor:** Auditor o farmacia. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-006. **Reglas:** RN-024, RN-033.

El sistema debe: Reconstruir las entradas, salidas y ubicaciones de un lote con documento y responsable.

**CA-011 — Aceptación principal:** Un lote trasladado conserva enlaces entre recepción original, salida de traslado y recepción de destino.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-012 — Alertar stock y vencimiento

**Actor:** Farmacia. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-006. **Reglas:** RN-009, RN-030.

El sistema debe: Mostrar alertas según umbrales configurados, sin crear operaciones de inventario.

**CA-012 — Aceptación principal:** Al cruzarse un umbral aparece la alerta con sede, producto o lote y fecha de corte; el saldo no cambia.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-013 — Crear solicitud interna

**Actor:** Solicitante. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-007. **Reglas:** RN-017, RN-027, RN-016, RN-044.

El sistema debe: Preparar y enviar cantidades requeridas por un servicio y sede, sin datos clínicos personales.

**CA-013 — Aceptación principal:** Enviar una solicitud válida crea un número de seguimiento y mantiene intacto el stock.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-014 — Consultar o cancelar solicitud

**Actor:** Solicitante. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-007. **Reglas:** RN-015, RN-017, RN-044.

El sistema debe: Consultar estado y cancelar solo las cantidades pendientes permitidas por su estado.

**CA-014 — Aceptación principal:** Después de una entrega parcial se puede cancelar el remanente; las unidades entregadas y sus movimientos se conservan.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-015 — Evaluar disponibilidad FEFO

**Actor:** Farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-008. **Reglas:** RN-008, RN-009, RN-010, RN-011, RN-032, RN-044.

El sistema debe: Proponer asignación de lotes elegibles para una solicitud, con cantidades y faltantes.

**CA-015 — Aceptación principal:** Con lotes elegibles de diez unidades que vencen en distinto orden, solicitar doce propone diez del primero y dos del siguiente.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-016 — Confirmar despacho

**Actor:** Farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-008. **Reglas:** RN-011, RN-012, RN-013, RN-014, RN-044.

El sistema debe: Confirmar la salida por lote, descontar stock y registrar documento, resultado y auditoría coherentes.

**CA-016 — Aceptación principal:** Dos solicitudes de siete unidades compiten por diez; solo una completa siete y ninguna deja saldo negativo.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-017 — Atender parcialmente

**Actor:** Farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-008. **Reglas:** RN-015, RN-044.

El sistema debe: Permitir atención parcial solo con aceptación explícita y conservar el remanente.

**CA-017 — Aceptación principal:** Solicitar doce con diez disponibles no descuenta nada sin aceptar parcial; al aceptarla entrega diez y mantiene dos pendientes.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-018 — Recuperar resultado

**Actor:** Usuario que opera. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-003. **Caso:** CU-008. **Reglas:** RN-014, RN-034.

El sistema debe: Consultar el resultado de una operación incierta y reconocer reintentos con la misma identidad.

**CA-018 — Aceptación principal:** Tras perderse una respuesta posterior a confirmar, consultar o reenviar la misma operación devuelve su despacho sin otro descuento.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-019 — Emitir constancia de salida

**Actor:** Farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-003. **Caso:** CU-008. **Reglas:** RN-024, RN-035, RN-036.

El sistema debe: Mostrar constancia de despacho con solicitud, servicio, responsables, lotes y cantidades.

**CA-019 — Aceptación principal:** La constancia coincide con las líneas confirmadas y no afirma administración de medicamentos a pacientes.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-020 — Solicitar traslado

**Actor:** Responsable de sede. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-001. **Caso:** CU-009. **Reglas:** RN-018.

El sistema debe: Crear solicitud entre ubicaciones de custodia distintas, dentro de una sede o entre establecimientos, con productos y cantidades. Incluye central a sede y almacén de sede a farmacia; no confundir con salida final a servicio.

**CA-020 — Aceptación principal:** Origen igual a destino se rechaza; enviar la solicitud de traslado no cambia saldos.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-021 — Autorizar y expedir traslado

**Actor:** Responsable de origen. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-001. **Caso:** CU-009. **Reglas:** RN-010, RN-012, RN-014, RN-018.

El sistema debe: Autorizar y confirmar salida con detalle por lote y existencia en tránsito.

**CA-021 — Aceptación principal:** Expedir ocho unidades reduce ocho del origen y aumenta ocho en tránsito, sin acreditar todavía al destino.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-022 — Recibir traslado

**Actor:** Receptor de destino. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-001. **Caso:** CU-010. **Reglas:** RN-014, RN-018, RN-019.

El sistema debe: Recibir cantidades por lote y registrar aceptación, observaciones y diferencias.

**CA-022 — Aceptación principal:** De ocho en tránsito se aceptan seis y se observan dos recibidas: tránsito queda en cero, seis utilizables y dos segregadas; no se crean diez unidades.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-023 — Resolver diferencia de traslado

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-010. **Reglas:** RN-019, RN-021, RN-031.

El sistema debe: Cerrar diferencias mediante evidencia y movimiento autorizado cuando corresponda.

**CA-023 — Aceptación principal:** Un faltante de dos no se elimina del tránsito mediante editar el documento; se resuelve con constancia y movimiento vinculado.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-024 — Registrar devolución

**Actor:** Receptor de farmacia. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-011. **Reglas:** RN-020.

El sistema debe: Registrar unidades devueltas contra un despacho y ubicarlas en cuarentena.

**CA-024 — Aceptación principal:** De una entrega de cinco con dos ya devueltas, intentar devolver otras cuatro se rechaza.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-025 — Evaluar devolución

**Actor:** Responsable farmacéutico. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-011. **Reglas:** RN-008, RN-020, RN-022.

El sistema debe: Liberar o rechazar devolución con evaluación documentada y verificación de lote.

**CA-025 — Aceptación principal:** Un producto devuelto y vencido no pasa a utilizable aunque su envase aparente estar íntegro.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-026 — Registrar conteo

**Actor:** Almacenero. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-012. **Reglas:** RN-021, RN-031.

El sistema debe: Registrar conteo físico y diferencias contra un corte identificable, sin cambiar saldos directamente.

**CA-026 — Aceptación principal:** Una diferencia de menos tres genera propuesta de ajuste con referencia al conteo; el saldo aún no cambia.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-027 — Autorizar ajuste

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-012. **Reglas:** RN-013, RN-021, RN-023.

El sistema debe: Aprobar o rechazar ajuste; al aprobar, aplicar compensación sin borrar historial.

**CA-027 — Aceptación principal:** El creador no aprueba su ajuste; un ajuste aprobado que dejaría stock negativo se rechaza sin efectos.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-028 — Bloquear y liberar lote

**Actor:** Responsable farmacéutico. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-002. **Caso:** CU-013. **Reglas:** RN-011, RN-022.

El sistema debe: Bloquear lotes por alcance y motivo, y liberar solo con permiso y evidencia.

**CA-028 — Aceptación principal:** Un lote bloqueado después de una propuesta FEFO queda excluido en la confirmación y se recalcula o rechaza el despacho.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-029 — Gestionar retiro de lote

**Actor:** Responsable central. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-013. **Reglas:** RN-022, RN-024.

El sistema debe: Identificar ubicaciones y movimientos afectados por retiro, registrar seguimiento y segregación.

**CA-029 — Aceptación principal:** Una búsqueda de retiro informa las sedes con saldo, tránsito y despachos previos del lote en el ámbito autorizado.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-030 — Registrar baja

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-014. **Reglas:** RN-021, RN-022, RN-023.

El sistema debe: Registrar salida por vencimiento, daño o retiro con autorización y documento.

**CA-030 — Aceptación principal:** La baja descuenta la condición segregada correspondiente; conserva el motivo y no certifica destrucción física.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-031 — Compensar error

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-014. **Reglas:** RN-013, RN-020, RN-023.

El sistema debe: Corregir una operación confirmada mediante compensación vinculada tras verificar movimientos posteriores.

**CA-031 — Aceptación principal:** Una recepción cuyas unidades ya fueron despachadas no se revierte de forma ciega generando negativos.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-032 — Consultar auditoría

**Actor:** Auditor. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-015. **Reglas:** RN-024, RN-033.

El sistema debe: Buscar eventos por autor, sede, operación, documento, lote y periodo con permisos de lectura.

**CA-032 — Aceptación principal:** El auditor consulta el evento y sus vínculos, pero no puede editar la cantidad ni borrar el evento.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-033 — Verificar integridad

**Actor:** Auditor. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-003. **Caso:** CU-015. **Reglas:** RN-025.

El sistema debe: Verificar cadena de auditoría y declarar alcance, referencia, resultado y primer punto de anomalía.

**CA-033 — Aceptación principal:** Alterar o quitar un evento de una copia de prueba causa resultado de anomalía; una copia truncada se contrasta con la referencia de cierre esperada.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-034 — Consolidar reportes

**Actor:** Responsable central. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-001. **Caso:** CU-016. **Reglas:** RN-031, RN-033.

El sistema debe: Consolidar existencias, vencimientos y movimientos con filtros y fecha de corte coherentes.

**CA-034 — Aceptación principal:** Un traslado interno conserva el total de cadena contando tránsito una sola vez.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-035 — Exportar resultados

**Actor:** Auditor o responsable. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-016. **Reglas:** RN-002, RN-033.

El sistema debe: Exportar resultados autorizados con filtros y corte identificados, sin información personal de pacientes.

**CA-035 — Aceptación principal:** El archivo contiene solo sedes permitidas y conserva el mismo corte del reporte solicitado.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-036 — Desactivar sin borrar

**Actor:** Administrador autorizado. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-003. **Reglas:** RN-026.

El sistema debe: Desactivar entidades conservando historial y bloquear cierre operativo con pendientes.

**CA-036 — Aceptación principal:** Una sede con dos unidades o un traslado pendiente no queda cerrada hasta resolverlos.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-037 — Configurar políticas

**Actor:** Responsable central. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-004. **Reglas:** RN-028, RN-030.

El sistema debe: Cambiar umbrales autorizados y parámetros operativos con registro de versión y efecto futuro.

**CA-037 — Aceptación principal:** Cambiar el umbral de vencimiento no modifica fechas de lote ni movimientos confirmados.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-038 — Auditar acceso y administración

**Actor:** Administrador y auditor. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-004. **Caso:** CU-002. **Reglas:** RN-024, RN-025, RN-029.

El sistema debe: Registrar cambios de roles y eventos de acceso relevantes sin conservar contraseñas ni tokens.

**CA-038 — Aceptación principal:** Una asignación de privilegios queda vinculada a su autor y fecha; el registro no muestra secretos.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-039 — Reconciliar inventario

**Actor:** Auditor o responsable. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-003. **Caso:** CU-015. **Reglas:** RN-012, RN-031.

El sistema debe: Comparar balances y movimientos, incluyendo tránsito y compensaciones, y señalar discrepancias.

**CA-039 — Aceptación principal:** Una diferencia introducida en una copia de ensayo se informa sin autocorregir ni ocultar la discrepancia.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-040 — Mostrar errores y seguimiento

**Actor:** Usuario. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-006. **Caso:** CU-001. **Reglas:** RN-014, RN-034.

El sistema debe: Informar causas de rechazo y referencia de seguimiento, diferenciando rechazo y resultado incierto.

**CA-040 — Aceptación principal:** Una respuesta perdida no se presenta como operación cancelada; se indica consultar el resultado original.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-041 — Registrar consentimiento de entrega parcial

**Actor:** Farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-008. **Reglas:** RN-015, RN-024, RN-044.

El sistema debe: Registrar la aceptación explícita de cantidad parcial, actor, fecha y remanente antes de confirmar esa salida.

**CA-041 — Aceptación principal:** Dadas veinte unidades solicitadas y autorizadas, y doce disponibles, sin aceptación no hay salida; con aceptación quedan doce entregadas y ocho pendientes, con responsable identificado.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-042 — Continuar o cerrar remanentes

**Actor:** Solicitante y farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-007. **Reglas:** RN-015, RN-017, RN-044.

El sistema debe: Permitir nuevas entregas contra el remanente y su cancelación explícita, conservando las entregas anteriores.

**CA-042 — Aceptación principal:** De veinte solicitadas y autorizadas y doce entregadas, entregar cinco más deja tres pendientes; cancelar esas tres deja una solicitud cerrada parcialmente, no una entrega de veinte.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-043 — Consultar seguimiento de parciales

**Actor:** Solicitante. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-006. **Caso:** CU-007. **Reglas:** RN-015, RN-033, RN-044.

El sistema debe: Mostrar por línea solicitado, por decidir, rechazado, autorizado, entregado, cancelado antes/después de autorizar, pendiente autorizado y reserva vigente. Identificar urgencia y avisar al responsable si queda saldo urgente; la reserva no reduce otra vez el pendiente.

**CA-043 — Aceptación principal:** Una solicitud con veinte solicitadas y autorizadas, doce entregadas, dos canceladas y cuatro reservadas muestra seis pendientes, cuatro de ellos comprometidos; no resta la reserva otra vez del pendiente.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-044 — Crear reserva explícita por lote

**Actor:** Farmacia autorizada. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-017. **Reglas:** RN-016, RN-037, RN-038, RN-014, RN-044.

El sistema debe: Apartar cantidades contra el saldo de una solicitud autorizada y vigente mediante una operación explícita, asignación FEFO, vigencia finita y registro de resultado. Enviar una solicitud por sí solo no reserva.

**CA-044 — Aceptación principal:** Con solicitud autorizada por veinte, treinta unidades utilizables elegibles y sin reservas, reservar veinte deja físico treinta, reservado veinte y libre diez; el reintento de esa reserva no aparta otras veinte.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-045 — Consultar libre y comprometido

**Actor:** Usuario autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-017. **Reglas:** RN-037, RN-033.

El sistema debe: Separar existencias físicas, utilizables elegibles, reservas vigentes y libre para nuevas asignaciones, con corte y ámbito.

**CA-045 — Aceptación principal:** Con treinta elegibles y veinte reservadas vigentes se muestran diez libres; una reserva cancelada no continúa reduciendo el libre.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-046 — Cancelar y liberar reserva

**Actor:** Farmacia autorizada. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-017. **Reglas:** RN-014, RN-037, RN-039.

El sistema debe: Cancelar el remanente de una reserva y liberar solo la cantidad comprometida no consumida; conservar motivo y vínculo.

**CA-046 — Aceptación principal:** De veinte reservadas y cinco consumidas, cancelar libera quince, sin reingresar físicamente cinco ya entregadas ni alterar el físico por cancelar.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-047 — Expirar reserva por tiempo operativo

**Actor:** Farmacia con vencimiento temporal automático. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-017. **Reglas:** RN-028, RN-039.

El sistema debe: Hacer ineficaz una reserva al alcanzar su instante de fin y comprobarlo al consultar y confirmar, aunque el proceso de limpieza llegue después.

**CA-047 — Aceptación principal:** Para una reserva cuyo fin es T, al operar en T o después ya no se permite consumirla ni mantiene compromiso efectivo; la hora enviada por el navegador no modifica T.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-048 — Consumir reserva al despachar

**Actor:** Farmacia. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-017. **Reglas:** RN-012, RN-013, RN-038, RN-042, RN-044.

El sistema debe: Usar una reserva vigente de la solicitud para confirmar entrega, descontando físico y compromiso por la misma cantidad en una unidad de negocio.

**CA-048 — Aceptación principal:** De treinta físicas elegibles y veinte reservadas, consumir cinco deja físico veinticinco, reservado quince y libre diez; no se descuenta dos veces ni se consume reserva ajena.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-049 — Invalidar reserva no elegible

**Actor:** Responsable farmacéutico. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-017. **Reglas:** RN-008, RN-022, RN-039.

El sistema debe: Impedir el consumo de cantidades reservadas afectadas por bloqueo, vencimiento, cancelación de solicitud o restricción de ámbito.

**CA-049 — Aceptación principal:** Bloqueado un lote de diez con seis reservadas, las seis dejan de ser consumibles, pero no aparecen diez libres: el lote completo continúa no elegible.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-050 — Auditar ciclo de reserva

**Actor:** Auditor y farmacia. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-017. **Reglas:** RN-024, RN-039, RN-042.

El sistema debe: Consultar creación, consumo, cancelación, expiración e invalidación de una reserva sin tratarlas como entradas o salidas físicas ficticias.

**CA-050 — Aceptación principal:** El historial de una reserva consumida en parte muestra cantidades y resultados recuperables; crear o expirar no genera una recepción física.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-051 — Capturar precisión del vencimiento

**Actor:** Almacenero. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-002. **Caso:** CU-018. **Reglas:** RN-006, RN-009.

El sistema debe: Conservar valor declarado y precisión día o mes/año del vencimiento y rechazar formatos inválidos o interpretaciones no aprobadas.

**CA-051 — Aceptación principal:** Un rótulo 05/2027 se conserva como mes/año; no se transforma silenciosamente en 01/05/2027 ni se habilita para despacho sin política aplicable.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-052 — Versionar interpretación de fechas

**Actor:** Responsable farmacéutico. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-002. **Caso:** CU-018. **Reglas:** RN-009, RN-028, RN-040.

El sistema debe: Registrar política de interpretación, zona operativa, aprobador, vigencia y evidencia; revisar lotes afectados al cambiarla, conservando decisiones históricas.

**CA-052 — Aceptación principal:** Una política nueva no cambia silenciosamente la interpretación de una entrega ya confirmada; su efecto futuro y revisión de lotes quedan identificados.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-053 — Identificar próximos vencimientos

**Actor:** Responsable de farmacia. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-018. **Reglas:** RN-009, RN-030.

El sistema debe: Configurar y consultar alertas por proximidad a vencimiento, con umbral aplicable, fecha de corte y stock afectado.

**CA-053 — Aceptación principal:** Con umbral de ensayo de treinta días, un lote a veinte aparece en la alerta; una alerta por proximidad no lo declara vencido automáticamente.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-054 — Revalidar fechas al comprometer stock

**Actor:** Farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-018. **Reglas:** RN-009, RN-011, RN-038.

El sistema debe: Comprobar elegibilidad temporal tanto al reservar como al confirmar salida; no confiar en una consulta o reserva antigua.

**CA-054 — Aceptación principal:** Si el lote deja de ser elegible después de mostrarlo y antes de confirmar, no se reserva ni se despacha aunque su pantalla o reserva previa indique unidades.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-055 — Solicitar autorización vinculada

**Actor:** Operador habilitado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-004. **Caso:** CU-019. **Reglas:** RN-021, RN-029, RN-040, RN-044.

El sistema debe: Presentar para los tipos configurados una solicitud de aprobación vinculada a cantidades, lotes, motivo, evidencia y versión del documento.

**CA-055 — Aceptación principal:** La aprobación solicitada para un ajuste de menos dos identifica ese contenido; no es una aprobación genérica reutilizable para cualquier operación.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-056 — Aprobar o rechazar con alcance

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-004. **Caso:** CU-019. **Reglas:** RN-002, RN-021, RN-040, RN-044.

El sistema debe: Registrar decisión, autor, fecha y razón según tipo y ámbito, sin que aprobar ejecute por sí solo movimientos reservados para otra confirmación.

**CA-056 — Aceptación principal:** Un responsable de A no aprueba un ajuste de B; un rechazo conserva solicitud y causa sin aplicar el ajuste.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-057 — Exigir separación de funciones

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-004. **Caso:** CU-019. **Reglas:** RN-021, RN-029.

El sistema debe: Impedir que quien propone un ajuste o baja se otorgue la aprobación de ese mismo documento, incluso si reúne varios roles.

**CA-057 — Aceptación principal:** El creador con rol adicional de aprobador sigue sin poder aprobar su propio ajuste; otra identidad autorizada sí puede revisarlo.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-058 — Invalidar aprobaciones desactualizadas

**Actor:** Responsable y operador. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-004. **Caso:** CU-019. **Reglas:** RN-011, RN-040, RN-044.

El sistema debe: Exigir nueva revisión si cambia el contenido aprobado y revalidar permisos y condiciones antes de ejecutar. Una aprobación no omite controles actuales de stock.

**CA-058 — Aceptación principal:** Cambiar cantidad de menos dos a menos tres invalida la decisión previa; aunque no cambie cantidad, si el saldo ya no alcanza, la ejecución se rechaza.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-059 — Documentar causas y conservación del retorno

**Actor:** Receptor de farmacia. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-011. **Reglas:** RN-020, RN-041.

El sistema debe: Registrar causa, despacho y lote de origen, cantidades, evidencia de conservación y ubicación segregada de cada retorno.

**CA-059 — Aceptación principal:** Una devolución con referencia y cantidad pero sin causa/evidencia requerida queda sin liberar; se registra lo faltante para evaluación.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-060 — Controlar saldo retornable concurrente

**Actor:** Receptor de farmacia. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-011. **Reglas:** RN-013, RN-014, RN-020.

El sistema debe: Comprobar acumulado retornado por línea y lote de origen al confirmar cada devolución concurrente o reintento.

**CA-060 — Aceptación principal:** Para cinco entregadas y dos ya devueltas, dos devoluciones concurrentes de dos no pueden dejar seis retornadas acumuladas.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-061 — Evaluar retorno por línea

**Actor:** Responsable farmacéutico. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-011. **Reglas:** RN-008, RN-020, RN-041.

El sistema debe: Decidir por línea o subcantidad si se libera, rechaza o mantiene en evaluación, con evidencia y responsable; conservar el remanente evaluable.

**CA-061 — Aceptación principal:** De seis recibidas en cuarentena, liberar dos y rechazar una deja tres en evaluación; no se liberan automáticamente las seis.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-062 — Disponer retorno rechazado

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-014. **Reglas:** RN-021, RN-023, RN-041.

El sistema debe: Vincular devolución rechazada con baja, retorno a proveedor u otra disposición autorizada y conservar la evidencia de salida.

**CA-062 — Aceptación principal:** Una unidad rechazada continúa segregada hasta confirmar su disposición; cambiar una etiqueta no la elimina del balance físico.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-063 — Consultar decisión y evidencia operativa

**Actor:** Auditor. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-015. **Reglas:** RN-024, RN-033, RN-040, RN-041.

El sistema debe: Reconstruir decisiones de parcialidad, fechas, autorizaciones y devoluciones con versión, evidencia y ámbito.

**CA-063 — Aceptación principal:** El auditor puede enlazar liberación de dos unidades a evaluación y retorno de origen, sin editar la decisión ni acceder a otras sedes.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-064 — Conciliar compromisos y saldos físicos

**Actor:** Auditor o responsable. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-015. **Reglas:** RN-031, RN-037, RN-042.

El sistema debe: Contrastar cantidades físicas, elegibles, compromisos vigentes y consumos de reservas, detectando diferencias sin autocorrección.

**CA-064 — Aceptación principal:** Una reserva expirada no reduce el libre efectivo; una cantidad consumida ya es salida física y no permanece también como compromiso activo.

**Origen y estado:** FU-001; capacidad incluida, criterios de detalle sujetos a las PP relacionadas.

## RF-065 — Configurar la red de custodia

**Actor:** Administrador. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-001. **Caso:** CU-003. **Reglas:** RN-001, RN-002, RN-043.

El sistema debe: Registrar establecimiento central, sedes clínicas y ubicaciones tipificadas, vinculando cada farmacia y servicio a su sede y permisos.

**CA-065 — Aceptación principal:** Crear central y tres clínicas, cada una con almacén y farmacia, sin saldos iniciales ficticios; añadir otra farmacia o sede no requiere código.

**Origen y estado:** FU-001; decisión de producto aceptada; parámetros operativos PN-002/PN-004/PN-007 pendientes.

## RF-066 — Autorizar cantidades de solicitud

**Actor:** Farmacia o responsable facultado. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-019. **Reglas:** RN-017, RN-040, RN-044.

El sistema debe: Decidir cantidades por línea y registrar versión, responsable y motivo de rechazo parcial/total; impedir reserva o despacho sin saldo autorizado. Mantener visible la demanda no autorizada.

**CA-066 — Aceptación principal:** Solicitar 100 y autorizar 80 deja 20 por decidir o rechazadas según decisión explícita. Entregar 40 deja 40 autorizadas pendientes; intentar reservar o despachar 81 se rechaza. Autorizar 100 y entregar 40 deja 60 pendientes.

**Origen y estado:** FU-001; decisión de producto aceptada; parámetros operativos PN-002/PN-004/PN-007 pendientes.

## RF-067 — Analizar cobertura y riesgo de merma

**Actor:** Responsable de farmacia o cadena. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-020. **Reglas:** RN-030, RN-033, RN-045.

El sistema debe: Mostrar demanda solicitada, autorizada y atendida, saldos pendientes, salidas finales, bajas por causa, libre, compromiso, antigüedad y próximos vencimientos por producto y ubicación; señalar sobrestock/baja rotación con parámetros versionados y corte.

**CA-067 — Aceptación principal:** En un periodo de ensayo con 30 unidades de salidas finales y traslado interno de 50, la demanda atendida no se infla a 80. Sin historial suficiente, la cobertura se marca no calculable y no se recomienda reposición automática.

**Origen y estado:** FU-001; decisión de producto aceptada; parámetros operativos PN-002/PN-004/PN-007 pendientes.

## RF-068 — Evaluar redistribución preventiva

**Actor:** Responsable de cadena. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-020. **Reglas:** RN-008, RN-018, RN-044, RN-046.

El sistema debe: Preparar propuesta trazable de redistribución, con origen/destino, lotes, cantidad, demanda, restricciones y fundamento. Registrar aceptación o descarte y vincular traslado sujeto a autorización.

**CA-068 — Aceptación principal:** De 100 elegibles con 80 comprometidas, no proponer más de 20 libres. Aceptar la propuesta no cambia saldos; si se bloquea el lote antes de expedir, el traslado no sale.

**Origen y estado:** FU-001; decisión de producto aceptada; parámetros operativos PN-002/PN-004/PN-007 pendientes.
