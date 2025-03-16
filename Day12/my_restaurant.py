from tkinter import *
import datetime
import random
from tkinter import filedialog, messagebox

operator = ''
prices_food = [1.32, 2.34, 3.50, 4.20, 5.10, 6.75, 7.99, 8.45, 9.60, 10.99, 11.30, 12.15, 13.40, 14.25, 15.80]
prices_drinks = [0.99, 1.50, 2.20, 2.75, 3.10, 3.80, 4.25, 4.60, 5.30, 5.75, 6.40, 6.90, 7.20, 7.80, 8.50]
prices_desserts = [2.50, 3.25, 3.90, 4.50, 5.25, 5.80, 6.40, 6.90, 7.50, 8.25, 8.90, 9.50, 10.10, 10.75, 11.30]

def click_btn(num):
    global operator
    operator = operator + num
    calc_viewer.delete(0, END)
    calc_viewer.insert(END, operator)

def delete():
    global operator
    operator = ''
    calc_viewer.delete(0, END)

def get_result():
    global operator
    result = str(eval(operator))
    calc_viewer.delete(0, END)
    calc_viewer.insert(0, result)
    operator = ''

def check_review():
    i = 0
    for c in box_food:
        if var_food[i].get() == 1:
            box_food[i].config(state=NORMAL)
            if box_food[i].get() == '0':
                box_food[i].delete(0, END)
            box_food[i].focus()
        else:
            box_food[i].config(state=DISABLED)
            text_food[i].set('0')
        i += 1
    j = 0
    for c in box_drink:
        if var_drink[j].get() == 1:
            box_drink[j].config(state=NORMAL)
            if box_drink[j].get() == '0':
                box_drink[j].delete(0, END)
            box_drink[j].focus()
        else:
            box_drink[j].config(state=DISABLED)
            text_drink[j].set('0')
        j += 1
    k = 0
    for c in box_dessert:
        if var_dessert[k].get() == 1:
            box_dessert[k].config(state=NORMAL)
            if box_dessert[k].get() == '0':
                box_dessert[k].delete(0, END)
            box_dessert[k].focus()
        else:
            box_dessert[k].config(state=DISABLED)
            text_dessert[k].set('0')
        k += 1

def calc_total():
    subtotal_food = 0
    p = 0
    for amount in box_food:
        subtotal_food = subtotal_food + (int(amount.get()) * prices_food[p])
        p += 1
    subtotal_drinks = 0
    p = 0
    for amount in box_drink:
        subtotal_drinks = subtotal_drinks + (int(amount.get()) * prices_drinks[p])
        p += 1
    subtotal_desserts = 0
    p = 0
    for amount in box_dessert:
        subtotal_desserts = subtotal_desserts + (int(amount.get()) * prices_desserts[p])
        p += 1
    subtotal = subtotal_food + subtotal_drinks + subtotal_desserts
    taxes = subtotal * 0.07
    total = subtotal + taxes
    var_food_cost.set(f'$ {round(subtotal_food, 2)}')
    var_drink_cost.set(f'$ {round(subtotal_drinks, 2)}')
    var_dessert_cost.set(f'$ {round(subtotal_desserts, 2)}')
    var_subtotal.set(f'$ {round(subtotal ,2)}')
    var_taxes.set(f'$ {round(taxes ,2)}')
    var_total.set(f'$ {round(total ,2)}')

def gen_receipt():
    text_receipt.delete(1.0, END)
    num_receipt = f'N# - {random.randint(1000, 9999)}'
    date = datetime.datetime.now()
    date_recept = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    text_receipt.insert(END, f'Receipt:\t{num_receipt}\t\t{date_recept}\n')
    text_receipt.insert(END, f'*' * 47)
    text_receipt.insert(END, f'\nITEMS\t\tAMOUNT\t\tCOST ITEMS\n')
    text_receipt.insert(END, f'- ' * 47 +'\n')

    i = 0
    for food in text_food:
        if food.get() != '0':
            text_receipt.insert(END, f'{food_list[i]}\t\t{food.get()}\t\t${round(int(food.get()) * prices_food[i], 2)}\n')
        i += 1

    i = 0
    for drink in text_drink:
        if drink.get() != '0':
            text_receipt.insert(END, f'{drinks_list[i]}\t\t{drink.get()}\t\t${round(int(drink.get()) * prices_drinks[i], 2)}\n')
        i += 1

    i = 0
    for dessert in text_dessert:
        if dessert.get() != '0':
            text_receipt.insert(END, f'{desserts_list[i]}\t\t{dessert.get()}\t\t${round(int(dessert.get()) * prices_desserts[i], 2)}\n')
        i += 1

    text_receipt.insert(END, f'- ' * 47)
    text_receipt.insert(END, f'\nFOOD COST:\t\t\t\t{var_food_cost.get()}')
    text_receipt.insert(END, f'\nDRINKS COST:\t\t\t\t{var_drink_cost.get()}')
    text_receipt.insert(END, f'\nDESSERT COST:\t\t\t\t{var_dessert_cost.get()}\n')
    text_receipt.insert(END, f'- ' * 47)
    text_receipt.insert(END, f'\nSUBTOTAL:\t\t\t\t{var_subtotal.get()}')
    text_receipt.insert(END, f'\nTAXES:\t\t\t\t{var_taxes.get()}')
    text_receipt.insert(END, f'\nTOTAL:\t\t\t\t{var_total.get()}\n')
    text_receipt.insert(END, f'*' * 47)
    text_receipt.insert(END, f'\nThank you for visiting us\nCOME BACK SOON!')

def save_ticket():
    info_receipt = text_receipt.get(1.0, END)
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    file.write(info_receipt)
    file.close()
    messagebox.showinfo('Information', 'Your ticket has been saved')

def reset():
    # Clear receipt
    text_receipt.delete(0.1, END)
    # Reset menu inputs values
    for text in text_food:
        text.set('0')
    for text in text_drink:
        text.set('0')
    for text in text_dessert:
        text.set('0')
    # Disable menu inputs
    for box in box_food:
        box.config(state=DISABLED)
    for box in box_drink:
        box.config(state=DISABLED)
    for box in box_dessert:
        box.config(state=DISABLED)
    # Clear check boxs
    for var in var_food:
        var.set(0)
    for var in var_drink:
        var.set(0)
    for var in var_dessert:
        var.set(0)
    # Clear totals
    var_food_cost.set('')
    var_drink_cost.set('')
    var_dessert_cost.set('')
    var_total.set('')
    var_subtotal.set('')
    var_taxes.set('')

# INIT TKINTER
application = Tk()
# window size
application.geometry("1350x630+0+0")
# avoid maximize window
application.resizable(0, 0)
# window title
application.title("Python Restaurant - Billing System")
# background color
application.config(bg="burlywood")

# ==============================   TOP PANEL   ============================== #
top_panel = Frame(application, bd=1, relief=SUNKEN)
top_panel.pack(side=TOP)
# title label
title_label = Label(top_panel, text="Billing System", fg="azure4", font=('Dosis', 58), bg="burlywood", width=27)
title_label.grid(row=0, column=0)

# ==============================   LEFT PANEL   ============================== #
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# COST PANEL #
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4')
cost_panel.pack(side=BOTTOM)

# FOOD PANEL #
food_panel = LabelFrame(left_panel, text="Food", font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg="azure4")
food_panel.pack(side=LEFT)

# DRINKS PANEL
drinks_panel = LabelFrame(left_panel, text="Drinks", font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg="azure4")
drinks_panel.pack(side=LEFT)

# DESSERTS PANEL
desserts_panel = LabelFrame(left_panel, text="Desserts", font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg="azure4")
desserts_panel.pack(side=LEFT)

# ==============================   RIGHT PANEL   ============================== #
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# CALCULATOR PANEL
calc_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
calc_panel.pack() # Default side = TOP

# RECEIPT PANEL
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
receipt_panel.pack() # Default side = TOP

# BUTTONS PANEL
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
buttons_panel.pack() # Default side = TOP

# ==============================   CONTENT   ============================== #
# MENU LISTS
food_list = ['chicken', 'lamb', 'kebab', 'hake', 'beef', 'salmon', 'pork', 'tofu', 'shrimp', 'duck', 'turkey',
             'mutton', 'fish', 'sausages', 'goat']
drinks_list = ['water', 'coffee', 'tea', 'soda', 'juice', 'beer', 'wine', 'whiskey', 'vodka', 'rum', 'milk',
               'smoothie', 'iced tea', 'lemonade', 'cocktail']
desserts_list = ['cake', 'pie', 'ice cream', 'cookies', 'brownies', 'cheesecake', 'pudding', 'muffins', 'tarts',
                 'cupcakes', 'macaroons', 'flan', 'churros', 'donuts', 'fruit salad']
# FOOD CHECK BUTTONS
var_food = []
box_food = []
text_food = []
counter = 0
for food in food_list:
    # Create check btn
    var_food.append('')
    var_food[counter] = IntVar()
    food = Checkbutton(food_panel,
                       text=food.title(),
                       font=('Dosis', 19, 'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=var_food[counter],
                       command=check_review)
    food.grid(row=counter,
              column=0,
              sticky='w')
    # Create the food boxes
    box_food.append('')
    text_food.append('')
    text_food[counter] = StringVar()
    text_food[counter].set('0')
    box_food[counter] = Entry(food_panel,
                               font=('Dosis', 18, 'bold'),
                               bd=1,
                               width=6,
                               state=DISABLED,
                               textvariable=text_food[counter])
    box_food[counter].grid(row=counter,
                           column=1,
                           sticky='w')
    counter += 1

# DRINKS CHECK BUTTONS
var_drink = []
box_drink = []
text_drink = []
counter = 0
for drink in drinks_list:
    var_drink.append('')
    var_drink[counter] = IntVar()
    # Create check btn
    drink = Checkbutton(drinks_panel,
                        text=drink.title(),
                        font=('Dosis', 19, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=var_drink[counter],
                        command=check_review)
    drink.grid(row=counter,
               column=0,
               sticky='w')
    # Create box input
    box_drink.append('')
    text_drink.append('')
    text_drink[counter] = StringVar()
    text_drink[counter].set('0')
    box_drink[counter] = Entry(drinks_panel,
                               font=('Dosis', 18, 'bold'),
                               bd=1,
                               width=6,
                               state=DISABLED,
                               textvariable=text_drink[counter])
    box_drink[counter].grid(row=counter,
                           column=1,
                           sticky='w')
    counter += 1

# DESSERTS CHECK BUTTONS
var_dessert = []
box_dessert = []
text_dessert = []
counter = 0
for dessert in desserts_list:
    var_dessert.append('')
    var_dessert[counter] = IntVar()
    # Create check btn
    desserts = Checkbutton(desserts_panel,
                           text=dessert.title(),
                           font=('Dosis', 19, 'bold'),
                           onvalue=1,
                           offvalue=0,
                           variable=var_dessert[counter],
                           command=check_review)
    desserts.grid(row=counter,
                  column=0,
                  sticky='w')
    # Create input box
    box_dessert.append('')
    text_dessert.append('')
    text_dessert[counter] = StringVar()
    text_dessert[counter].set('0')
    box_dessert[counter] = Entry(desserts_panel,
                                font=('Dosis', 18, 'bold'),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=text_dessert[counter])
    box_dessert[counter].grid(row=counter,
                             column=1,
                             sticky='w')
    counter += 1

# VARIABLES
var_food_cost = StringVar()
var_drink_cost = StringVar()
var_dessert_cost = StringVar()
var_total = StringVar()
var_subtotal = StringVar()
var_taxes = StringVar()

# ==============================   COSTS LABELS AND INPUTS   ============================== #
# FOOD COST LABELS AND INPUTS
label_cost_food = Label(cost_panel, text='Food Cost:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
label_cost_food.grid(row=0, column=0, sticky='w')
text_cost_food = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                       textvariable=var_food_cost)
text_cost_food.grid(row=0, column=1, sticky='w', padx=105)

# DRINKS COST LABELS AND INPUTS
label_cost_drink = Label(cost_panel, text='Drinks Cost:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
label_cost_drink.grid(row=1, column=0, sticky='w')
text_cost_drink = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                       textvariable=var_drink_cost)
text_cost_drink.grid(row=1, column=1, sticky='w', padx=105)

# DESSERTS COST LABELS AND INPUTS
label_cost_dessert = Label(cost_panel, text='Desserts Cost:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
label_cost_dessert.grid(row=2, column=0, sticky='w')
text_cost_dessert = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                       textvariable=var_dessert_cost)
text_cost_dessert.grid(row=2, column=1, sticky='w', padx=105)

# SUBTOTAL COST LABELS AND INPUTS
label_cost_subtotal = Label(cost_panel, text='Subtotal:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
label_cost_subtotal.grid(row=0, column=2, sticky='w')
text_cost_subtotal = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                       textvariable=var_subtotal)
text_cost_subtotal.grid(row=0, column=3, sticky='w', padx=105)

# TAXES COST LABELS AND INPUTS
label_cost_taxes = Label(cost_panel, text='Taxes:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
label_cost_taxes.grid(row=1, column=2, sticky='w')
text_cost_taxes = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                       textvariable=var_taxes)
text_cost_taxes.grid(row=1, column=3, sticky='w', padx=105)

# TOTAL COST LABELS AND INPUTS
label_cost_total = Label(cost_panel, text='TOTAL:', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
label_cost_total.grid(row=2, column=2, sticky='w')
text_cost_total = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly',
                       textvariable=var_total)
text_cost_total.grid(row=2, column=3, sticky='w', padx=105)

# ==============================   BUTTONS   ============================== #
buttons = ['total', 'receipt', 'save', 'reset']
buttons_created = []
columns = 0
for button in buttons:
    button = Button(buttons_panel, text=button.title(), font=('Dosis', 14, 'bold'), bg='azure4', fg='white',
                    bd=1, width=9)
    buttons_created.append(button)
    button.grid(row = 0, column = columns)
    columns += 1

buttons_created[0].config(command = calc_total)
buttons_created[1].config(command = gen_receipt)
buttons_created[2].config(command = save_ticket)
buttons_created[3].config(command = reset)


# RECEIPT AREA
text_receipt = Text(receipt_panel, font=('Dosis', 12, 'bold'), bd=1, width=57, height=10)
text_receipt.grid(row=0, column=0)

# ==============================   CALCULATOR   ============================== #
calc_viewer = Entry(calc_panel, font=('Dosis', 16, 'bold'), bd=1, width=42)
calc_viewer.grid(row=0, column=0, columnspan=4)
calc_buttons = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '=', 'DEL', '0', '÷']
btn_save = []
row = 1
column = 0
for btn in calc_buttons:
    btn = Button(calc_panel, text=btn.title(), fg='white', bg='azure4', font=('Dosis', 16, 'bold'), bd=1, width=8)
    btn_save.append(btn)
    btn.grid(row=row, column=column)
    if column == 3:
        row += 1
    column += 1
    if column == 4:
        column = 0

btn_save[0].config(command=lambda : click_btn('7'))
btn_save[1].config(command=lambda : click_btn('8'))
btn_save[2].config(command=lambda : click_btn('9'))
btn_save[3].config(command=lambda : click_btn('+'))
btn_save[4].config(command=lambda : click_btn('4'))
btn_save[5].config(command=lambda : click_btn('5'))
btn_save[6].config(command=lambda : click_btn('6'))
btn_save[7].config(command=lambda : click_btn('-'))
btn_save[8].config(command=lambda : click_btn('1'))
btn_save[9].config(command=lambda : click_btn('2'))
btn_save[10].config(command=lambda : click_btn('3'))
btn_save[11].config(command=lambda : click_btn('*'))
btn_save[12].config(command=get_result)
btn_save[13].config(command=delete)
btn_save[14].config(command=lambda : click_btn('0'))
btn_save[15].config(command=lambda : click_btn('/'))



# KEEP WINDOW OPEN
application.mainloop()


















