from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

GUI = Tk()
GUI.title('Car rental management system')
GUI.geometry('1920x1080')
bg_color = '#F5F5DC'


def Exit():
    if messagebox.askyesno('Exit', 'Do you want to exit'):
        GUI.destroy()


# program functions

def window2():
    def saveinfo():
        Ref_info = Ref.get()
        Ref_info = str(Ref_info)
        name_info = name.get()
        age_info = age.get()
        age_info = str(age_info)
        gender_info = gender.get()
        job_info = job.get()
        Address_info = Address.get()
        Phone_info = Phone.get()
        License_info = License.get()

        print(Ref_info, name_info, age_info, gender_info, job_info, Address_info, Phone_info, License_info)

        file1 = open("user.txt", "w")
        file1.write('Ref: ' + Ref_info + '\n')
        file1.write('Firstname: ' + name_info + '\n')
        file1.write('Age: ' + age_info + '\n')
        file1.write('Gender: ' + gender_info + '\n')
        file1.write('Job: ' + job_info + '\n')
        file1.write('Phone: ' + Phone_info + '\n')
        file1.write('License: ' + License_info + '\n')
        file1.write('Address: ' + Address_info + '\n')
        file1.close()

        print(" User ", Ref_info, name_info, "has been registered successfully")

        Ref_entry.delete(0, END)
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        gender_entry.delete(0, END)
        job_entry.delete(0, END)
        Address_entry.delete(0, END)
        Phone_entry.delete(0, END)
        License_entry.delete(0, END)

    # Defined variables

    Ref = IntVar()
    name = StringVar()
    age = IntVar()
    gender = StringVar()
    job = StringVar()
    Address = StringVar()
    Phone = StringVar()
    License = StringVar()

    w2 = Tk(className='Manage Customer')
    w2.geometry("1200x800")

    # headings

    title1 = Label(w2, text='Manage customer', bg=bg_color, fg='black', font=('arial', 35, 'bold'), relief=GROOVE,
                   bd=12)
    title1.pack(fill=X)

    # left side settings

    F5 = Frame(w2, bg=bg_color, relief=RIDGE, bd=15)
    F5.place(x=0, y=80, width=650, height=550)

    refLabel = Label(F5, text='Customer ref', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    refLabel.grid(row=0, column=0, padx=30, pady=10)
    Ref_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=Ref)
    Ref_entry.grid(row=0, column=1, pady=10, sticky='w')

    nameLabel = Label(F5, text='Full Name', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    nameLabel.grid(row=1, column=0, padx=30, pady=10)
    name_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=name)
    name_entry.grid(row=1, column=1, pady=10, sticky='w')

    ageLabel = Label(F5, text='Age', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    ageLabel.grid(row=2, column=0, padx=30, pady=10)
    age_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=age)
    age_entry.grid(row=2, column=1, pady=10, sticky='w')

    genderLabel = Label(F5, text='Gender', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    genderLabel.grid(row=3, column=0, padx=30, pady=10)

    gender_entry = ttk.Combobox(F5, font=('arial', 18), state='readonly', textvariable=gender)
    gender_entry['value'] = ('male', 'female')
    gender_entry.grid(row=3, column=1, pady=10)

    jobLabel = Label(F5, text='Job', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    jobLabel.grid(row=4, column=0, padx=30, pady=10)

    job_entry = ttk.Combobox(F5, font=('arial', 18), state='readonly', textvariable=job)
    job_entry['value'] = ('Business man', 'Teacher', ' Doctor ', 'Engineer', 'lawyer')
    job_entry.grid(row=4, column=1, pady=10)

    numberLabel = Label(F5, text='Contact No.', font=('arial', 20, 'bold'), fg='black', bg=bg_color)
    numberLabel.grid(row=5, column=0, padx=30, pady=10)
    Phone_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=Phone)
    Phone_entry.grid(row=5, column=1, pady=10, sticky='w')

    LicenseLabel = Label(F5, text='License', font=('arial', 20, 'bold'), fg='black', bg=bg_color)
    LicenseLabel.grid(row=6, column=0, padx=30, pady=10)
    License_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=License)
    License_entry.grid(row=6, column=1, pady=10, sticky='w')

    addressLabel = Label(F5, text='Address', font=('arial', 20, 'bold'), fg='black', bg=bg_color)
    addressLabel.grid(row=7, column=0, padx=30, pady=10)
    Address_entry = Entry(F5, font=('arial', 10), relief=RIDGE, bd=7, textvariable=Address)
    Address_entry.grid(row=7, column=1, pady=5, sticky='w')

    F6 = Frame(w2, bg=bg_color, relief=RIDGE, bd=15)
    F6.place(x=650, y=80, width=550, height=540)

    # Right-side-settings

    F7 = Frame(w2, bg=bg_color, relief=RIDGE, bd=15)
    F7.place(x=0, y=610, width=1200, height=600)

    # Buttons Settings

    button14 = Button(F7, text='Save in txt', font='arial 18 bold', bg='black', fg='white', width=8, command=saveinfo)
    button14.grid(row=0, column=1, padx=25, pady=8)

    button16 = Button(F7, text='Exit', font='arial 18 bold', bg='black', fg='white', width=8, command=Exit)
    button16.grid(row=0, column=4, padx=25, pady=8)


def window3():
    def saveInfo1():
        carname_info = carname.get()
        modelyear_info = modelyear.get()
        modelyear_info = str(modelyear_info)
        fueltype_info = fueltype.get()
        brandname_info = brandname.get()
        priceperday_info = priceperday.get()
        priceperday_info = str(priceperday_info)
        seatingcapacity_info = seatingcapacity.get()
        seatingcapacity_info = str(seatingcapacity_info)

        print(carname_info, modelyear_info, fueltype_info, brandname_info, priceperday_info, seatingcapacity_info)

        file2 = open("car.txt", "w")
        file2.write('Car name: ' + carname_info + '\n')
        file2.write('Model year: ' + modelyear_info + '\n')
        file2.write('Fuel type: ' + fueltype_info + '\n')
        file2.write('Brand name: ' + brandname_info + '\n')
        file2.write('Price per day: ' + priceperday_info + '\n')
        file2.write('seating capacity: ' + seatingcapacity_info + '\n')
        file2.close()
        print("The car ",  carname_info, "has been registered successfully")

        carname_entry.delete(0, END)
        modelyear_entry.delete(0, END)
        fueltype_entry.delete(0, END)
        brandname_entry.delete(0, END)
        priceperday_entry.delete(0, END)
        seatingcapacity_entry.delete(0, END)

    carname = StringVar()
    modelyear = IntVar()
    fueltype = StringVar()
    brandname = StringVar()
    priceperday = IntVar()
    seatingcapacity = IntVar()

    w3 = Tk(className='Manage Car')
    w3.geometry("1200x800")

    title2 = Label(w3, text='Manage car', bg=bg_color, fg='black', font=('arial', 35, 'bold'), relief=GROOVE, bd=12)
    title2.pack(fill=X)

    F5 = Frame(w3, bg=bg_color, relief=RIDGE, bd=15)
    F5.place(x=0, y=80, width=650, height=550)

    carnameLabel = Label(F5, text='Car name', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    carnameLabel.grid(row=1, column=0, padx=30, pady=10)
    carname_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=carname)
    carname_entry.grid(row=1, column=1, pady=10, sticky='w')

    modelyearLabel = Label(F5, text='Model year', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    modelyearLabel.grid(row=2, column=0, padx=30, pady=10)
    modelyear_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=modelyear)
    modelyear_entry.grid(row=2, column=1, pady=10, sticky='w')

    fueltypeLabel = Label(F5, text='Fuel type', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    fueltypeLabel.grid(row=3, column=0, padx=30, pady=10)

    fueltype_entry = ttk.Combobox(F5, font=('arial', 18), state='readonly', textvariable=fueltype)
    fueltype_entry['value'] = ('Unleaded 95', 'Unleaded 98 super')
    fueltype_entry.grid(row=3, column=1, pady=10)

    brandnameLabel = Label(F5, text='Brand name', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    brandnameLabel.grid(row=4, column=0, padx=30, pady=10)
    brandname_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=brandname)
    brandname_entry.grid(row=4, column=1, pady=10, sticky='w')

    priceperdayLabel = Label(F5, text='Price per day', font=('arial', 20, 'bold'), fg='black', bg=bg_color)
    priceperdayLabel.grid(row=5, column=0, padx=30, pady=10)
    priceperday_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=priceperday)
    priceperday_entry.grid(row=5, column=1, pady=10, sticky='w')

    seatingcapacityLabel = Label(F5, text='Seating capacity', font=('arial', 20, 'bold'), fg='black', bg=bg_color)
    seatingcapacityLabel.grid(row=6, column=0, padx=30, pady=10)
    seatingcapacity_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=seatingcapacity)
    seatingcapacity_entry.grid(row=6, column=1, pady=10, sticky='w')

    F6 = Frame(w3, bg=bg_color, relief=RIDGE, bd=15)
    F6.place(x=650, y=80, width=550, height=540)

    F7 = Frame(w3, bg=bg_color, relief=RIDGE, bd=15)
    F7.place(x=0, y=610, width=1200, height=600)

    button6 = Button(F7, text='Save in txt', font='arial 18 bold', bg='black', fg='white', width=8, command=saveInfo1)
    button6.grid(row=0, column=1, padx=25, pady=8)

    button8 = Button(F7, text='Exit', font='arial 18 bold', bg='black', fg='white', width=8, command=Exit)
    button8.grid(row=0, column=4, padx=25, pady=8)


def window4():
    def saveInfo2():
        choosecar_info = choosecar.get()
        customernumber_info = customernumber.get()
        customernumber_info = str(customernumber_info)
        From_info = From.get()
        From_info = str(From_info)
        To_info = To.get()
        To_info = str(To_info)
        Totaldays_info = Totaldays.get()
        Totaldays_info = str(Totaldays_info)
        priceperday_info = priceperday.get()
        priceperday_info = str(priceperday_info)
        total_info = total.get()
        total_info = str(total_info)

        print(choosecar_info, customernumber_info, From_info, To_info, Totaldays_info, priceperday_info, total_info)

        file3 = open("Rent receipt.txt", "w")
        file3.write('Car chosen: ' + choosecar_info + '\n')
        file3.write('Customer number: ' + customernumber_info + '\n')
        file3.write('From: ' + From_info + '\n')
        file3.write('To: ' + To_info + '\n')
        file3.write('Total days: ' + Totaldays_info + '\n')
        file3.write('Price per day: ' + priceperday_info + '\n')
        file3.write('Total:' + total_info + '\n')
        file3.close()
        print("Receipt of",  customernumber_info, "has been registered successfully")

        choosecar_entry.delete(0, END)
        customernumber_entry.delete(0, END)
        From_entry.delete(0, END)
        To_entry.delete(0, END)
        Totaldays_entry.delete(0, END)
        priceperday_entry.delete(0, END)
        total_entry.delete(0, END)

    choosecar = StringVar()
    customernumber = IntVar()
    From = IntVar()
    To = IntVar()
    Totaldays = IntVar()
    priceperday = IntVar()
    total = IntVar()

    w4 = Tk(className='Rent')
    w4.geometry("1200x800")

    title3 = Label(w4, text='Rent', bg=bg_color, fg='black', font=('arial', 35, 'bold'), relief=GROOVE, bd=12)
    title3.pack(fill=X)

    F5 = Frame(w4, bg=bg_color, relief=RIDGE, bd=15)
    F5.place(x=0, y=80, width=650, height=550)

    choosecarLabel = Label(F5, text='Choose car', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    choosecarLabel.grid(row=1, column=0, padx=30, pady=10)
    choosecar_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=choosecar)
    choosecar_entry.grid(row=1, column=1, pady=10, sticky='w')

    customernumberLabel = Label(F5, text='Customer number', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    customernumberLabel.grid(row=2, column=0, padx=30, pady=10)
    customernumber_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=customernumber)
    customernumber_entry.grid(row=2, column=1, pady=10, sticky='w')

    FromLabel = Label(F5, text='From', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    FromLabel.grid(row=3, column=0, padx=30, pady=10)
    From_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=From)
    From_entry.grid(row=3, column=1, pady=10, sticky='w')

    ToLabel = Label(F5, text='To', font=('arial', 18, 'bold'), fg='black', bg=bg_color)
    ToLabel.grid(row=4, column=0, padx=30, pady=10)
    To_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=To)
    To_entry.grid(row=4, column=1, pady=10, sticky='w')

    TotaldaysLabel = Label(F5, text='Total days', font=('arial', 20, 'bold'), fg='black', bg=bg_color)
    TotaldaysLabel.grid(row=5, column=0, padx=30, pady=10)
    Totaldays_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=Totaldays)
    Totaldays_entry.grid(row=5, column=1, pady=10, sticky='w')

    priceperdayLabel = Label(F5, text='Price per day', font=('arial', 20, 'bold'), fg='black', bg=bg_color)
    priceperdayLabel.grid(row=6, column=0, padx=30, pady=10)
    priceperday_entry = Entry(F5, font=('arial', 18, 'bold'), relief=RIDGE, bd=7, textvariable=priceperday)
    priceperday_entry.grid(row=6, column=1, pady=10, sticky='w')

    totalLabel = Label(F5, text='Total price', font=('arial', 20, 'bold'), fg='black', bg=bg_color)
    totalLabel.grid(row=7, column=0, padx=30, pady=10)
    total_entry = Entry(F5, width=40, font=('arial', 10), relief=RIDGE, bd=7, textvariable=total)
    total_entry.grid(row=7, column=1, pady=5, sticky='w')

    F6 = Frame(w4, bg=bg_color, relief=RIDGE, bd=15)
    F6.place(x=650, y=80, width=550, height=540)

    F7 = Frame(w4, bg=bg_color, relief=RIDGE, bd=15)
    F7.place(x=0, y=610, width=1200, height=600)

    button10 = Button(F7, text='Save in txt', font='arial 18 bold', bg='black', fg='white', width=8, command=saveInfo2)
    button10.grid(row=0, column=1, padx=25, pady=8)

    button12 = Button(F7, text='Exit', font='arial 18 bold', bg='black', fg='white', width=8, command=Exit)
    button12.grid(row=0, column=4, padx=25, pady=8)


# Heading

title = Label(GUI, text='Car rental management system', bg=bg_color, fg='black', font=('arial', 35, 'bold'),
              relief=GROOVE, bd=12)
title.pack(fill=X)

F3 = Frame(GUI, bg=bg_color, relief=GROOVE, bd=15)
F3.place(x=0, y=80, width=1920, height=1080)

button1 = Button(F3, text='Manage Customer ', font='arial 18 bold', bg='#000000', fg='white', width=15,
                 command=window2)
button1.grid(row=1, column=0, padx=25, pady=50)

button2 = Button(F3, text='Manage car', font='arial 18 bold', bg='#000000', fg='white', width=15, command=window3)
button2.grid(row=2, column=0, padx=25, pady=50)

button3 = Button(F3, text='Rent', font='arial 18 bold', bg='#000000', fg='white', width=15, command=window4)
button3.grid(row=3, column=0, padx=25, pady=50)

button4 = Button(F3, text='Exit', font='arial 18 bold', bg='#000000', fg='white', width=15, command=Exit)
button4.grid(row=4, column=0, padx=25, pady=50)

Label(GUI).pack()
image = Image.open(
    "C:\\Users\\hrida\\PycharmProjects\\Carrentalmangemantsystem\\2017-Mercedes-Benz-E-Class-E300-Sedan-(US-Spec)---Lineup-130942-2560x1440.jpg")

image = image.resize((1100, 700), Image.ANTIALIAS)

imagenew = ImageTk.PhotoImage(image)
Label(GUI, image=imagenew).place(x=400, y=100)

GUI.mainloop()
