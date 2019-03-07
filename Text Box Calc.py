# Nicholaus Whites
# Text Box Calulator
# plz don't steal thx

from tkinter import *

class Application(Frame):
    """ GUI Calculator Application. """
    def __init__(self, master):
        """Initialize the Frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.num = 0  # num of clicks
        self.num2 = 0
        self.operation = "add"
        self.create_widget()
    def create_widget(self):
        """ Create labels, buttons, and text boxes"""
        # create label
        self.inst_lbl = Label(self, text="Enter one number in both boxes")
        self.inst_lbl.grid(row=0, column=0, columnspan=4, sticky=N)
        # create label for password

        self.n1_lbl = Label(self, text="Num1:")
        self.n1_lbl.grid(row=1, column=0, sticky=W)
        self.n1_ent = Entry(self)
        self.n1_ent.grid(row=1, column=1, columnspan=1, sticky=W)

        self.n1_lbl = Label(self, text="Num2:")
        self.n1_lbl.grid(row=1, column=2)
        self.n2_ent = Entry(self)
        self.n2_ent.grid(row=1, column=3, columnspan=1)

        self.bttn = Button(self)
        self.bttn["text"] = "Add"
        self.bttn["command"] = self.add_num
        self.bttn.grid()

        self.bttn2 = Button(self)
        self.bttn2["text"] = "Subtract"
        self.bttn2["command"] = self.sub_num
        self.bttn2.grid()

        self.bttn3 = Button(self)
        self.bttn3["text"] = "Multiply"
        self.bttn3["command"] = self.mult_num
        self.bttn3.grid()

        self.bttn4 = Button(self)
        self.bttn4["text"] = "Divide"
        self.bttn4["command"] = self.div_num
        self.bttn4.grid()

        self.submit_bttn = Button(self, text="Submit", command=self.reveal)
        self.submit_bttn.grid(row=5, column=2, sticky=W)

        # Create text widget to display message
        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=7, column=0, columnspan=3, sticky=W)

    def add_num(self):
        self.operation = "add"

    def sub_num(self):
        self.operation = "sub"

    def mult_num(self):
        self.operation = "mult"

    def div_num(self):
        self.operation = "div"

    def reveal(self):
        contents = self.n1_ent.get()
        contents2 = self.n2_ent.get()
        if contents.isdigit() == True and contents2.isdigit() == True:
            if self.operation == "add":
                message = int(contents) + int(contents2)
            elif self.operation == "sub":
                message = int(contents) - int(contents2)
            elif self.operation == "mult":
                message = int(contents) * int(contents2)
            elif self.operation == "div":
                if contents2 == "0":
                    message = "Error: Can't divide by zero"
                else:
                    message = int(contents) / int(contents2)
            else:
                message = "something went wrong"
        else:
            message = "Only Integers"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


root = Tk()
#modify the window
root.title("Text Box Calculator")
root.geometry("430x240")
#root.iconbitmap("asdf.ico")

app = Application(root)

root.mainloop()

