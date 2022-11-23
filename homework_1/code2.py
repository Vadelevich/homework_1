def split(data):
    """Функция делает рекурсивное вложение словарей"""
    if len(data) == 0:
        return data
    else:
        first_value = data[0]
        coll = ({first_value: split(data[1:])})
        return coll


def set_(coll, path=[], value=0):
    """ Функция рекурсивно пробегается по существующему словарю и меняет значение в конце. Если таких ключей нет вызывает функцию создания нового словаря"""
    if path == []: return ''
    if path[0] not in coll.keys():
        new_coll = split(path)
        coll = coll | new_coll
    coll = coll[path[0]]
    if len(path) == 2:
        coll[path[1]] = value
        return value
    return set_(coll, path[1:], value)
