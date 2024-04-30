import random, os
import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import cv2
import qrcode as qrcode

def welcome_bill():

    txtarea.delete('1.0', END)
    txtarea.insert(END, '\t\t\tWELCOME SIES RETAIL\n')
    txtarea.insert(END, f'BILL NUMBER:. {bill_no.get()}\n\n')
    txtarea.insert(END, f'NAME: {c_name.get()}.\n\n')
    txtarea.insert(END, f'PHONE NUMBER: {c_pno.get()}.\n\n')
    txtarea.insert(END, f'----------------------------------------------------------------------------------------------\n')
    txtarea.insert(END, f'PRODUCTS\t\t\t QUANTITY\t\t\t  PRICE\n')
    txtarea.insert(END, f'----------------------------------------------------------------------------------------------\n')
    if fruits_dd.get() != '':
      txtarea.insert(END, f'{fruits_dd.get()}\t\t\t      {quantityfr_dd.get()}\t\t\t{priceFruits.get()}\n')
    if veggies_dd.get() != '':
        txtarea.insert(END, f'{veggies_dd.get()}\t\t\t      {quantityvg_dd.get()}\t\t\t{priceVeggies.get()}\n')
    if snacks_dd.get() != '':
        txtarea.insert(END, f'{snacks_dd.get()}\t\t\t      {quantitysn_dd.get()}\t\t\t{priceSnacks.get()}\n')
    if drinks_dd.get() != '':
        txtarea.insert(END, f'{drinks_dd.get()}\t\t\t      {quantitydr_dd.get()}\t\t\t{priceDrinks.get()}\n')
    if dairy_dd.get() != '':
        txtarea.insert(END, f'{dairy_dd.get()}\t\t\t      {quantityda_dd.get()}\t\t\t{priceDairy.get()}\n')
    if foodgrains_dd.get() != '':
        txtarea.insert(END, f'{foodgrains_dd.get()}\t\t\t      {quantityfg_dd.get()}\t\t\t{priceFoodgrains.get()}\n')
    if household_dd.get() != '':
        txtarea.insert(END, f'{household_dd.get()}\t\t\t      {quantityhh_dd.get()}\t\t\t{priceHousehold.get()}\n')
    if daal_dd.get() != '':
        txtarea.insert(END, f'{daal_dd.get()}\t\t\t      {quantitydl_dd.get()}\t\t\t{priceDaal.get()}\n')
    if stationary_dd.get() != '':
        txtarea.insert(END, f'{stationary_dd.get()}\t\t\t      {quantityst_dd.get()}\t\t\t{priceStationary.get()}\n')
    if cosmetics_dd.get() !='':
        txtarea.insert(END, f'{cosmetics_dd.get()}\t\t\t      {quantityct_dd.get()}\t\t\t{priceCosmetics.get()}\n')



def clear():
    c_name.set("")
    c_pno.set("")
    bill_no.set("")
    x = random.randint(1000, 999999)
    bill_no.set(str(x))
    fruits_dd.set("")
    priceFruits.set("")
    quantityfr_dd.set("QTY")

    veggies_dd.set("")
    priceVeggies.set("")
    quantityvg_dd.set("QTY")


    snacks_dd.set("")
    priceSnacks.set("")
    quantitysn_dd.set("QTY")



    drinks_dd.set("")
    priceDrinks.set("")
    quantitydr_dd.set("QTY")


    dairy_dd.set("")
    priceDairy.set("")
    quantityda_dd.set("QTY")



    foodgrains_dd.set("")
    priceFoodgrains.set("")
    quantityfr_dd.set("QTY")



    household_dd.set("")
    priceHousehold.set("")
    quantityhh_dd.set("QTY")



    daal_dd.set("")
    priceDaal.set("")
    quantitydl_dd.set("QTY")



    stationary_dd.set("")
    priceStationary.set("")
    quantityst_dd.set("QTY")




    cosmetics_dd.set("")
    priceCosmetics.set("")
    quantityct_dd.set("QTY")








    welcome_bill()


def sum():
        pass





def bill_area():
    welcome_bill()







def save_bill():
    op = messagebox.askyesno("SAVE BILL",'DO YOU WANT TO SAVE THE BILL?')
    if op>0:
       bill_data = txtarea.get('1.0',END)
       f1 = open('bills/'+str(bill_no.get())+'.txt','w')
       f1.write(bill_data)
       f1.close()
       messagebox.showinfo('SAVED',f'Bill Number {bill_no.get()} saved Successfully.')
    else:
        return


def gen_qrcode():
    qr_data=(f"Phone Number:{c_pno.get()}\nCustomer:{c_name.get()}\nBILL NUMBER:. {bill_no.get()}\nBILL:.{find_bill()}")
    qr_code=qrcode.make(qr_data)
    qr_code.save('Cust'+str(c_name.get())+'.png')
    im = ImageTk.PhotoImage(qr_code)
    qr_area.config(image=im)


def find_bill():
    present = 'no'
    import os


    for i in os.listdir('bills/'):
        if i.split('.')[0]== search_bill.get():
            f1=open(f'bills/{i}','r')
            txtarea.delete('1.0',END)
            for d in f1:
                txtarea.insert(END,d)
            f1.close()
            present='yes'
    if present=='no':
        messagebox.showerror('ERROR','Invalid Bill Number.')






win = Tk()
win.geometry('2000x1050')  # Adjust the dimensions as per your laptop screen resolution
win.title('BILLING SOFTWARE')


title=Label(win,text ='Billing Software',bd=12,relief=RIDGE,bg = 'dark blue',fg='white',font=('times New Roman',30,'bold'),pady=3).pack(fill='x')






# Customer
c_name = StringVar()
c_pno = StringVar()
bill_no = StringVar()
x = random.randint(1000, 999999)
bill_no.set(str(x))
search_bill = StringVar()

# FRAME
F1 = LabelFrame(win, bd=10, relief=GROOVE, text='Customer Details', font=('times New Roman', 17, 'bold'),
                fg='white', bg='dark blue')
F1.place(x=0,y=80,relwidth=1)
# customer label
cname = Label(F1, text='Customer name', bg='dark blue', fg='gold', font=('times New Roman', 15, 'bold')). \
    grid(row=0, column=0, padx=0, pady=0)
cname= Entry(F1, width=20, font='arial 15', relief=RAISED, textvariable=c_name).grid(row=0, column=1, pady=5,
                                                                                           padx=10)

# phone number
cphone = Label(F1, text='Phone number', bg='dark blue', fg='gold', font=('times New Roman', 15, 'bold')).grid(
    row=0, column=2, padx=10, pady=0)
cphone= Entry(F1, width=20, font='arial 15', relief=RAISED, textvariable=c_pno). \
    grid(row=0, column=3, padx=10, pady=5)

# bill
cbill = Label(F1, text='BILL', bg='dark blue', fg='gold', font=('times New Roman', 15, 'bold')).grid(
    row=0, column=4, padx=0, pady=0)
cbill= Entry(F1, width=20, font='arial 15', relief=RAISED, textvariable=search_bill).grid(row=0, column=5,
                                                                                                padx=10, pady=5)

# search button
search = Button(F1, text='Search',command=find_bill, width=12, font='arial 12 bold').grid(row=0, column=8, padx=10, pady=10)



# BILLAREA
F5 = LabelFrame(win, bd=10, relief=SUNKEN,bg='white')
F5.place(x=1300, y=170, width=610, height=650)
bill_title = Label(F5, text='Bill Area', font='arial 17 bold', bd=7, relief=SUNKEN).pack(fill=X)
scroll_y = Scrollbar(F5, orient=VERTICAL)
txtarea = Text(F5, yscrollcommand=scroll_y.set,font='arial 13 bold')
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=txtarea.yview)
txtarea.pack()


#QRCODE
F7 = LabelFrame(win,bd=10,relief = SUNKEN, bg='cyan')
F7.place(x=700,y=170,width=600,height=650)
qr_title = Label(F7,text='QR CODE', font='arial 17 bold',bd=7,relief=SUNKEN).pack(fill=X)
qr_area = Label(F7,text='No QR GENERATED',font='arial 17 bold',relief=RIDGE,bg='white',bd=5)
qr_area.place(x=10,y=55,width=570,height=520)

#SCANNERAREA
#SCANNERAREA
F8 = LabelFrame(win,bd=10,relief = SUNKEN, bg='white')
F8.place(x=0,y=170,width=700,height=650)
scanner = Label(F8,text='SCANNER', font='arial 17 bold',bd=7,relief=SUNKEN).pack(fill=X)
fruits = Label(F8,text='FRUITS',font='arial 17 bold',bg='white').place(x=10,y=50)
fruits_dd = Combobox(F8,values=['Banana','Apple','Mango','Grapes','Pears','Guava','DragonFruit'],font='arial 17',width=14)
fruits_dd.place(x=120,y=50)
quantityfr_dd = Combobox(F8,values=[1,2,3,4,5,6],font='arial 17',width=4)
quantityfr_dd.place(x=350,y=50)
quantityfr_dd.set('QTY')
priceLabel1 = Label(F8,text="PRICE",font='arial 17 bold', bg='white').place(x=430,y=50)
#priceFr = Combobox(F8,font='arial 17',width=6,values=['100','200','300','150','250','350']).place(x=510,y=50)
priceFruits = Entry(F8,width=6,font='arial 17',bd='5',relief="groove")
priceFruits.place(x=510,y=50)






veggies = Label(F8,text='VEGGIES',font='arial 17 bold',bg='white').place(x=10,y=100)
veggies_dd = Combobox(F8,values=['LadyFinger','Pumkin','Cauliflower','Carrot','Brinjal','Onion','Cabbage'],font='arial 17',width=14)
veggies_dd.place(x=120,y=100)
quantityvg_dd = Combobox(F8,values=['1kg','2kg','3kg','4kg','5kg','6kg'],font='arial 17',width=4)
quantityvg_dd.place(x=350,y=100)
quantityvg_dd.set('QTY')
priceLabel2 = Label(F8,text='PRICE',font='arial 17 bold',bg='white').place(x=430,y=100)
priceVeggies = Combobox(F8,font='arial 17',values=['10','20','30','40','50',100,150,200],width=6)
priceVeggies.place(x=510,y=100)





snacks = Label(F8,text='SNACKS',font='arial 17 bold',bg='white').place(x=10,y=150)
snacks_dd = Combobox(F8,values=['Aalo bhujia','Shev Bhujia','Baarik Shev','Shev','ABC','DEF','GHI'],font='arial 17',width=14)
snacks_dd.place(x=120,y=150)
quantitysn_dd = Combobox(F8,values=['1kg','2kg','3kg','4kg','5kg','6kg'],font='arial 17',width=4)
quantitysn_dd.place(x=350,y=150)
quantitysn_dd.set('QTY')

priceLabel3 = Label(F8,text='PRICE',font='arial 17 bold',bg='white').place(x=430,y=150)
priceSnacks = Combobox(F8,font='arial 17',width=6)
priceSnacks.place(x=510,y=150)






drinks = Label(F8,text='SOFT DRINKS',font='arial 17 bold',bg='white').place(x=10,y=200)
drinks_dd = Combobox(F8,values=['Pepsi','Mazza','Soda','Tang','Coca Cola','Limca','XYZ'],font='arial 17',width=14)
drinks_dd.place(x=180,y=200)
quantitydr_dd = Combobox(F8,values=['1','2','3','4','5','6'],font='arial 17',width=4)
quantitydr_dd.place(x=400,y=200)
quantitydr_dd.set('QTY')
priceLabel4 = Label(F8,text='PRICE',font='arial 17 bold',bg='white').place(x=475,y=200)
priceDrinks = Combobox(F8,font='arial 17',width=6)
priceDrinks.place(x=560,y=200)






dairy = Label(F8,text='DAIRY',font='arial 17 bold',bg='white').place(x=10,y=250)
dairy_dd = Combobox(F8,values=['Milk(0.5L)','Curd','Milk(1L)','Chaas','Paneer','IIII','JJJJ'],font='arial 17',width=14)
dairy_dd.place(x=120,y=250)
quantityda_dd = Combobox(F8,values=['1kg','2kg','3kg','4kg','5kg','6kg'],font='arial 17',width=4)
quantityda_dd.place(x=350,y=250)
quantityda_dd.set('QTY')
priceLabel5 = Label(F8,text='PRICE',font='arial 17 bold',bg='white').place(x=430,y=250)
priceDairy = Combobox(F8,font='arial 17',width=6)
priceDairy.place(x=510,y=250)





foodgrains = Label(F8,text='GRAINS',font='arial 17 bold',bg='white').place(x=10,y=300)
foodgrains_dd = Combobox(F8,values=['Wheat','Cornflour','Rawa','Basan','Sooji','Rice'],font='arial 17',width=14)
foodgrains_dd.place(x=120,y=300)
quantityfg_dd = Combobox(F8,values=['1kg','2kg','3kg','4kg','5kg','6kg'],font='arial 17',width=4)
quantityfg_dd.place(x=350,y=300)
quantityfg_dd.set('QTY')
priceLabel6 = Label(F8,text='PRICE',font='arial 17 bold',bg='white').place(x=430,y=300)
priceFoodgrains = Combobox(F8,font='arial 17',width=6)
priceFoodgrains.place(x=510,y=300)





household = Label(F8,text='HOUSEHOLD',font='arial 17 bold',bg='white').place(x=10,y=350)
household_dd = Combobox(F8,values=['Vim','Scrubber','LiquidGel','Detergent','Disinfectent Toilet','XYZ'],font='arial 17',width=14)
household_dd.place(x=180,y=350)
quantityhh_dd = Combobox(F8,values=['1','2','3','4','5','6'],font='arial 17',width=4)
quantityhh_dd.place(x=400,y=350)
quantityhh_dd.set('QTY')
priceLabel7 = Label(F8,text='PRICE',font='arial 17 bold',bg='white').place(x=480,y=350)
priceHousehold = Combobox(F8,font='arial 17',width=6)
priceHousehold.place(x=560,y=350)





daal = Label(F8,text='DAAL',font='arial 17 bold',bg='white').place(x=10,y=400)
daal_dd = Combobox(F8,values=['Toor','Maasur','Lobia','Moong','Chana','Rajma','Chole'],font='arial 17',width=14)
daal_dd.place(x=120,y=400)
quantitydl_dd = Combobox(F8,values=['1kg','2kg','3kg','4kg','5kg','6kg'],font='arial 17',width=4)
quantitydl_dd.place(x=350,y=400)
quantitydl_dd.set('QTY')
priceLabel8 = Label(F8,text='PRICE',font='arial 17 bold',bg='white').place(x=430,y=400)
priceDaal = Combobox(F8,font='arial 17',width=6)
priceDaal.place(x=510,y=400)





stationary = Label(F8,text='STATIONARY',font='arial 17 bold',bg='white').place(x=10,y=450)
stationary_dd = Combobox(F8,values=['Pencil','Sharpner','Pen','Eraser','SketchPen','Chalk'],font='arial 17',width=14)
stationary_dd.place(x=180,y=450)
quantityst_dd = Combobox(F8,values=['1','2','3','4','5','6'],font='arial 17',width=4)
quantityst_dd.place(x=400,y=450)
quantityst_dd.set('QTY')
priceLabel9 = Label(F8,text='PRICE',font='arial 17 bold',bg='white').place(x=480,y=450)
priceStationary = Combobox(F8,font='arial 17',width=6)
priceStationary.place(x=560,y=450)






cosmetics = Label(F8,text='COSMETICS',font='arial 17 bold',bg='white').place(x=10,y=500)
cosmetics_dd = Combobox(F8,values=['Nail Polish','Perfume','HairOil','Comb','HairGel','Siuu'],font='arial 17',width=14)
cosmetics_dd.place(x=180,y=500)
quantityct_dd = Combobox(F8,values=['1','2','3','4','5','6'],font='arial 17',width=4)
quantityct_dd.place(x=400,y=500)
quantityct_dd.set('QTY')
priceLabel10 = Label(F8,text='PRICE',font='arial 17 bold',bg='white').place(x=480,y=500)
priceCosmetics = Combobox(F8,font='arial 17',width=6)
priceCosmetics.place(x=560,y=500)




 #BUTTONFRAME
F6 = LabelFrame(win, bd=10, relief=SUNKEN, bg='dark blue',text='Billing Tools',font = 'arial 17 bold',fg='gold')
F6.place(x=0, y=770,relwidth=1, height=230)


button_frame = Frame(F6,bd=7,relief=SUNKEN,pady=30,bg='black')
button_frame.place(x=0,width=1900,height=195)



printb = Button(button_frame,text = 'PRINT BILL',font='arial 15 bold',bg = 'cyan',fg='black',width = 11,pady=10,height=2,padx=50,).grid(row=0,column=0,padx=100, pady=5,sticky='w')
gen_bill = Button(button_frame,command=welcome_bill, text='GENERATE BILL', font='arial 15 bold', bg='cyan', fg='black', width=11,padx=50,pady=10,height=2).grid(row=0, column=1, padx=30, pady=5, sticky='w')
gen_qr = Button(button_frame,command=gen_qrcode, text='GENERATE QR CODE', font='arial 15 bold', bg='cyan', fg='black', width=11, pady=10,padx=50,
                       height=2).grid(row=0, column=2, padx=100, pady=5, sticky='w')
total = Button(button_frame,text='TOTAL',command=sum, font='arial 15 bold', bg='cyan', fg='black', width=11, pady=10,padx=50,
                       height=2).grid(row=0, column=3, padx=30, pady=5, sticky='w')
clr = Button(button_frame,text='CLEAR',command=clear, font='arial 15 bold', bg='cyan', fg='black', width=11, pady=10,padx=50,
                       height=2).grid(row=0, column=8, padx=100, pady=5, sticky='w')





welcome_bill()







win.mainloop()

