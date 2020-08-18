# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 01:29:22 2020

@author: Ahmed Alaa
"""

import sqlite3
import pandas as pd
from time import sleep

timeframes = ['2009-06']

for timeframe in timeframes:
    connection = sqlite3.connect('{}.db'.format(timeframe))
    c = connection.cursor()
    limit = 5000
    last_unix = 0
    cur_length = limit
    counter = 0
    test_done = False

    while cur_length == limit :

        #df = #pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} AND parent NOT NULL AND score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix, limit), connection) #before last_unix
        df = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} and parent NOT NULL and score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix,limit),connection) 
        
        # if df.count == 0:      
        last_unix = df.tail(1)['unix'].values[0]
        cur_length = len(df)
        #     print('i am in if: sleepin 5 sec')
        #     sleep(5)
            
        print(df.tail(1)['unix'].values)
        # else:
        if not test_done:
            with open('test.from','a', encoding='utf8') as f:
                for content in df['parent'].values:
                    f.write(content+'\n')

            with open('test.to','a', encoding='utf8') as f:
                for content in df['comment'].values:
                    f.write(str(content)+'\n')

            test_done = True

        else:
            with open('train.from','a', encoding='utf8') as f:
                for content in df['parent'].values:
                    f.write(content+'\n')

            with open('train.to','a', encoding='utf8') as f:
                for content in df['comment'].values:
                    f.write(str(content)+'\n')
                    
        print(cur_length)
        sleep(1)
        counter += 1
        if counter % 20 == 0:
            print(counter*limit,'rows completed so far')