#!/usr/bin/env python

from app import init_db
from productInsertionHandler import dbProductSetup
import os

if __name__ == "__main__":

    ans = input("Run Setup? y or n\n")
    if ans == 'y':
        dirs = os.listdir()
        if 'main.db' in dirs:
            print("DB already exists. Please delete and run setup again")
            quit()
        else:
            init_db()
            dbProductSetup()
            quit()
