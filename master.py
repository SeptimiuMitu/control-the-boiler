#!/usr/bin/env python

import sqlite3

import os
import time
import glob
import controlrelay

# global variables
dbname='/var/www/templog.db'

# display the contents of the database
def get_last_action():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    for row in curs.execute("SELECT action FROM actions order by timestamp desc limit 1"):
        print str(row[0])
    conn.close()

# main function
def main():
    get_last_action()

if __name__=="__main__":
    main()
