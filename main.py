from pprint import pprint

import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: "netology/test2505.txt"):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        response_data = response.json()

        href = response_data["href"]
        response = requests.put(href, data=open(path_to_file, 'rb'))
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ("test.txt")
    token = "y0_AgAAAAARsZOyAADLWwAAAADkJtSkE5aPnFuhRJ2OUS_JqT2T0TKPFgY"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)