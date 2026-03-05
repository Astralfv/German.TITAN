import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import os

# =========================
# VERBI
# =========================

verbi = {
"andare": ("gehen","ging","ist gegangen"),
"essere": ("sein","war","ist gewesen"),
"avere": ("haben","hatte","hat gehabt"),
"diventare": ("werden","wurde","ist geworden"),
"venire": ("kommen","kam","ist gekommen"),
"vedere": ("sehen","sah","hat gesehen"),
"dare": ("geben","gab","hat gegeben"),
"prendere": ("nehmen","nahm","hat genommen"),
"mangiare": ("essen","aß","hat gegessen"),
"bere": ("trinken","trank","hat getrunken"),
"parlare": ("sprechen","sprach","hat gesprochen"),
"leggere": ("lesen","las","hat gelesen"),
"scrivere": ("schreiben","schrieb","hat geschrieben"),
"dormire": ("schlafen","schlief","hat geschlafen"),
"correre": ("laufen","lief","ist gelaufen"),
"trovare": ("finden","fand","hat gefunden"),
"rimanere": ("bleiben","blieb","ist geblieben"),
"chiamare": ("rufen","rief","hat gerufen"),
"aiutare": ("helfen","half","hat geholfen"),
"pensare": ("denken","dachte","hat gedacht"),
"sapere": ("wissen","wusste","hat gewusst"),
"conoscere": ("kennen","kannte","hat gekannt"),
"portare": ("tragen","trug","hat getragen"),
"cadere": ("fallen","fiel","ist gefallen"),
"iniziare": ("beginnen","begann","hat begonnen"),
"vincere": ("gewinnen","gewann","hat gewonnen"),
"perdere": ("verlieren","verlor","hat verloren"),
"decidere": ("entscheiden","entschied","hat entschieden"),
"guidare": ("fahren","fuhr","ist gefahren"),
"incontrare": ("treffen","traf","hat getroffen"),
"stare": ("stehen","stand","hat gestanden"),
"sedersi": ("sitzen","saß","hat gesessen"),
"mentire": ("lügen","log","hat gelogen"),
"cantare": ("singen","sang","hat gesungen"),
"nuotare": ("schwimmen","schwamm","ist geschwommen"),
"tagliare": ("schneiden","schnitt","hat geschnitten"),
"offrire": ("bieten","bot","hat geboten"),
"chiudere": ("schließen","schloss","hat geschlossen"),
"aprire": ("öffnen","öffnete","hat geöffnet"),
"comprare": ("kaufen","kaufte","hat gekauft"),
"bruciare": ("brennen","brannte","hat gebrannt"),
"portare2": ("bringen","brachte","hat gebracht"),
"tenere": ("halten","hielt","hat gehalten"),
"lasciare": ("lassen","ließ","hat gelassen"),
"chiamarsi": ("heißen","hieß","hat geheißen"),
"salire": ("steigen","stieg","ist gestiegen"),
"affondare": ("sinken","sank","ist gesunken"),
"tirare": ("ziehen","zog","hat gezogen"),
"crescere": ("wachsen","wuchs","ist gewachsen")
}

lista = list(verbi.keys())
random.shuffle(lista)

indice = 0
punti = 0
tempo = 15
giocatore = ""

# =========================
# SALVA PUNTEGGIO
# =========================

def salva_score():
    with open("scores.txt","a") as f:
        f.write(f"{giocatore}:{punti}\n")

# =========================
# CLASSIFICA
# =========================

def mostra_classifica():

    if not os.path.exists("scores.txt"):
        messagebox.showinfo("Classifica","Nessun punteggio salvato.")
        return

    with open("scores.txt") as f:
        scores = f.readlines()

    scores = [s.strip().split(":") for s in scores]
    scores.sort(key=lambda x:int(x[1]),reverse=True)

    testo = ""

    for s in scores[:10]:
        testo += f"{s[0]} - {s[1]}\n"

    messagebox.showinfo("🏆 CLASSIFICA",testo)

# =========================
# TIMER
# =========================

def countdown():

    global tempo

    if tempo > 0:
        timer_label.config(text=f"Tempo: {tempo}")
        tempo -= 1
        root.after(1000,countdown)
    else:
        controlla()

# =========================
# DOMANDA
# =========================

def nuova_domanda():

    global tempo

    if indice >= len(lista):
        fine_quiz()
        return

    verbo = lista[indice]
    verbo_label.config(text=verbo)

    entry_inf.delete(0,tk.END)
    entry_pra.delete(0,tk.END)
    entry_per.delete(0,tk.END)

    tempo = 15
    countdown()

# =========================
# CONTROLLO
# =========================

def controlla():

    global indice,punti

    verbo = lista[indice]
    inf,pra,per = verbi[verbo]

    if entry_inf.get()==inf and entry_pra.get()==pra and entry_per.get()==per:
        punti+=1

    indice+=1
    progress["value"]=(indice/len(lista))*100

    nuova_domanda()

# =========================
# FINE
# =========================

def fine_quiz():

    salva_score()

    percent = (punti/len(lista))*100

    if percent==100:
        rank="🏆 LEGGENDARIO"
    elif percent>=80:
        rank="🥇 ESPERTO"
    elif percent>=60:
        rank="🥈 BUONO"
    else:
        rank="📚 STUDIA DI PIÙ"

    messagebox.showinfo(
        "RISULTATO",
        f"{giocatore}\n\nPunteggio {punti}/{len(lista)}\n{rank}"
    )

    root.destroy()

# =========================
# START
# =========================

def start():

    global giocatore

    giocatore = nome_entry.get()

    if giocatore=="":
        messagebox.showwarning("Errore","Inserisci nome")
        return

    menu_frame.pack_forget()
    quiz_frame.pack()

    nuova_domanda()

# =========================
# FINESTRA
# =========================

root=tk.Tk()
root.title("Quiz Verbi Tedeschi - TITAN EDITION")
root.geometry("600x650")
root.config(bg="#101820")

# =========================
# MENU
# =========================

menu_frame=tk.Frame(root,bg="#101820")
menu_frame.pack()

try:
    logo=tk.PhotoImage(file="logo.png")
    tk.Label(menu_frame,image=logo,bg="#101820").pack(pady=20)
except:
    pass

tk.Label(menu_frame,text="Quiz Verbi Tedeschi",
font=("Helvetica",24,"bold"),
fg="cyan",bg="#101820").pack(pady=10)

nome_entry=tk.Entry(menu_frame,font=("Helvetica",14))
nome_entry.pack(pady=10)

tk.Button(menu_frame,text="START",
font=("Helvetica",14),
command=start).pack(pady=5)

tk.Button(menu_frame,text="CLASSIFICA",
command=mostra_classifica).pack(pady=5)

tk.Button(menu_frame,text="ESCI",
command=root.quit).pack(pady=5)

# =========================
# QUIZ FRAME
# =========================

quiz_frame=tk.Frame(root,bg="#101820")

verbo_label=tk.Label(
quiz_frame,
font=("Helvetica",26),
fg="white",
bg="#101820"
)

verbo_label.pack(pady=20)

entry_inf=tk.Entry(quiz_frame,font=("Helvetica",14))
entry_inf.pack(pady=5)

entry_pra=tk.Entry(quiz_frame,font=("Helvetica",14))
entry_pra.pack(pady=5)

entry_per=tk.Entry(quiz_frame,font=("Helvetica",14))
entry_per.pack(pady=5)

tk.Button(
quiz_frame,
text="Controlla",
font=("Helvetica",14),
command=controlla
).pack(pady=20)

timer_label=tk.Label(
quiz_frame,
text="Tempo",
font=("Helvetica",14),
bg="#101820",
fg="white"
)

timer_label.pack()

progress=ttk.Progressbar(
quiz_frame,
length=400
)

progress.pack(pady=20)

root.mainloop()
