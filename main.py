from tkinter import*
from tkinter.messagebox import*
import case
import random,deposit

def update_user_account(ID):
    global user_coins,case_prices
    user_coins-=case_prices[ID]
    balance.config(text="Balance: "+str(user_coins))

def keepSkin(info):
    global inventory
    inventory.append(info)
    main_menu(None)

def sellSkin(info):
    global user_coins
    user_coins+=info[1]
    balance.config(text="Balance: "+str(user_coins))
    main_menu(None)

def case_info(ID):
    for widget in frame.winfo_children():
        widget.destroy()
    case_info=case.get_case_info(filenames[ID])
    for loop in range(len(case_info)):
        texte=str((case_info[loop][1]-case_info[loop][0]+1)/1000)+" % (tickets "+str(case_info[loop][0])+" to "+str(case_info[loop][1])+") to get "+case_info[loop][2].split(".")[0]+" worth "+str(case_info[loop][3])+" $."
        Label(frame,text=texte,bg="grey40",font="Verdana 10").grid(column=0,row=loop,padx=5,pady=5,sticky=W,columnspan=2)
    Button(frame,bg="green",text="Open case",command=lambda x = ID: open_case(x),font="Verdana 10",width=30,height=1).grid(column=0,row=len(case_info),padx=5,pady=5)
    Button(frame,bg="orange",text="Back to menu",command= lambda x = None: main_menu(x),font="Verdana 10",width=30,height=1).grid(column=1,row=len(case_info),padx=5,pady=5)

def open_case(ID):
    def changeImage(index,images_representation,info):
        if index<len(images_representation)-1:
            index+=1
            photo=PhotoImage(file="Images/skins/"+images_representation[index])
            label1.configure(image=photo)
            label1.image=photo
            label1.update()
            fen.after(100,changeImage,index,images_representation,info)
        else:
            fen.title(images_representation[index])

            Button(frame,text="Instant sell for "+str(info[1])+" $. ",font="Verdana 12",bg="green",width=22,height=2,command= lambda x = info: sellSkin(x)).grid(column=0,row=1,padx=5,pady=5)
            Button(frame,text="Send to inventory.",font="Verdana 12",bg="orange",width=22,height=2,command= lambda x = info: keepSkin(x)).grid(column=1,row=1,padx=5,pady=5)

    global index,user_coins

    if user_coins-case_prices[ID] >= 0:
        update_user_account(ID)
        for widget in frame.winfo_children():
            widget.destroy()
        index=0

        info=case.pull(filenames[ID])
        images_representation=case.generate_image_series(filenames[ID])
        images_representation.append(info[0])

        label1=Label(frame,borderwidth=2, relief="solid")
        label1.grid(column=0,row=0,padx=20,pady=10,columnspan=2)
        menubar.entryconfig(1,state=DISABLED)
        menubar.entryconfig(2,state=DISABLED)
        menubar.entryconfig(3,state=DISABLED)
        fen.after(100,changeImage,index,images_representation,info)
    else:
        showerror("Error","Not enough balance to open this case.")
        main_menu(None)

def main_menu(event):
    for widget in frame.winfo_children():
        widget.destroy()

    menubar.entryconfig(1,state=NORMAL)
    menubar.entryconfig(2,state=NORMAL)
    menubar.entryconfig(3,state=NORMAL)
    fen.title("CS:GO Case opening")

    photo1=PhotoImage(file=case_thumbnails[0])
    photo1=photo1.subsample(2,2)
    b1=Button(frame,text="AWP-DELUXE-CASE",command = lambda x=0: case_info(x),image=photo1, compound="top",bg="white",font="Verdana 11")
    b1.image=photo1
    b1.grid(column=0,row=0,padx=10,pady=10)

    photo2=PhotoImage(file=case_thumbnails[1])
    photo2=photo2.subsample(2,2)
    b2=Button(frame,text="AK-DELUXE-CASE",command = lambda x=1: case_info(x),image=photo2, compound="top",bg="white",font="Verdana 11")
    b2.image=photo2
    b2.grid(column=1,row=0,padx=10,pady=10)

    photo3=PhotoImage(file=case_thumbnails[2])
    photo3=photo3.subsample(2,2)
    b3=Button(frame,text="M4-DELUXE-CASE",command = lambda x=2: case_info(x),image=photo3, compound="top",bg="white",font="Verdana 11")
    b3.image=photo3
    b3.grid(column=2,row=0,padx=10,pady=10)

def item_iventory(ID):
    for widget in frame.winfo_children():
        widget.destroy()
    Button(frame,text="Send to account",width=50,height=2).grid(column=0,row=0,padx=50,pady=20,sticky=W)
    Button(frame,text="Sell back",command = lambda x = ID: delete_item(x),width=50,height=2).grid(column=0,row=1,padx=50,pady=20,sticky=W)

def delete_item(ID):
    global inventory,user_coins
    user_coins+=inventory[ID][1]
    balance.config(text="Balance: "+str(user_coins))
    del inventory[ID]
    inventoryUI()

def inventoryUI():
    global inventory
    items=[]
    total=0
    for widget in frame.winfo_children():
        widget.destroy()

    for loop in range(len(inventory)):
        total+=inventory[loop][1]
        photo=PhotoImage(file="Images/skins/"+inventory[loop][0])
        photo=photo.subsample(3,3)
        items.append(Button(frame,image=photo,text=inventory[loop][0].split(".")[0]+" / "+str(inventory[loop][1])+" $",compound="top",command = lambda x = loop: item_iventory(x)))
        items[-1].image=photo
        items[-1].grid(column=loop%4,row=loop//4,padx=10,pady=10)
    try:
        print(loop)
    except:
        loop=-1
    Label(frame,text="Total inventory value: "+str(total),bg="grey40",font="Verdana 11").grid(column=0,row=loop//4+1,padx=10,pady=10)

        

def depositUI():

    def checkCODE():
        global user_coins
        user_coins+=deposit.check_coupon(code.get())
        balance.config(text="Balance: "+str(user_coins))
        main_menu(None)

    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame,text="Promo code: ",bg="grey40").grid(column=0,row=0,padx=10,pady=20)
    code=StringVar()
    Entry(frame,textvariable=code,width=35).grid(column=1,row=0,padx=10,pady=10)
    Button(frame,text="Confirm",command = checkCODE,width=50,bg="green").grid(column=0,row=1,columnspan=2,padx=20,pady=10)

filenames=["Cases/case1.txt","Cases/case2.txt","Cases/case3.txt"]
casenames=["AWP-DELUXE-CASE","AK-DELUXE-CASE","M4-DELUXE-CASE"]
case_prices=[70,66,66]
case_thumbnails=["Images/cases/Case1.png","Images/cases/Case2.png","Images/cases/Case3.png"]

inventory=[]
user_coins=1000

fen=Tk()

menubar = Menu(fen)

menu0 = Menu(menubar, tearoff=0)
menu0.add_command(label="Home", command= lambda x = None: main_menu(x))
menubar.add_cascade(label="Home", menu=menu0)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Deposit",command = depositUI)
menubar.add_cascade(label="Deposit", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Inventory", command=inventoryUI)
menubar.add_cascade(label="Inventory", menu=menu2)

fen.config(menu=menubar)

frame=Frame(fen,bg="grey40")
frame.grid(column=0,row=0,columnspan=3)

balance=Label(fen,text="Balance: "+str(user_coins),font="Verdana 10")
balance.grid(column=0,row=1,padx=10,pady=10)

main_menu(None)

fen.mainloop()
