# MedStock

**Sistema de Trazabilidad de Inventario Farmacéutico y Médico en una Cadena de Clínicas.**

Proyecto individual de **Alexander Gómez de la Cruz**, UNSCH, IS-488 Arquitectura de
Software, semestre 2026-II. Desarrollo guiado por especificaciones (SDD) con GitHub
Spec Kit y Codex, y gestión del flujo con Kanban.

## Estado actual

Análisis inicial 0.2.0 preparado para revisión, con Spec Kit configurado. Incluye
21 documentos de análisis, 64 requisitos funcionales, 42 reglas de negocio, 19 casos
de uso y 90 criterios/escenarios de aceptación. La aplicación y las pruebas de carga
todavía no están implementadas.

La cadena debe admitir nuevas sedes por configuración. Tres clínicas serán los datos
iniciales de demostración. El objetivo de 2 000 usuarios activos simultáneos requiere
un perfil de carga y evidencia; no es capacidad ya demostrada.

## Documentación para comenzar

- [Comenzar por el análisis](specs/analisis/00-indice-y-estado.md).
- [Especificación base Spec Kit](specs/001-trazabilidad-inventario/spec.md).
- [Revisión del análisis](docs/revision-analisis.md).
- [Principios del proyecto](.specify/memory/constitution.md).
- [Preparación en Windows y uso de Spec Kit](docs/preparacion-spec-kit.md).
- [Trabajo con ramas y pull requests](docs/flujo-github.md).
- [Mapa del próximo entregable de análisis](docs/mapa-analisis.md).
- [Registro de comprobaciones de la preparación](docs/verificacion-configuracion.md).
- [Instrucciones para asistentes](AGENTS.md).

## Alcance de negocio acordado

Sedes y ubicaciones; catálogo de medicamentos e insumos médicos; recepción por lote;
existencias; solicitudes internas; reservas explícitas; despacho FEFO; traslados; devoluciones; ajustes;
bloqueo y retiro de lotes; consultas consolidadas; auditoría verificable.

El análisis distinguirá alcance completo y entregas incrementales. Las historias
clínicas y la dispensación clínica completa no forman parte de la primera versión.

## Base tecnológica propuesta

TypeScript, React, Vite, Tailwind CSS, Hono, Zod, SQL y Drizzle. Cloudflare es la
plataforma prioritaria; Workers y D1 son candidatos iniciales. Los límites gratuitos,
la transacción de despacho y el rendimiento se validarán antes de cerrar decisiones.
Durable Objects, KV, R2 y Workers AI son opcionales y requieren justificación.

## Organización SDD

| Ubicación | Responsabilidad |
|---|---|
| `.specify/memory/constitution.md` | Principios del proyecto |
| `.specify/templates/` | Plantillas oficiales; no son requisitos de MedStock |
| `.specify/scripts/` | Automatización oficial de Spec Kit |
| `.agents/skills/` | Skills oficiales para Codex |
| `docs/` | Guías de trabajo y evidencias de preparación |
| `specs/analisis/` | Análisis transversal y sus modelos |
| `specs/<numero>-<funcionalidad>/` | Especificación base y futuras capacidades |

Las reglas y RF normativos están en el dossier de análisis; la especificación
base los incorpora por referencia, sin copias divergentes.

## Herramienta incorporada

Spec Kit **1.2.0**, origen `github/spec-kit`, etiqueta `v1.2.0`, commit
`4ca46a0706a662b1edc07086ef16f021820c2db0`. Integración `codex`, scripts Python y
fallback Bash. Sus archivos distribuidos conservan la
[licencia MIT de GitHub](.specify/UPSTREAM-LICENSE.txt).
Esta licencia de terceros no asigna una licencia al código propio de MedStock.
