#!/usr/bin/python3
import urllib.request
import urllib.parse
import re
import sys

query = "start"
output_file = input("Enter a file to output to, or type 'none' to print to the screen \n")

if output_file == "none":
    while query != "quit":
        query = input("Enter a song: \n")
        query_string = urllib.parse.urlencode({"search_query" : query})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        if query == "quit":
            break
        print("http://www.youtube.com/watch?v=" + search_results[0])
else:
    text_file = open(output_file, "a")
    while query != "quit":
        query = input("Enter a song: \n")
        query_string = urllib.parse.urlencode({"search_query" : query})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        if query == "quit":
            break
            text_file.close
        text_file.write("http://www.youtube.com/watch?v=" + search_results[0] + "\n")
