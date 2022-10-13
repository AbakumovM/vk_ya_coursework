import time
import requests
from progress.bar import Bar
from pprint import pprint




class YaUploader():
    
    def __init__(self, token):
        self.token = token


    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }


    def get_folder_in_path(self, path):
        url_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        respons = requests.get(url_upload, headers=headers, params=params)
        return respons


    def create_folder(self, file_path):
        url_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        respons = requests.put(url_upload, headers=headers, params=params)
        return respons.json()   


    def upl_photo(self, url, file_path):
        url_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'url': url, 'overwrite': 'true'}  
        response = requests.post(url_upload, headers=headers, params=params) 
        return 'готово'


    def import_photo_yadi(self, vk, path):
        bar = Bar('Загрузка фото на Яндекс.Диск..', max=5)
        for j in vk.all_photos:
            time.sleep(0.33)
            self.upl_photo(j['sizes']['url'], f"{path}/{j['id']}")
            bar.next()    
        return 'Фото загрузил'    


    def uploads_file_disc(self, vk, id):
        folder_path = input('Введите название папки, куда загрузить фото: ')
        if not self.get_folder_in_path(folder_path) == True:
            self.create_folder(folder_path)
        self.import_photo_yadi(vk, folder_path)    


    
   
    