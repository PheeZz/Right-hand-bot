from pprint import pprint
from bs4 import BeautifulSoup
import requests as req


def get_description(link: str) -> str:
    """Get description from link"""
    page = req.get(link)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'lxml')
        description = soup.find('title').getText()
        # description = [line for line in description.splitlines(
        # ) if line != '' and line != ' ' and line != '⠀']
        # string = '\n'.join(description)
        return description
    else:
        return '🔴Error. code: ' + str(page.status_code)


if __name__ == '__main__':
    print(get_description(
        'https://www.instagram.com/p/CdJFIDmqll8/?utm_source=ig_web_copy_link'))
