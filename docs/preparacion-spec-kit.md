# Preparación y uso de Spec Kit

## Lo que ya contiene el repositorio

Spec Kit 1.2.0 inicializado con la integración `codex` y scripts principales Python.
Los scripts Bash incluidos son el fallback generado en el entorno Linux de
preparación. Para el uso en Windows se priorizan las rutas Python de las skills.
La ejecución en Windows aún requiere comprobación en la computadora de Alexander.

Los archivos del proyecto están en GitHub, pero eso no instala Python, uv, Codex
ni la herramienta `specify` en la computadora del usuario.

## Preparar Windows

Abrir la terminal PowerShell de VS Code dentro del clon de `medstock` y comprobar:

```powershell
git --version
python --version
uv --version
codex --version
```

Se requiere Python 3.11 o superior. Si falta una herramienta, seguir su instalador
oficial y abrir una terminal nueva antes de repetir la comprobación:

- [Python](https://www.python.org/downloads/).
- [uv](https://docs.astral.sh/uv/getting-started/installation/).
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli).

Instalar la misma versión de Specify CLI usada para preparar el repositorio:

```powershell
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@v1.2.0
specify version
specify integration status
```

Si `specify` no aparece en PATH, seguir el aviso de `uv` para actualizar la ruta de
herramientas y abrir una terminal nueva. No volver a ejecutar `specify init --force`
sobre este clon: la configuración ya está versionada y debe revisarse antes de
cualquier actualización.

## Abrir Codex

Ejecutar `codex` dentro de la carpeta `medstock` e iniciar sesión con la cuenta de
ChatGPT. La instalación de Spec Kit no instala Codex ni concede uso ilimitado del
asistente. Reiniciar la sesión de Codex si las skills recién incorporadas no aparecen.

Las skills se invocan en el chat del agente, NO en PowerShell. Ejemplo de entrada:

```text
$speckit-clarify Revisa las ambigüedades de la especificación de recepción por lote.
```

Ese ejemplo requiere que exista la especificación correspondiente; todavía no existe
en esta rama de preparación. No ejecutar pasos técnicos sin sus documentos previos.

## Orden de uso

| Paso | Skill en Codex | Momento |
|---|---|---|
| Principios | `$speckit-constitution` | Ya se redactó la constitución inicial; revisar mediante PR |
| Especificar | `$speckit-specify` | Definir comportamiento por funcionalidad |
| Aclarar | `$speckit-clarify` | Resolver ambigüedades antes del diseño |
| Planificar | `$speckit-plan` | Fase técnica posterior al análisis |
| Desglosar | `$speckit-tasks` | Con un plan técnico disponible |
| Consistencia técnica | `$speckit-analyze` | Cuando existan spec, plan y tasks |
| Implementar | `$speckit-implement` | Tras definir y revisar el trabajo |
| Contrastar resultado | `$speckit-converge` | Con implementación disponible |

El análisis transversal de `specs/analisis/` complementará las especificaciones por
funcionalidad. Spec Kit no genera por sí solo un dossier académico completo.

## Procedencia y reproducción

- Fuente: [github/spec-kit, etiqueta v1.2.0](https://github.com/github/spec-kit/tree/v1.2.0).
- Commit: `4ca46a0706a662b1edc07086ef16f021820c2db0`.
- Licencia de archivos oficiales: [MIT de GitHub](../.specify/UPSTREAM-LICENSE.txt).
- Inicialización efectuada en un clon que solo contenía el README inicial:

```text
specify init --here --force --non-interactive --integration codex --script py --ignore-agent-tools
```

`--ignore-agent-tools` omitió comprobar el ejecutable de Codex en el entorno de
preparación; no prueba que esté instalado en Windows. `--force` se usó sobre el
clon limpio y no constituye una recomendación para futuras actualizaciones.

Las skills, scripts y plantillas oficiales se mantienen sin modificaciones. La
constitución es contenido propio generado sobre su plantilla. La herramienta CLI
fue instalada en el entorno de preparación; no es una instalación en GitHub como
servidor ni en el equipo del usuario.
