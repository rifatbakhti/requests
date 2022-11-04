# Task 1

import requests

def superhero():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    heroes = response.json()
    heroes_dict = {}
    for hero in heroes:
        if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
            heroes_dict[hero['name']] = hero['powerstats']['intelligence']
    most_intelligence = max(heroes_dict)
    print(f'{most_intelligence} - {heroes_dict[most_intelligence]}')

if __name__ == '__main__':
    superhero()

# Task 2
import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def upload(self, file_path: str):
        """Метод загружает файлы на яндекс диск"""
        url = "http://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        response = response.json()

        href = response.get("href", "")
        result = requests.put(href, data=open("task_to_yadisk.txt", 'rb'))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "Netology/hometask_to_yadisk.txt"
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)