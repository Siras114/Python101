import pandas as pd
import tkinter as tk
from tkinter import ttk

file_path = 'C:\\Users\\WIN10\\OneDrive\\Desktop\\Uncle Engineer Class\\Python101\\abc.xlsx'

# อ่านไฟล์จากExcel
df = pd.read_excel(file_path, sheet_name='Sheet1')

# สร้างClass Bill
class Bill:
    def __init__(self, room_no, room_rent, electricity, internet, parking):
        self.room_no = room_no
        self.room_rent = room_rent
        self.electricity = electricity
        self.internet = internet
        self.parking = parking

    def total(self):
        return self.room_rent + self.electricity + self.internet + self.parking

    def total_by_room(self, bills):
        total_by_room = {}
        for bill in bills:
            if bill.room_no in total_by_room:
                total_by_room[bill.room_no] += bill.total()
            else:
                total_by_room[bill.room_no] = bill.total()
        return total_by_room

# สร้าง list สำหรั้บเก็บ bills
bills = []

# Loop through Excel data to create bills
for index, row in df.iterrows():
    room_no = row['Room No.']
    room_rent = row['Room Rent']
    electricity = row['Electricity']
    internet = row['Internet']
    parking = row['Parking']
    bill = Bill(room_no, room_rent, electricity, internet, parking)
    bills.append(bill)

# สร้าง GUI
root = tk.Tk()
root.geometry("300x250")
root.title("Select Room")

# สร้าง drop-down box เพื่อเลือกห้องที่จะทำการแสดงผล
room_options = [bill.room_no for bill in bills]
selected_room = tk.StringVar()
selected_room.set(room_options[0])
room_dropdown = ttk.Combobox(root, textvariable=selected_room, values=room_options)
room_dropdown.pack()

# ฟังค์ชั่นสร้างรายละเอียดบิลตามห้องที่ทำการเลือก
def show_bill():
    selected_room_no = int(selected_room.get())
    bills_for_room = [bill for bill in bills if bill.room_no == selected_room_no]

        # สร้าง window ใหม่สำหรับโชว์รายละเอียดการเช่า
    bill_window = tk.Toplevel(root)
    bill_window.geometry("250x250")
    bill_window.title(f'Room {selected_room_no}')

    room_rent_label = tk.Label(bill_window, text=f'Room Rent: {bills_for_room[0].room_rent}')
    room_rent_label.pack()
    electricity_label = tk.Label(bill_window, text=f'Electricity: {bills_for_room[0].electricity}')
    electricity_label.pack()
    internet_label = tk.Label(bill_window, text=f'Internet: {bills_for_room[0].internet}')
    internet_label.pack()
    parking_label = tk.Label(bill_window, text=f'Parking: {bills_for_room[0].parking}')
    parking_label.pack()
    total_label = tk.Label(bill_window, text=f'Total: {bills_for_room[0].total()}')
    total_label.pack()
# Create button for showing rent details
show_bill_button = tk.Button(root, text="Show Bill", command=show_bill)
show_bill_button.pack()

root.mainloop()
