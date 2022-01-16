import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import sqlite3


#pandas is a Python package that provides fast, flexible and expressive data structures
#NumPy is a library for the Python programming language, which provides support for large, multidimensional arrays and arrays
#Requests allows you to send HTTP/1.1 requests extremely easily.

no_pages = 1

#woordsList =  Library().txtBA
woordsList ="kitchen"
 
def get_data(no_pages):

    # Read html 
    r = requests.get('https://www.amazon.nl/s?k='+str(woordsList)+'&i=stripbooks&page='+str(no_pages)+'&__mk_nl_NL=ÅMÅŽÕÑ&qid=1596990030&ref=sr_pg_'+str(no_pages))

    content = r.content
    # BeautifulSoup object from webpage.
    soup = BeautifulSoup(content)
    
    # Getting all data based on the tags and class
    # Getting titles, author, rating, price, bookcase, publish date, 
    alls = []
    for d in soup.findAll('div', attrs={'class':'s-include-content-margin s-border-bottom s-latency-cf-section'}):
        #print(d)
        name = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
        author = d.find('div', attrs={'class':'a-row a-size-base a-color-secondary'})
        n = author.find_all('span', attrs={'class':'a-size-base'})
        rating = d.find('span', attrs={'class':'a-icon-alt'})
        date = d.find('span', attrs={'class':'a-size-base a-color-secondary a-text-normal'})
        price = d.find('span', attrs={'class':'a-price-whole'})
        isbn = d.find('span', attrs={'class':'a-price-whole'})
        bookcase = d.find('span', attrs={'class':'a-price-whole'})
        

        all1=[]

        #Titles list
        if name is not None:
            
            all1.append(name.text)
        else:
            all1.append("unknown-product")
        #Authors list
        if author is not None:
            #print(author.text)
            all1.append(n[1].text)
       
        else:    
                all1.append('0')
        #Ratings list
        if rating is not None:
            
            all1.append(rating.text)
        else:
            all1.append('No Rating')

        #Publish dates list
        if date is not None:
            #print(rating.text)
            all1.append(date.text)
        else:
            all1.append('No Publish Date')
        #Prices list
        if price is not None:
            #print(price.text)
            all1.append(price.text + " €")
        else:
            all1.append('0')

        #ISBN list
        if isbn is not None:
            all1.append('none')
        else:
            all1.append('none')

        #Bookcases list
        if bookcase is not None:
            all1.append('none')
        else:
            all1.append('none')
        
        
        alls.append(all1) 
    return alls


#For loop will iterate over get_data() function starting from 1 till the number of pages+1
#Since the output will be a nested list, I would first flatten the list and then pass it to the DataFrame.

results = []
for i in range(1, no_pages+2):
    results.append(get_data(i))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Book', 'Author', 'Rating', 'Publish', 'Price', 'ISBN', 'Bookcase'])
#df.to_csv('Amazonbooks.csv', index=False, encoding='utf-8')
#df = pd.read_csv("Amazonbooks.csv")

#a Connection object that represents the database
conn= sqlite3.connect('Amazonbooks.db')
#a Cursor object and call its execute() method to perform SQL commands
c = conn.cursor()
#c.execute("CREATE TABLE IF NOT EXIST Amazonbooks ({})".format(' ,'.join(df.columns)))

#Creat Table
c.execute("CREATE TABLE IF NOT EXISTS Amazonbooks (Book text,Author text,Rating text,Price text,Publish text,ISBN text,Bookcase text)")

#DataFrame to sql
df.to_sql('Amazonbooks', conn, if_exists='replace', index=False)
#COMMIT is the SQL command that is used for storing changes performed by a transaction.
conn.commit()
conn.close()

#df.shape
#(100, 5)
#df.head(100)
