# Especificaciones de MedStock

1. Leer la [constitución](../.specify/memory/constitution.md).
2. Revisar el [índice del análisis](analisis/00-indice-y-estado.md).
3. Consultar la [especificación base Spec Kit](001-trazabilidad-inventario/spec.md).
4. Revisar [checklist y pendientes](001-trazabilidad-inventario/checklists/requirements.md).

El análisis 0.1.0 es un borrador completo para revisión documental; no contiene
implementación ni valida procesos en campo. Los archivos canónicos de reglas y RF
están en `analisis/07-*` y `analisis/08-*`; las historias los incorporan por referencia.

La carpeta `001-trazabilidad-inventario` identifica la capacidad especificada. Su
nombre es independiente de la rama `docs/analisis-inicial`. El puntero local
`.specify/feature.json` no se versiona: en un nuevo clon se puede seleccionar la
capacidad dentro de Codex o preparar el puntero explícito al continuar.

Para establecer el puntero desde PowerShell, situado en la raíz del proyecto,
usar Python para producir UTF-8 sin BOM:

```powershell
python -c "import json,pathlib; pathlib.Path('.specify/feature.json').write_text(json.dumps(dict(feature_directory='specs/001-trazabilidad-inventario')), encoding='utf-8')"
```

Después, dentro del chat de Codex:

```text
$speckit-clarify Revisa la especificación de specs/001-trazabilidad-inventario y prioriza las políticas del primer incremento. No implementes la aplicación.
```

No ejecutar `$speckit-plan` ni `$speckit-implement` como sustituto de revisar las
políticas. Los contratos técnicos y decisiones se prepararán en una fase posterior.
