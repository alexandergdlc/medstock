"""Verifica referencias documentales y estructura de los modelos, no la aplicación."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from urllib.parse import unquote
root = Path(__file__).resolve().parents[1]
a = root / 'specs/analisis'
files = list(a.rglob('*.md')) + list((root/'docs').glob('*.md')) + [root/'README.md', root/'specs/001-trazabilidad-inventario/spec.md']
errors=[]; links=0
for p in files:
    s=p.read_text()
    assert 'tokens truncated' not in s, p
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',s):
        target=target.split('#')[0]
        if not target or re.match(r'[a-zA-Z]+:',target): continue
        links+=1
        if not (p.parent/unquote(target)).exists():errors.append(f'Enlace roto: {p.name}: {target}')
    rows=[]
    for line in s.splitlines()+['']:
        if line.startswith('|'):
            width=len(line.split('|'))
            if rows and width!=rows[-1]: errors.append(f'Tabla incoherente: {p.name}: {line[:70]}')
            rows.append(width)
        else: rows=[]
rftext=(a/'03-requisitos/08-requisitos-funcionales.md').read_text()
rf=re.findall(r'^## (RF-\d+) —',rftext,re.M)
rn=re.findall(r'^\| (RN-\d+) \|',(a/'02-negocio/07-reglas-del-negocio.md').read_text(),re.M)
cu=re.findall(r'^## (CU-\d+) —',(a/'04-casos-de-uso/10-casos-de-uso-e-historias.md').read_text(),re.M)
ca=re.findall(r'^\*\*(CA-\d+) —',rftext,re.M)+re.findall(r'^\| (CA-\d+) \|',(a/'06-calidad-y-validacion/15-trazabilidad-y-validacion.md').read_text(),re.M)
for label,ids,count in [('RF',rf,68),('RN',rn,46),('CU',cu,20),('CA',ca,94)]:
    if len(ids)!=count or len(set(ids))!=count:errors.append(f'{label}: conteo/duplicación {len(ids)}/{count}')
    known=set(ids)
    for p in files:
        for ref in set(re.findall(rf'\b{label}-\d{{3}}\b',p.read_text()))-known:errors.append(f'{p.name}: {ref} no definido')
trace=(a/'06-calidad-y-validacion/15-trazabilidad-y-validacion.md').read_text()
for block in re.split(r'\n## RF-',rftext)[1:]:
    id='RF-'+block[:3]; n=block[:3]
    for pattern in [r'\*\*Objetivo:\*\* OBJ-\d+',r'\*\*Caso:\*\* CU-\d+',r'\*\*Reglas:\*\* RN-\d+',rf'\*\*CA-{n} —']:
        if not re.search(pattern,block):errors.append(f'{id}: falta {pattern}')
    if len(re.findall(rf'^\| OBJ-\d+ \| {id} \|',trace,re.M))!=1:errors.append(f'{id}: matriz funcional incompleta')
for id in rn:
    if not re.search(rf'^\| {id} \| RF-',trace,re.M):errors.append(f'{id}: sin cobertura')
atlas=(a/'04-casos-de-uso/21-diagramas-de-casos-de-uso.md').read_text()
for id in cu:
    if len(re.findall(rf'^## {id} —',atlas,re.M))!=1:errors.append(f'{id}: gráfico ausente/duplicado')
ns={'b':'http://www.omg.org/spec/BPMN/20100524/MODEL','d':'http://www.omg.org/spec/BPMN/20100524/DI'}
bpmns=list((a/'diagramas/bpmn').glob('*.bpmn'))
for p in bpmns:
    doc=ET.parse(p); ids=[n.get('id') for n in doc.iter() if n.get('id')];known=set(ids)
    if len(ids)!=len(known):errors.append(f'{p.name}: IDs BPMN duplicados')
    nodes={n.get('id') for n in doc.iter() if n.tag.split('}')[-1] in ('task','startEvent','endEvent','exclusiveGateway')}
    lane_nodes=[n.text for n in doc.findall('.//b:flowNodeRef',ns)]
    if sorted(nodes)!=sorted(lane_nodes):errors.append(f'{p.name}: carriles incompletos')
    for n in doc.iter():
        for attr in ('sourceRef','targetRef','processRef','bpmnElement'):
            if n.get(attr) and n.get(attr) not in known:errors.append(f'{p.name}: referencia {attr} inválida')
    for node in nodes:
        if not any(n.get('bpmnElement')==node for n in doc.findall('.//d:BPMNShape',ns)):errors.append(f'{p.name}: nodo sin posición')
if len(bpmns)!=14:errors.append('Faltan procesos BPMN')
if errors:raise SystemExit('\n'.join(errors))
print(f'OK: {len(files)} MD revisados; {links} enlaces locales; 68 RF, 46 RN, 20 CU, 94 CA; 14 BPMN con referencias y carriles coherentes.')
print('No valida esquema BPMN XSD ni certifica semántica de negocio o pruebas de aplicación.')
