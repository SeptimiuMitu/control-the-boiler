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
    cursor=conn.cursor()
    cursor.execute("SELECT action FROM actions order by timestamp desc limit 1"):
<<<<<<< HEAD
    result=cursor.fetchone()
=======
    result=cursor.fetchone()[0]
>>>>>>> 58d7742ee4e19e1b09697676b6ee94df0ad22b14
    connection.close()

def execute_action(action)


# main function
def main():
    get_last_action()

if __name__=="__main__":
    main()
