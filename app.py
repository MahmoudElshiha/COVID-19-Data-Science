import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the dataset
def load_data():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        status_label.config(text=f"Loaded: {file_path.split('/')[-1]}")

def plot_age_distribution():
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df['AGE'], bins=30, kde=True, color='blue', ax=ax)
    ax.set_title('Age Distribution of COVID-19 Patients')
    show_plot(fig)

def plot_icu_admission():
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x='ICU', data=df, palette='coolwarm', ax=ax)
    ax.set_title('ICU Admissions')
    ax.set_xticklabels(['No ICU', 'ICU'])
    show_plot(fig)

def plot_comorbidities_vs_mortality():
    comorbidities = ['DIABETES', 'COPD', 'ASTHMA', 'HIPERTENSION', 'OBESITY', 'RENAL_CHRONIC']
    df_melted = df.melt(id_vars=['DATE_DIED'], value_vars=comorbidities, var_name='Condition', value_name='Has_Condition')
    
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(x='Condition', y='Has_Condition', hue='DATE_DIED', data=df_melted, palette='coolwarm', ax=ax)
    ax.set_title('Effect of Comorbidities on Mortality')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    show_plot(fig)

def plot_correlation_heatmap():
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    ax.set_title('Feature Correlation Matrix')
    show_plot(fig)

def show_plot(fig):
    for widget in frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Tkinter App Setup
root = tk.Tk()
root.title("COVID-19 Data Analysis")
root.geometry("800x600")

tk.Button(root, text="Load Dataset", command=load_data, bg='lightblue').pack(pady=5)
status_label = tk.Label(root, text="No file loaded", fg='red')
status_label.pack()

tk.Button(root, text="Age Distribution", command=plot_age_distribution).pack(pady=5)
tk.Button(root, text="ICU Admissions", command=plot_icu_admission).pack(pady=5)
tk.Button(root, text="Comorbidities & Mortality", command=plot_comorbidities_vs_mortality).pack(pady=5)
tk.Button(root, text="Correlation Heatmap", command=plot_correlation_heatmap).pack(pady=5)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
