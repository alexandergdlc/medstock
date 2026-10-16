# MedStock Constitution

## Core Principles

### I. Especificaciones comprobables y evidencia

Toda función DEBE tener requisitos identificados, reglas, excepciones y criterios
de aceptación antes de implementarse. Un cambio de comportamiento DEBE actualizar
la especificación y su trazabilidad. Los documentos DEBEN distinguir decisiones
confirmadas, propuestas y pendientes. Las fuentes públicas NO DEBEN presentarse
como entrevistas ni como evidencia de procesos internos de una clínica. El análisis
DEBE incluir interesados, restricciones y drivers arquitectónicos del curso IS-488.

### II. Integridad del inventario y trazabilidad

Las existencias DEBEN distinguir establecimiento, ubicación, producto y lote. El
despacho DEBE aplicar FEFO a lotes elegibles y excluir existencias vencidas o
bloqueadas. La confirmación DEBE impedir stock negativo, doble descuento y movimientos
duplicados ante concurrencia o reintentos. El diseño DEBE definir la fuente de verdad
y la unidad transaccional que une descuento, despacho y auditoría. Las correcciones
DEBEN conservar el movimiento original y registrar su compensación. Una cadena
SHA-256 se DEBE describir como detección de alteraciones; por sí sola NO demuestra
inmutabilidad absoluta ni validez legal.

### III. Seguridad y responsabilidades por sede

Cada operación protegida DEBE comprobar identidad, permiso y ámbito de sede en el
backend. Las operaciones DEBEN identificar a sus responsables según una matriz de
permisos. Los secretos y datos reales de pacientes NO DEBEN incorporarse al
repositorio, ejemplos, pruebas ni logs. La primera versión se centra en inventario y
solicitudes internas; no incorpora historias clínicas ni dispensación clínica completa.
La verificación humana NO sustituye autenticación ni autorización.

### IV. Crecimiento y rendimiento demostrables

Tres clínicas son los datos iniciales de demostración, NO un límite funcional.
Agregar sedes y ubicaciones DEBE ser posible mediante datos y configuración, sin
editar código por cada incorporación. El objetivo de carga es 2 000 usuarios activos
simultáneos. Su evaluación DEBE definir mezcla de operaciones, ritmo, duración,
volumen de datos, distribución por sede y contención sobre lotes. Se DEBEN registrar
percentiles de latencia, errores e invariantes del inventario. Los tiempos p95 de
500 ms para consultas y 1 s para movimientos son candidatos por validar, NO resultados
obtenidos ni compromisos ya aprobados. Las pruebas locales NO demuestran por sí solas
la capacidad del despliegue remoto.

### V. Simplicidad, compatibilidad y costo verificable

La infraestructura DEBE priorizar Cloudflare y servicios sin costo adicional dentro
de cuotas verificadas; la renovación del dominio se reconoce por separado. Cada
componente DEBE responder a un requisito. La base propuesta es TypeScript, React,
Vite, Tailwind CSS, Hono, Zod, SQL y Drizzle; Workers y D1 son candidatos iniciales.
La persistencia y concurrencia DEBEN validarse mediante una prueba técnica antes de
cerrar la arquitectura. Durable Objects, KV, R2 y Workers AI requieren justificación.
KV NO DEBE decidir existencias ni elegibilidad de lotes en despachos críticos. Una
alternativa externa DEBE justificar compatibilidad, cuota gratuita y beneficio.

## Restricciones y alcance

- Proyecto individual de Alexander Gómez de la Cruz para IS-488, Arquitectura de
  Software, UNSCH, semestre 2026-II.
- Título: Sistema de Trazabilidad de Inventario Farmacéutico y Médico en una Cadena
  de Clínicas. Nombre de la aplicación: MedStock.
- Alcance de negocio: sedes, catálogo, recepción, lotes, solicitudes, FEFO, traslados,
  devoluciones, ajustes, bloqueos, consultas y auditoría. El análisis DEBE distinguir
  alcance completo y entregas incrementales.
- Las redes reales como Auna contextualizan la organización; no se asumen conocidos
  sus procesos internos. Las reglas farmacéuticas requieren fuentes oficiales
  aplicables y revisión de sus modificaciones.
- La fase actual es análisis; API detallada, SQL físico y despliegue son posteriores.

## Flujo de trabajo y revisiones

1. Trabajar en ramas temporales; `main` conserva la versión revisada.
2. Configurar Spec Kit en `chore/configurar-spec-kit`. Preparar después el análisis
   en `docs/analisis-inicial`, desde la base integrada.
3. Usar las skills oficiales para especificar y aclarar. Enlazar el análisis
   transversal con las especificaciones por función sin duplicar reglas normativas.
4. Revisar enlaces, identificadores, contradicciones y pendientes. Los criterios de
   aceptación DEBEN cubrir errores, alternativas y concurrencia cuando corresponda.
5. Abrir pull requests con alcance y validaciones. La integración en `main` queda a
   cargo de Alexander o de una instrucción explícita suya.

## Governance

Esta constitución rige el trabajo, sujeta a instrucciones explícitas del propietario.
Cada modificación DEBE explicar motivo e impacto en requisitos y documentos dentro
de un pull request. Se usa SemVer: MAJOR para principios incompatibles, MINOR para
nuevas obligaciones compatibles y PATCH para aclaraciones. Las revisiones DEBEN
comprobar integridad, permisos, trazabilidad, rendimiento y costo. Los pendientes
se registran explícitamente; no se completan con hechos inventados.

**Version**: 1.0.0 | **Ratified**: 2026-10-15 | **Last Amended**: 2026-10-15
