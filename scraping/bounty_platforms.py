from bs4 import BeautifulSoup as sp
import requests
import tldextract
import subprocess as ssp

# Sites list

def get_sites_list():
    """
    Get the list of bounty platforms from vulnerability lab and save them to a text file.
    :return:
    """
    url = "https://www.vulnerability-lab.com/list-of-bug-bounty-programs.php"
    webpage = requests.get(url=url) # send a get request
    soup = sp(webpage.content, 'html.parser')
    tables = soup.find_all('table')
    a_tags = tables[4].find_all('a')
    sites_list = open("bug-bounty-sites.txt", 'w')

    for a in a_tags:
        sites_list.write(a.get('href') + "\n")
    print("List of sites saved to bug-bounty-sites.txt")

def sanitize():
    """
    Sanitize the list of sites to get only the domain names.
    :return:
    """
    site_list = open("bug-bounty-sites.txt", "r")
    domain_list = open("bug-bounty-domains.txt", "w")

    for site in site_list.readlines():
        tld = tldextract.extract(site)
        domain_list.write(tld.domain + "." + tld.suffix + "\n")

def extract_keywords():
    domain_list = open("bug-bounty-domains.txt", "r")
    word_list = open("bug-bounty-wordlist.txt", 'w')

    for domain in domain_list.readlines():
        tld = tldextract.extract(domain)
        word_list.write(tld.domain + "\n")