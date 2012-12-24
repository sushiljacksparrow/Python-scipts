#!C:\Python27

import argparse
import urllib
import sys
from xml.etree import ElementTree

def retrieve_movie(title):
	title = urllib.quote(title.encode("utf8"))
	URL="http://www.omdbapi.com/?r=xml&plot=full&t=%s" % title
	xml = ElementTree.parse(urllib.urlopen(URL))
	
	for A in xml.iter('root'):
		if(A.get('respone')==False):
			print "movie not found"
			sys.exit()
	xml=xml.getroot()
	printInfo(xml)
	return xml
	
def search_movie(title):
	title = urllib.quote(title.encode("utf8"))
	URL="http://www.omdbapi.com/?r=xml&s=%s" % title
	xml = ElementTree.parse(urllib.urlopen(URL))
	xml = xml.getroot()
	for B in xml.findall('Movie'):
		apicall=retrieve_movie(B.get('Title'))
		printInfo(apicall)
	return xml
	
def printInfo(xml):
	for B in xml.findall('movie'):
		print "\n%s %s || %s || %s\n" % (B.get('title'), B.get('year'), B.get('runtime'), B.get('imdbRating'))
		print "Genre : %s" %(B.get('genre'))
		print "Director: %s\n Actors: %s\n" %(B.get('director'), B.get('actors'))
		print "%s\n" % (B.get('plot'))
		
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Command-Line interface for IMDB')
	parser.add_argument('-t', help='Search by title, returns first result')
	parser.add_argument('-s', help='Search and return result')
	
	
	args = parser.parse_args()
	choices=['None']
	
	try:
		choices[0]=sys.argv[1]
		value=sys.argv[2]
	except:
		parser.print_usage()
		sys.exit()
		
	if choices[0]=='-t':
		retrieve_movie(value)
	else:
		search_movie(value)