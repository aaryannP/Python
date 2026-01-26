from tkinter import *
import random

screen = Tk()
screen.geometry("1000x600")
screen.config(background="lightgreen")


# simple printin logic of numbers
    # Row 1 starts at 3, increases by 3
    # Row 2 starts at 2, increases by 3
    # Row 3 starts at 1, increases by 3

    # for row in range(3):
    #     num = 3 - row
    #     for column in range(12):
    #         print(num,end=" ")
    #         num+=3
    #     print()

# --------------------------------------
                                # padx=10 → horizontal gap
                                # pady=10 → vertical gap

main_dict = {}
RED_NUMBERS = {i for i in range(1,37) if i%2!=0}
BLACK_NUMBERS = {i for i in range(1,37) if i%2==0}

spin_value = 0
INITIAL_BALANCE = 2000
Balance = INITIAL_BALANCE

is_play_again = False

spin_result_lb = None
earn_lb = None
loss_lb = None
bet_display_lb = None
insufficient_lb = None


# ----------------------------- display user bets --------------------------
def bat_display():
    global bet_display_lb
    print(main_dict)  # ----------------- just display the dictionary
    if bet_display_lb:
        bet_display_lb.destroy()

    data = ""
    for k, v in main_dict.items():
        data += f"{k} : {v[0]} Rs.\n"

    bet_display_lb = Label(
        screen,
        text=data,
        background="lightgreen",
        font=('arial',15,'bold'),
        justify='left'
    )
    bet_display_lb.place(x=5, y=395)

# ----------------------------- number bet ---------------------------------
def click(n, color):
    global Balance, insufficient_lb

    if Balance <= 0:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Game Over! Balance is 0!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if Balance < 100:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Insufficient Balance!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if insufficient_lb:
        insufficient_lb.destroy()

    if n in main_dict:
        main_dict[n][0] += 100
    else:
        main_dict[n] = [100, color]

    bat_display()
    set_bat()


# ----------------------------- 12 group bets ------------------------------
def first():
    global Balance, insufficient_lb

    if Balance <= 0:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Game Over! Balance is 0!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if "1st 12" not in main_dict:
        main_dict["1st 12"] = [100, [i for i in range(1,13)]]
    else:
        main_dict["1st 12"][0] += 100
    bat_display()
    set_bat()

def second():
    global Balance, insufficient_lb

    if Balance <= 0:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Game Over! Balance is 0!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if "2nd 12" not in main_dict:
        main_dict["2nd 12"] = [100, [i for i in range(13,25)]]
    else:
        main_dict["2nd 12"][0] += 100
    bat_display()
    set_bat()

def third():
    global Balance, insufficient_lb

    if Balance <= 0:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Game Over! Balance is 0!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if "3rd 12" not in main_dict:
        main_dict["3rd 12"] = [100, [i for i in range(25,37)]]
    else:
        main_dict["3rd 12"][0] += 100
    bat_display()
    set_bat()

def odd():
    global Balance, insufficient_lb

    if Balance <= 0:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Game Over! Balance is 0!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if "odd" not in main_dict:
        main_dict["odd"] = [100,[i for i in range(1,37) if i%2!=0]]
    else:
        main_dict["odd"][0] += 100
    bat_display()
    set_bat()

def even():
    global Balance, insufficient_lb

    if Balance <= 0:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Game Over! Balance is 0!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if "even" not in main_dict:
        main_dict["even"] = [100,[i for i in range(1,37) if i%2==0]]
    else:
        main_dict["even"][0] += 100
    bat_display()
    set_bat()

def red():
    global Balance, insufficient_lb

    if Balance <= 0:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Game Over! Balance is 0!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if "red" not in main_dict:
        main_dict["red"] = [100, list(RED_NUMBERS)]
    else:
        main_dict["red"][0] += 100

    bat_display()
    set_bat()

def black():
    global Balance, insufficient_lb

    if Balance <= 0:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Game Over! Balance is 0!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if "black" not in main_dict:
        main_dict["black"] = [100, list(BLACK_NUMBERS)]
    else:
        main_dict["black"][0] += 100

    bat_display()
    set_bat()

def one_to_eighteen():
    global Balance, insufficient_lb

    if Balance <= 0:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Game Over! Balance is 0!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if "1-18" not in main_dict:
        main_dict["1-18"] = [100, [i for i in range(1,19)]]
    else:
        main_dict["1-18"][0] += 100

    bat_display()
    set_bat()


def nineteen_to_thirtysix():
    global Balance, insufficient_lb

    if Balance <= 0:
        if insufficient_lb:
            insufficient_lb.destroy()

        insufficient_lb = Label(
            screen,
            text="Game Over! Balance is 0!",
            background="white",
            foreground="red",
            font=('arial',16,'bold')
        )
        insufficient_lb.place(x=340, y=350)
        return

    if "19-36" not in main_dict:
        main_dict["19-36"] = [100, [i for i in range(19,37)]]
    else:
        main_dict["19-36"][0] += 100

    bat_display()
    set_bat()

# ----------------------------- set balance --------------------------------
def set_bat():
    global Balance

    total_bet = 0
    for v in main_dict.values():
        total_bet += v[0]

    if total_bet <= INITIAL_BALANCE:
        Balance = INITIAL_BALANCE - total_bet
    else:
        Balance = 0

    your_balanc_lb.config(text=f"Your Balance = {Balance}")

# ----------------------------- play again ---------------------------------
def play_again():
    global is_play_again, main_dict

    main_dict.clear()

    if spin_result_lb: 
        spin_result_lb.destroy()
    if earn_lb:
        earn_lb.destroy()
    if loss_lb: 
        loss_lb.destroy()
    if bet_display_lb: 
        bet_display_lb.destroy()

    spin_btn.config(
        text="SPIN",
        background="green",
        command=win_bat
    )

    is_play_again = False

# ----------------------------- win logic ----------------------------------
def win_bat():
    global Balance, INITIAL_BALANCE
    global spin_result_lb, earn_lb, loss_lb, is_play_again, insufficient_lb

    if is_play_again:
        play_again()
        return

    if not main_dict:
        return

    # Clear the insufficient balance message
    if insufficient_lb:
        insufficient_lb.destroy()
        insufficient_lb = None

    earn = 0
    loss = 0

    # generate random spin
    spin_value = random.randint(1, 36)

    # show spin result
    if spin_result_lb:
        spin_result_lb.destroy()

    spin_result_lb = Label(
        screen,
        text=f"Spin Result = {spin_value}",
        background="white",
        font=('arial',18,'bold')
    )
    spin_result_lb.place(x=625, y=417)

    # -------------------- WIN LOGIC --------------------
    for k, v in main_dict.items():

        bet_amount = v[0]

        # -------- NUMBER BET (×36) --------
        if type(k) == int:
            if k == spin_value:
                earn += bet_amount * 36
                Balance += bet_amount * 36

        # -------- 1st / 2nd / 3rd 12 (×2) --------
        elif k == "1st 12" or k == "2nd 12" or k == "3rd 12" or k == "1-18" or k == "19-36":
            if spin_value in v[1]:
                earn += bet_amount * 2
                Balance += bet_amount * 2

        # -------- ODD (×2) --------
        elif k == "odd":
            if spin_value != 0 and spin_value % 2 != 0:
                earn += bet_amount * 2
                Balance += bet_amount * 2

        # -------- EVEN (×2) --------
        elif k == "even":
            if spin_value != 0 and spin_value % 2 == 0:
                earn += bet_amount * 2
                Balance += bet_amount * 2

        # -------- RED (×2) --------
        elif k == "red":
            if spin_value in RED_NUMBERS:
                earn += bet_amount * 2
                Balance += bet_amount * 2

        # -------- BLACK (×2) --------
        elif k == "black":
            if spin_value in BLACK_NUMBERS:
                earn += bet_amount * 2
                Balance += bet_amount * 2

    # -------------------- LOSS LOGIC --------------------
    for k, v in main_dict.items():

        bet_amount = v[0]

        if type(k) == int:
            if k != spin_value:
                loss += bet_amount
        else:
            if spin_value not in v[1]:
                loss += bet_amount

    # -------------------- DISPLAY --------------------
    if earn_lb:
        earn_lb.destroy()

    earn_lb = Label(
        screen,
        text=f"You Earned = {earn}",
        background="white",
        foreground="darkgreen",
        font=('arial',18,'bold')
    )
    earn_lb.place(x=340, y=478)

    if loss_lb:
        loss_lb.destroy()

    loss_lb = Label(
        screen,
        text=f"You Loss = {loss}",
        background="white",
        foreground="red",
        font=('arial',18,'bold')
    )
    loss_lb.place(x=360, y=520)

    your_balanc_lb.config(text=f"Your Balance = {Balance}")
    INITIAL_BALANCE = Balance

    # change button to PLAY AGAIN
    spin_btn.config(
        text="PLAY AGAIN",
        background="red",
        command=play_again
    )

    is_play_again = True

# ----------------------------- UI -----------------------------------------
# ---------------- 1 to 36 buttons ---------------------------------
for rows in range(3):
    num = 3 - rows
    for cols in range(12):
        bg = "black" if num % 2 == 0 else "red"
        Button(screen, text=num, width=4,background=bg, foreground="white",font=('arial',19,'bold'),command=lambda n=num, c=bg: click(n, c)).grid(row=rows, column=cols, padx=3, pady=3)
        num += 3

# -------------- group buttons ------------------------
# --------------------- 1-12 ---------------
Button(screen, text="1st 12", width=19, background="green",font=('arial',19,'bold'), command=first).place(x=4, y=180)
# --------------------- 13-25 ------------------
Button(screen, text="2nd 12", width=19, background="green",font=('arial',19,'bold'), command=second).place(x=308, y=180)
# -------------------- 26-36 ------------------------------------
Button(screen, text="3rd 12", width=19, background="green",font=('arial',19,'bold'), command=third).place(x=612, y=180)

# odd and even button
odd_btn = Button(screen,text="odd",height=1,width=9,background="green",foreground="white",font=('arial',19,'bold'),command=odd)
odd_btn.place(x=4,y=240)
even_btn = Button(screen,text="even",height=1,width=9,background="green",foreground="white",font=('arial',19,'bold'),command=even)
even_btn.place(x=153,y=240)

# red and balck button
red_btn = Button(screen,text="red",height=1,width=9,background="red",foreground="red",font=('arial',19,'bold'),command=red)
red_btn.place(x=308,y=240)
black_btn = Button(screen,text="black",height=1,width=9,background="black",foreground="black",font=('arial',19,'bold'),command=black)
black_btn.place(x=457,y=240)

# 1-18 and 19-36 butoon
eighting_btn = Button(screen,text="1-18",height=1,width=9,background="green",foreground="white",font=('arial',19,'bold'),command=one_to_eighteen)
eighting_btn.place(x=612,y=240)
three_six_btn = Button(screen,text="19-36",height=1,width=9,background="green",foreground="white",font=('arial',19,'bold'),command=nineteen_to_thirtysix)
three_six_btn.place(x=760,y=240)

# ----------- show user balance ------------
your_balanc_lb = Label(screen, text=f"Your Balance = {Balance}",width=60, background="white",font=('arial',18,'bold'))
your_balanc_lb.place(x=5, y=310)

# ------------ show the user bat -----------------------
Label(screen, text="-:   Your Bets   :-",background="lightgreen",font=('arial',15,'bold')).place(x=5, y=350)

# ------------------ spin button --------------------------
spin_btn = Button(screen, text="SPIN",height=2, width=19,background="green",foreground="white",font=('arial',19,'bold'),command=win_bat)
spin_btn.place(x=308, y=390)

screen.mainloop()


