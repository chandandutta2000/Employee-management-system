import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

app = customtkinter.CTk()
app.title('Employee Management System')
app.geometry('900x420')
app.config(bg='#161C25')
app.resizable(False,False)

font1 = ('Arial',20,'bold')
font2 = ('Arial',12,'bold')
def add_to_treeview():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)
def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        Id_entry.insert(0,row[0])
        Name_entry.insert(0,row[1])
        Role_entry.insert(0,row[2])
        variable1.set(row[3])
    else:
        pass

def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose any option to delete.')
    else:
        Id=Id_entry.get()
        database.delete_employees(Id)
        clear()
        messagebox.showinfo('Success','Data has been deleted.')

def update():
    selected_item=tree.focus()
    if not selected_item:
        messagebox.showerror('Error','Choose an Employee to update.')
    else:
        Id=Id_entry.get()
        Name=Name_entry.get()
        Role=Role_entry.get()
        Gender=variable1.get()
        Status=Status_entry.get()
        database.update_employees(Name,Role,Gender,Status,Id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success','Data has been updated.')



def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
    Id_entry.delete(0,END)
    Name_entry.delete(0,END)
    Role_entry.delete(0,END)
    variable1.set('Male')
    Status_entry.delete(0,END)


def insert():
    Id=Id_entry.get()
    Name= Name_entry.get()
    Role=Role_entry.get()
    Gender=variable1.get()
    Status=Status_entry.get()
    if not (Id and Name and Role and Gender and Status):
            messagebox.showerror('Error','Enter all fields')
    elif database.id_exists(Id):
            messagebox.showerror('Error','Id already exists.')
    else:
        database.insert_employees(Id,Name,Role,Gender,Status)
        add_to_treeview()
        messagebox.showinfo('Success','Data has been inserted')

Id_label1 = customtkinter.CTkLabel(app,font=font1,text='ID:',text_color='#fff',bg_color='#161C25')
Id_label1.place(x=20,y=20)
Id_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=180)
Id_entry.place(x=100,y=20)


Name_label1 = customtkinter.CTkLabel(app,font=font1,text='Name:',text_color='#fff',bg_color='#161C25')
Name_label1.place(x=20,y=80)
Name_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=180)
Name_entry.place(x=100,y=80)


Role_label1 = customtkinter.CTkLabel(app,font=font1,text='Role',text_color='#fff',bg_color='#161C25')
Role_label1.place(x=20,y=140)
Role_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=180)
Role_entry.place(x=100,y=140)


Gender_label1 = customtkinter.CTkLabel(app,font=font1,text='Gender',text_color='#fff',bg_color='#161C25')
Gender_label1.place(x=20,y=200)


options = ['Male','Female']
variable1 = StringVar()

Gender_option = customtkinter.CTkComboBox(app,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#0C9295',button_color='#0C9295',button_hover_color='#0C9295',border_color='#0C9295',width=180,variable=variable1,values=options,state='readonly')
Gender_option.set('Male')
Gender_option.place(x=100,y=200)


Status_label1 = customtkinter.CTkLabel(app,font=font1,text='Status',text_color='#fff',bg_color='#161C25')
Status_label1.place(x=20,y=260)
Status_entry = customtkinter.CTkEntry(app,font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=180)
Status_entry.place(x=100,y=260)

add_button = customtkinter.CTkButton(app,command=insert,font=font1,text_color='#fff',text='Add Employee',fg_color='#05A312',hover_color='#00850B',bg_color='#161C25',cursor='hand2',corner_radius=15,width=260)
add_button.place(x=20,y=310)

clear_button = customtkinter.CTkButton(app,command=lambda:clear(True),font=font1,text_color='#fff',text='New Employee',fg_color='#05A312',hover_color='#00850B',bg_color='#161C25',cursor='hand2',corner_radius=15,width=260)
clear_button.place(x=20,y=360)

update_button = customtkinter.CTkButton(app,command=update,font=font1,text_color='#fff',text='Update Employee',fg_color='#05A312',hover_color='#00850B',bg_color='#161C25',cursor='hand2',corner_radius=15,width=260)
update_button.place(x=300,y=360)

delete_button = customtkinter.CTkButton(app,command=delete,font=font1,text_color='#fff',text='Delete Employee',fg_color='#E40404',hover_color='#00850B',bg_color='#161C25',cursor='hand2',corner_radius=15,width=260)
delete_button.place(x=580,y=360)

style = ttk.Style(app)

style.theme_use('clam')
style.configure('TreeView',font=font2,foreground='#fff', background='#000',fieldbackground='#313837')
style.map('Treeview',background=[('selected','#1A8F2D')])
tree = ttk.Treeview(app,height=15)
tree['columns']=('Id','Name','Role','Gender','Status')
tree.column('#0',width=0,stretch=tk.NO)
tree.column('Id',anchor=tk.CENTER,width=120)
tree.column('Name',anchor=tk.CENTER,width=120)
tree.column('Role',anchor=tk.CENTER,width=120)
tree.column('Gender',anchor=tk.CENTER,width=100)
tree.column('Status',anchor=tk.CENTER,width=120)

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Status',text='Status')
tree.place(x=300,y=20)

tree.bind('<ButtonRelease>',display_data)

add_to_treeview()

app.mainloop()