from tkinter import *
from tkinter import messagebox

class SumAverageCount:
    def __init__(self):
        #-----------------------------------------Window-------------------------------
        self.window = Tk()
        self.window.title("tk")
        self.window.geometry("300x120") #LXW
        #------------------------------------Frame------------------------------
        self.top_frame = Frame(self.window)
        self.middle_frame = Frame(self.window)
        self.bottom_frame = Frame(self.window)
        self.footer_frame = Frame(self.window)
        self.footer_max = Frame(self.window)
        #--------------------------Widgets---------------------------------

        self.label1 = Label(self.top_frame, text="Enter the score for test 1:", foreground="blue", font=("arial", 10))
        self.n1 = Entry(self.top_frame)
        self.label2 = Label(self.middle_frame, text="Enter the score for test 2:", foreground="blue", font=("arial", 10))
        self.n2 = Entry(self.middle_frame)
        self.label3 = Label(self.bottom_frame, text="Enter the score for test 3:", foreground="blue", font=("arial", 10))
        self.n3 = Entry(self.bottom_frame)
        self.average = Button(self.footer_max, text="Average", command=self.calculate)
        self.quit = Button(self.footer_max, text="Quit", command=self.exit_program)
        self.result = StringVar(value="")
        self.result_label = Label(self.footer_frame, textvariable=self.result)
        #=======================pack--------------------------------
        # for num in range (1,4)
        self.label1.pack(side="left")
        self.label2.pack(side="left")
        self.label3.pack(side="left")
        self.n1.pack()
        self.n2.pack()
        self.n3.pack()
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.footer_frame.pack()
        self.footer_max.pack()
        self.average.pack(side="left")
        self.quit.pack(side="right")
        self.result_label.pack(side="right")
        self.window.mainloop()

    def calculate(self):
        try:
            n1 = float(self.n1.get())
            n2 = float(self.n2.get())
            n3 = float(self.n3.get())
            result = (n1+n2+n3)/3
            self.result.set( f'Average: {result}')
        except Exception as e:
            messagebox.showerror("ERROR!", 'input must be numeric!')
            self.n1.delete(0,END)

    def exit_program(self):
        if messagebox.askyesno("Confirmation","Are you sure to exit?"):
            self.window.destroy()

if __name__ == "__main__":
    some = SumAverageCount()