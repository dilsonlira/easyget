#!/usr/bin/env python

from requests import get


def download_file(url):
    """Downloads file from url"""

    # TODO: Validate url
    # TODO: Improve file_name extraction from url
    # TODO: Add HTTP headers support
    # TODO: Add folder support
    # TODO: Add unit tests

    file_name = ''

    if '/' in url:
        file_name = url.split('/')[-1]

    with open(file_name, 'wb') as file:
        response = get(url)
        if response.ok:
            file.write(response.content)
        else:
            print('error ' + str(response.status_code))

    return file_name


def main():
    """ """

    url_list = [
        'https://raw.githubusercontent.com/dilsonlira/project_euler/master/pe010.py',
        'https://klauslaube.com.br/2016/04/26/o-simples-e-poderoso-pyenv.html',
        'https://upload.wikimedia.org/wikipedia/commons/8/81/Capitanias.jpg',
        'https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_1920_18MG.mp4',
        'https://www.bbc.com'
    ]

    for url in url_list:
        print(f'file_name: {download_file(url)}')

if __name__ == '__main__':
    main()