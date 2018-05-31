from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
import argparse


parser = argparse.ArgumentParser(description='Download images by using FlickrAPI.')
parser.add_argument('-k', '--key', default=None, required=True)
parser.add_argument('-s', '--secret', default=None, required=True)
parser.add_argument('-n', '--name', default=None, required=True, help='monkey/crow/boar')
args = parser.parse_args()

key = args.key
secret = args.secret
wait_time = 0.5

animal_name = args.name
save_dir = "../images/" + animal_name

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text=animal_name,
    per_page=400,
    media='photos',  # 画像を検索する
    sort='relevance',  # 関連度順にソートする
    safe_search=1,  # UIコンテンツは表示しない（アイコン、ボタンなど）
    extras='url_q, licence'
)

photos = result['photos']
# 確認用
pprint(photos)


for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
    if i%10 == 0:
        print('downloaded {0} images.'.format(i))
