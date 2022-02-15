import sys, yaml

with open('rendered_wano.yml') as file:
        wano_file = yaml.full_load(file)

file_name = "Stop-msg"
with open(file_name, 'w') as f:
    f.write(wano_file["Stop-msg"]+'\n')
