import webbrowser
from urllib.parse import quote
#
topic = input("what kind of flyer? ")
mood = input("what mood? (bold, elegant, fun) ")
search = quote(topic + " " + mood + " flyer design")
#
webbrowser.open("https://www.pinterest.com/search/pins/?q=" + search)
webbrowser.open("https://www.behance.net/search/projects?search=" + search)
webbrowser.open("https://www.google.com/search?tbm=" + search)