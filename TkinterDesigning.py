from tkinter import *





root = Tk()
root.title("tkinter App")
root.geometry("500x500")

root.title("All about Labels, Text, Button")
Label(root,text="Tkinter",font=("times new roman",20),fg="blue",bg="black",height=2).grid(row=0,rowspan=2,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)
Label(root,text="Capturing Samples and Maintaining Database",font=("times new roman",20),fg="black",bg="red",height=2).grid(row=3,rowspan=2,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Create and Reset Database",font=("times new roman",20),fg="red",bg="black",height=2).grid(row=5,column=0,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Create and Reset Database",font=("times new roman",20),fg="red",bg="black",height=2).grid(row=5,column=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Create and Reset Database",font=("times new roman",20),fg="red",bg="black",height=2).grid(row=7,column=0,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Create and Reset Database",font=("times new roman",20),fg="red",bg="black",height=2).grid(row=7,column=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Label(root,text="Capturing Samples and Maintaining Database",font=("times new roman",20),fg="black",bg="red",height=2).grid(row=8,column=0,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Create and Reset Database",font=("times new roman",20),fg="red",bg="black",height=2).grid(row=9,column=0,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Create and Reset Database",font=("times new roman",20),fg="red",bg="black",height=2).grid(row=9,column=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Create and Reset Database",font=("times new roman",20),fg="red",bg="black",height=2).grid(row=10,column=0,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Create and Reset Database",font=("times new roman",20),fg="red",bg="black",height=2).grid(row=10,column=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(root,text="Exit",font=("times new roman",20),fg="red",bg="black",height=2).grid(row=11,column=0,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)






root.mainloop()

