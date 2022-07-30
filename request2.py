import requests, os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        # yaUrl = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        # pathToFile = os.path.join(currentВirectory, 'FileForeUpload.txt')
        HEADERS = {"Authorization": f'OAuth {self.token}'}
        FILES = {"file": open(file_path, 'rb')}
        name = os.path.basename(file_path)
        print()

        params = {"path": name}

        response_url = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload", params=params, headers=HEADERS)

        url = response_url.json().get('href')

        response_upload = requests.put(url, files=FILES, headers={})

        if response_upload.status_code == 201:
            print('Файл успешно загружен на Я.Диск')
            return 'Файл успешно загружен на Я.Диск'

if __name__ == '__main__':

    currentВirectory = os.getcwd()

    path_to_file = os.path.join(currentВirectory, 'FileForeUpload.txt')
    token = 'myTkn'

    uploader = YaUploader(token)

    uploader.upload(path_to_file)
