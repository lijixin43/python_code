# AUTHOR lijixin

import collections
def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        if (type(v) == type([])):
            for i in v:
                items.extend(flatten(i,k, sep=sep).items())
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

if __name__ == '__main__':
    dict01 = {'a': '1', 'b': '2', 'm': [{'c': 'li', 'age': 18, 'error': []}, {'c': 'li', 'age': 18,'error': []}],
          'd': {'hobby': {'hight': 172, 'hobby': 160}, 'sex': 'w', 'error1': []}
          }

    for k,v in dict01.items():
        if len(v)!=1: