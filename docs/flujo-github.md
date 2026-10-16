# Flujo de GitHub para MedStock

## Ramas

`main` contiene la versión revisada. Cada cambio coherente se prepara en una rama
temporal y se presenta mediante un pull request. No se necesita `develop` permanente.

1. `chore/configurar-spec-kit`: configuración y principios iniciales.
2. Integrar su PR tras revisión de Alexander.
3. `docs/analisis-inicial`: documentos de análisis desde `main` actualizado.
4. Revisar el segundo PR y corregir observaciones.
5. Integrar y etiquetar una entrega de análisis cuando esté revisada.

El nombre de una rama no representa la aprobación del contenido. Los commits y PR
deben describir cambios concretos y sus comprobaciones.

## Primera copia local en Windows

Después de integrar la preparación, abrir PowerShell en la carpeta donde se guardan
los proyectos y ejecutar:

```powershell
git clone https://github.com/alexandergdlc/medstock.git
cd medstock
code .
```

Si la preparación sigue pendiente, se puede inspeccionar su rama con:

```powershell
git fetch origin
git switch --track origin/chore/configurar-spec-kit
```

No crear otra copia si ya existe un clon con trabajo local. Revisar `git status`
antes de cambiar de rama o actualizar.

## Comenzar el análisis después de integrar la preparación

```powershell
git switch main
git pull --ff-only origin main
git switch -c docs/analisis-inicial
```

Preparar commits por bloques completos de documentación. Revisar `git diff` y
seleccionar los archivos con `git add` antes de cada commit. Para publicar la rama:

```powershell
git push -u origin docs/analisis-inicial
```

Crear un PR con `base: main` y `compare: docs/analisis-inicial`, indicando alcance,
criterios de revisión y pendientes. Eliminar la rama después de integrarla.

Si Git pide nombre y correo, configurar los datos propios de Alexander; no usar
datos inventados ni la identidad de otra persona. El asistente publicará cambios
mediante la conexión GitHub autorizada cuando las herramientas lo permitan.

## Relación con Spec Kit

Las ramas de configuración y análisis transversal son convenciones de MedStock.
Al especificar funcionalidades, revisar los mensajes de Spec Kit y cualquier
automatización Git instalada antes de crear ramas: no asumir que todos sus comandos
conservan o cambian la rama automáticamente.
