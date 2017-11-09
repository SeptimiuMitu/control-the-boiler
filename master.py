#!/usr/bin/env python

import sqlite3

import os
import time
import glob
import controlrelay
import config

# global variables
dbname='/var/www/templog.db'
# Get the last action
def get_last_action():
    connection=sqlite3.connect(dbname)
    cursor1=conn.cursor()
    cursor1.execute("SELECT action FROM actions order by timestamp desc limit 1"):
    result=cursor1.fetchone()
    connection.close()

def execute_action(action)


# main function
def main():
    get_last_action()

if __name__=="__main__":
    main()
