import yaml
def cargar_autoconfig(path='autoconfig/autoconfig.yaml'):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
