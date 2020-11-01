from tkinter import*
import case

def open_case(ID):
    info=case.pull(filenames[ID])
    fen2=Toplevel()
    fen2.title(info[0].split(".")[0])
    photo=PhotoImage(file="Images/skins/"+info[0])
    label1=Label(fen2,image=photo)
    label1.image=photo
    label1.grid(column=0,row=0)
    Label(fen2,text=str(info[1]),font="Verdana 12").grid(column=0,row=1)

filenames=["case1.txt","case2.txt","case3.txt"]

fen=Tk()
fen.title("CS:GO Case opening")

frame=Frame(fen,bg="grey40")
frame.grid()

Button(frame,width=50,height=10,text="AWP-DELUXE-CASE",command = lambda x=0: open_case(x)).grid(column=0,row=0,padx=10,pady=10)
Button(frame,width=50,height=10,text="AK-DELUXE-CASE",command = lambda x=1: open_case(x)).grid(column=1,row=0,padx=10,pady=10)
Button(frame,width=50,height=10,text="M4-DELUXE-CASE",command = lambda x=2: open_case(x)).grid(column=2,row=0,padx=10,pady=10)

fen.mainloop()
