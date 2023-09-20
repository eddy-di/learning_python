def pluck(data, path, default=None):
    if len(path) > 1:
        path = path.split('.')
        def yield_from_data(dictionary):
            for key, value in dictionary.items():
                yield key, value
        indexes = 0
        for key, value in yield_from_data(data):
            if path[indexes] == key and indexes <= len(path):
                default = value
                indexes += 1
            else:
                return default
    elif len(path) == 1:
        default = data[path]
        return default
    else:
        return default
        
d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'a.b'))