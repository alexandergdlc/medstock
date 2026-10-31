# Drivers y escenarios de calidad

**Proyecto:** MedStock · **Versión:** 0.3.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Decisiones del propietario aceptadas; detalles operativos pendientes según 14.

## Fundamento

Los drivers son requisitos/condiciones que condicionarán el diseño. El sílabo exige
su identificación y escenarios medibles (FU-002). Se adapta la estructura de escenarios
de calidad del SEI (FU-007), sin afirmar que se realizó un taller QAW con actores reales.
Las prioridades de esta versión son propuestas por riesgo para revisión de Alexander.

| ID | Driver | Prioridad / impacto | Origen | Implicación para el diseño posterior |
| --- | --- | --- | --- | --- |
| DRV-001 | Integridad de stock y operación indivisible | P1 / crítico | RF-009, RF-016, RF-018, RF-021, RF-027; RNF-001 | Elegir límites de transacción y fuente de verdad; evitar escritura doble sin recuperación. |
| DRV-002 | 2 000 usuarios activos y respuesta rápida | P1 / alto | RNF-003, RNF-004, RNF-005 | Distinguir lectura/escritura, distribución y puntos calientes; medir antes de prometer. |
| DRV-003 | Permisos por sede | P1 / crítico | RF-001, RF-002; RNF-002 | Identidad y autorización coherentes en todo acceso y exportación. |
| DRV-004 | Crecimiento de la cadena | P1 / alto | RF-003, RF-004, RF-034; RNF-006 | Sedes configurables y visibilidad agregada sin constantes por clínica. |
| DRV-005 | Auditoría verificable | P1 / alto | RF-032, RF-033, RF-039; RNF-007 | Definir orden, alcance de cadena, referencias independientes y acceso privilegiado. |
| DRV-006 | Recuperación de incertidumbre | P1 / alto | RF-018, RF-031; RNF-008 | Identidad de operación, respuesta persistente y reconciliación tras restaurar. |
| DRV-007 | Operación comprensible | P2 / medio | RF-040; RNF-009, RNF-010 | Errores claros, teclado, navegadores y tamaño de pantalla. |
| DRV-008 | Desarrollo individual y evolución SDD | P1 / alto | RNF-011 | Módulos comprensibles e incrementos; no imponer microservicios por prestigio. |
| DRV-009 | Presupuesto gratuito | P1 / alto | RNF-012 | Consumo, cuota, portabilidad y alcance de pruebas; puede limitar objetivos remotos. |

## Escenarios de calidad

### ESC-001

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-001 |
| Fuente del estímulo | Dos operadores autorizados |
| Estímulo | Intentan confirmar siete unidades cada uno de las diez disponibles |
| Entorno | Operación normal con solicitudes concurrentes y sin parcial |
| Elemento afectado | Confirmación de despacho |
| Respuesta | Una confirma; la otra conoce rechazo recuperable; historia y saldo coherentes |
| Medida | Saldo final tres; una entrega de siete; cero doble efecto/negativos. |

### ESC-002

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-003, RNF-004, RNF-005 |
| Fuente del estímulo | 2 000 usuarios de ensayo |
| Estímulo | Recorren consultas, solicitudes, despachos y reportes |
| Entorno | Perfil CP-01, dataset VD-01 y entorno declarado |
| Elemento afectado | Servicio MedStock completo de ensayo |
| Respuesta | Respuestas clasificadas y movimientos íntegros |
| Medida | Candidatos: p95 consulta <=500 ms; movimiento <=1 s; error técnico <1 %; cero violaciones. |

### ESC-003

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-002 |
| Fuente del estímulo | Usuario de sede A o con permiso revocado |
| Estímulo | Solicita datos o confirma cambios en sede B |
| Entorno | Sesión válida pero ámbito no autorizado |
| Elemento afectado | Control de acceso de cada operación |
| Respuesta | Rechazo sin datos ni efectos y con seguimiento seguro |
| Medida | 100 % de casos negativos del alcance rechazados; revocación en siguiente operación. |

### ESC-004

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-006 |
| Fuente del estímulo | Administrador autorizado |
| Estímulo | Agrega cuarta sede, ubicaciones y usuarios |
| Entorno | Cadena con historia y tres sedes iniciales |
| Elemento afectado | Configuración y consultas por ámbito |
| Respuesta | La sede opera sin editar código; otras sedes conservan saldos |
| Medida | Cuarta sede creada y CA-118 cumplido; 0 cambios de código por sede. |

### ESC-005

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-007 |
| Fuente del estímulo | Auditor en copia controlada |
| Estímulo | Modifica/trunca una cadena o sustituye contenido |
| Entorno | Referencia independiente conocida y verificador disponible |
| Elemento afectado | Historial del ámbito auditado |
| Respuesta | Declara divergencia o límite de evidencia |
| Medida | Detecta los casos CA-108/CA-109; informa primer punto o referencia divergente. |

### ESC-006

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-008 |
| Fuente del estímulo | Red/cliente |
| Estímulo | Pierde respuesta después de confirmar |
| Entorno | Operación persistida; cliente desconoce resultado |
| Elemento afectado | Consulta de resultado e inventario |
| Respuesta | Recupera documento al reintentar identidad original |
| Medida | Un solo efecto y mismo documento; tiempo de recuperación operativa por acordar. |

### ESC-007

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-009, RNF-010 |
| Fuente del estímulo | Operador con teclado y pantalla pequeña |
| Estímulo | Solicita y confirma un recorrido permitido |
| Entorno | Navegadores y tamaños documentados |
| Elemento afectado | Interfaz operativa |
| Respuesta | Controles accesibles y errores comprensibles |
| Medida | Completa recorridos sin ratón y sin campos/acciones críticas inaccesibles; revisión manual registrada. |

### ESC-008

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-011 |
| Fuente del estímulo | Responsable del producto |
| Estímulo | Cambia una política de parcialidad |
| Entorno | Nueva revisión antes de implementar |
| Elemento afectado | Especificaciones y cambios derivados |
| Respuesta | Actualiza reglas y vínculos afectados |
| Medida | 100 % de RF afectados con aceptación revisada; ningún ID o enlace huérfano. |

### ESC-009

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-012 |
| Fuente del estímulo | Responsable de pruebas |
| Estímulo | Prepara un ensayo remoto |
| Entorno | Plan gratuito con consumo previo conocido |
| Elemento afectado | Plan de carga y presupuesto |
| Respuesta | Calcula consumo y reduce/separa ensayo si excede cuota |
| Medida | No ejecutar sin presupuesto; informar cuota, consumo previsto y condición de parada. |

## Escenarios especializados

### ESC-010

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-013 |
| Fuente del estímulo | Dos operadores |
| Estímulo | Reservar o consumir/cancelar las mismas unidades |
| Entorno | Lote con diez libres o reserva activa, sin fallo artificial |
| Elemento afectado | Compromisos y salida física |
| Respuesta | Resolver una sola vez sin sobreasignar ni doble liberar |
| Medida | CA-119, CA-120 y CA-121; cero violaciones de RN-037/RN-042. |

### ESC-011

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-014 |
| Fuente del estímulo | Tiempo operativo |
| Estímulo | Alcanzar fin T o cambiar elegibilidad del lote |
| Entorno | Limpieza de reservas retrasada y hora de cliente manipulada |
| Elemento afectado | Decisión de consumo y disponible |
| Respuesta | Aplicar vigencia efectiva, sin depender de etiqueta antigua |
| Medida | CA-122 y CA-126; no consumo en T o después ni libre falso por bloqueo. |

### ESC-012

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-016 |
| Fuente del estímulo | Operador y aprobador |
| Estímulo | Cambiar contenido o revocar permiso tras aprobar |
| Entorno | Aprobación de una versión anterior |
| Elemento afectado | Autorización al ejecutar |
| Respuesta | Exigir revisión vigente y condiciones actuales |
| Medida | CA-123; 100 % de variantes no autorizadas rechazadas. |

### ESC-013

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-015 |
| Fuente del estímulo | Auditor |
| Estímulo | Reconstruir liberación y parcialidad por evidencia |
| Entorno | Datos de ensayo con revisiones y devoluciones por subcantidad |
| Elemento afectado | Historial de decisiones |
| Respuesta | Mostrar autor, contenido, motivo y vínculo sin sobrescritura |
| Medida | RF-063 y CA-124/CA-125; decisiones y acumulados reconstruibles. |

### ESC-014

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-017 |
| Fuente del estímulo | Usuario |
| Estímulo | Consultar compromisos y confirmar después de otro cambio |
| Entorno | Otra operación entre vista y confirmación |
| Elemento afectado | Consulta y ejecución |
| Respuesta | Mostrar corte y revalidar asignación efectiva |
| Medida | RF-045 y RF-054; ningún saldo de pantalla sustituye validación al confirmar. |

### ESC-015

| Campo | Definición |
| --- | --- |
| Requisitos | RNF-018 |
| Fuente del estímulo | Responsable de revisión |
| Estímulo | Cambiar una de las cinco políticas |
| Entorno | Análisis especializado antes de implementar |
| Elemento afectado | Requisitos y evidencias |
| Respuesta | Actualizar aceptación y atribución de origen |
| Medida | Cinco capacidades cubiertas con positivos/negativos y trazabilidad de 18/20. |

## CP-01 — Perfil candidato de carga

**Estado:** propuesta PN-005, no aprobado ni ejecutado. Es carga de aplicación,
no la afirmación de que una cadena particular tenga esa demanda medida.

- 2 000 usuarios virtuales con identidades y permisos diferenciados.
- Rampa de cinco minutos hasta el pico; diez minutos en pico; dos de descenso.
- Cada usuario inicia aproximadamente una acción de negocio cada diez segundos,
  incluyendo pausa; mezcla: 80 % consultas paginadas, 10 % creación/seguimiento de
  solicitudes, 8 % confirmaciones y 2 % reportes acotados.
- Durante el pico eso ofrece aproximadamente 200 acciones de negocio por segundo,
  NO 2 000 RPS. Una acción puede generar varias solicitudes y escrituras.
- Distribución propuesta entre 50 sedes; una prueba aparte concentra escrituras en
  un mismo producto/lote para medir contención. No se reemplaza esa prueba por lecturas.
- Contabilizar respuestas correctas, rechazos de negocio, conflictos, 429, 5xx,
  timeouts y solicitudes abandonadas. Un 429 por cuota cuenta como limitación técnica.
- Medir latencia por categoría; no usar el buen p95 de lecturas para ocultar despachos
  lentos. Medir también cantidad ofrecida/completada para detectar un generador saturado.
- Interpretar el p95 desde el envío al recibir respuesta completa en la ubicación
  declarada; tiempo de renderizado y carga inicial de la interfaz son métricas separadas.

**Presupuesto:** solo el tramo pico representa unas 120 000 acciones. Si cada una
hiciera una solicitud al backend ya excedería las 100 000 solicitudes/día consultadas
para Workers Free. Además hay rampa, lecturas/escrituras y consumo previo. Por tanto
CP-01 no está autorizado para ejecutarse íntegramente sobre ese plan. El ensayo local
separa lógica/capacidad del equipo de la evidencia remota limitada. No prueba 2 000
usuarios remotos por extrapolación. Ver FU-008, FU-009 y RSK-003.

## VD-01 — Volumen candidato de ensayo

50 sedes; 5 000 productos; 50 000 lotes y 500 000 movimientos históricos, con balances
suficientes y casos de agotamiento. La cantidad de balances depende de ubicaciones y
condiciones y se documentará al generar el dataset. Son datos sintéticos y una
hipótesis de escala; estimar tamaño y cuotas antes de cargarlos en un servicio.
La demostración inicial usa tres sedes y después incorpora una cuarta.

## Compromisos que deberá resolver arquitectura

Centralizar historia facilita consulta, pero puede concentrar escrituras. Distribuir
por sede puede reducir contención local, pero complica traslados e integridad global.
Cachear acelera lecturas tolerantes a desactualización, no decisiones de stock. Una
cadena única de auditoría requiere orden global; varias cadenas requieren alcance y
referencias explícitos. No se elige una solución en esta fase sin evaluar esos costos.
