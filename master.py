#!/usr/bin/env python

import sqlite3

import os
import time
import glob
import controlrelay

# global variables
dbname='/var/www/templog.db'

# Get the last action
def get_last_action():
    connection=sqlite3.connect(dbname)
    cursor=conn.cursor()
    cursor.execute("SELECT action FROM actions order by timestamp desc limit 1"):
    result=cursor.fetcone()[0]
    connection.close()
    return result

def execute_action(action)


# main function
def main():
    get_last_action()

if __name__=="__main__":
    main()