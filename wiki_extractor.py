import json
import argparse
from bs4 import BeautifulSoup
import requests
import time


def getresult(search_str, limit, filename):
    data = [] #To store the url and paragraphs
    i = 0 
    try:
        #attach the search string with the base url
        srch_url = 'https://en.wikipedia.org/w/index.php?title=Special:Search&limit=500&offset=0&ns0=1&search='+search_str
        
        page = requests.get(srch_url) #fetch result
    except:
        print("Search string is incorrect")  #print if some error occurs
    else:
        soup = BeautifulSoup(page.content, 'html.parser')  #parse the page content using bs4

        res = {} #to store the titles of the urls

        headings = soup.find_all('div', class_='mw-search-result-heading') #find all the titles available in the page

        for h in headings:  #store urls until the limit exceeds
            res[h.find('a').text] = h.find('a')['href']
            i+=1
            if i >= limit:
                break

    print(len(res),'urls found.')

    time.sleep(5)

    try:
        for url in res:
            search_page = 'https://en.wikipedia.org'+res[url]   #fetch the page
            search_content = requests.get(search_page)

            soup_pg = BeautifulSoup(search_content.content, 'lxml')  #parse the page in lxml format

            para = soup_pg.find_all('p')[1].text  #extract only the first paragraph

            data.append({'url':search_page,'paragraph':para})  #insert data into the list

            time.sleep(5) 
        
    except:
        print("Error fetching page")   

    finally:

        """
        create a file with the given filename 
        and convert the list to json 
        save the json file
        """

        write_to = open(filename,'w')
        serialized= json.dump(data, write_to, indent=3)
        write_to.close()


if __name__ == '__main__':

    #argument parser 
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-kw", "--keyword", help = "Keyword to be searched")
    parser.add_argument("-n", "--num_urls", help = "Number of urls")
    parser.add_argument("-o", "--output", help = "Output file name")
    
    args = parser.parse_args()

    if args.keyword == None or args.num_urls == None or args.output == None:
        print("Keyword, number of urls and output file name required.\nType python wiki_extractor.py -h for help.")

    else:
        search_str = args.keyword
        search_str = '+'.join(search_str.split(' ')).lower()

        limit = int(args.num_urls)

        filename = args.output

        if not filename.endswith('.json') :
            filename+='.json'

        getresult(search_str, limit, filename)

        print('Data saved in {}'.format(filename))