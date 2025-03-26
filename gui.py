import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import time
from main import run_algorithm

def start_algorithm():
    result_label.config(text="Obliczanie i tworzenie wykresów...")
    root.update_idletasks()

    params = {
        "population_size": int(population_entry.get()),
        "precision": int(precision_entry.get()),
        "num_epochs": int(epochs_entry.get()),
        "selection_method": selection_var.get(),
        "crossover_method": crossover_var.get(),
        "mutation_method": mutation_var.get(),
        "elitism": int(elitism_entry.get()),
        "mutation_rate": float(mutation_rate_entry.get()),
        "crossover_probability": float(crossover_prob_entry.get()),
        "inversion_probability": float(inversion_prob_entry.get()),
        "begin_range": float(begin_range_entry.get()),
        "end_range": float(end_range_entry.get()),
        "select_best_amount": int(select_best_entry.get()) if selection_var.get() == "select_best" else 0,
        "tournament_size": int(tournament_size_entry.get()) if selection_var.get() == "tournament" else 0,
        "maximize": maximize_var.get()
    }

    start_time = time.time()
    best_fitness = run_algorithm(**params)
    end_time = time.time()

    result_label.config(text=f"Czas: {end_time - start_time:.2f} s\nNajlepszy wynik: {best_fitness}")
    print("Wyniki i wykresy zostały zapisane w folderze 'results'.")

root = tb.Window(themename="superhero")
root.title("Optymalizacja dla funkcji Martin and Gaddy")

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, padx=20, pady=20)

header_label = ttk.Label(frame, text="Optymalizacja dla funkcji Martin and Gaddy", font=("Helvetica", 16, "bold"))
header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

def create_labeled_entry(parent, label_text, default_value, row):
    label = ttk.Label(parent, text=label_text)
    label.grid(row=row, column=0, sticky=W, pady=5, padx=10)
    entry = ttk.Entry(parent)
    entry.grid(row=row, column=1, pady=5, padx=10)
    entry.insert(0, default_value)
    return entry

population_entry = create_labeled_entry(frame, "Rozmiar populacji:", "20", 1)
precision_entry = create_labeled_entry(frame, "Precyzja:", "6", 2)
epochs_entry = create_labeled_entry(frame, "Liczba epok:", "20", 3)
begin_range_entry = create_labeled_entry(frame, "Początek zakresu:", "-20", 4)
end_range_entry = create_labeled_entry(frame, "Koniec zakresu:", "20", 5)
select_best_entry = create_labeled_entry(frame, "Wybór najlepszych:", "0", 7)
tournament_size_entry = create_labeled_entry(frame, "Wielkość turnieju:", "3", 8)

ttk.Label(frame, text="Metoda selekcji:").grid(row=6, column=0, sticky=W, pady=5, padx=10)
selection_var = tk.StringVar(value="tournament")
selection_menu = ttk.Combobox(frame, textvariable=selection_var, values=["select_best", "roulette", "tournament"])
selection_menu.grid(row=6, column=1, pady=5, padx=10)

ttk.Label(frame, text="Metoda krzyżowania:").grid(row=9, column=0, sticky=W, pady=5, padx=10)
crossover_var = tk.StringVar(value="one_point")
crossover_menu = ttk.Combobox(frame, textvariable=crossover_var, values=["one_point", "two_point", "uniform", "granular"])
crossover_menu.grid(row=9, column=1, pady=5, padx=10)

crossover_prob_entry = create_labeled_entry(frame, "Prawdopodobieństwo krzyżowania:", "0.8", 10)

ttk.Label(frame, text="Metoda mutacji:").grid(row=11, column=0, sticky=W, pady=5, padx=10)
mutation_var = tk.StringVar(value="one_point")
mutation_menu = ttk.Combobox(frame, textvariable=mutation_var, values=["boundary", "one_point", "two_point"])
mutation_menu.grid(row=11, column=1, pady=5, padx=10)

mutation_rate_entry = create_labeled_entry(frame, "Prawdopodobieństwo mutacji mutacji:", "0.5", 12)

elitism_entry = create_labeled_entry(frame, "Elitaryzm:", "1", 13)

inversion_prob_entry = create_labeled_entry(frame, "Prawdopodobieństwo inwersji:", "0.1", 14)

def update_entry_visibility(*args):
    tournament_size_entry.config(state="normal" if selection_var.get() == "tournament" else "disabled")
    select_best_entry.config(state="normal" if selection_var.get() == "select_best" else "disabled")

selection_var.trace_add("write", update_entry_visibility)
update_entry_visibility()

maximize_var = tk.BooleanVar()
maximize_checkbox = ttk.Checkbutton(frame, text="Maksymalizacja", variable=maximize_var)
maximize_checkbox.grid(row=15, column=0, columnspan=2, pady=5, padx=10)

style = tb.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10, relief="raised", borderwidth=2)
start_button = ttk.Button(frame, text="Uruchom", bootstyle=SUCCESS, command=start_algorithm, width=20)
start_button.grid(row=16, column=0, columnspan=2, pady=20)

result_label = ttk.Label(frame, text="", font=("Helvetica", 12), bootstyle="info")
result_label.grid(row=17, column=0, columnspan=2, pady=10)

root.mainloop()