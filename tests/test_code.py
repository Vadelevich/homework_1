from homework_1.code import get_val
def test_get_val():
    assert get_val({"hello": "world" }, "hello") == 'world'
    assert get_val({ "hello": "world" }, "hello", "python") == 'python'
    assert get_val({}, "hello", "python") =='python'

def test_get_val_2():
    assert get_val({},'','') == ''
