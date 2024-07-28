import tkinter as tk
import requests
from bs4  import BeautifulSoup


rr=tk.Tk()
rr.geometry("1000x1000")

def üüp():
    qqo=ww.get()
    urlm=f"https://www.arabam.com/ikinci-el?searchText={qqo}"


    


    aal=requests.get(urlm)
    l=aal.content
    vv=BeautifulSoup(l,'html.parser')
    """ fiyat """
    tur=vv.find_all('span', class_='db no-wrap listing-price' )
    fiyat_list=[fiyat.text.strip() for fiyat in tur]

    ll.config(text="\n".join(fiyat_list[:100]))
    """ model """
    mdol=vv.find_all('h4',  class_="crop-after crop-after-40 odd-ca40"  )  

   
    isim_list=[mm.text.strip() for mm in mdol]  

    
    ff.config(text="\n".join(isim_list[:100]))

""" button """
gg=tk.Button(rr, text="al", command=üüp )
gg.place(x=30, y=1)

""" label fiyat """
ll=tk.Label(rr)
ll.place(x=50,y=210)
""" label model ismi"""
ff=tk.Label(rr,)
ff.place(x=400, y=40)

ww=tk.Entry(rr,)
ww.place(x=50, y=10)
rr.mainloop()



""" arama verisi 
 """