from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
import argparse


parser = argparse.ArgumentParser(description='Download images by using FlickrAPI.')
parser.add_argument('-k', '--key', default=None, required=True, help='Input your FlickrAPI KEY')
parser.add_argument('-s', '--secret', default=None, required=True, help='Input your FlickrAPI SECRET')
parser.add_argument('-n', '--name', default=None, required=True, help='Input the animalname you will download (monkey / boar / crow)')
args = parser.parse_args()

key = args.key
secret = args.secret
wait_time = 1

animalname = args.name
savedir = "../images/" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos', #画像を検索する
    sort = 'relevance', #関連度順にソートする
    safe_search = 1, #UIコンテンツは表示しない（アイコン、ボタンなど）
    extras = 'url_q, licence'
)

photos = result['photos']
pprint(photos)
