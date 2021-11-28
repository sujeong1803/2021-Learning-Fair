from tkinter import*
from tkinter import messagebox


window=Tk()
window.title("키오스크")
window.geometry("800x500")
window.resizable(width=FALSE, height=FALSE)
window.configure(background='MistyRose3')

label1=Label(window, text="3 SOO SUNGHO CAFE",font=("Times New Roman",25),bg='MistyRose3', fg="ghost white")
label1.pack()

total=0
americano, strawberry, caramel, latte, honey, muffin=0,0,0,0,0,0

def clickImage1():
    global total
    global americano
    global msg1
    americano+=1
    total+=2500
    label2.configure(text=str(total)+" 원")
    label3.configure(text="아메리카노 "+str(americano)+" 잔")
    msg1=messagebox.askquestion("HOT/ICE", "HOT으로 주문하시겠습니까?")
    if msg1=='yes':
        messagebox.showinfo("HOT/ICE","HOT으로 선택되었습니다.")
    elif msg1=='no':
        messagebox.showinfo("HOT/ICE","ICE로 선택되었습니다.")
    
def clickImage2():
    global total
    global latte
    global msg2
    latte+=1
    total+=3000
    label2.configure(text=str(total)+" 원")
    label4.configure(text="카페라떼 "+str(latte)+" 잔")
    msg2=messagebox.askquestion("HOT/ICE", "HOT으로 주문하시겠습니까?")
    if msg2=='yes':
        messagebox.showinfo("HOT/ICE","HOT으로 선택되었습니다.")
    elif msg2=='no':
        messagebox.showinfo("HOT/ICE","ICE로 선택되었습니다.")
        
def clickImage3():
    global total
    global caramel
    global msg3
    caramel+=1
    total+=3500
    label2.configure(text=str(total)+" 원")
    label5.configure(text="캬라멜 마끼아또 "+str(caramel)+" 잔")
    msg3=messagebox.askquestion("HOT/ICE", "HOT으로 주문하시겠습니까?")
    if msg3=='yes':
        messagebox.showinfo("HOT/ICE","HOT으로 선택되었습니다.")
    elif msg3=='no':
        messagebox.showinfo("HOT/ICE","ICE로 선택되었습니다.")
        
def clickImage4():
    global total
    global strawberry
    strawberry+=1
    total+=4000
    label2.configure(text=str(total)+" 원")
    label6.configure(text="딸기라떼 "+str(strawberry)+" 잔")
def clickImage5():
    global total
    global honey
    honey+=1
    total+=5000
    label2.configure(text=str(total)+" 원")
    label7.configure(text="허니브레드 "+str(honey)+" 개")
def clickImage6():
    global total
    global muffin
    muffin+=1
    total+=3000
    label2.configure(text=str(total)+" 원")
    label8.configure(text="머핀 "+str(muffin)+" 개")
choose=""
def pay():
    global choose
    if var.get()==1:
        label10.configure(text="선택한 결제방법: 현금",bg='MistyRose3')
        choose="현금"
    elif var.get()==2:
        label10.configure(text="선택한 결제방법: 카드",bg='MistyRose3')
        choose="카드"

label0=Label(window, text="--------주문 내역--------",bg='MistyRose3')
label0.pack()
label3=Label(window,text="아메리카노 0 잔", font=("Times New Roman",10),bg='MistyRose3',fg="IndianRed4")
label3.pack()
label4=Label(window,text="카페라떼 0 잔", font=("Times New Roman",10),bg='MistyRose3',fg="IndianRed4")
label4.pack()
label5=Label(window,text="캬라멜 마끼아또 0 잔", font=("Times New Roman",10),bg='MistyRose3',fg="IndianRed4")
label5.pack()
label6=Label(window,text="딸기라떼 0 잔", font=("Times New Roman",10),bg='MistyRose3',fg="IndianRed4")
label6.pack()
label7=Label(window,text="허니브레드 0 개", font=("Times New Roman",10),bg='MistyRose3',fg="IndianRed4")
label7.pack()
label8=Label(window,text="머핀 0 개", font=("Times New Roman",10),bg='MistyRose3',fg="IndianRed4")
label8.pack()

label9=Label(window, text="--------총 금액--------",bg='MistyRose3')
label9.pack()
label2=Label(window,text="0 원", font=("Times New Roman",12),bg='MistyRose3', fg="red")
label2.pack()

label11=Label(window, text="-----결제 방법-----",bg='MistyRose3')
label11.pack()

var=IntVar()
rb1=Radiobutton(window, text="현금", variable=var, value=1,bg='MistyRose3', command=pay)
rb2=Radiobutton(window, text="카드", variable=var, value=2,bg='MistyRose3', command=pay)
label10=Label(window, text="선택한 결제방법:       ",bg='MistyRose3',fg="red")

rb1.pack()
rb2.pack()
label10.pack()

def paycheck():
    messagebox.showinfo("결제","총 "+str(total)+" 원 "+choose+"(으)로 결제하시겠습니까?")
    messagebox.showinfo("결제","결제 완료되었습니다.")
    window.quit()
    window.destroy()
    
btn0=Button(window, text="결제하기", command=paycheck)
btn0.pack(side=TOP)
photo1=PhotoImage(file="C:/Temp/picture/1.gif")
btn1=Button(window, image=photo1, command=clickImage1)
btn1.pack(side=LEFT)

photo2=PhotoImage(file="C:/Temp/picture/2.gif")
btn2=Button(window, image=photo2, command=clickImage2)
btn2.pack(side=LEFT)

photo3=PhotoImage(file="C:/Temp/picture/3.gif")
btn3=Button(window, image=photo3, command=clickImage3)
btn3.pack(side=LEFT)

photo4=PhotoImage(file="C:/Temp/picture/4.gif")
btn4=Button(window, image=photo4, command=clickImage4)
btn4.pack(side=LEFT)

photo5=PhotoImage(file="C:/Temp/picture/5.gif")
btn5=Button(window, image=photo5, command=clickImage5)
btn5.pack(side=LEFT)

photo6=PhotoImage(file="C:/Temp/picture/6.gif")
btn6=Button(window, image=photo6, command=clickImage6)
btn6.pack(side=LEFT)


window.mainloop()
