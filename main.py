from tkinter import *
root = Tk()
root.title("메뉴")
root.geometry("600x300+200+200")
root.resizable(False,False)

def cook():
    top=Toplevel(root)
    top.title("식사")
    top.geometry("700x100+100+100")
    top.resizable(False,False)

    def hamberger():
        print("2000원입니다")

    btn2 = Button(top,text="햄버거",command=hamberger)
    btn2.pack()

    def nuddle():
        print("1500원입니다")


    btn3 = Button(top,text = "라면",command=nuddle)
    btn3.pack()

btn1= Button(root,text = "식사",command=cook,width=30,height=7)
btn1.place(x=40,y=10)

def drink():
    top=Toplevel(root)
    top.title("음료")
    top.geometry("900x300+100+100")
    top.resizable(False,False)
    
    def coke():
        print("1000원입니다")


    button_image = PhotoImage(file="4632.png")
    btn5 = Button(top,text="콜라",command=coke,image = button_image,width =130,height=150)
    btn5.place(x=40,y=10)
 
    btn5.image = button_image 
    btn8 = Button(top,text="콜라",bg="red",width= 3,height=1)
    btn8.place(x=80,y=165)

    def cider():
        print("1000원입니다")
    
    button_image = PhotoImage(file="1.png")
    btn6 = Button(top,text="사이다",command=coke,image = button_image,width =130,height=150)
    btn6.place(x=370,y=10)
 
    btn6.image = button_image 
    btn6 = Button(top,text="사이다",bg="green",width= 3,height=1)
    btn6.place(x=424,y=165)

    def water():
        print("500원입니다")

    button_image = PhotoImage(file="13.png")
    btn6 = Button(top,text="생수",command = water,image = button_image,width = 130,height=150)
    btn6.place(x=650,y=10)
 
    btn6.image = button_image 
    btn6 = Button(top,text="생수",bg="blue",width = 3,height=1)
    btn6.place(x=700,y=165)
   
btn4 = Button(root,text = "음료",command=drink,width=30,height=7)
btn4.place(x=350,y=10)

def message():
    from tkinter import messagebox
    messagebox.showinfo("주문완료!","주문이 완료되었습니다,맛있게 드세요!")

btn6 = Button(root,text = "주문하기!",command = message,bg ="yellow",width=15,height=3)
btn6.place(x=480,y=240)

def close():
    root.destroy()
   
btn7 = Button(root,text = "나가기",command=close,width=15,height=3,bg="yellow")
btn7.place(x=1,y=240)


root.mainloop()
    

#하하 호호 

