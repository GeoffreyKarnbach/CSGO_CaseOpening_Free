from tkinter import*
import case
import random

def update_user_account(ID):
    print("Bought case "+casenames[ID]+" for "+str(case_prices[ID])+" $.")

def keepSkin(info):
    print("KEEP ",info)
    main_menu(None)

def sellSkin(info):
    print("SOLD ",info)
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

    global index

    update_user_account(ID)
    for widget in frame.winfo_children():
        widget.destroy()
    index=0

    info=case.pull(filenames[ID])
    images_representation=case.generate_image_series(filenames[ID])
    images_representation.append(info[0])

    label1=Label(frame,borderwidth=2, relief="solid")
    label1.grid(column=0,row=0,padx=20,pady=10,columnspan=2)
    fen.after(100,changeImage,index,images_representation,info)

def main_menu(event):
    for widget in frame.winfo_children():
        widget.destroy()

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

filenames=["Cases/case1.txt","Cases/case2.txt","Cases/case3.txt"]
casenames=["AWP-DELUXE-CASE","AK-DELUXE-CASE","M4-DELUXE-CASE"]
case_prices=[60,66,66]
case_thumbnails=["Images/cases/Case1.png","Images/cases/Case2.png","Images/cases/Case3.png"]

inventory=[]

fen=Tk()
frame=Frame(fen,bg="grey40")
frame.grid(column=0,row=0)
main_menu(None)

fen.mainloop()
