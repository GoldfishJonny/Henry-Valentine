from cgitb import reset
import requests
from datetime import datetime 
from bs4 import BeautifulSoup
import glob 
import os
import filecmp

class search():
    def main(self, link):
        s = search.search(self, link)
        f = search.format(self, s)
        p = search.prevfile(self)
        c = search.createFile(self, f)
        m = search.checkMulti(self, c, p)
        return m

    def search(self,link):
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        print(r.url)
        a = soup.find('div', class_="markdown-body my-3")
        b = a.find('h1')
        print(b.text)
        c = a.find_all('p')
        d = []
        d.append(b.text)
        for line in c:
            d.append(line.text)    
        return d
    
    
    def format(self, e):
        g = []
        if len(e) >= 2:
           title = e[0]
           Title = title.split()
           Title.insert(0, '>>> **')
           Title.append('**')
           Title = ' '.join(Title)
           g.append(Title)
           for x in range(1, len(e)):
                parag = e[x]
                Para = parag.split()
                Para.insert(0, "_")
                Para.append("_")
                Para = ' '.join(Para)
                g.append(Para)   
        return g

    def prevfile(self):
        try:
            list_o_files = glob.glob('logs/**.txt', recursive=True)
            latest_f = max(list_o_files, key=os.path.getctime) 
            return latest_f
        except:
            print('no file yet')

    def createFile(self, g):
        x = datetime.now()
        file_name =r"logs/" + x.strftime('%M-%H-%d-%Y.txt')
        with open(file_name, 'w') as fp:
            print('created', file_name)
            for x in range(len(g)):
                a = g[x]
                fp.write(a)
                fp.write('\n')
        return file_name

    def checkMulti(self, f, p):
        try:
            f1 = str(p)
            f2 = str(f)
            print(f1)
            print(f2)
            result = filecmp.cmp(f1, f2)
            print(result)
            if result == True:
                os.remove(f2)
                return None
            else:
                return f2
        except:
            return str(f)

        