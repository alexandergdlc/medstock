# Glosario y significado de cantidades

**Proyecto:** MedStock · **Versión:** 0.2.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Las políticas PP son propuestas.

| Término | Definición en MedStock |
|---|---|
| Cadena | Organización única con varias sedes; no plataforma multicliente en este alcance |
| Sede / clínica | Establecimiento incorporable por configuración |
| Ubicación | Punto de custodia: almacén, farmacia o ubicación lógica de tránsito |
| Servicio | Área solicitante, por ejemplo emergencia; no implica subinventario gestionado |
| Producto | Identidad del medicamento o insumo, distinta del lote y de la presentación |
| DCI | Denominación común internacional; atributo pertinente a medicamentos, no sustitución clínica |
| Presentación | Forma de recepción/entrega con factor a unidad base, por ejemplo caja de veinte |
| Unidad base | Unidad mínima discreta de control; no equivale siempre a dosis |
| Lote | Partida identificada por producto, fabricante y código; conserva vencimiento |
| Existencia | Cantidad de un lote en ubicación y condición determinadas |
| Físico en sede | Unidades presentes, sumadas por condiciones; no implica que todas sean despachables |
| Utilizable | Condición que cumple los controles para participar en selección |
| Disponible libre | Utilizable elegible menos compromisos vigentes para otras asignaciones; no incluye tránsito o bloqueo |
| Cuarentena | Segregado mientras se decide aceptación o liberación |
| Bloqueado | No elegible por una restricción documentada |
| Vencido | No elegible según la fecha operativa; físico hasta su baja autorizada |
| Tránsito | Custodia lógica después de expedir y antes de aceptar/resolver en destino |
| Solicitud | Demanda de un servicio; no reserva stock en PP-006 |
| Reserva | Compromiso temporal explícito por lote y solicitud; incluido para I3 con vigencia y liberación |
| Despacho | Salida confirmada de farmacia/almacén hacia un servicio |
| Dispensación | Acto farmacéutico clínico; no se confunde con la salida logística del prototipo |
| Movimiento | Efecto registrado sobre ubicación, condición o cantidad de un lote |
| Ajuste | Compensación autorizada por diferencia acreditada |
| Baja | Salida autorizada por daño, vencimiento u otra causa; no certifica destrucción |
| FEFO | Primero en vencer, primero en salir entre existencias elegibles |
| Idempotencia | Repetir una misma operación lógica no multiplica sus efectos |
| Atomicidad de negocio | Documento, cambios y auditoría quedan completos o sin efectos parciales |
| Conciliación | Contraste entre movimientos, saldos y tránsito para detectar diferencias |
| Ledger / cadena de hashes | Historial enlazado para detectar cambios frente a evidencia confiable |
| Corte | Instante/alcance al que corresponde un saldo o reporte |
| Usuario simultáneo activo | Sesión que ejecuta un recorrido durante la ventana de carga, con pausas definidas |
| RPS | Solicitudes por segundo; no equivale al número de usuarios |
| p95 | Latencia que no supera el 95 % de observaciones del grupo medido |

## Ejemplo de balance

Para un lote: 12 utilizables + 3 bloqueadas + 2 en cuarentena = 17 físicas en sede.
Si además hay 4 en tránsito, el total bajo custodia de cadena es 21. El disponible
ordinario puede ser 12, sujeto a vigencia y controles de confirmación. No se suman
las mismas unidades como disponibles del destino antes de recibirlas.

Sin reservas vigentes, libre = utilizable elegible. Con reservas activas,
libre = utilizable elegible - compromiso vigente. Reservar no cambia el físico;
consumir sí produce salida. Lo reservado a una solicitud no puede consumirse desde
otra. Caducidad o bloqueo del lote impiden consumo aun con reserva previa.
Las cantidades de distintas unidades base no se suman como un único stock operativo:
veinte tabletas y cinco frascos son dos saldos distintos.
