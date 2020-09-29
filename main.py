import feedparser
from colorama import Fore
from colorama import Style
from colorama import Back

fullfeed = feedparser.parse("https://www.vaticannews.va/en.rss.xml")
#entry = NewsFeed.entries[1]
entries = fullfeed.entries
latestentries = fullfeed.entries[:10]
#print(entries)

# print the fields available/provided by the RSS feed
#print(entry.keys())

#print('Number of RSS posts :', len(NewsFeed.entries))

for post in latestentries:
    print(f'{Fore.WHITE}{Back.RED}   {post.title} {Style.RESET_ALL}')
    print(f'{post.summary}')
    print(f'{Fore.GREEN}{post.link} {Style.RESET_ALL}')
    print('\n')