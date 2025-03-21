import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from ttkthemes import ThemedTk
import tkinter.font as tkFont

# Create the Tkinter app
class VisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Visualizer")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")  # Light gray background
        self.root.resizable(True, True)  # Allow resizing
        self.root.minsize(800, 600)  # Set minimum window size

        # List of available charts
        self.chart_files = [
            f for f in os.listdir('charts')
            if os.path.isfile(os.path.join('charts', f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))
        ]
        self.selected_chart = tk.StringVar()
        self.selected_chart.set(self.chart_files[0] if self.chart_files else "No charts found")  # Default value

        # Build the UI
        self.create_widgets()

        # Automatically display the first chart (if available)
        if self.chart_files:
            self.show_chart()

    def create_widgets(self):
        # Custom font for the title
        title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")

        # Add a title label
        title_label = tk.Label(self.root, text="COVID-19 Visualizer", font=title_font, bg="#f0f0f0")
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Label for the dropdown
        dropdown_label = tk.Label(self.root, text="Select a Chart:", font=("Helvetica", 12), bg="#f0f0f0")
        dropdown_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        # Modern combobox
        self.chart_menu = ttk.Combobox(self.root, textvariable=self.selected_chart, values=self.chart_files, font=("Helvetica", 12))
        self.chart_menu.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)
        self.chart_menu.bind("<<ComboboxSelected>>", lambda event: self.show_chart())  # Update chart on dropdown change

        # Frame to display the chart
        self.chart_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.chart_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#f0f0f0")
        status_bar.grid(row=3, column=0, columnspan=2, sticky=tk.EW)

    def show_chart(self):
        # Clear the previous chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        # Load and display the selected chart
        chart_file = self.selected_chart.get()
        image_path = os.path.join('charts', chart_file)
        if os.path.exists(image_path):
            image = Image.open(image_path)
            # Use Image.Resampling.LANCZOS or Image.LANCZOS instead of Image.ANTIALIAS
            image = image.resize((700, 500), Image.Resampling.LANCZOS)  # Resize for display
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self.chart_frame, image=photo, bg="#f0f0f0")
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack(fill=tk.BOTH, expand=True)
            self.status_var.set(f"Loaded: {chart_file}")
        else:
            error_label = tk.Label(self.chart_frame, text="Chart not found!", fg="red", bg="#f0f0f0")
            error_label.pack()
            self.status_var.set("Error: Chart not found")

# Run the app
if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # Use a modern theme
    app = VisualizerApp(root)
    root.mainloop()