#Driver Code

from db import create_db, insert_item
from parser import parse
from os.path import exists
import pyfiglet

# 1)Parse news
# 2)Add them to the news.db

if __name__ == '__main__':
    print(pyfiglet.figlet_format("News"))
    db_exists = exists('./news.db')

    dict = parse()
    
    if(db_exists):
        for key in dict.keys():
            insert_item(key, dict[key])
    else:
        create_db()

    