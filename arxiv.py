'''

Testing arXiv's API and parsing the strings 

'''

from random import shuffle

import urllib2
from bs4 import BeautifulSoup 


def scrapeNewFeed(): 
    '''
    '''
    page = urllib2.urlopen('https://arxiv.org/list/astro-ph/new/') 
    soup = BeautifulSoup(page, "html.parser")

    urls = []
    for dt in soup.find_all('dt'): 
        urls.append(''.join(['https://arxiv.org', dt.span.a['href']]))
    
    arxiv_entries = [] 
    for i_dd, dd in enumerate(soup.find_all('dd')): 
        arxiv_entry = {} 
        
        for attr in ['title', 'comments', 'subjects']: 
            if attr == 'title': 
                attr_name = 'title mathjax'
            else: 
                attr_name = attr 

            for div in dd.find_all('div', "list-"+attr_name): 
                arxiv_entry[attr] = div.prettify().split('</span>')[-1].split('</div>')[0]
    
        # authors
        arxiv_entry['authors'] = [] 
        for div in dd.find_all('div', "list-authors"):
            for auth in div.find_all('a'): 
                arxiv_entry['authors'].append(auth.string)  
        arxiv_entry['authors_str'] = ', '.join(arxiv_entry['authors'])
        # abstract 
        try: 
            arxiv_entry['abstract'] = unicode(dd.p.string)
        except AttributeError: 
            arxiv_entry['abstract'] = '' 
        arxiv_entry['url'] = urls[i_dd]

        arxiv_entries.append(arxiv_entry)
   
    assert len(urls) == len(arxiv_entries)
    shuffle(arxiv_entries)
    return arxiv_entries

if __name__=='__main__': 
    scrapeNewFeed()
