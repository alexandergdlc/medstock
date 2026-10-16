# Requisitos de calidad y restricciones

**Proyecto:** MedStock · **Versión:** 0.1.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Las políticas PP son propuestas.

## Alcance de las medidas

Los valores propuestos deben revisarse antes de convertirlos en compromisos. Ninguna
medición fue ejecutada. La métrica debe registrar entorno, volumen, corte, clase de
operación y perfil de carga; promedio sin percentiles no acredita rapidez.

| ID | Atributo | Estado | Criterio | Verificación | Driver |
| --- | --- | --- | --- | --- | --- |
| RNF-001 | Integridad | ACORDADO | Cero negativos, dobles efectos u operaciones parcialmente confirmadas en todos los CA aplicables. | Ensayos concurrentes, fallos y conciliación; CA-101 a CA-105 y CA-112. | DRV-001 |
| RNF-002 | Autorización | ACORDADO | El 100 % de operaciones protegidas de la matriz rechaza actor sin permiso o sede; revocación efectiva en la siguiente solicitud. | Pruebas positivas/negativas por rol, sede e identidad manipulada. | DRV-003 |
| RNF-003 | Rapidez de consulta | PROPUESTO | p95 <= 500 ms para consultas paginadas ordinarias durante el perfil ESC-002; medir también p99 sin ocultar errores. | Medición desde generador al recibir respuesta completa, por clase de operación. | DRV-002 |
| RNF-004 | Rapidez de movimiento | PROPUESTO | p95 <= 1 s para confirmaciones operativas de hasta diez líneas durante ESC-002, con resultado e invariantes correctos. | Latencia por operación, validaciones y relectura tras confirmar; excluye reportes grandes. | DRV-002 |
| RNF-005 | Capacidad de pico | OBJETIVO ACORDADO; PERFIL PROPUESTO | 2 000 usuarios activos con mezcla/ritmo/pausas definidos en ESC-002; error técnico < 1 % propuesto, sin excluir rechazos del reporte. | Informe repetible con peticiones ofrecidas/completadas, 429, 5xx, conflictos y conciliación. | DRV-002 |
| RNF-006 | Crecimiento funcional | ACORDADO | Alta de una cuarta sede y luego otras por configuración, conservando separación de saldos y permisos. | Recorrido de alta sin cambios de código; prueba con datos de ensayo de 50 sedes. | DRV-004 |
| RNF-007 | Auditoría verificable | ACORDADO | Todo movimiento y cambio de privilegios tiene datos de RN-024; inserción, cambio, supresión y truncado se evalúan contra referencia. | CA-108/CA-109 con copia de ensayo y referencia de cierre independiente. | DRV-005 |
| RNF-008 | Recuperación | PROPUESTO | No informar éxito si no existe confirmación persistente; recuperar resultado incierto. RPO/RTO operativos aún PN-006. | Interrumpir una respuesta y verificar un solo efecto; ejercicio de recuperación cuando exista diseño. | DRV-006 |
| RNF-009 | Usabilidad/accesibilidad | PROPUESTO | Operaciones críticas con confirmación comprensible, navegación de teclado y errores asociados a campos; sin depender solo del color. | Recorridos con usuarios representativos; teclado y validación accesible; no declarar conformidad formal sin auditoría. | DRV-007 |
| RNF-010 | Compatibilidad | PROPUESTO | Recorridos principales operables en versiones estables de Chrome, Edge y Firefox disponibles al ejecutar la prueba, a 360 y 1366 px. | Registrar versiones, resolución y resultados; no asegurar versiones futuras. | DRV-007 |
| RNF-011 | Trazabilidad/mantenibilidad | ACORDADO | Cada cambio de comportamiento enlaza RF/RN, aceptación y evidencia; no hay IDs ni enlaces internos huérfanos. | Revisión de PR, enlaces y matriz; pruebas afectadas antes de integrar código. | DRV-008 |
| RNF-012 | Costo y observabilidad | RESTRICCIÓN ACORDADA | Sin contratar servicios adicionales ni ejecutar carga que exceda el presupuesto de cuotas aprobado; identificar cada operación y sus fallos sin secretos. | Revisión de cuotas oficiales, cálculo previo de consumo y logs de ensayo sanitizados. | DRV-009 |

## Restricciones técnicas propuestas

Cloudflare y TypeScript son la base preferida del propietario. Workers, D1 y el
resto de herramientas se evaluarán en diseño; no se presupone una transacción
conjunta entre dos almacenamientos. El componente fuente de verdad se debe elegir
mediante una prueba de despacho con varios lotes y fallos. Una caché de lectura no
es autoridad para confirmar saldos.

El presupuesto gratuito no implica capacidad ilimitada ni disponibilidad contractual.
FU-008 y FU-009 documentan cuotas consultadas; deben comprobarse de nuevo al desplegar.
El dominio existente tiene renovación independiente. La prueba local masiva y la
prueba remota limitada se informarán como evidencias distintas.

## Disponibilidad y recuperación

No se fija un SLA empresarial ni una retención legal inventada. PN-006 exige acordar
RPO, RTO, periodicidad de respaldos, referencia de auditoría y procedimiento de
restauración. Cerrar ese punto bloquea operación productiva; no bloquea describir
los procesos y escenarios. Una restauración debe conciliar movimientos y referencias
antes de habilitar nuevos despachos.

## Dependencias humanas y físicas

Son necesarias identidad de operadores, calidad del catálogo y revisión de productos.
MedStock no reemplaza transporte adecuado, inspección, conservación ni autorizaciones
profesionales. No declarar una devolución utilizable solo por integridad del envase.
La aplicación debe permitir documentar la decisión del responsable competente.
