import pytest
import yaml

def get_datas():
    with open("./date.yml") as f:
         datas = yaml.safe_load(f)
         add_datas = datas["adddatas"]
         add_ids = datas["addmyids"]
         sub_data = datas["subdatas"]
         sub_ids = datas["submyids"]
         mul_data = datas["muldatas"]
         mul_ids = datas["mulmyids"]
         div_data = datas["divdatas"]
         div_ids = datas["divmyids"]
         return [add_datas,add_ids,sub_data,sub_ids,mul_data,mul_ids,div_data,div_ids]


def add_function(a,b):
    return a + b

def sub_function(a,b):
    return a - b

def mul_function (a,b):
    return a * b

def div_function(a,b):
    return a / b



@pytest.mark.parametrize("a,b,expected",get_datas()[0],ids=get_datas()[1])
def test_add(a,b,expected):
    assert add_function(a,b) == expected


@pytest.mark.parametrize("a,b,expected",get_datas()[2],ids=get_datas()[3])
def test_sub(a,b,expected):
    assert sub_function(a,b) == expected


@pytest.mark.parametrize("a,b,expected", get_datas()[4], ids=get_datas()[5])
def test_mul(a, b, expected):
    assert mul_function(a,b) == expected


@pytest.mark.parametrize("a,b,expected",get_datas()[6],ids=get_datas()[7])
def test_div(a,b,expected):
    assert div_function(a,b) == expected


