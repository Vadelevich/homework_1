from homework_1.code2 import set_

def test_set_():
    assert set_({"a": {"b": {"c": 3}}}, ["a", "b", "c"], 4) == 4
    assert set_({"a": {"b": {"c": 3}}}, ['x', 'y', 'z'], 5) == 5


def test_set_2():
    assert set_({"a": {"b": {"c": 3}}}) == ''
    assert set_({"a": {"b": {"c": 3}}}, [], 5) == ''
    assert set_({"a": {"b": {"c": 3}}}, ["a", "b", "c"]) == 0

