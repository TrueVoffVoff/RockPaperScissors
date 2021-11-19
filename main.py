from tkinter import  *
import random

root = Tk()
root.iconbitmap(r"Pictures/rockico.ico")
root.title("Rock Paper Scissors")
root.resizable(width=False, height=False)

click = True

# ==================== Pictures ==============================
rock_hand = PhotoImage(file=r"Pictures/rockhand.png")
paper_hand = PhotoImage(file=r"Pictures/paperhand.png")
scissor_hand = PhotoImage(file=r"Pictures/scissorshand.png")
rock = PhotoImage(file=r"Pictures/rock.png")
paper = PhotoImage(file=r"Pictures/paper.png")
scissor = PhotoImage(file=r"Pictures/scissor.png")
you_win = PhotoImage(file=r"Pictures/win.png")
you_lose = PhotoImage(file=r"Pictures/lose.png")
tie = PhotoImage(file=r"Pictures/tie.png")
# =============================================================

rock_hand_button_1 = ""
paper_hand_button_2 = ""
scissor_hand_button_3 = ""

def Play():
    global rock_hand_button_1, paper_hand_button_2, scissor_hand_button_3

    rock_hand_button_1 = Button(root, image=rock_hand, command=lambda: YouPick("rock"))
    paper_hand_button_2 = Button(root, image=paper_hand, command=lambda: YouPick("paper"))
    scissor_hand_button_3 = Button(root, image=scissor_hand, command=lambda: YouPick("scissor"))

    rock_hand_button_1.grid(row=0, column=0)
    paper_hand_button_2.grid(row=0, column=1)
    scissor_hand_button_3.grid(row=0, column=2)


def ComputerPick():
    choise = random.choice(["rock", "paper", "scissors"])
    return choise

def YouPick(your_choice):
    global click

    comp_pick = ComputerPick()

    if click == True:
        if your_choice == "rock":
            rock_hand_button_1.configure(image=rock_hand)
            if comp_pick == "rock":
                paper_hand_button_2.configure(image=rock)
                scissor_hand_button_3.configure(image=tie)
            elif comp_pick == "paper":
                paper_hand_button_2.configure(image=paper)
                scissor_hand_button_3.configure(image=you_lose)
            else:
                paper_hand_button_2.configure(image=scissor)
                scissor_hand_button_3.configure(image=you_win)
            click = False
        elif your_choice == "paper":
            rock_hand_button_1.configure(image=paper_hand)
            if comp_pick == "paper":
                paper_hand_button_2.configure(image=paper)
                scissor_hand_button_3.configure(image=tie)
            elif comp_pick == "scissors":
                paper_hand_button_2.configure(image=scissor)
                scissor_hand_button_3.configure(image=you_lose)
            else:
                paper_hand_button_2.configure(image=rock)
                scissor_hand_button_3.configure(image=you_win)
            click = False
        else:
            rock_hand_button_1.configure(image=scissor_hand)
            if comp_pick == "scissors":
                paper_hand_button_2.configure(image=scissor)
                scissor_hand_button_3.configure(image=tie)
            elif comp_pick == "rock":
                paper_hand_button_2.configure(image=rock)
                scissor_hand_button_3.configure(image=you_lose)
            else:
                paper_hand_button_2.configure(image=paper)
                scissor_hand_button_3.configure(image=you_win)
            click = False

    else:  # Reset to start new game
        if your_choice == "rock" or your_choice == "paper" or your_choice == "scissors":
            rock_hand_button_1.configure(image=rock_hand)
            paper_hand_button_2.configure(image=paper_hand)
            scissor_hand_button_3.configure(image=scissor_hand)
            click = True

Play()

root.mainloop()
