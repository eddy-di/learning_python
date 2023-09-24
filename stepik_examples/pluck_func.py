def pluck(data, path, default=None):
    if not isinstance(data, dict) or not path:
        return default
    
    key = path[0]
    if key in data:
        if len(path) == 1:
            default = data[key]
            return default
        else:
            return pluck(data[key], path[2:], default=None)
    else:
        return default
        
d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.b.c'))