import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import sqlite3




num_pages = 1

#woordsList =  Library().txtBA
woordsList ="good"
 
def get_data(num_pages):  
    

    r = requests.get('https://www.biblio.com/search.php?stage=1&result_type=works&keyisbn='+str(woordsList)+'&page='+str(num_pages)+'&sid=1506537980')
    content = r.content
    soup = BeautifulSoup(content)
    

    alls = []
    for d in soup.findAll('div', attrs={'itemtype':'http://schema.org/Book'}):
        
        n1 = d.find('div', attrs={'class':'basic-info'})
        n2 = n1.find('header', attrs={'class':'item-title'})
        n3 = n2.find('h2', attrs={'class':'title'})
        
        author = d.find_all('h3', attrs={'class':'author'})
        isbn = n1.find('dl', attrs={'class':'fact-list'})
        isbn2 = isbn.find_all('dd')
        
        Price = d.find('span', attrs={'class':'item-price'})
        seller = d.find('a', attrs={'class':'bd-seller-name'})
        Rating = d.find('div', attrs={'class':'speech'})
        bookcase = d.find('div', attrs={'class':'item-description'})

        all1=[]

        if n3 is not None:
            
            all1.append(n3.text)
        else:
            all1.append("Null")

        if author is not None:
            
            all1.append(author[0].text)
        else:    
            all1.append('Null')

        if Rating is not None:
            
            all1.append(Rating.text)
        else:
            all1.append('Null')

        if seller is not None:
            
            all1.append(seller.text)
        else:
            all1.append('Null')

        if Price is not None:
            
            all1.append(Price.text)
        else:
            all1.append('Null') 

        if len(isbn2[2].text) == 13 or len(isbn2[2].text) == 10 :
            
            all1.append(isbn2[2].text)


        elif len(isbn2[3].text) == 13 or len(isbn2[3].text) == 10 :
            
            all1.append(isbn2[3].text)

        else:
            all1.append('Null')

        if bookcase is not None:
            all1.append('none')
        else:
            all1.append('none')

       
        alls.append(all1)    
    return alls


#For loop will iterate over get_data() function starting from 1 till the number of pages+1
#Since the output will be a nested list, I would first flatten the list and then pass it to the DataFrame.

results = []
for i in range(1, num_pages+2):
    results.append(get_data(i))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Book', 'Author', 'Rating', 'Publish', 'Price', 'ISBN', 'Bookcase'])
df['Rating'] = df['Rating'].str.replace('This seller has earned a', '')
df['Rating'] = df['Rating'].str.replace('rating from Biblio customers.', '')
df['Author'] = df['Author'].str.replace('by ', '')
df.to_csv('Biblio.csv', index=False, encoding='utf-8')
df = pd.read_csv("Biblio.csv")


#a Connection object that represents the database
conn= sqlite3.connect('Biblio.db')
#a Cursor object and call its execute() method to perform SQL commands
c = conn.cursor()

#Creat Table
c.execute("CREATE TABLE IF NOT EXISTS Biblio (Book text,Author text,Rating text,Price text,Publish text,ISBN text,Bookcase text)")

#DataFrame to sql
df.to_sql('Biblio', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

#df.shape
#(100, 5)
#df.head(100)
