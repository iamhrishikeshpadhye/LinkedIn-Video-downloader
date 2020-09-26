#!/usr/bin/env python

import html.parser
import requests
import wget
import argparse
from datetime import datetime

def dl(url,output):
	html_source = requests.get(url).text
	html_source = html_source.split()
	for i in html_source:
		i = html.unescape(i)
		if 'dms.licdn.com' in i:
			final_url = i.split(",")[0].split('"src":')[1][1:-1]
			print("\nDownload in progress ...\n")
			wget.download(final_url, str(output + ".mp4"))
			print('\n\nVideo : "' + output + ".mp4" + '" has been downloaded successfully!\n')

def main():
	link = args.url
	name = args.output
	dl(link, name)

if __name__ == '__main__':
	now = datetime.now()
	now_string = now.strftime("%d-%m-%Y-%H-%M-%S")
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", dest="url", required=True, help="URL of the post")
	parser.add_argument("-o", dest="output", default=now_string, help="Name of the output file")
	args = parser.parse_args()
	main()