'''
This is a training with bs4 and requests where
we are getting the a['href'] of the representatives 
that has press_releases containing 'data' in the text
'''

from bs4 import BeautifulSoup
import requests

import re

from typing import Dict, Set


def paragraph_mentions(
        text: str,
        keyword: str
    ) -> bool:
    """
    Return True if there's a '<p> that mentions {keyword} in the text
    Args.:
        text: str - html web path
        keyword: str - word we are searching / using to filter
    """
    soup = BeautifulSoup(text, 'html5lib')
    paragraphs = [p.get_text() for p in soup('p')]
    return any(keyword.lower() in paragraph.lower() for paragraph in paragraphs)


html_url = "https://www.house.gov/representatives"
html = requests.get(html_url).text
soup = BeautifulSoup(html, 'html5lib')

all_urls = [a['href'] for a in soup('a') if a.has_attr('href')]
regex = r"^https?://.*\.house\.gov/?$"
good_urls = [url for url in all_urls if re.match(regex, url)]

press_releases: Dict[str, Set[str]] = {}
for url in good_urls:  # only 50
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower() and a['href'] != set()}
    press_releases[url] = links

for house_url, links in press_releases.items():
    for link in links:
        url = f"{house_url}/{link}"
        text = requests.get(url).text
        if paragraph_mentions(text, 'data'):    # keyword = data
            print(f'{house_url}')

'''
https://obernolte.house.gov
https://rivas.house.gov/
https://rutherford.house.gov
https://clyde.house.gov
https://davidscott.house.gov/
https://mann.house.gov
https://pressley.house.gov
https://vandrew.house.gov
https://menendez.house.gov
https://morelle.house.gov
https://morelle.house.gov
https://edwards.house.gov
https://latta.house.gov/
https://perry.house.gov/
https://johnjoyce.house.gov/
https://harshbarger.house.gov
https://moran.house.gov
https://beyer.house.gov
'''
