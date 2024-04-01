from tkinter import PhotoImage, Frame, Button, Tk, Menu, Canvas, StringVar, Label
from tkinter import TOP, W, NW, NORMAL, DISABLED
from tkinter import messagebox, simpledialog
from random import randrange

global image
HiddenWord = ""


# συνάρτηση αλλαγής της λέξης που βλέπει ο χρήστης (με τις παύλες)
def changelabel(word):
    DisplayWord.set(word)


# συνάρτηση όπου γίνεται όλος ο έλεγχος όταν παίζει ο παίκτης
def checkWord(letter):
    global HiddenWord
    global DisplayWord
    global img_index
    letterFound = False
    DWord = DisplayWord.get()
    HWord = HiddenWord[0]
    DisableLettersBtn(letter)

    for i in range(1, len(HiddenWord) - 1):
        if HiddenWord[i] == letter:
            HWord += HiddenWord[i]
            letterFound = True
        else:
            HWord += DWord[i]
    HWord += HiddenWord[len(HiddenWord) - 1]
    changelabel(HWord)
    if (
        HWord == HiddenWord
    ):  # ο παίκτης βλήκες όλα τα γράμματα της λέξης άρα και τη λέξη
        messagebox.showinfo("Παιχνίδι Κρεμάλα", "Μπράβο βρήκες τη λέξη!")
        DisableLettersBtn("All")
    if not letterFound:  # το γράμμα που επίλεξε ο παίκτης δεν υπάρχει στη λέξη
        img_index += 1
        showImg()
    if img_index == 7:  # Ο παίκτης έκανε ανεπιτυχή προσπάθεια και δυστυχώς κρεμάστηκε
        DisableLettersBtn("All")
        messagebox.showinfo(
            "Παιχνίδι Κρεμάλα",
            "Δυστυχώς δε μπόρεσες να βρεις τη λέξη!\nΗ λέξη είναι: " + HiddenWord,
        )


# Συνάρτηση η οποία εκτελείται όταν χρήστης κάνει κλικ στο κουμπί "Βρήκα τη λέξη"
def KnowWord():
    global DisplayWord
    global HiddenWord
    answer = simpledialog.askstring(
        "Βρήκα τη λέξη",
        "Πιστεύεις ότι βρήκες τη λέξη!\nΓράψε τη λέξη με κεφαλαία ελληνικά χωρίς τονισμό.",
        parent=root,
    )
    if answer == HiddenWord:
        messagebox.showinfo("Παιχνίδι Κρεμάλα", "Μπράβο βρήκες τη λέξη!")
        DisableLettersBtn("All")
        DisplayWord.set(HiddenWord)
    elif not (answer == None) and not (answer == ""):
        messagebox.showinfo(
            "Παιχνίδι Κρεμάλα",
            "Λυπάμαι! Δεν είναι αυτή η λέξη. Συνέχισε τη προσπάθεια.",
        )
    else:
        return


# Συνάρτηση η οποία εκτελείται όταν χρήστης κάνει κλικ στο κουμπί "Παραιτούμαι! Εμφάνισε τη λέξη."
def GiveUp():
    global img_index
    MsgBox = messagebox.askquestion(
        "Επιβεβαίωση παραίτησης", "Ζήτησες παραίτηση. Να συνεχίσω;", icon="warning"
    )
    if MsgBox == "yes":
        img_index = 7
        showImg()
        DisableLettersBtn("All")
        messagebox.showinfo(
            "Παιχνίδι Κρεμάλα",
            "Δυστυχώς δήλωσες παραίτηση!\nΗ λέξη είναι: " + HiddenWord,
        )


# Συνάρτηση που επιστρέφει μία λέξη η οποία επιλέγεται στην τύχη από τη λίστα λέξεων
def readWord(WordsList):
    return WordsList[randrange(len(WordsList))]


# Συνάρτηση που διαβαζει το αρχείο λέξεων
def readfile():
    WordsList = []
    dataFile = open("wordlist.txt", "r", encoding="utf8")
    for line in dataFile:
        word = line
        WordsList.append(word[0 : len(word) - 1])
    dataFile.close()
    return WordsList


# Συνάρτηση που εμφανίζει τις εικόνες
def showImg():
    global img_index
    if img_index == 0:
        image = PhotoImage(file="HangmanImages//hang.gif")
    elif img_index == 1:
        image = PhotoImage(file="HangmanImages//hangman1.gif")
    elif img_index == 2:
        image = PhotoImage(file="HangmanImages//hangman2.gif")
    elif img_index == 3:
        image = PhotoImage(file="HangmanImages//hangman3.gif")
    elif img_index == 4:
        image = PhotoImage(file="HangmanImages//hangman4.gif")
    elif img_index == 5:
        image = PhotoImage(file="HangmanImages//hangman5.gif")
    elif img_index == 6:
        image = PhotoImage(file="HangmanImages//hangman6.gif")
    else:
        image = PhotoImage(file="HangmanImages//hangman7.gif")

    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.image = image


# Συνάρτηση ενεργοποίησης των κουμπιών
def EnableLettersBtn():
    BtnA.configure(state=NORMAL)
    BtnB.configure(state=NORMAL)
    BtnGama.configure(state=NORMAL)
    BtnDelta.configure(state=NORMAL)
    BtnE.configure(state=NORMAL)
    BtnZ.configure(state=NORMAL)
    BtnH.configure(state=NORMAL)
    BtnThita.configure(state=NORMAL)
    BtnI.configure(state=NORMAL)
    BtnK.configure(state=NORMAL)
    BtnL.configure(state=NORMAL)
    BtnM.configure(state=NORMAL)
    BtnN.configure(state=NORMAL)
    BtnXi.configure(state=NORMAL)
    BtnO.configure(state=NORMAL)
    BtnPi.configure(state=NORMAL)
    BtnP.configure(state=NORMAL)
    BtnS.configure(state=NORMAL)
    BtnT.configure(state=NORMAL)
    BtnY.configure(state=NORMAL)
    BtnF.configure(state=NORMAL)
    BtnX.configure(state=NORMAL)
    BtnPsi.configure(state=NORMAL)
    BtnOmega.configure(state=NORMAL)
    BtnKnowWord.configure(state=NORMAL)
    BtnGiveUp.configure(state=NORMAL)


# Διαδικασία απενεργοποίησης των κουμπιών
def DisableLettersBtn(letter):
    if letter == "Α":
        BtnA.configure(state=DISABLED)
    elif letter == "Β":
        BtnB.configure(state=DISABLED)
    elif letter == "Γ":
        BtnGama.configure(state=DISABLED)
    elif letter == "Δ":
        BtnDelta.configure(state=DISABLED)
    elif letter == "Ε":
        BtnE.configure(state=DISABLED)
    elif letter == "Ζ":
        BtnZ.configure(state=DISABLED)
    elif letter == "Η":
        BtnH.configure(state=DISABLED)
    elif letter == "Θ":
        BtnThita.configure(state=DISABLED)
    elif letter == "Ι":
        BtnI.configure(state=DISABLED)
    elif letter == "Κ":
        BtnK.configure(state=DISABLED)
    elif letter == "Λ":
        BtnL.configure(state=DISABLED)
    elif letter == "Μ":
        BtnM.configure(state=DISABLED)
    elif letter == "Ν":
        BtnN.configure(state=DISABLED)
    elif letter == "Ξ":
        BtnXi.configure(state=DISABLED)
    elif letter == "Ο":
        BtnO.configure(state=DISABLED)
    elif letter == "Π":
        BtnPi.configure(state=DISABLED)
    elif letter == "Ρ":
        BtnP.configure(state=DISABLED)
    elif letter == "Σ":
        BtnS.configure(state=DISABLED)
    elif letter == "Τ":
        BtnT.configure(state=DISABLED)
    elif letter == "Υ":
        BtnY.configure(state=DISABLED)
    elif letter == "Φ":
        BtnF.configure(state=DISABLED)
    elif letter == "Χ":
        BtnX.configure(state=DISABLED)
    elif letter == "Ψ":
        BtnPsi.configure(state=DISABLED)
    elif letter == "Ω":
        BtnOmega.configure(state=DISABLED)
    else:  # Απενεργοποίηση όλων των κουμπιών
        BtnA.configure(state=DISABLED)
        BtnB.configure(state=DISABLED)
        BtnGama.configure(state=DISABLED)
        BtnDelta.configure(state=DISABLED)
        BtnE.configure(state=DISABLED)
        BtnZ.configure(state=DISABLED)
        BtnH.configure(state=DISABLED)
        BtnThita.configure(state=DISABLED)
        BtnI.configure(state=DISABLED)
        BtnK.configure(state=DISABLED)
        BtnL.configure(state=DISABLED)
        BtnM.configure(state=DISABLED)
        BtnN.configure(state=DISABLED)
        BtnXi.configure(state=DISABLED)
        BtnO.configure(state=DISABLED)
        BtnPi.configure(state=DISABLED)
        BtnP.configure(state=DISABLED)
        BtnS.configure(state=DISABLED)
        BtnT.configure(state=DISABLED)
        BtnY.configure(state=DISABLED)
        BtnF.configure(state=DISABLED)
        BtnX.configure(state=DISABLED)
        BtnPsi.configure(state=DISABLED)
        BtnOmega.configure(state=DISABLED)
        BtnKnowWord.configure(state=DISABLED)
        BtnGiveUp.configure(state=DISABLED)


# Συνάρτηση Εμφάνισης των Button με τα 24 γράμματα του Ελληνικού Αλφάβητου
def showLettersBtn():
    global HiddenWord
    global DisplayWord
    global img_index
    # Δημιουργία ενός πλαισίου μέσα στο οποίο τα τοποθετηθούν τα 24 Buttons
    frameBtn = Frame(root)
    frameBtn.pack()
    frameBtn.pack(side=TOP)
    # Δημιουργία και εμφάνιση των 24 Buttons μέσα στο πλαίσιο
    global BtnA
    BtnA = Button(
        frameBtn, text="Α", state=DISABLED, width=3, command=lambda: checkWord("Α")
    )
    BtnA.grid(row=0, column=0, sticky=W)
    global BtnB
    BtnB = Button(
        frameBtn, text="B", state=DISABLED, width=3, command=lambda: checkWord("Β")
    )
    BtnB.grid(row=0, column=1, sticky=W)
    global BtnGama
    BtnGama = Button(
        frameBtn, text="Γ", state=DISABLED, width=3, command=lambda: checkWord("Γ")
    )
    BtnGama.grid(row=0, column=2, sticky=W)
    global BtnDelta
    BtnDelta = Button(
        frameBtn, text="Δ", state=DISABLED, width=3, command=lambda: checkWord("Δ")
    )
    BtnDelta.grid(row=0, column=3, sticky=W)
    global BtnE
    BtnE = Button(
        frameBtn, text="Ε", state=DISABLED, width=3, command=lambda: checkWord("Ε")
    )
    BtnE.grid(row=0, column=4, sticky=W)
    global BtnZ
    BtnZ = Button(
        frameBtn, text="Z", state=DISABLED, width=3, command=lambda: checkWord("Ζ")
    )
    BtnZ.grid(row=0, column=5, sticky=W)
    global BtnH
    BtnH = Button(
        frameBtn, text="H", state=DISABLED, width=3, command=lambda: checkWord("Η")
    )
    BtnH.grid(row=0, column=6, sticky=W)
    global BtnThita
    BtnThita = Button(
        frameBtn, text="Θ", state=DISABLED, width=3, command=lambda: checkWord("Θ")
    )
    BtnThita.grid(row=0, column=7, sticky=W)
    global BtnI
    BtnI = Button(
        frameBtn, text="I", state=DISABLED, width=3, command=lambda: checkWord("Ι")
    )
    BtnI.grid(row=0, column=8, sticky=W)
    global BtnK
    BtnK = Button(
        frameBtn, text="K", state=DISABLED, width=3, command=lambda: checkWord("Κ")
    )
    BtnK.grid(row=0, column=9, sticky=W)
    global BtnL
    BtnL = Button(
        frameBtn, text="Λ", state=DISABLED, width=3, command=lambda: checkWord("Λ")
    )
    BtnL.grid(row=0, column=10, sticky=W)
    global BtnM
    BtnM = Button(
        frameBtn, text="M", state=DISABLED, width=3, command=lambda: checkWord("Μ")
    )
    BtnM.grid(row=0, column=11, sticky=W)
    global BtnN
    BtnN = Button(
        frameBtn, text="N", state=DISABLED, width=3, command=lambda: checkWord("Ν")
    )
    BtnN.grid(row=1, column=0, sticky=W)
    global BtnXi
    BtnXi = Button(
        frameBtn, text="Ξ", state=DISABLED, width=3, command=lambda: checkWord("Ξ")
    )
    BtnXi.grid(row=1, column=1, sticky=W)
    global BtnO
    BtnO = Button(
        frameBtn, text="O", state=DISABLED, width=3, command=lambda: checkWord("Ο")
    )
    BtnO.grid(row=1, column=2, sticky=W)
    global BtnPi
    BtnPi = Button(
        frameBtn, text="Π", state=DISABLED, width=3, command=lambda: checkWord("Π")
    )
    BtnPi.grid(row=1, column=3, sticky=W)
    global BtnP
    BtnP = Button(
        frameBtn, text="Ρ", state=DISABLED, width=3, command=lambda: checkWord("Ρ")
    )
    BtnP.grid(row=1, column=4, sticky=W)
    global BtnS
    BtnS = Button(
        frameBtn, text="Σ", state=DISABLED, width=3, command=lambda: checkWord("Σ")
    )
    BtnS.grid(row=1, column=5, sticky=W)
    global BtnT
    BtnT = Button(
        frameBtn, text="T", state=DISABLED, width=3, command=lambda: checkWord("Τ")
    )
    BtnT.grid(row=1, column=6, sticky=W)
    global BtnY
    BtnY = Button(
        frameBtn, text="Y", state=DISABLED, width=3, command=lambda: checkWord("Υ")
    )
    BtnY.grid(row=1, column=7, sticky=W)
    global BtnF
    BtnF = Button(
        frameBtn, text="Φ", state=DISABLED, width=3, command=lambda: checkWord("Φ")
    )
    BtnF.grid(row=1, column=8, sticky=W)
    global BtnX
    BtnX = Button(
        frameBtn, text="X", state=DISABLED, width=3, command=lambda: checkWord("Χ")
    )
    BtnX.grid(row=1, column=9, sticky=W)
    global BtnPsi
    BtnPsi = Button(
        frameBtn, text="Ψ", state=DISABLED, width=3, command=lambda: checkWord("Ψ")
    )
    BtnPsi.grid(row=1, column=10, sticky=W)
    global BtnOmega
    BtnOmega = Button(
        frameBtn, text="Ω", state=DISABLED, width=3, command=lambda: checkWord("Ω")
    )
    BtnOmega.grid(row=1, column=11, sticky=W)

    # κώδικας δημιουργίας ενός πλαισίου που περιέχει τα δύο κουμπιά "Βρήκα τη λέξη" και "Παραιτούμαι! Εμφάνισε τη λέξη"
    frameBtn1 = Frame(root)
    frameBtn1.pack()
    frameBtn1.pack(side=TOP)
    global BtnKnowWord
    BtnKnowWord = Button(
        frameBtn1, text="Βρήκα τη λέξη.", state=DISABLED, command=lambda: KnowWord()
    )
    BtnKnowWord.grid(row=2, column=0, sticky=W)
    global BtnGiveUp
    BtnGiveUp = Button(
        frameBtn1,
        text="Παραιτούμαι!\nΕμφάνισε τη λέξη.",
        state=DISABLED,
        command=lambda: GiveUp(),
    )
    BtnGiveUp.grid(row=2, column=1, sticky=W)


# Συνάρτηση Νέο Παιχνίδι
def StartNewGame():
    global HiddenWord
    global DisplayWord
    global img_index
    img_index = 0
    showImg()
    WordsList = readfile()  # κλήση συνάρτησης που διαβάζει το αρχείο των λέξεων
    HiddenWord = readWord(
        WordsList
    )  # κλήση συνάρτησης που διαβάζει - επιλέγει μία λέξη από τη λίστα των λέξεων
    hword = (
        HiddenWord[0] + "-" * (len(HiddenWord) - 2) + HiddenWord[len(HiddenWord) - 1]
    )
    changelabel(hword)  # κλήση συνάρτησης αλλαγής της εμφανιζόμενης λέξης με τις παύλες
    EnableLettersBtn()  # κλήση συνάρτησης ενεργοποίησης κουμπιών με τα γράμματα


# Κύριο Πρόγραμμα
root = Tk()
root.title("Παιχνίδι Κρεμάλα")
root.geometry("450x350+0+0")

# Δημιουργία drop Down Menu
menu = Menu(root)
root.config(menu=menu)
# Δημιουργία μενού "Παιχνίδι" με τα υπομενού του
subMenu_Game = Menu(menu, tearoff=0)
menu.add_cascade(label="Παιχνίδι", menu=subMenu_Game)
subMenu_Game.add_command(label="Νέο", command=StartNewGame)
subMenu_Game.add_separator()
subMenu_Game.add_command(label="Έξοδος", command=root.destroy)

# Δημιουργία μενού "Ρυθμίσεις" με τα υπομενού του
subMenu_Set = Menu(menu, tearoff=0)
menu.add_cascade(label="Ρυθμίσεις", menu=subMenu_Set)
subMenu_Set.add_command(label="Αρχείο Λέξεων")
subMenu_Set.add_command(label="Επίπεδο Δυσκολίας")

canvas = Canvas(root, width=200, height=200)
canvas.pack()
img_index = 0
showImg()
DisplayWord = StringVar()
WordLabel = Label(
    root,
    textvariable=DisplayWord,
    font=("Ariar", 18),
    height=1,
    bg="white",
    width=30,
    relief="ridge",
).pack()
showLettersBtn()  # κληση συνάρτησης που εμφανίζει τα κουμπιά με τα γράμματα

root.mainloop()
