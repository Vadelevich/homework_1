def get_val(collection, key, default=''):
    if key in collection.keys() and default == '': default = collection[key]
    else : default = default
    return default
