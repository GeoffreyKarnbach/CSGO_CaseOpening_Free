from tkinter import*
import case
import random



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
            Label(frame,text=str(info[1]),font="Verdana 12",bg="grey40").grid(column=0,row=1)

    global index

    for widget in frame.winfo_children():
        widget.destroy()

    index=0

    info=case.pull(filenames[ID])
    images_representation=case.generate_image_series(filenames[ID])
    images_representation.append(info[0])

    label1=Label(frame,borderwidth=2, relief="solid")
    label1.grid(column=0,row=0,padx=20,pady=20)
    fen.after(100,changeImage,index,images_representation,info)

def main_menu(event):
    for widget in frame.winfo_children():
        widget.destroy()

    fen.title("CS:GO Case opening")
    Button(frame,width=50,height=10,text="AWP-DELUXE-CASE",command = lambda x=0: open_case(x)).grid(column=0,row=0,padx=10,pady=10)
    Button(frame,width=50,height=10,text="AK-DELUXE-CASE",command = lambda x=1: open_case(x)).grid(column=1,row=0,padx=10,pady=10)
    Button(frame,width=50,height=10,text="M4-DELUXE-CASE",command = lambda x=2: open_case(x)).grid(column=2,row=0,padx=10,pady=10)

filenames=["case1.txt","case2.txt","case3.txt"]
casenames=["AWP-DELUXE-CASE","AK-DELUXE-CASE","M4-DELUXE-CASE"]
case_prices=[60,66,66]
case_thumbnails=[]

fen=Tk()
frame=Frame(fen,bg="grey40")
frame.grid(column=0,row=0)
main_menu(None)

fen.bind("<F1>",main_menu)
fen.mainloop()
