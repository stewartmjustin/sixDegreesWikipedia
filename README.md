# Depth-First Six Degrees of Seperation WIkipedia

## Created By

Justin Stewart

> Email: stewartm.justin@outook.com

> Github: https://github.com/stewartmjustin

## How to use the program

**python3 must be installed to use this program.**

After downloading the program, it can be running by opening a terminal at the files location and typing

```
python3 SixDegreeWiki.py
```

It will then ask you to enter the two wikipedia pages you want to compare.
```
Please enter the end of the wikipedia page you wish to start with ( The part after /wiki/ ):

Please enter the end of the wikipedia page you wish to end with ( The part after /wiki/ ):
```

**Do not enter the entire link**, only the part after /wiki/.

This means instead of entering:
> https://en.wikipedia.org/wiki/Six_degrees_of_separation

Only enter:
> Six_degrees_of_separation

It will then ask you to enter how many pages you wish to visit.
```
Please enter the max number of pages you would be willing to search through:
```

The program will then run through wikipedia pages until it finds the page you are searching for or reach the set max number of searches.

## What is the Purpose of this Program?

As you might have noticed, depth first is a terrible way to search wikipedia.

This was an experiement on discovering how pages are connected and which pages are connected to what. I hope you enjoy messing around with it.

## How does it work

This program uses the <a href='https://requests.readthedocs.io/'>requests</a> and <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/'>BeautifulSoup</a> library's to scrape and naviage wikipedia pages for links and navigate through them.