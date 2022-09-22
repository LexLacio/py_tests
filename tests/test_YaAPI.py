import pytest

import configparser

from YaAPI import YandexDisk

config = configparser.ConfigParser()
config.read("../settings.ini")

ya_token = config["Yandex_disk"]["token"]
ya_folder = config["Yandex_disk"]["ya_folder"]
expected = 201

fixture = [
    (ya_folder, ya_token, expected)
]


@pytest.mark.parametrize("folder_name, token, expected", fixture)
def test_multiplication_int(folder_name, token, expected):
    ya_client = YandexDisk(ya_token)
    result = ya_client.folder_creation(folder_name)
    assert result == expected
