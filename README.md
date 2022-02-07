# Data Engineering 

## Task 1 
The script `wiki_extractor.py` performs a Wikipedia search using the provided keyword, and returns urls of “n” related Wikipedia pages.

Working : 

1. Related keywords are fetched from the wikipedia search page using BeautifulSoup.
2. For each keyword returned from the previous step, visit each page and fetch only the first paragraph (again, using BeautifulSoup).
3. Store the url and paragraph in a dict -> `{'url':fetched_url, 'paragraph':'fetched_para'}`
4. Append the dict in a list and finally convert to JSON which will be saved separately with the user-defined file name. 


To run the program:
<br />
`python wiki_extractor.py --keyword=”Indian Historical Events” --num_urls=100 --output=”out.json”`
1. Enter the keyword to be searched
2. Mention the total number of urls requried
3. Mention the desired name for resultant JSON file.
