__author__ = "Foleevora"
__version__ = "1.0.0"
__email__ = "foleevora@gmail.com"

import sys
import urllib.request
from bs4 import BeautifulSoup

def parsing(url):
    req = urllib.request.Request(url)
    data = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data, 'html.parser')

    title = "Title          : " + soup.find(id='eow-title').get_text().strip()
    uploader = "Uploader       : " + soup.find(class_='yt-user-info').find('a').get_text().strip()
    view_count = "View Count     : " + soup.find(class_='watch-view-count').get_text().strip()[4:]
    like = "Like Count     : " + soup.find_all(class_='like-button-renderer-like-button')[0].find('span').get_text().strip() + " 회"
    dislike = "Dislike Count  : " + soup.find_all(class_='like-button-renderer-dislike-button')[0].find('span').get_text().strip() + " 회"
    post_day = "Post Day       : " + soup.find(class_='watch-time-text').get_text().strip()[5:]
    category = "Category       : " + soup.find(class_='content watch-info-tag-list').find_all('li')[0].find('a').get_text().strip()

    print(title)
    print(uploader)
    print(view_count)
    print(like)
    print(dislike)
    print(post_day)
    print(category)


if __name__ == "__main__":

    if len(sys.argv) is not 2:
        print("UASGE: YoutubesongInfo.py [Url]")
    else:
        parsing(sys.argv[1])
