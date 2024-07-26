import tkinter as tk
import requests
from bs4  import BeautifulSoup


rr=tk.Tk()
rr.geometry("1000x1000")

def üüp():
    urlm="https://tr.wikipedia.org/wiki/BMW"


    aal=requests.get(urlm)
    l=aal.content
    vv=BeautifulSoup(l,'html.parser')
    tur=vv.find_all('p')
    for nn in tur:
         ll.config(text=nn.text)
""" button """
gg=tk.Button(rr, text="all", command=üüp )
gg.place(x=100, y=100)

""" label """
ll=tk.Label(rr)
ll.place(x=50,y=50)
rr.mainloop()