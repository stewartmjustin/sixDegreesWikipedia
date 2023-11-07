import requests 
from bs4 import BeautifulSoup

last = ""
max = 1000
visited = []

def scrape(url, depth):
    if depth == 7:
        return 0
    
    if url in visited:
        return 0
    
    print(url + " " + str(len(visited)))
    
    if url == last:
        print("PASS")
        return 1
    
    if len(visited) > max:
        print("Greater than 100 attempts")
        return 1
    
    for i in range(depth):
        print('\t', end='')
    
    visited.append(url)
    
    r = requests.get('https://en.wikipedia.org' + url)

    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find(id='bodyContent').find_all('a')

    for link in links:
        if url == last:
            print("PASS")
            return 1
        
    if depth == 6:
        return 0

    for link in links:
        if len(visited) > max:
            break
        if not link.has_attr('href'):
            continue
        if not link.has_attr('title'):
            continue
        if not link['href'].startswith('/wiki/'):
            continue
        if link['href'].startswith('/wiki/Wikipedia'):
            continue
        if link['href'].startswith('/wiki/File'):
            continue
        if link['href'].startswith('/wiki/Template'):
            continue
        if link['href'].startswith('/wiki/Special'):
            continue
        if link['href'].startswith('/wiki/Category'):
            continue
        if link['href'].startswith('/wiki/Help'):
            continue
        if scrape(link['href'], depth + 1):
            break
        else:
            continue


print("------Wiki Scrape-----")

start = '/wiki/' + input("Please enter the end of the wikipedia page you wish to start with ( The part after /wiki/ ): ")

last = '/wiki/' + input("Please enter the end of the wikipedia page you wish to end with ( The part after /wiki/ ): ")

max = int(input("Please enter the max number of pages you would be willing to search through: "))

scrape(start, 0) == 1