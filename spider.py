import requests
import re
import urlparse


target_url = raw_input("Target URL : ")
target_links = []


def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)


def crawl(url):
    href_links = extract_links(target_url)
    for link in href_links:
        link = urlparse.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)
