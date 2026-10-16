# Alcance, límites y entregas incrementales

**Proyecto:** MedStock · **Versión:** 0.1.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Las políticas PP son propuestas.

## Frontera funcional

MedStock gestiona inventario logístico de una cadena: de la recepción al despacho
a un servicio, tránsito, retorno y salida autorizada. El servicio y su responsable
identifican el destino. La administración al paciente y el inventario interno de
los servicios están fuera de la primera versión (RN-035, PP-014).

## Incluido

Organización, usuarios y permisos; catálogo común y presentaciones; procedencias;
recepción con lotes y condición; consultas de stock; solicitudes; FEFO; confirmación
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
| I2 | Solicitud y despacho confiable | FEFO, parcialidad, idempotencia, concurrencia, constancia, verificación y conciliación |
| I3 | Operación de cadena | Traslados, devoluciones, conteos/ajustes, retiros, bajas, alertas y reportes |

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
