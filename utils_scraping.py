# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup,SoupStrainer 
import requests
import requests.exceptions
import codecs
from urllib.parse import urlparse
from urllib.parse import urlsplit
from collections import deque
import pandas as pd
from user_agent import generate_user_agent
import pandas as pd



def return_url(url):
	"""returns an online url and catches all exceptions just to be sure the connection worked
	"""
	headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
	try:
		request_object = requests.get(url, verify=True, headers=headers, timeout=10)
	except requests.ConnectionError as e:
		print("OOPS!! Connection Error on : "+ url +" Make sure you are connected to Internet. Technical Details given below.\n")
		print(str(e))
		pass
	except requests.Timeout as e:
		print("OOPS!! Timeout Error on "+url )
		print(str(e))
		pass
	except requests.RequestException as e:
		print("OOPS!! General Error on :"+url)
		print(str(e))
		pass
	except KeyboardInterrupt:
		print("Someone closed the program")
	else:
		print('no connection error')
	finally:
		print(url+ ' - request result stored!')
		return request_object


def make_soup(url):
	"""makes a soup from an online url
	"""
	r = return_url(url)
	soup = BeautifulSoup(r.content, 'html.parser')
	return soup

def make_local_soup(link):
	"""returns a soup of content from an HTML file stored locally
	"""
	f=codecs.open(link, 'r','utf-8')
	content=BeautifulSoup(f.read(), "html.parser")
	return content


def get_urls(soup):
	"""returns all urls in a soup by getting all the <a> tags with an href that starts with http://
	"""
	url=[]
	url_tags=soup.find_all('a', {'href': lambda x : x.startswith('http://')})
	if url_tags != []:
		for elem in url_tags:
			url.append(elem.text)
	return url
 

def get_mails(soup):
	"""returns all emails in a soup by getting all the <a> tags with an href that starts with mailto:
	"""
	mail=[]
	mail_tags=soup.find_all('a', {'href': lambda x : x.startswith('mailto:')})
	if mail_tags != []:
		for elem in mail_tags:
			mail.append(elem.text)
	return mail

def resolve_link(base,url):
 """extract base url to resolve relative links
 returns an absolute url
 """
	urls=[]
	link=''
	parts = urlsplit(base)
	base_url = "{0.scheme}://{0.netloc}".format(parts)
	# resolve relative links
	if url.startswith('/'):
		link = base_url + url
	elif url.startswith('http'):
		link = url
	return link


def get_links(url):
	"""returns a list of links contained in a given url, including relative links contained on the page, filtering all <a> tags 
	"""
	r = return_url(url)
	filter=SoupStrainer('a')
	links=[]
	soup = BeautifulSoup(r.content,parseOnlyThese=filter)
	a_tags = soup.findAll("a", href=True)
	for i in range(len(a_tags)):
		print('processing links for:'+url)
		links.append(resolve_link(url,a_tags[i].attrs['href']))
	return links


def filter_internal_links(list,url):
	"""returns a resolvable list of links who belong to the domain of a given url
	"""
	links=[]
	domain=urlparse(url).netloc
	for l in list:
		parse_object = urlparse(l)
		g=parse_object.netloc
		if g == domain:
			links.append(l)
	return links

def get_emails(list):
	"""Returns a set of emails addresses contained in a list of pages to be crawled
	"""
	new_emails = set()
	# a queue of urls to be crawled
	new_urls = deque(list)
	# a set of urls that we have already crawled
	processed_urls = set()
	# a set of crawled emails
	emails = set()
	# process urls one by one until we exhaust the queue
	while len(new_urls):
	# move next url from the queue to the set of processed urls
		url = new_urls.popleft()
		print('processing emails for:'+url)
		processed_urls.add(url)
		response = return_url(url)
		# extract all email addresses and add them into the resulting set
		new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
		emails.update(new_emails)
	return emails

def process_emails(url):
	"""Returns all email adresses contained in the pages of a given domain
	this function will take one url as input, lists all pages with relative links in the same domain, and then extract the emails contained in all these pages
	"""
	links=filter_internal_links(get_links(url),url)
	pages=[]
	for item in links:
		pages.append(resolve_link(url,item))
	return get_emails(pages)
