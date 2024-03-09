import os
import requests

def get_extension(url_name):
    extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg']
    for ext in extensions:
        if ext in url_name:
            return ext
        

def download_image(url, name, folder=None):
    if ext:=get_extension(url):
        if folder:
            image_name = f'{folder}/{name}{ext}'
        else:
            image_name = f'{name}{ext}'
    else:
        raise Exception("Image extension cannot be located.")
    
    try:
        image_content = requests.get(url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded {image_name} successfully')
    except Exception as e:
        print(f'Error{e}')


if __name__ == '__main__':
    
    input_url = input("Url: ")
    input_name = input("Name: ")
    print("Downloading...")

    download_image(input_url, input_name, folder='images')
