import csv
import requests
from http import HTTPStatus
from fake_useragent import UserAgent

def get_websites(csv_path):
    websites = []
    with open (csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if "https://" not in row[1] or "http://" in row[1]:
                websites.append(f"https://{row[1]}")
            else :
                websites.append(row[1])     
    return websites


def get_userAgent():
    ua = UserAgent()
    return ua.edge


def description(code):
    for value in HTTPStatus:
        if value == code:
            description = f'({value} {value.name}) {value.description}'
            return description
    return '(???) Unknown status code.'
        

def check_website(website, user_agent):
    try:
        code = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, description(code))
    except requests.RequestException:
        print(f'Could not get information form website: {website}')


def main():
    sites = get_websites('websites.csv')
    userAgent = get_userAgent()
    for i, site in enumerate(sites):
        check_website(site, userAgent)


if __name__ =='__main__':
    main()