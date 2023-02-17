from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวณค่าไฟ v.1')
GUI.geometry('600x300')
FONT1 = ('Angsana New', 15)

FB1 = LabelFrame(GUI,text='กรอกข้อมูล')
FB1.place(x=5,y=5)

FB2 = Frame(GUI)
FB2.place(x=250,y=5)


#WATT
watt_label = Label(FB1, text='กำลังใช้ไฟฟ้า(หน่วย:วัตต์ w)', font=FONT1)
watt_entry = Entry(FB1)
watt_label.pack()
watt_entry.pack()
#TIME/HOUR
hours_label = Label(FB1, text='ระยะเวลาการใช้ (ชั่วโมง)', font=FONT1)
hours_entry = Entry(FB1)
hours_label.pack()
hours_entry.pack()
#RATE/UNIT
rate_label = Label(FB1, text='ราคา (บาท/ยูนิต)', font=FONT1)
rate_entry = Entry(FB1)
rate_label.pack()
rate_entry.pack()

def Calculate():
    global total
    watt = float(watt_entry.get())
    time = float(hours_entry.get())
    uprice = float(rate_entry.get())
    unit = watt*time/1000
    total = unit*uprice
    text = 'จำนวนยูนิตที่ใช้ {:.2f} ยูนิต คิดเป็นเงิน{:.2f}บาท'.format(unit,total)
    messagebox.showinfo('ค่าไฟทั้งสิ้น',text)

#####BUTTON#####
total = 0
B1 = ttk.Button(GUI,text='คำนวณค่าไฟ',command=Calculate)
B1.place(x=60,y=220)

####frameแสดงผล####

text = 'แสดงผลรวมของค่าไฟแต่ละอย่าง\nจำนวนยูนิต x ค่าไฟ y\nจำนวนยูนิต x ค่าไฟ y'
total_electric = StringVar()
total_electric.set(text)
R2 = Label(FB2,textvariable=total_electric)
R2.pack()
G_total = StringVar()
G_total.set('รวมค่าไฟทั้งสิ้น')

####ปุ่มเริ่มใหม่####
FB = Frame(GUI)
FB.place(x=250,y=200)
B1 = ttk.Button(FB,text='เริ่มใหม่')
B1.pack(ipadx=30, ipady=20)

GUI.mainloop()