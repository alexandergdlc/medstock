# Requisitos funcionales y aceptación principal

**Proyecto:** MedStock · **Versión:** 0.1.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Las políticas PP son propuestas.

## Convenciones del catálogo

Cada RF tiene un criterio principal CA con el mismo número; CA-101 y siguientes
amplían concurrencia y fallos en 15. P1/P2 indican prioridad. I1/I2/I3 son incrementos
propuestos, no autorizaciones de implementación. El origen general es FU-001
(acuerdos de Alexander); las reglas enlazadas indican cualquier política PP pendiente.
La aceptación del borrador no reemplaza validar las políticas con un responsable.

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

## RF-001 — Acceder y cerrar sesión

**Actor:** Usuario. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-004. **Caso:** CU-001. **Reglas:** RN-002.

El sistema debe: Identificar usuarios y permitir cierre de sesión, sin aceptar acceso anónimo a inventario.

**CA-001 — Aceptación principal:** Dadas credenciales inválidas, el acceso falla sin mostrar existencias; al cerrar sesión no se admiten nuevas operaciones protegidas con esa sesión.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-002 — Administrar permisos

**Actor:** Administrador. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-004. **Caso:** CU-002. **Reglas:** RN-002, RN-029.

El sistema debe: Asignar y revocar roles por sede a usuarios activos, registrando quién cambió el permiso.

**CA-002 — Aceptación principal:** Revocado el permiso de una sede, la siguiente operación protegida en esa sede se rechaza y el cambio queda auditado.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-003 — Gestionar sedes

**Actor:** Administrador. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-001. **Caso:** CU-003. **Reglas:** RN-001, RN-026.

El sistema debe: Registrar, modificar y desactivar establecimientos mediante configuración y código único.

**CA-003 — Aceptación principal:** Con tres sedes existentes se registra una cuarta con otro código, sin cambiar ni desplegar el programa.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-004 — Gestionar ubicaciones y servicios

**Actor:** Responsable de sede. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-001. **Caso:** CU-003. **Reglas:** RN-001, RN-002.

El sistema debe: Registrar almacenes, farmacias y servicios solicitantes, vinculados a una sede.

**CA-004 — Aceptación principal:** Una ubicación de la sede A no puede utilizarse como ubicación de salida de la sede B.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-005 — Gestionar catálogo

**Actor:** Gestor de catálogo. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-002. **Caso:** CU-004. **Reglas:** RN-003, RN-026.

El sistema debe: Registrar productos con tipo, descripción, unidad base, fabricante y datos de identificación pertinentes.

**CA-005 — Aceptación principal:** Desactivar un producto con movimientos impide nuevas operaciones ordinarias sin eliminar sus registros históricos.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-006 — Definir presentaciones

**Actor:** Gestor de catálogo. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-002. **Caso:** CU-004. **Reglas:** RN-004, RN-005.

El sistema debe: Registrar factores positivos de conversión a unidad base y conservar el factor aplicado en cada movimiento.

**CA-006 — Aceptación principal:** Dos cajas de veinte unidades generan cuarenta unidades base; cambiar después la presentación no altera el movimiento anterior.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-007 — Registrar procedencias

**Actor:** Almacenero. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-005. **Reglas:** RN-007.

El sistema debe: Registrar proveedor o procedencia y referencia documental para una recepción.

**CA-007 — Aceptación principal:** No se confirma recepción sin procedencia identificable y documento con número o referencia controlada.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-008 — Preparar recepción

**Actor:** Almacenero. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-005. **Reglas:** RN-006, RN-007, RN-009.

El sistema debe: Capturar líneas recibidas, presentación, cantidad base, lote, fecha y evaluación inicial.

**CA-008 — Aceptación principal:** Una línea con cantidad cero o lote contradictorio queda sin confirmar y muestra la causa.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-009 — Confirmar recepción

**Actor:** Almacenero autorizado. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-005. **Reglas:** RN-007, RN-012, RN-014.

El sistema debe: Confirmar recepción y clasificar cantidades utilizables u observadas de forma trazable.

**CA-009 — Aceptación principal:** Confirmar dos veces la misma recepción produce una sola entrada y un único resultado de operación.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-010 — Consultar existencias

**Actor:** Usuario autorizado. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-002. **Caso:** CU-006. **Reglas:** RN-002, RN-008.

El sistema debe: Consultar saldos por sede, ubicación, producto, lote y condición, distinguiendo disponible y no disponible.

**CA-010 — Aceptación principal:** Cinco unidades en cuarentena aparecen separadas y no aumentan el saldo despachable.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-011 — Consultar historial por lote

**Actor:** Auditor o farmacia. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-006. **Reglas:** RN-024, RN-033.

El sistema debe: Reconstruir las entradas, salidas y ubicaciones de un lote con documento y responsable.

**CA-011 — Aceptación principal:** Un lote trasladado conserva enlaces entre recepción original, salida de traslado y recepción de destino.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-012 — Alertar stock y vencimiento

**Actor:** Farmacia. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-006. **Reglas:** RN-009, RN-030.

El sistema debe: Mostrar alertas según umbrales configurados, sin crear operaciones de inventario.

**CA-012 — Aceptación principal:** Al cruzarse un umbral aparece la alerta con sede, producto o lote y fecha de corte; el saldo no cambia.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-013 — Crear solicitud interna

**Actor:** Solicitante. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-007. **Reglas:** RN-017, RN-027, RN-016.

El sistema debe: Preparar y enviar cantidades requeridas por un servicio y sede, sin datos clínicos personales.

**CA-013 — Aceptación principal:** Enviar una solicitud válida crea un número de seguimiento y mantiene intacto el stock.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-014 — Consultar o cancelar solicitud

**Actor:** Solicitante. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-007. **Reglas:** RN-015, RN-017.

El sistema debe: Consultar estado y cancelar solo las cantidades pendientes permitidas por su estado.

**CA-014 — Aceptación principal:** Después de una entrega parcial se puede cancelar el remanente; las unidades entregadas y sus movimientos se conservan.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-015 — Evaluar disponibilidad FEFO

**Actor:** Farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-008. **Reglas:** RN-008, RN-009, RN-010, RN-011, RN-032.

El sistema debe: Proponer asignación de lotes elegibles para una solicitud, con cantidades y faltantes.

**CA-015 — Aceptación principal:** Con lotes elegibles de diez unidades que vencen en distinto orden, solicitar doce propone diez del primero y dos del siguiente.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-016 — Confirmar despacho

**Actor:** Farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-008. **Reglas:** RN-011, RN-012, RN-013, RN-014.

El sistema debe: Confirmar la salida por lote, descontar stock y registrar documento, resultado y auditoría coherentes.

**CA-016 — Aceptación principal:** Dos solicitudes de siete unidades compiten por diez; solo una completa siete y ninguna deja saldo negativo.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-017 — Atender parcialmente

**Actor:** Farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-002. **Caso:** CU-008. **Reglas:** RN-015.

El sistema debe: Permitir atención parcial solo con aceptación explícita y conservar el remanente.

**CA-017 — Aceptación principal:** Solicitar doce con diez disponibles no descuenta nada sin aceptar parcial; al aceptarla entrega diez y mantiene dos pendientes.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-018 — Recuperar resultado

**Actor:** Usuario que opera. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-003. **Caso:** CU-008. **Reglas:** RN-014, RN-034.

El sistema debe: Consultar el resultado de una operación incierta y reconocer reintentos con la misma identidad.

**CA-018 — Aceptación principal:** Tras perderse una respuesta posterior a confirmar, consultar o reenviar la misma operación devuelve su despacho sin otro descuento.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-019 — Emitir constancia de salida

**Actor:** Farmacia. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-003. **Caso:** CU-008. **Reglas:** RN-024, RN-035, RN-036.

El sistema debe: Mostrar constancia de despacho con solicitud, servicio, responsables, lotes y cantidades.

**CA-019 — Aceptación principal:** La constancia coincide con las líneas confirmadas y no afirma administración de medicamentos a pacientes.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-020 — Solicitar traslado

**Actor:** Responsable de sede. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-001. **Caso:** CU-009. **Reglas:** RN-018.

El sistema debe: Crear solicitud entre ubicaciones de sedes distintas, con productos y cantidades.

**CA-020 — Aceptación principal:** Origen igual a destino se rechaza; enviar la solicitud de traslado no cambia saldos.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-021 — Autorizar y expedir traslado

**Actor:** Responsable de origen. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-001. **Caso:** CU-009. **Reglas:** RN-010, RN-012, RN-014, RN-018.

El sistema debe: Autorizar y confirmar salida con detalle por lote y existencia en tránsito.

**CA-021 — Aceptación principal:** Expedir ocho unidades reduce ocho del origen y aumenta ocho en tránsito, sin acreditar todavía al destino.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-022 — Recibir traslado

**Actor:** Receptor de destino. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-001. **Caso:** CU-010. **Reglas:** RN-014, RN-018, RN-019.

El sistema debe: Recibir cantidades por lote y registrar aceptación, observaciones y diferencias.

**CA-022 — Aceptación principal:** De ocho en tránsito se aceptan seis y se observan dos recibidas: tránsito queda en cero, seis utilizables y dos segregadas; no se crean diez unidades.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-023 — Resolver diferencia de traslado

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-010. **Reglas:** RN-019, RN-021, RN-031.

El sistema debe: Cerrar diferencias mediante evidencia y movimiento autorizado cuando corresponda.

**CA-023 — Aceptación principal:** Un faltante de dos no se elimina del tránsito mediante editar el documento; se resuelve con constancia y movimiento vinculado.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-024 — Registrar devolución

**Actor:** Receptor de farmacia. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-011. **Reglas:** RN-020.

El sistema debe: Registrar unidades devueltas contra un despacho y ubicarlas en cuarentena.

**CA-024 — Aceptación principal:** De una entrega de cinco con dos ya devueltas, intentar devolver otras cuatro se rechaza.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-025 — Evaluar devolución

**Actor:** Responsable farmacéutico. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-011. **Reglas:** RN-008, RN-020, RN-022.

El sistema debe: Liberar o rechazar devolución con evaluación documentada y verificación de lote.

**CA-025 — Aceptación principal:** Un producto devuelto y vencido no pasa a utilizable aunque su envase aparente estar íntegro.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-026 — Registrar conteo

**Actor:** Almacenero. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-012. **Reglas:** RN-021, RN-031.

El sistema debe: Registrar conteo físico y diferencias contra un corte identificable, sin cambiar saldos directamente.

**CA-026 — Aceptación principal:** Una diferencia de menos tres genera propuesta de ajuste con referencia al conteo; el saldo aún no cambia.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-027 — Autorizar ajuste

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-012. **Reglas:** RN-013, RN-021, RN-023.

El sistema debe: Aprobar o rechazar ajuste; al aprobar, aplicar compensación sin borrar historial.

**CA-027 — Aceptación principal:** El creador no aprueba su ajuste; un ajuste aprobado que dejaría stock negativo se rechaza sin efectos.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-028 — Bloquear y liberar lote

**Actor:** Responsable farmacéutico. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-002. **Caso:** CU-013. **Reglas:** RN-011, RN-022.

El sistema debe: Bloquear lotes por alcance y motivo, y liberar solo con permiso y evidencia.

**CA-028 — Aceptación principal:** Un lote bloqueado después de una propuesta FEFO queda excluido en la confirmación y se recalcula o rechaza el despacho.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-029 — Gestionar retiro de lote

**Actor:** Responsable central. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-013. **Reglas:** RN-022, RN-024.

El sistema debe: Identificar ubicaciones y movimientos afectados por retiro, registrar seguimiento y segregación.

**CA-029 — Aceptación principal:** Una búsqueda de retiro informa las sedes con saldo, tránsito y despachos previos del lote en el ámbito autorizado.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-030 — Registrar baja

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-014. **Reglas:** RN-021, RN-022, RN-023.

El sistema debe: Registrar salida por vencimiento, daño o retiro con autorización y documento.

**CA-030 — Aceptación principal:** La baja descuenta la condición segregada correspondiente; conserva el motivo y no certifica destrucción física.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-031 — Compensar error

**Actor:** Responsable autorizado. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-014. **Reglas:** RN-013, RN-020, RN-023.

El sistema debe: Corregir una operación confirmada mediante compensación vinculada tras verificar movimientos posteriores.

**CA-031 — Aceptación principal:** Una recepción cuyas unidades ya fueron despachadas no se revierte de forma ciega generando negativos.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-032 — Consultar auditoría

**Actor:** Auditor. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-015. **Reglas:** RN-024, RN-033.

El sistema debe: Buscar eventos por autor, sede, operación, documento, lote y periodo con permisos de lectura.

**CA-032 — Aceptación principal:** El auditor consulta el evento y sus vínculos, pero no puede editar la cantidad ni borrar el evento.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-033 — Verificar integridad

**Actor:** Auditor. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-003. **Caso:** CU-015. **Reglas:** RN-025.

El sistema debe: Verificar cadena de auditoría y declarar alcance, referencia, resultado y primer punto de anomalía.

**CA-033 — Aceptación principal:** Alterar o quitar un evento de una copia de prueba causa resultado de anomalía; una copia truncada se contrasta con la referencia de cierre esperada.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-034 — Consolidar reportes

**Actor:** Responsable central. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-001. **Caso:** CU-016. **Reglas:** RN-031, RN-033.

El sistema debe: Consolidar existencias, vencimientos y movimientos con filtros y fecha de corte coherentes.

**CA-034 — Aceptación principal:** Un traslado interno conserva el total de cadena contando tránsito una sola vez.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-035 — Exportar resultados

**Actor:** Auditor o responsable. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-003. **Caso:** CU-016. **Reglas:** RN-002, RN-033.

El sistema debe: Exportar resultados autorizados con filtros y corte identificados, sin información personal de pacientes.

**CA-035 — Aceptación principal:** El archivo contiene solo sedes permitidas y conserva el mismo corte del reporte solicitado.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-036 — Desactivar sin borrar

**Actor:** Administrador autorizado. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-003. **Caso:** CU-003. **Reglas:** RN-026.

El sistema debe: Desactivar entidades conservando historial y bloquear cierre operativo con pendientes.

**CA-036 — Aceptación principal:** Una sede con dos unidades o un traslado pendiente no queda cerrada hasta resolverlos.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-037 — Configurar políticas

**Actor:** Responsable central. **Prioridad:** P2. **Incremento:** I3.

**Objetivo:** OBJ-002. **Caso:** CU-004. **Reglas:** RN-028, RN-030.

El sistema debe: Cambiar umbrales autorizados y parámetros operativos con registro de versión y efecto futuro.

**CA-037 — Aceptación principal:** Cambiar el umbral de vencimiento no modifica fechas de lote ni movimientos confirmados.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-038 — Auditar acceso y administración

**Actor:** Administrador y auditor. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-004. **Caso:** CU-002. **Reglas:** RN-024, RN-025, RN-029.

El sistema debe: Registrar cambios de roles y eventos de acceso relevantes sin conservar contraseñas ni tokens.

**CA-038 — Aceptación principal:** Una asignación de privilegios queda vinculada a su autor y fecha; el registro no muestra secretos.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-039 — Reconciliar inventario

**Actor:** Auditor o responsable. **Prioridad:** P1. **Incremento:** I2.

**Objetivo:** OBJ-003. **Caso:** CU-015. **Reglas:** RN-012, RN-031.

El sistema debe: Comparar balances y movimientos, incluyendo tránsito y compensaciones, y señalar discrepancias.

**CA-039 — Aceptación principal:** Una diferencia introducida en una copia de ensayo se informa sin autocorregir ni ocultar la discrepancia.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.

## RF-040 — Mostrar errores y seguimiento

**Actor:** Usuario. **Prioridad:** P1. **Incremento:** I1.

**Objetivo:** OBJ-006. **Caso:** CU-001. **Reglas:** RN-014, RN-034.

El sistema debe: Informar causas de rechazo y referencia de seguimiento, diferenciando rechazo y resultado incierto.

**CA-040 — Aceptación principal:** Una respuesta perdida no se presenta como operación cancelada; se indica consultar el resultado original.

**Origen y estado:** FU-001; borrador verificable condicionado a las PP de sus reglas.
