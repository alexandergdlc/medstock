# Alcance, límites y entregas incrementales

**Proyecto:** MedStock · **Versión:** 0.3.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Decisiones del propietario aceptadas; detalles operativos pendientes según 14.

## Frontera funcional

MedStock gestiona inventario logístico de una cadena: de la recepción al despacho
a un servicio, tránsito, retorno y salida autorizada. El servicio y su responsable
identifican el destino. La administración al paciente y el inventario interno de
los servicios están fuera de la primera versión (RN-035, PP-014).

## Incluido

Organización, usuarios y permisos; catálogo común y presentaciones; procedencias;
recepción con lotes y condición; consultas de stock; solicitudes; reservas explícitas; FEFO; confirmación
indivisible; recuperación de operaciones; traslados con diferencias; devoluciones;
conteos y ajustes; bloqueos/retiros; bajas; auditoría, conciliación y reportes.

## Exclusiones explícitas

- Diagnóstico, receta clínica completa, historia clínica y datos identificables de pacientes.
- Facturación, POS, pagos, aseguradoras, contabilidad y contratos de compra.
- Control autónomo de cadena de frío o sensores; certificación de almacenamiento físico.
- Estupefacientes, psicotrópicos, radiofármacos y otros circuitos especiales hasta un análisis específico.
- Fraccionamiento farmacéutico, fórmulas magistrales, productos a granel y dispositivos serializados/implantes en el primer alcance funcional.
- Operación offline con modificación de stock y conciliación automática posterior.
- Blockchain pública, validez legal automática o auditoría resistente a todo administrador privilegiado.
- Recomendaciones clínicas por IA o sustitución terapéutica automática.

Registrar metadatos de conservación no demuestra que se hayan mantenido las condiciones.
El alcance se ampliará mediante requisitos y revisión, no por un cambio oculto de pantalla.

## Incrementos propuestos para un desarrollador

| Incremento | Valor demostrable | Grupos de capacidades |
|---|---|---|
| I1 | Recepción y visibilidad segura por sede | Acceso, sedes, catálogo, lotes, stock, bloqueo y auditoría de cambios |
| I2 | Solicitud y despacho confiable | Autorización de demanda, FEFO, parcialidad, idempotencia, concurrencia, constancia, verificación y conciliación |
| I3 | Operación de cadena | Reservas finitas, traslados, devoluciones, conteos/ajustes, retiros, bajas, alertas y reportes |

Las funciones de I3 siguen incluidas en el análisis. El primer incremento no se
presentará como sistema empresarial terminado ni se programará sin sus criterios.
El calendario se definirá al estimar el diseño; no existe fecha de entrega confirmada.

## Interfaces de negocio

Usuarios web son actores. Base de datos, caché y componentes internos no son actores.
Proveedores suministran documentos físicos/digitales, pero no tienen cuenta ni API
confirmada. Una plataforma clínica externa para recetas es una posible evolución,
no una integración ya acordada. El evaluador recibe documentación/demostración, sin
requerir acceso a datos operativos reales.

## Restricciones y viabilidad preliminar

Desarrollo individual, presupuesto de infraestructura dentro de cuotas gratuitas,
dominio ya adquirido y Cloudflare prioritario. El objetivo de gran escala puede
entrar en tensión con cuota gratuita y tiempo individual: se evaluará mediante
prototipos técnicos e incrementos, sin reducir controles de integridad para aparentar
mayor rendimiento. La viabilidad de producción real no está acreditada.

## Especialización confirmada

Las cinco capacidades están incluidas en el análisis para implementación posterior.
En I2 se puede operar todavía sin reservas, pero la evolución I3 requiere reserva
explícita, libre/comprometido, consumo y liberación coherentes. No se incorpora la
reserva automática por enviar solicitud ni se promete implementar todo en un Sprint.

## Organización y optimización confirmadas

Se incluye un establecimiento logístico central y almacenes por sede. Inicialmente
cada sede clínica tiene una farmacia principal; el modelo permite más ubicaciones.
El stock se conserva en almacenes y farmacias, no se duplica por compartir un local.
Transferir de almacén a farmacia usa traslado entre ubicaciones; entregar a servicio
sale de la custodia gestionada. Activar un stock de emergencia futuro requiere
especificar su ubicación, responsables y circuito de reposición/consumo.

I1 incluye RF-065; I2 incluye RF-066 aunque las reservas se implementen en I3.
I3 incluye RF-067/RF-068: análisis explicable de riesgos y redistribución supervisada.
La optimización se evalúa por disponibilidad y reducción de pérdida evitable; no por
cantidad de movimientos. No se promete merma cero ni un motor predictivo entrenado.
