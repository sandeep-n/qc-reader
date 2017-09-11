#!/usr/bin/env python
# Downloads images from Questionable Content - either all at once, or between specified issue numbers.

import requests
import os
from bs4 import BeautifulSoup

qc_url = 'http://questionablecontent.net/view.php?comic=3560'
response = requests.get(qc_url)
qc_soup = BeautifulSoup(response.text)
strip = qc_soup.select('a #strip')
img_url = strip[0].attrs['src'][1:]
tld = 'http://questionablecontent.net'

image_file = open(os.path.join(os.getcwd(), 'test-data', 'comic.png'), 'wb')


def get_qc_strip(strip_num):
    """
    Get image file of specified QC strip
    :param strip_num: Strip number
    :type strip_num: int
    :return: ?
    """
    COMIC_HOME = 'http://questionablecontent.net'
    URL_PREFIX = 'http://questionablecontent.net/view.php?comic='
    strip_url = URL_PREFIX + str(strip_num)

    strip_soup = BeautifulSoup(requests.get(strip_url).text)
    image_loc = strip_soup.select('a #strip')[0].attrs['src'][1:]
    response = requests.get(COMIC_HOME + image_loc)

    return response


for strip_num in range(1, 3565):
    image_file = open(os.path.join(os.getcwd(), 'data', 'qc' + str(strip_num) + '.png'), 'wb')
    res = get_qc_strip(strip_num)
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    print('Strip number {} downloaded'.format(strip_num))
    image_file.close()


def scrape_archives():  # TODO implement
    """
    Looks at QC archive page to get a list of comics. Avoids hardcoding of issue number.
    """


def main():
    pass

if __name__ == '__main__':
    main()
