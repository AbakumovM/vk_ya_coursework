from pprint import pprint
import requests
from token_ya import token_ya_
from token_vk import token_vk_
from YaDi import YaUploader
from Vk_photo import VkPhoto 


if __name__ == '__main__':
    id = input('Введите свой id_vk: ')
    vk_man = VkPhoto(token_vk_)
    ya_man = YaUploader(token_ya_)
    vk_man.get_vk_photo(id)
    vk_man.write_json()
    ya_man.uploads_file_disc(vk_man, id)

