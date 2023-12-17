import re

path_template = './template.tex'
path_output = './output.tex'

path_componente = './cvevent.template'
cv_event_componente = open(path_componente, 'r').read()
print(cv_event_componente)

project_component = ''
items = [("@TIME", "20XX"), ("@TIME", "19XX")]
for item in items:
    project_component += cv_event_componente.replace(item[0], item[1]) + '\n\n'

#load_componente = cv_event_componente.replace("@TIME", "20XX")

with open(path_template, 'r') as f:
    template = f.read()
    substring = '%{PROJECTS}%'
    template = template.replace(substring, project_component)
    print(template)

open(path_output, 'w').write(template)