import requests 
from bs4 import BeautifulSoup

#Declare Global Variables
last = ""
max = 1000
visited = []

#function: scrape(url, depth)
#Purpose: search through wikipedia pages depth first to find the target url.
#parameters:
#   url: the current url that the program scrapes
#   depth: The current depth of the search, ranges between 0-6
#Returns: 1 if successfull, 0 if unsuccessfull
def scrape(url, depth):
    #Check if search has gone too deep
    if depth == 7:
        return 0
    
    #Check if we are in a loop
    if url in visited:
        return 0
    
    print(url + " " + str(len(visited)))
    
    #Check if we have found the goal
    if url == last:
        print("-" * 25 + 'End Found!' + "-" * 25)
        print("The path is:")
        print(str(depth) + ". " + url)
        return 1
    
    #Check if we have reached the max searches
    if len(visited) > max:
        print("Greater than 100 attempts")
        return 1
    
    #Print the current page being scrapped
    for i in range(depth):
        print('\t', end='')
    visited.append(url)
    
    #Scrape the new page
    r = requests.get('https://en.wikipedia.org' + url)

    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find(id='bodyContent').find_all('a')
        
    if depth == 6:
        return 0
    
    #Search for new pages
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

        #Search new page
        if scrape(link['href'], depth + 1):
            print(str(depth) + ". " + url)
            return 1
        else:
            continue


print("------Wiki Scrape-----")

start = '/wiki/' + input("Please enter the end of the wikipedia page you wish to start with ( The part after /wiki/ ): ")

last = '/wiki/' + input("Please enter the end of the wikipedia page you wish to end with ( The part after /wiki/ ): ")

max = int(input("Please enter the max number of pages you would be willing to search through: "))

scrape(start, 0) == 1

print("\nExiting Program...\n")