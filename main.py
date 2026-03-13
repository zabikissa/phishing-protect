import tkinter as tk
from tkinter import ttk
from detector import analyze_mail
import datetime
import os

# Création des dossiers si inexistant
os.makedirs("logs", exist_ok=True)
os.makedirs("quarantine", exist_ok=True)

def run_analysis():
    sender = sender_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    score, niveau, raisons = analyze_mail(sender, subject, body)

    result_text.delete("1.0", tk.END)

    icon = ""
    if niveau == "FAIBLE":
        result_text.config(bg="#d4edda")
        icon = "✅"
    elif niveau == "MOYEN":
        result_text.config(bg="#fff3cd")
        icon = "⚠️"
    else:
        result_text.config(bg="#f8d7da")
        icon = "🛑"

    result_text.insert(tk.END, f"{icon} Score : {score}\nNiveau : {niveau}\n\n")
    result_text.insert(tk.END, "Raisons :\n")
    for r in raisons:
        result_text.insert(tk.END, "- " + r + "\n")

    # Barre de score
    progress['value'] = score
    if score >= 50:
        progress.configure(style="Red.Horizontal.TProgressbar")
    elif score >= 30:
        progress.configure(style="Yellow.Horizontal.TProgressbar")
    else:
        progress.configure(style="Green.Horizontal.TProgressbar")

    # Log
    with open("logs/log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} | {sender} | {subject} | {score} | {niveau}\n")

def quarantine_mail():
    sender = sender_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"quarantine/mail_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Sender: {sender}\nSubject: {subject}\n{body}")
    result_text.insert(tk.END, f"\n📦 Mail mis en quarantaine : {filename}\n")

root = tk.Tk()
root.title("Analyseur de phishing")
root.geometry("650x700")
root.configure(bg="#f0f0f0")

title = tk.Label(root, text="Analyseur de mail suspect", font=("Arial",16,"bold"), bg="#f0f0f0")
title.pack(pady=10)

tk.Label(root, text="Expéditeur", bg="#f0f0f0").pack()
sender_entry = tk.Entry(root, width=60)
sender_entry.pack(pady=5)

tk.Label(root, text="Sujet", bg="#f0f0f0").pack()
subject_entry = tk.Entry(root, width=60)
subject_entry.pack(pady=5)

tk.Label(root, text="Contenu du mail", bg="#f0f0f0").pack()
body_text = tk.Text(root, height=10, width=75)
body_text.pack(pady=5)

tk.Button(root, text="Analyser le mail", bg="#0078D7", fg="white", width=25, height=2, command=run_analysis).pack(pady=5)
tk.Button(root, text="Mettre en quarantaine", bg="#6c757d", fg="white", width=25, height=2, command=quarantine_mail).pack(pady=5)

style = ttk.Style()
style.theme_use('default')
style.configure("Green.Horizontal.TProgressbar", troughcolor='#d6d6d6', background='#28a745')
style.configure("Yellow.Horizontal.TProgressbar", troughcolor='#d6d6d6', background='#ffc107')
style.configure("Red.Horizontal.TProgressbar", troughcolor='#d6d6d6', background='#dc3545')
progress = ttk.Progressbar(root, length=400, maximum=100, style="Green.Horizontal.TProgressbar")
progress.pack(pady=10)

tk.Label(root, text="Résultat", bg="#f0f0f0").pack()
result_text = tk.Text(root, height=12, width=75, bg="white")
result_text.pack(pady=5)

root.mainloop()
