from tkinter import *
from tkinter import Scrollbar
from bs4 import BeautifulSoup
import requests
import webbrowser

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# import manan as m
jumia=''
amazon=''
olx=''

def jumia(name = ""):
    try:
        global jumia
        name1 = name.replace(" ","+")   #iphone x  -> iphone+x
        jumia=f'https://www.jumia.com.ng/catalog/?q={name1}'
        res = requests.get(f'https://www.jumia.com.ng/catalog/?q={name1}',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        jumia_name = soup.select('.name')[0].getText().strip()  ### New Class For Product Name
        jumia_name = jumia_name.upper()
        if name.upper() in jumia_name:
            jumia_price = soup.select('.prc')[0].getText().strip()  ### New Class For Product Price
            jumia_name = soup.select('.name')[0].getText().strip()

            return f"{jumia_name}\nPrise : {jumia_price}\n"
        else:

            jumia_price='           Product Not Found'
        return jumia_price
    except:

        jumia_price= '           Product Not Found'
    return jumia_price

def amazon(name):
    try:
        global amazon
        name1 = name.replace(" ","-")
        name2 = name.replace(" ","+")
        amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0,amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name[0:20]:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()

                break
            else:
                i+=1
                i=int(i)
                if i==amazon_page_length:

                    amazon_price = '           Product Not Found'
                    break
        return f"{amazon_name}\nPrise : {amazon_price}\n"
    except:

        amazon_price = '           Product Not Found'
    return amazon_price

def olx(name):
    try:
        global olx
        name1 = name.replace(" ","-")
        olx=f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
        res = requests.get(f'https://www.olx.in/items/q-{name1}?isSearchCall=true',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        olx_name = soup.select('._2tW1I')
        olx_page_length = len(olx_name)
        for i in range(0,olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                olx_name = soup.select('._2tW1I')[i].getText().strip()
                olx_loc = soup.select('.tjgMj')[i].getText().strip()
                try:
                    label = soup.select('._2Vp0i span')[i].getText().strip()
                except:
                    label = "OLD"   

                break
            else:
                i+=1
                i=int(i)
                if i==olx_page_length:

                    olx_price = '           Product Not Found'
                    break
        return f"{olx_name}\nPrise :{olx_price}\n"
    except:

        olx_price = '           Product Not Found'
    return olx_price

# Another function
def convert(a):
    b=a.replace(" ",'')
    c=b.replace("NGN",'')
    d=c.replace(",",'')
    f=d.replace("NGN",'')
    g=int(float(f))
    return g


def urls():
    global jumia
    global amazon
    global olx
    return f"{jumia}\n\n\n{amazon}\n\n\n{olx}"



def open_url(event):
        global jumia
        global amazon
        global olx
        webbrowser.open_new(jumia)
        webbrowser.open_new(amazon)
        webbrowser.open_new(olx)

def search():
    box1.insert(1.0,"Loding...")
    box4.insert(1.0,"Loding...")
    box5.insert(1.0,"Loding...")
    box6.insert(1.0,"Loding...")


    search_button.place_forget()


    box1.delete(1.0,"end")
    box4.delete(1.0,"end")
    box5.delete(1.0,"end")
    box6.delete(1.0,"end")

    t1=jumia(product_name.get())
    box1.insert(1.0,t1)

    t4=amazon(product_name.get())
    box4.insert(1.0,t4)

    t5=olx(product_name.get())
    box5.insert(1.0,t5)

    t6 = urls()
    box6.insert(1.0,t6)


window = Tk()
window.wm_title("Alfred Price Comparison")
window.minsize(1500,700)

lable_one =  Label(window, text="Enter Product Name :", font=("courier", 10))
lable_one.place(relx=0.2, rely=0.1, anchor="center")

product_name =  StringVar()
product_name_entry =  Entry(window, textvariable=product_name, width=50)
product_name_entry.place(relx=0.5, rely=0.1, anchor="center")

search_button =  Button(window, text="Search", width=12, command= search)
search_button.place(relx=0.5, rely=0.2, anchor="center")


l1 =  Label(window, text="Jumia", font=("courier", 20))
l4 =  Label(window, text="amazon", font=("courier", 20))
l5 =  Label(window, text="olx", font=("courier", 20))
l6 =  Label(window, text="All urls", font=("courier", 20))
l8 =  Label(window, text="Loding.....", font=("courier", 30))

l1.place(relx=0.1, rely=0.3, anchor="center")
l4.place(relx=0.6, rely=0.3, anchor="center")
l5.place(relx=0.4, rely=0.6, anchor="center")
l6.place(relx=0.8, rely=0.6, anchor="center")

scrollbar = Scrollbar(window)
box1 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)

box4 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)

box5 =  Text(window, height=7, width=50, yscrollcommand=scrollbar.set)


box1.place(relx=0.2, rely=0.4, anchor="center")
box4.place(relx=0.5, rely=0.4, anchor="center")
box5.place(relx=0.4 , rely=0.7, anchor="center")

box6 =  Text(window, height=15, width=50, yscrollcommand=scrollbar.set, fg="blue", cursor="hand2")
box6.place(relx=0.8, rely=0.6, anchor="center")
box6.bind("<Button-1>", open_url)


window.mainloop()