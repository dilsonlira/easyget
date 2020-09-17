#!/usr/bin/env python

from requests import get


def get_content(url, success_logs=True):
    """Returns content from url"""

    # TODO: Validate url
    # TODO: Improve file_name extraction from url
    # TODO: Add HTTP headers support
    # TODO: Add folder support
    # TODO: Add unit tests

    if url:
        try:
            response = get(url)
            if response.ok:
                content = response.content
                if success_logs:
                    print(url)
                    print(f'{len(content)} bytes successfully received.')

                return content

            print(f'Error {response.status_code}')
        
        except:
            print('Connection Error')

        return ''


def download_file(url):
    """Downloads file from url"""

    file_name = ''

    if '/' in url:
        file_name = url.split('/')[-1]

    data_folder = 'data/'

    file_path = data_folder + file_name

    with open(file_path, 'wb') as file:
        content = get_content(url, success_logs=False)
        file.write(content)

    return file_path


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