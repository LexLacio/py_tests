import configparser

from YaAPI import YandexDisk

config = configparser.ConfigParser()
config.read("settings.ini")

ya_token = config["Yandex_disk"]["token"]
ya_folder = config["Yandex_disk"]["ya_folder"]

if __name__ == '__main__':
    ya_client = YandexDisk(ya_token)
    new_folder = ya_client.folder_creation(ya_folder)


