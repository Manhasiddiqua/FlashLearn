#imports
import tkinter as tk
import tkinter.font as font
from random import randint

#window
window = tk.Tk()
window.title("FlashLearn")
window.geometry("500x450")
window.configure(background ='#F2E3FA')

#words french-english (50 words)
word = [
    (("Bonjour"), ("Hello")),
    (("Oui"), ("Yes")),
    (("Merci"), ("Thank You")),
    (("Bonsoir"), ("Good Evening")),
    (("Excusez-moi "), ("Excuse Me")),
    (("De Rien"), ("Your Welcome")),
    (("Non"), ("No")),
    (("Au revoir"), ("Goodbye")),
    (("Amour"), ("Love")),
    (("S’il vous plaît:"), ("Please")),
    (("Monde"), ("World")),
    (("Chat"), ("Cat")),
    (("Chien"), ("Dog")),
    (("Maison"), ("House")),
    (("L’ordinateur"), ("Computer")),
    (("L’horloge"), ("Clock")),
    (("Pomme"), ("Apple")),
    (("Le dîner"), ("Dinner")),
    (("Le déjeuner"), ("Lunch")),
    (("Le petit-déjeuner"), ("Breakfast")),
    (("Le goûter"), ("Snack")),
    (("L’école"), ("School")),
    (("ville"), ("City")),
    (("Heureux / heureuse "), ("Happy")),
    (("Beau / belle"), ("Beautiful")),
    (("Train"),("Train")), 
    (("Aide-moi"),("Help me")),
    (("Le magazinage"),("Shopping")),
    (("Telephone"),("Phone")),
    (("L'argent"),("Money")),
    (("Je ne comprends pas"),("I don’t understand")),
    (("Aéroport"), ("Airport")),
    (("Salle de bain"),("Bathroom")),
    (("Taxi"),("Taxi")),
    (("Que recommandez-vous?"),("What do you recommend?")),
    (("Passeport"),("Passport")),
    (("le restaurant"),("Restaurant")),
    ((" le transport"), ("Transportation")),
    (("Attraction"),("Attractions")),
    (("Hôtel"),("Hotel")),
    (("Souvenir"),("Souvenir")),
    (("Quelle heure est-il?"),("What time is it?")),
    (("Quel est le prix?"),("What is the price?")),
    (("Puis-je avoir l'addition?"),("Can I have the bill?")),
    (("Autobus"),("Bus")),
    (("Où"),("Where")),
    (("Lorsque"),("When")),
    (("Temps"),("Weather")),
    (("Terrible!"),("Terrible!")),
    (("Génial!"),("Great!")),
    (("Aller"),("To go")) 
]

count = len(word)

#command next
def next():
    global hinter, hint_count
    answer_label.config(text="")
    my_entry.delete(0, 'end')
    hint_label.config(text="")
    hinter = ""
    hint_count = 0

    global random_word
    random_word = randint(0, count - 1)
    french_word.config(text=word[random_word][0])


#command check
def answer():

     if my_entry.get().capitalize() == word[random_word][1]:
        answer_label.config(text=f"Correct! {word[random_word][0]} means {word[random_word][1]}")
     else:
        answer_label.config(text=f"Incorrect :( {word[random_word][0]} does not mean {my_entry.get().capitalize()}")
       
        

#command hint
hinter = ""
hint_count = 0
def hint():
    global hint_count
    global hinter

    if hint_count < len(word[random_word][1]):
        hinter = hinter + word[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count +=1


#intro message
hello = tk.Label(text="\nWelcome to FlashLearn, Learn words in a Flash", font = font.Font(family='Times New Roman', size=12, weight="normal"), fg ='#592E4F')
hello.configure(background = '#F2E3FA')
hello.pack()
french_word = tk.Label(window, text="", font=font.Font(family='Times New Roman', size=27, weight="normal"), fg = '#4B3636')
french_word.pack(pady=50)
french_word.configure(background = '#F2E3FA')


answer_label = tk.Label(window, text="")
answer_label.configure(background='#F2E3FA')
answer_label.pack(pady=20)

my_entry = tk.Entry(window, font=("Helvetica, 18"))
my_entry.pack(pady=20)

#buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)
button_frame.configure(background = '#F2E3FA')

check_button = tk.Button(button_frame, text="Check", font = font.Font(family='Times New Roman', size=12, weight="normal"), fg ='#4B3636', command=answer)
check_button.grid(row=0, column=0, padx=20)
check_button.configure(background = '#C0DEF6')

next_button = tk.Button(button_frame, text="Next",font = font.Font(family='Times New Roman', size=12, weight="normal"), fg ='#4B3636',command=next)
next_button.grid(row=0, column=1)
next_button.configure(background = '#C0DEF6')

hint_button = tk.Button(button_frame, text="Hint",font = font.Font(family='Times New Roman', size=12, weight="normal"), fg ='#4B3636',command=hint)
hint_button.grid(row=0, column=2, padx=20)
hint_button.configure(background = '#C0DEF6')

#hint label
hint_label = tk.Label(window, text="")
hint_label.pack(pady=20)
hint_label.configure(background='#F2E3FA') 

#run when program starts
next()
tk.mainloop()
