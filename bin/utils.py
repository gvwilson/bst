import yaml


def read_yaml(filename):
    '''Load and return a YAML file.'''
    with open(filename, 'r') as reader:
        return yaml.load(reader, Loader=yaml.FullLoader)


def report(title, **kwargs):
    '''Report items if present.'''
    assert len(kwargs) == 2, 'Must have two sets to report'
    left, right = kwargs.keys()
    onlyLeft = kwargs[left] - kwargs[right]
    onlyRight = kwargs[right] - kwargs[left]
    if (not onlyLeft) and (not onlyRight):
        return
    print(f'- {title}')
    if (onlyLeft):
        print(f'  - {left} but not {right}')
        for item in sorted(onlyLeft):
            print(f'    - {item}')
    if (onlyRight):
        print(f'  - {right} but not {left}')
        for item in sorted(onlyRight):
            print(f'    - {item}')
