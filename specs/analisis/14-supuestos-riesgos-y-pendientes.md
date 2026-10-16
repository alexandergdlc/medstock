# Supuestos, políticas propuestas y riesgos

**Proyecto:** MedStock · **Versión:** 0.2.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Las políticas PP son propuestas.

## Decisiones ya aceptadas

Cadena ampliable, tres sedes de ensayo, catálogo compartido con saldos separados,
medicamentos e insumos, solicitudes internas validadas por farmacia, conversiones
explícitas, trazabilidad y operación individual del desarrollo. El propietario
aceptó incorporar los procesos logísticos. El pico objetivo es 2 000 usuarios activos;
no fija por sí solo ritmo ni capacidad demostrada.

## Políticas concretas propuestas

No se confunden con las decisiones aceptadas: precisan detalles que no se habían
confirmado. El borrador permite revisarlas sin pedir respuestas para cada párrafo.

| ID | Tema | Valor propuesto | Validador requerido | Pendiente |
| --- | --- | --- | --- | --- |
| PP-001 | Unidades | Solo cantidades enteras de unidades discretas; frasco completo, no mililitros fraccionados. | Responsable farmacéutico | PN-001 |
| PP-002 | Identidad de lote | Producto + fabricante + código; fecha conflictiva pasa a revisión. | Gestor de catálogo / farmacia | PN-001 |
| PP-003 | Fecha | Excluir vencimiento <= fecha operativa; mes/año no se normaliza sin validación. | Responsable farmacéutico | PN-001 |
| PP-004 | Empate FEFO | Primera recepción en la ubicación de salida y después identificador de lote. | Farmacia | PN-002 |
| PP-005 | Parciales | Rechazar insuficiencia salvo aceptación explícita; conservar remanente. | Responsable de servicio / farmacia | PN-002 |
| PP-006 | Reservas | Capacidad incluida por Alexander: reserva explícita y finita en I3; solicitar/consultar no reserva. Plazo y autoridades se validan. | Propietario / farmacia | PN-002 |
| PP-007 | Edición de solicitud | No editar líneas atendidas; cancelar solo remanente. | Responsable de servicio | PN-002 |
| PP-008 | Diferencias | Faltante conserva tránsito; daño recibido se segrega en destino. | Logística y destino | PN-003 |
| PP-009 | Ajustes | Aprobador distinto; revalidar saldo/corte antes de confirmar. | Responsable de cadena | PN-003 |
| PP-010 | Tiempo | Zona por sede; fecha local operativa e instante inequívoco. | Propietario / farmacia | PN-001 |
| PP-011 | Roles | Matriz de 04; administrador no obtiene facultad clínica automática. | Dirección / responsable farmacéutico | PN-004 |
| PP-012 | Alertas | Umbrales configurables por sede/producto; valores iniciales deben validarse, sin número universal. | Farmacia | PN-002 |
| PP-013 | No caducables | Categoría autorizada o exclusión del prototipo; sin FEFO artificial. | Gestor de catálogo / farmacia | PN-001 |
| PP-014 | Frontera de stock | La salida al servicio deja el inventario gestionado; subinventario clínico posterior. | Propietario / responsable de servicio | PN-004 |

## Políticas de detalle añadidas en 0.2.0

| ID | Tema | Valor propuesto | Validador requerido | Pendiente |
| --- | --- | --- | --- | --- |
| PP-015 | Asignación de reserva | Consumir el lote reservado si sigue elegible, sin reasignación silenciosa porque apareció otro lote anterior; revisión de prioridad pendiente. | Farmacia | PN-002 |
| PP-016 | Plazo | Cada reserva exige fin T definido por política configurada; no hay duración universal aprobada ni reserva indefinida. | Responsable de cadena | PN-002 |
| PP-017 | Contenido aprobado | Cambios significativos de cantidades/lotes requieren nueva revisión; aprobación no omite controles actuales. | Responsable de cadena | PN-003 |
| PP-018 | Retorno por línea | Conservar evidencia de conservación y origen; decidir por cantidad y mantener evaluación pendiente para el remanente. | Responsable farmacéutico | PN-001 |


## Pendientes y momentos de cierre

| ID | Decisión / evidencia faltante | Impacto | Responsable / cierre |
|---|---|---|---|
| PN-001 | Unidades, lote, vencimiento y categorías especiales | Elegibilidad y calidad de datos | Responsable farmacéutico antes de diseñar recepción/FEFO |
| PN-002 | Detalles de parcialidad; duración, consumo y liberación de reservas; empates y umbrales | Las cinco capacidades están incluidas; quedan parámetros y políticas operativas | Alexander con representantes operativos antes de diseñar cada capacidad |
| PN-003 | Aprobaciones y resolución de diferencias | Integridad logística y correcciones | Responsable de cadena antes de diseñar I3 |
| PN-004 | Roles finales y frontera de stock del servicio | Alcance y privacidad | Alexander y organización antes de fijar permisos |
| PN-005 | Perfil, volumen y tiempos objetivos de carga | Factibilidad de 2 000 usuarios y cuota | Alexander antes de plan de carga / diseño de rendimiento |
| PN-006 | Retención, respaldos, RPO/RTO y referencia confiable de auditoría | Recuperación y capacidad de detectar reescritura/truncado | Organización y arquitectura antes de producción |
| PN-007 | Organización concreta, entrevistas y normativa aplicable consolidada | Validación externa y afirmaciones sanitarias | Alexander / profesional competente antes de alegar uso real |
| PN-008 | Rúbrica, fecha y exigencia de diagramas del profesor | Forma de entrega | Alexander con docente antes de entrega académica |
| PN-009 | Fuente de verdad y transacción stock-documento-auditoría | Viabilidad técnica del núcleo | Fase de arquitectura; prototipo antes de implementar I2 |

PN-001 a PN-004 no bloquean revisar el dossier, pero bloquean implementar sus decisiones
como si ya estuvieran aprobadas. PN-006 y PN-007 bloquean afirmar preparación productiva.
Ningún pendiente está resuelto por el hecho de integrar un archivo de documentación.

## Supuestos explícitos

Operación online; una sola cadena en el alcance; usuarios de ensayo sin pacientes;
catálogo inicial preparado; ubicaciones y lotes identificables; recepción/entrega
físicas ejecutadas por personal responsable. No se presume integración con sistemas
clínicos, un almacén central obligatorio ni cuota ilimitada de servicios gratuitos.

## Riesgos

| ID | Riesgo | Probabilidad / impacto preliminar | Tratamiento |
|---|---|---|---|
| RSK-001 | Doble salida o negativos concurrentes | Media / crítico | Atomicidad, idempotencia y ensayos de contención |
| RSK-002 | Fecha o presentación mal interpretada | Media / alto | Validar PP; rechazar ambigüedad; conservar conversiones |
| RSK-003 | Cuotas gratuitas impiden carga remota | Alta / alto | Presupuesto previo; pruebas locales y remotas separadas |
| RSK-004 | Alcance excede desarrollo individual | Alta / alto | Incrementos y recorte explícito de implementación, sin ocultar análisis |
| RSK-005 | Reescritura privilegiada de auditoría | Media / alto | Referencia externa confiable, accesos y recuperación; no prometer inmutabilidad absoluta |
| RSK-006 | Duplicación o pérdida en traslado | Media / alto | Tránsito, recepciones parciales y diferencias documentadas |
| RSK-007 | Modelo no validado con clínica | Alta / alto | Evidenciar fuentes, marcar propuestas y entrevistar cuando sea posible |
| RSK-008 | Exposición por permisos o exportaciones | Media / alto | Pruebas por ámbito, mínimo privilegio y datos sintéticos |
| RSK-009 | Backup restaura saldos e historia incompatibles | Media / alto | Ejercicio de recuperación y conciliación antes de operar |

Estas estimaciones orientan el análisis; no son frecuencias observadas ni evaluación
actuarial. La mitigación técnica se justificará posteriormente con evidencia.

## Aclaración del alcance aceptado

Alexander confirmó que las cinco capacidades deben contemplarse para implementación
posterior: parcialidad, reservas, vencimientos, autorizaciones y devoluciones. La
inclusión deja de ser una duda de alcance. Permanecen por validar los detalles PP,
como duración de reserva y precisión de vencimiento. Esto no acredita validación de
un responsable farmacéutico ni convierte una decisión del producto en mandato legal.

La elección entre Scrum, un enfoque inspirado en él o SDD con Kanban sigue propuesta;
ver [alternativas de organización](19-organizacion-agil-y-sdd.md).
