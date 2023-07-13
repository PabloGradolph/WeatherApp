import json
import os
from weather.storage import Storage
from pytest import MonkeyPatch

def test_storage_in_json_is_generated():
    data_dict = {}
    for idx in range(100):
        data_dict[f"City {idx}"] = False
    Storage.store_in_json(data_dict)

    file_name = Storage.file_name
    assert os.path.exists(file_name)

def test_storage_in_json_is_correct():
    data_dict = {}
    for idx in range(100):
        data_dict[f"City {idx}"] = False
    Storage.store_in_json(data_dict)

    file_name = Storage.file_name
    with open(file=file_name, mode='r') as file:
        data = json.load(file)

    for key in data:
        assert key in data_dict
        assert data[key] == data_dict[key]

def test_retrieve_from_json_return_is_correct():
    result = Storage.retrieve_from_json()
    assert type(result) == dict

def test_storage_config_mapper_return_is_correct():
    result = Storage.storage_config_mapper()
    assert type(result) == dict

def test_read(monkeypatch: MonkeyPatch):

    def mocked_function() -> dict:
        return {f"City {idx}": False for idx in range(100)}

    monkeypatch.setattr(Storage, 'retrieve_from_json', mocked_function)

    # Ejecución
    result = Storage.read()

    # Verificación
    mocked_function_dict = mocked_function()
    for key in mocked_function_dict:
        assert key in result
        assert mocked_function_dict[key] == result[key]

def test_write():
    # Ejecución
    Storage.write({})

    file_name = Storage.file_name
    assert os.path.exists(file_name)