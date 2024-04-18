from typing import Final
import requests

API_KEY: Final[str] = '7ad42e7f204e7be557d6ac940a40d3de'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'

def shorten_link(full_link):
    payload = {'Key': API_KEY, 'short': full_link}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link = url_data['shortLink']
            print("Link: ", short_link)
        else:
            print("Error status: ", url_data['status'])


def main():
    link = input("Link: ")
    shorten_link(link)


if __name__=='__main__':
    main()