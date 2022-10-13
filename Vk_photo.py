import time
import json
import requests
from tqdm import tqdm
from progress.bar import Bar

class VkPhoto:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version='5.131'):
        self.params = {
            'access_token': token,
            'v': version    
        }
        self.all_photos = []
        

    def get_vk_photo(self, owner_id, count=5):
        get_vk_photo_url = self.url + 'photos.get'
        get_vk_photo_params = {'owner_id': owner_id, 'album_id': 'profile', 'extended': 1, 'photo_sizes': 0, 'count': 5}
        req = requests.get(get_vk_photo_url, params={**self.params, **get_vk_photo_params}).json()
        photo_list = req['response']['items']
        for i in tqdm(range(count), desc='Загрузка данных о фото..', unit_scale=1):
            time.sleep(0.33)
            self.all_photos.append({'file_names': str((photo_list[i])['likes']['count']) + '.jpg', 'id': (photo_list[i])['id'], 'sizes': max((photo_list[i])['sizes'], key=lambda size: size['type'])})
        return 
    

    def write_json(self, count=5):    
        with open('my_photo.json', 'w', encoding='utf-8') as f:
            itog = []
            bar = Bar('Записываю данные в файл my.photo.json', max=count)
            for i in self.all_photos:
                time.sleep(0.33)
                itog.append({'file_id': i['id'], 'file_name': i['file_names'], 'size': i['sizes']['type']})
                bar.next()
            json.dump(itog, f, ensure_ascii=False, indent=2)
            bar.finish()
        return    








