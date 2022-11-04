import tkinter as tk
from tkinter import font  as tkfont
import time


current_balance = 1000



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        self.shared_data = {"Balance": tk.IntVar()}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#808080")
        self.controller = controller
        self.controller.title("ATM Service")
        self.controller.state("zoomed")
        self.controller.iconphoto(False, tk.PhotoImage(file="images/atm.png"))

        heading_label = tk.Label(self,
                                 text="ATM Service",
                                 font=("Arial", 45, "bold"),
                                 foreground="white",
                                 background="#333333")
        heading_label.pack(pady=100, fill="x")

        space_label = tk.Label(self, height=10, bg="#808080")
        space_label.pack()

        password_label = tk.Label(self,
                                  text="Enter your password:",
                                  bg="#808080",
                                  font=("Arial", 25, "bold"),
                                  fg = "white")
        password_label.pack(pady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self,
                                      textvariable = my_password,
                                      font=("Arial", 23, "bold"),
                                      width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(pady=20)

        def handle_focus_in(_):
            password_entry_box.configure(fg="white", show ="*")

        password_entry_box.bind("<FocusIn>", handle_focus_in)


        def check_password():
            if my_password.get() == "0123":
                my_password.set("")
                incorrect_password_label["text"]=""
                controller.show_frame("MenuPage")
            else:
                incorrect_password_label["text"] = "Incorrect Password"
        enter_button = tk.Button(self,
                                 text="Enter",
                                 command=check_password,
                                 relief="raised",
                                 borderwidth= 3,
                                 width = 40,
                                 height= 4)

        enter_button.pack(pady=8)

        incorrect_password_label = tk.Label(self,
                                            text="",
                                            font=("Arial", 20, "bold"),
                                            fg="red",
                                            bg="#333333",
                                            anchor="n")
        incorrect_password_label.pack(fill="both", expand=True)

        bottom_frame = tk.Frame(self,
                                relief="ridge",
                                borderwidth=3)
        bottom_frame.pack(fill="x", side="bottom")

        visa_photo = tk.PhotoImage(file="images/visa.png")
        visa_label = tk.Label(bottom_frame, image = visa_photo)
        visa_label.pack(side="left")
        visa_label.image = visa_photo

        master_card_photo = tk.PhotoImage(file="images/master_card.png")
        master_card_label = tk.Label(bottom_frame, image=master_card_photo)
        master_card_label.pack(side="left")
        master_card_label.image = master_card_photo

        american_express_photo = tk.PhotoImage(file="images/american_express.png")
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side="left")
        american_express_label.image = american_express_photo


        def tick_tock():
            current_time = time.strftime("%I:%M %p")
            time_label.config(text=current_time)
            time_label.after(200, tick_tock)

        time_label = tk.Label(bottom_frame, font=("Arial", 35, "bold"))
        time_label.pack(side="right")
        tick_tock()

class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background="#808080")
        self.controller = controller

        heading_label = tk.Label(self,
                                 text="ATM Service",
                                 font=("Arial", 45, "bold"),
                                 foreground="white",
                                 background="#333333")
        heading_label.pack(pady=100, fill="x")

        main_menu_label = tk.Label(self,
                                   text="Main Menu",
                                   font=("Arial", 45, "bold"),
                                   foreground="white",
                                   background="#333333"
                                   )
        main_menu_label.pack(pady=45)


        selection_label = tk.Label(self,
                                   text = "Select one of the following:",
                                   font=("Arial", 20, "bold"),
                                   fg="white",
                                   background="#808080",
                                   anchor="w"
                                   )

        selection_label.pack(fill="x", pady=15)



        button_frame = tk.Frame(self,
                                bg="#333333")
        button_frame.pack(fill="both", expand=True)



        def withdraw():
            controller.show_frame("WithdrawPage")
        withdraw_button = tk.Button(button_frame,
                                  text="Withdraw",
                                  command=withdraw,
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        withdraw_button.grid(row=0, column=0, pady=10)

        def deposit():
            controller.show_frame("DepositPage")
        deposit_button = tk.Button(button_frame,
                                  text="Deposit",
                                  command=deposit,
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        deposit_button.grid(row=1, column=0, pady=5)

        def balance():
            controller.show_frame("BalancePage")
        balance_button = tk.Button(button_frame,
                                  text="Balance",
                                  command=balance,
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        balance_button.grid(row=2, column=0, pady=5)

        def start_page():
            controller.show_frame("StartPage")
        exit_button = tk.Button(button_frame,
                                  text="Exit",
                                  command=start_page,
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        exit_button.grid(row=3, column=0, pady=5)








        bottom_frame = tk.Frame(self,
                                relief="ridge",
                                borderwidth=3)
        bottom_frame.pack(fill="x", side="bottom")

        visa_photo = tk.PhotoImage(file="images/visa.png")
        visa_label = tk.Label(bottom_frame, image = visa_photo)
        visa_label.pack(side="left")
        visa_label.image = visa_photo

        master_card_photo = tk.PhotoImage(file="images/master_card.png")
        master_card_label = tk.Label(bottom_frame, image=master_card_photo)
        master_card_label.pack(side="left")
        master_card_label.image = master_card_photo

        american_express_photo = tk.PhotoImage(file="images/american_express.png")
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side="left")
        american_express_label.image = american_express_photo


        def tick_tock():
            current_time = time.strftime("%I:%M %p")
            time_label.config(text=current_time)
            time_label.after(200, tick_tock)

        time_label = tk.Label(bottom_frame, font=("Arial", 35, "bold"))
        time_label.pack(side="right")
        tick_tock()


class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#808080")
        self.controller = controller

        heading_label = tk.Label(self,
                                 text="ATM Service",
                                 font=("Arial", 45, "bold"),
                                 foreground="white",
                                 background="#333333")
        heading_label.pack(pady=100, fill="x")

        choose_amount_label = tk.Label(self,
                                   text="Choose the amount:",
                                   font=("Arial", 30, "bold"),
                                   foreground="white",
                                   background="#333333"
                                   )
        choose_amount_label.pack(pady=45)

        button_frame = tk.Frame(self,
                                bg="#333333")
        button_frame.pack(fill="both", expand=True)


        def withdraw(amount):
            global current_balance
            current_balance -= amount
            controller.shared_data["Balance"].set(current_balance)
            controller.show_frame("MenuPage")




        twenty_button = tk.Button(button_frame,
                                  text="20",
                                  command=lambda: withdraw(20),
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        twenty_button.grid(row=0, column=1, pady=15, padx=50)

        forty_button = tk.Button(button_frame,
                                  text="40",
                                  command=lambda: withdraw(40),
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        forty_button.grid(row=1, column=1, pady=15, padx=15)

        sixty_button = tk.Button(button_frame,
                                  text="60",
                                  command=lambda: withdraw(60),
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        sixty_button.grid(row=2, column=1, pady=15, padx=15)

        eighty_button = tk.Button(button_frame,
                                  text="80",
                                  command=lambda: withdraw(80),
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        eighty_button.grid(row=3, column=1, pady=20)

        one_hundred_button = tk.Button(button_frame,
                                  text="100",
                                  command=lambda: withdraw(100),
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        one_hundred_button.grid(row=0, column=2, pady=20, padx=550)

        two_hundred_button = tk.Button(button_frame,
                                  text="200",
                                  command=lambda: withdraw(200),
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        two_hundred_button.grid(row=1, column=2, pady=15, padx=15)

        three_hundred_button = tk.Button(button_frame,
                                  text="300",
                                  command=lambda: withdraw(300),
                                  relief="raised",
                                  borderwidth=3,
                                  width=50,
                                  height=5)
        three_hundred_button.grid(row=2, column=2, pady=15, padx=15)

        cash=tk.StringVar()

        other_amount_entry=tk.Entry(button_frame,
                                    textvariable=cash,
                                    width=53,
                                    justify="right")
        other_amount_entry.grid(row=3, column=2, pady=15, padx=15, ipady=30)


        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data["Balance"].set(current_balance)
            cash.set("")
            controller.show_frame("MenuPage")
        other_amount_entry.bind("<Return>", other_amount)





        bottom_frame = tk.Frame(self,
                                relief="ridge",
                                borderwidth=3)
        bottom_frame.pack(fill="x", side="bottom")

        visa_photo = tk.PhotoImage(file="images/visa.png")
        visa_label = tk.Label(bottom_frame, image = visa_photo)
        visa_label.pack(side="left")
        visa_label.image = visa_photo

        master_card_photo = tk.PhotoImage(file="images/master_card.png")
        master_card_label = tk.Label(bottom_frame, image=master_card_photo)
        master_card_label.pack(side="left")
        master_card_label.image = master_card_photo

        american_express_photo = tk.PhotoImage(file="images/american_express.png")
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side="left")
        american_express_label.image = american_express_photo


        def tick_tock():
            current_time = time.strftime("%I:%M %p")
            time_label.config(text=current_time)
            time_label.after(200, tick_tock)

        time_label = tk.Label(bottom_frame, font=("Arial", 35, "bold"))
        time_label.pack(side="right")
        tick_tock()






class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#808080")
        self.controller = controller

        heading_label = tk.Label(self,
                                 text="ATM Service",
                                 font=("Arial", 45, "bold"),
                                 foreground="white",
                                 background="#333333")
        heading_label.pack(pady=100, fill="x")

        space_label = tk.Label(self, height=10, bg="#808080")
        space_label.pack()

        enter_amount_label = tk.Label(self,
                                  text="Enter amount:",
                                  bg="#808080",
                                  font=("Arial", 25, "bold"),
                                  fg="white")
        enter_amount_label.pack(pady=10)


        cash=tk.StringVar()
        deposit_entry = tk.Entry(self,
                                 textvariable=cash,
                                 bg="#333333",
                                 font=("Arial", 20, "bold"),
                                 fg="white",
                                 width=22
                                 )
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            current_balance += int(cash.get())
            controller.shared_data["Balance"].set(current_balance)
            controller.show_frame("MenuPage")
            cash.set("")

        enter_button = tk.Button(self,
                                 text="Enter",
                                 command=deposit_cash,
                                 relief="raised",
                                 borderwidth=3,
                                 width=40,
                                 height=3)
        enter_button.pack(pady=10)

        two_tone_label = tk.Label(self,
                                  bg="#333333")
        two_tone_label.pack(fill="both", expand=True)










        bottom_frame = tk.Frame(self,
                                relief="ridge",
                                borderwidth=3)
        bottom_frame.pack(fill="x", side="bottom")

        visa_photo = tk.PhotoImage(file="images/visa.png")
        visa_label = tk.Label(bottom_frame, image = visa_photo)
        visa_label.pack(side="left")
        visa_label.image = visa_photo

        master_card_photo = tk.PhotoImage(file="images/master_card.png")
        master_card_label = tk.Label(bottom_frame, image=master_card_photo)
        master_card_label.pack(side="left")
        master_card_label.image = master_card_photo

        american_express_photo = tk.PhotoImage(file="images/american_express.png")
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side="left")
        american_express_label.image = american_express_photo


        def tick_tock():
            current_time = time.strftime("%I:%M %p")
            time_label.config(text=current_time)
            time_label.after(200, tick_tock)

        time_label = tk.Label(bottom_frame, font=("Arial", 35, "bold"))
        time_label.pack(side="right")
        tick_tock()

class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="#808080")
        self.controller = controller

        heading_label = tk.Label(self,
                                 text="ATM Service",
                                 font=("Arial", 45, "bold"),
                                 foreground="white",
                                 background="#333333")
        heading_label.pack(pady=100, fill="x")


        controller.shared_data["Balance"].set(current_balance)
        balance_label = tk.Label(self,
                                 textvariable=controller.shared_data["Balance"],
                                 font=("Arial", 30, "bold"),
                                 fg= "white",
                                 background="#4d4d4d",
                                 anchor="w")
        balance_label.pack(fill="x")


        button_frame = tk.Frame(self,
                                bg="#333333")
        button_frame.pack(fill="both", expand=True)


        def menu():
            controller.show_frame("MenuPage")
        menu_button = tk.Button(button_frame,
                                command=menu,
                                text="Menu",
                                relief="raised",
                                borderwidth=3,
                                width=50,
                                height=5)
        menu_button.grid(row=0, column=0, pady=5)

        def exit():
            controller.show_frame("StartPage")
        menu_button = tk.Button(button_frame,
                                command=exit,
                                text="Exit",
                                relief="raised",
                                borderwidth=3,
                                width=50,
                                height=5)
        menu_button.grid(row=1, column=0, pady=5)




        bottom_frame = tk.Frame(self,
                                relief="ridge",
                                borderwidth=3)
        bottom_frame.pack(fill="x", side="bottom")

        visa_photo = tk.PhotoImage(file="images/visa.png")
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side="left")
        visa_label.image = visa_photo

        master_card_photo = tk.PhotoImage(file="images/master_card.png")
        master_card_label = tk.Label(bottom_frame, image=master_card_photo)
        master_card_label.pack(side="left")
        master_card_label.image = master_card_photo

        american_express_photo = tk.PhotoImage(file="images/american_express.png")
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side="left")
        american_express_label.image = american_express_photo

        def tick_tock():
            current_time = time.strftime("%I:%M %p")
            time_label.config(text=current_time)
            time_label.after(200, tick_tock)

        time_label = tk.Label(bottom_frame, font=("Arial", 35, "bold"))
        time_label.pack(side="right")
        tick_tock()




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()