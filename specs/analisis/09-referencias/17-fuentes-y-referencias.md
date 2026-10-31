# Fuentes, alcance de evidencia y referencias

**Proyecto:** MedStock · **Versión:** 0.3.0 · **Fecha:** 2026-10-15

**Estado:** borrador de análisis para revisión del propietario. Decisiones del propietario aceptadas; detalles operativos pendientes según 14.

## Registro de procedencia

Consulta documental: 15 de octubre de 2026, America/Lima. Los enlaces dinámicos y
cuotas deberán comprobarse de nuevo al diseñar/desplegar. No se copiaron manuales
enteros ni imágenes de terceros al repositorio. Los modelos y políticas PP son
elaboración propia para MedStock.

| ID | Fuente | Uso limitado en este dossier |
|---|---|---|
| FU-001 | Acuerdos de Alexander en esta sesión de trabajo | Título, procesos aceptados, alcance ampliable y objetivo de 2 000 usuarios; no validación clínica externa |
| FU-002 | Sílabo IS-488 Arquitectura de Software, UNSCH 2026-II, entregado por Alexander | Proyecto incremental, requisitos/drivers, calidad y C4; no contiene rúbrica específica de esta fase |
| FU-003 | Auna, página oficial de sedes | Existencia de red multisede; no procedimientos internos ni métricas |
| FU-004 | MINSA/DIGEMID, página RM 554-2022 | Identifica el Manual de Buenas Prácticas de Oficina Farmacéutica; anexo completo no revisado |
| FU-005 | MINSA, RM 810-2024, texto publicado en El Peruano | Contexto de modificación y trazabilidad; no evaluación exhaustiva de vigencia/aplicabilidad |
| FU-006 | ISO, ficha pública ISO/IEC/IEEE 29148:2018 | Referencia de ingeniería de requisitos; no lectura íntegra ni declaración de conformidad |
| FU-007 | SEI, QAW tercera edición y material de escenarios | Identificar calidad antes de diseñar; no taller efectivamente realizado |
| FU-008 | Cloudflare, límites de Workers | Presupuesto de prueba: cuota gratuita consultada de 100 000 solicitudes/día |
| FU-009 | Cloudflare, precios D1 | Cuotas consultadas: 5 millones de filas leídas y 100 000 escritas/día; no equivalen a despachos |
| FU-010 | GitHub Spec Kit 1.2.0, skills oficiales instaladas | Estructura de especificación y checklist; herramienta y metodología no certifican el producto |

## Fuentes adicionales de la revisión 0.2.0

| ID | Fuente | Uso limitado |
| --- | --- | --- |
| FU-011 | DIRIS Lima Este, acta de inspección BPOF y hojas modificatorias | Entrega parcial en receta 7.5.2.27, p. 11; no extrapolar como obligación idéntica a solicitud interna |
| FU-012 | GERESA Arequipa, guía de inspección BPOF publicada en sitio oficial | Numerales 7.5.1.19/.20 (p. 7) y 7.5.1.27–.31 (p. 8): vencimientos, rotación y retorno; no reemplaza manual íntegro |
| FU-013 | Schwaber y Sutherland, Guía Scrum 2020 oficial | Responsabilidades y marco completo; sirve para comparar, no declarar adopción ya realizada |
| FU-014 | The Kanban Guide, edición mayo 2025 oficial | Visualización, control de flujo y mejora; gestión aceptada por Alexander; políticas de flujo y medidas |

## Citas utilizadas

Auna (s. f.) presenta establecimientos de su red en distintas ciudades; se toma solo
como referencia organizacional. MINSA (2022, 2024) aporta contexto sanitario de oficina
farmacéutica y trazabilidad. Las reglas particulares de unidades, fechas, parciales
y autorizaciones en MedStock son propuestas PP, no transcripciones normativas.

ISO (2018) orienta el ámbito de ingeniería de requisitos desde su ficha pública.
Barbacci et al. (2003) explican el trabajo temprano con atributos de calidad; aquí se
redactan escenarios, sin atribuir consenso a actores no entrevistados. GitHub (2026)
proporciona el flujo de especificación usado. Cloudflare (s. f.-a, s. f.-b) informa
cuotas que limitan la interpretación de un ensayo gratuito.

## Referencias bibliográficas (APA 7)

Auna. (s. f.). *Sedes Auna en Perú*. Recuperado el 15 de octubre de 2026, de
https://auna.org/pe/sedes

Barbacci, M. R., Ellison, R. J., Lattanze, A. J., Stafford, J. A., Weinstock, C. B.,
& Wood, W. G. (2003). *Quality attribute workshops (QAWs), third edition*
(CMU/SEI-2003-TR-016). Software Engineering Institute, Carnegie Mellon University.
https://doi.org/10.1184/R1/6582656.v1

Cloudflare. (s. f.-a). *Limits: Cloudflare Workers*. Recuperado el 15 de octubre de
2026, de https://developers.cloudflare.com/workers/platform/limits/

Cloudflare. (s. f.-b). *Pricing: Cloudflare D1*. Recuperado el 15 de octubre de 2026,
de https://developers.cloudflare.com/d1/platform/pricing/

GitHub. (2026). *Spec Kit* (Versión 1.2.0) [Software].
https://github.com/github/spec-kit/tree/v1.2.0

International Organization for Standardization. (2018). *ISO/IEC/IEEE 29148:2018:
Systems and software engineering — Life cycle processes — Requirements engineering*.
https://www.iso.org/standard/72089.html

Ministerio de Salud. (2022, 27 de julio). *Resolución Ministerial N.º 554-2022/MINSA*.
https://www.digemid.minsa.gob.pe/webDigemid/normas-legales/2022/resolucion-ministerial-n-554-2022-minsa/

Ministerio de Salud. (2024, 22 de noviembre). *Resolución Ministerial N.º 810-2024/MINSA:
Modifican el Documento Técnico: Manual de Buenas Prácticas de Oficina Farmacéutica*.
El Peruano. https://www.digemid.minsa.gob.pe/Archivos/Normatividad/2024/PERUANO_RM_810-2024-MINSA.pdf

Universidad Nacional de San Cristóbal de Huamanga. (2026). *Arquitectura de Software
[IS-488]: Sílabo, semestre 2026-II* [Material de curso proporcionado por el estudiante].

FU-001 es información de primera parte y no se presenta como publicación académica.
El sílabo está en los archivos suministrados por Alexander, no se inventa una URL pública.

## Verificación sanitaria pendiente

La revisión 0.2.0 añadió guías oficiales de inspección con numerales concretos
registrados en [correspondencia](20-correspondencia-minsa-digemid.md). Antes de
sostener aplicación profesional se debe revisar el anexo completo original de 2022,
sus modificaciones y el marco vigente de establecimientos farmacéuticos. La búsqueda
identificó también cambios posteriores del reglamento, que no se analizaron aquí.
La revisión documental parcial no certifica cumplimiento ni habilita uso asistencial.
Se debe identificar qué disposiciones corresponden a cada establecimiento y a los
productos concretos del alcance. Este punto se mantiene en PN-007.

## Referencias añadidas en 0.2.0 (APA 7)

Dirección de Redes Integradas de Salud Lima Este. (s. f.). *Acta de inspección de
buenas prácticas de oficina farmacéutica* [Guía e instrumentos modificatorios].
https://www.dirislimaeste.gob.pe/Virtual2/Otros_Link/DFCVS/ACTA%20DE%20INSPECCI%C3%93N%20BPOF%20ASF.pdf

Gerencia Regional de Salud Arequipa. (s. f.). *Guía de inspección de buenas prácticas
de oficina farmacéutica: Anexo N.º 4*.
https://saludarequipa.gob.pe/wp-content/uploads/2025/09/ACTA-GUIA-BPOF-6.0.22_ANEXO-4.pdf

Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide*.
https://scrumguides.org/scrum-guide.html

Orderly Disruption Limited, & Daniel S. Vacanti, Inc. (2025, 1 de mayo). *The Kanban
Guide*. https://kanbanguides.org/the-kanban-guide/

Las referencias nuevas se separan para facilitar revisión del cambio; en una
exportación académica se ordenará alfabéticamente la lista conjunta. No se afirma
una revisión exhaustiva de toda la normativa a partir de búsquedas parciales.

## Referencia institucional incorporada en 0.3.0

| ID | Fuente | Uso limitado |
|---|---|---|
| FU-015 | Hospital II-1 Rioja, página oficial de Farmacia | Ejemplo público de organización de farmacia central, emergencia, dosis unitaria y almacén; no prueba un modelo obligatorio ni procesos de una clínica privada |

Hospital II-1 Rioja. (s. f.). *Farmacia*. Recuperado el 15 de octubre de 2026, de
https://hospitalrioja.gob.pe/servicio/farmacia/

Las decisiones de topología, reserva después de autorizar y optimización son FU-001.
FU-015 contextualiza roles, no impone una farmacia única por sede. Las comparaciones
internacionales futuras deberán registrar país, institución, fecha y límites de uso;
no se presentan como normas peruanas ni entrevistas realizadas.
