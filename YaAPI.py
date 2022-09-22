import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def folder_creation(self, folder_name):

        """Функция создаёт папки на ya.disk"""

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/"
        headers = self.get_headers()
        params = {"path": folder_name}
        response = requests.put(upload_url, headers=headers, params=params)
        if response.status_code == 201:
            print(f'Папка {folder_name} cоздана на Яндекс диске. Код {response.status_code}')
            return response.status_code
        else:
            print(f'Папка {folder_name} cоздана на Яндекс диске. Ошибка {response.status_code}')
            return response.status_code
