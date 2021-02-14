import yaml


def read_yaml(filename):
    '''Load and return a YAML file.'''
    with open(filename, 'r') as reader:
        return yaml.load(reader, Loader=yaml.FullLoader)


def report(title, items):
    '''Report items if present.'''
    if (items):
        print(title)
        for item in sorted(items):
            print(f'-  {item}')
