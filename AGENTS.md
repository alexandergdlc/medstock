# Instrucciones de trabajo para MedStock

## Contexto

Leer primero `README.md` y `.specify/memory/constitution.md`. El propietario es
Alexander. La fase actual es preparación y análisis, sin autorización implícita
para desplegar infraestructura o implementar la aplicación.

## Especificaciones

- Escribir documentos propios en español. Mantener nombres y contenido oficiales
  de las skills y plantillas de Spec Kit.
- Antes de cambios de negocio, leer los documentos afectados y sus referencias.
- No inventar entrevistas, procesos de Auna, métricas obtenidas ni cumplimiento legal.
- Diferenciar hecho documentado, decisión aceptada, propuesta y pendiente.
- Usar IDs estables para requisitos, reglas, casos de uso y criterios de aceptación.
- Mantener una fuente normativa por regla y enlazarla desde otros documentos.
- Los 2 000 usuarios concurrentes son una meta, no una medición. El perfil de carga
  y los tiempos p95 todavía requieren validación.
- La base tecnológica es propuesta. No asumir transacciones distribuidas entre D1
  y Durable Objects ni usar KV para confirmar inventario.

## Git y comprobaciones

- Trabajar en una rama temporal y abrir PR hacia `main`; no integrar en `main`
  sin instrucción de Alexander.
- No sustituir cambios ajenos ni usar actualizaciones forzadas del historial.
- Antes del PR, revisar `git diff --check`, enlaces locales y ausencia de secretos.
- Para documentos, comprobar consistencia y trazabilidad; no crear pruebas de
  aplicación ficticias. Para código futuro, ejecutar pruebas relevantes al cambio.
- No versionar entornos, credenciales, archivos `.env` ni estado local del agente.
  Las skills oficiales de `.agents/skills/` sí son parte del repositorio.

## Spec Kit

Usar las skills oficiales desde Codex. `specify` prepara el proyecto, mientras que
`$speckit-*` se invoca en la conversación del agente, no en PowerShell. Si cambia
la versión de Spec Kit, registrar versión, origen e impacto en un PR específico.
La skill `speckit-analyze` compara spec, plan y tasks: no sustituye la revisión del
análisis de negocio cuando esos documentos técnicos todavía no existen.
