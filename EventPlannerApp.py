import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from datetime import datetime

class EventPlannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Planner Pro")

        # Add a logo
        original_logo = tk.PhotoImage(file="event_logo.png")  # Replace with the actual path to your logo
        self.features_logo = tk.PhotoImage(file="features_logo.png")
        self.logo = original_logo.subsample(2, 2)  # Adjust the subsample values to resize the logo
        self.canvas = tk.Canvas(root, width=self.logo.width(), height=self.logo.height())
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.logo)

        # Create tabs
        tabs = ttk.Notebook(root)
        event_tab = ttk.Frame(tabs)
        features_tab = ttk.Frame(tabs)

        # Add tabs to the notebook
        tabs.add(event_tab, text='Event')
        tabs.add(features_tab, text='Contact Us')

        # Pack the notebook
        tabs.pack(expand=1, fill='both')

        # Create the event tab
        self.create_event_tab(event_tab)

        # Create the additional features tab
        self.create_additional_features_tab(features_tab)

    def create_event_tab(self, tab):
        # Labels
        tk.Label(tab, text="Event Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(tab, text="Event Date:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(tab, text="Event Time:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(tab, text="Location:").grid(row=3, column=0, padx=10, pady=10)
        
        # Entry Fields
        self.event_name_entry = tk.Entry(tab)
        self.event_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.event_date_entry = tk.Entry(tab, state='disabled')
        self.event_date_entry.grid(row=1, column=1, padx=10, pady=10)

        self.event_time_entry = tk.Entry(tab, state='disabled')
        self.event_time_entry.grid(row=2, column=1, padx=10, pady=10)

        self.event_location_entry = tk.Entry(tab)
        self.event_location_entry.grid(row=3, column=1, padx=10, pady=10)

        # Date Button
        date_button = tk.Button(tab, text="Choose Date", command=self.get_date)
        date_button.grid(row=1, column=2, padx=10, pady=10)

        # Time Button
        time_button = tk.Button(tab, text="Choose Time", command=self.get_time)
        time_button.grid(row=2, column=2, padx=10, pady=10)

        # Save Button
        save_button = tk.Button(tab, text="Save Event", command=self.save_event)
        save_button.grid(row=4, column=0, columnspan=3, pady=10)

        # Exit Button
        exit_button = tk.Button(tab, text="Exit Application", command=self.exit_application)
        exit_button.grid(row=4, column=2, padx=10, pady=10)

    def create_additional_features_tab(self, tab):
        # Placeholder for additional features
        tk.Label(tab, text="Cellphone: 123-456-7890").pack(padx=20, pady=20)
        tk.Label(tab, text="Instagram: @EventPlanner").pack(padx=20, pady=20)
        tk.Label(tab, text="Twitter: @EventPlanner").pack(padx=20, pady=20)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_entry.config(state='normal')
            self.image_entry.delete(0, tk.END)
            self.image_entry.insert(0, file_path)
            self.image_entry.config(state='disabled')

    def save_event(self):
        event_name = self.event_name_entry.get()
        event_date = self.event_date_entry.get()
        event_time = self.event_time_entry.get()

        # Simple input validation
        if not event_name or not event_date or not event_time:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Further processing, e.g., save to a database or perform other actions
        messagebox.showinfo("Success", f"Event '{event_name}' saved successfully.")

        # Show the features logo in a pop-up window
        self.show_features_popup()

    def show_features_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("features_logo.png")
        popup.geometry("500x500")  # Adjust the size as needed

        features_logo_label = tk.Label(popup, image=self.features_logo)
        features_logo_label.pack(padx=10, pady=10)

        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=10)

    def get_date(self):
        # Use simpledialog to get the date from the user
        date_str = simpledialog.askstring("Event Date", "Enter the event date (YYYY-MM-DD):")
        try:
            # Parse the date string into a datetime object
            event_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            # Format the date and insert it into the entry field
            formatted_date = event_date.strftime("%Y-%m-%d")
            self.event_date_entry.config(state='normal')
            self.event_date_entry.delete(0, tk.END)
            self.event_date_entry.insert(0, formatted_date)
            self.event_date_entry.config(state='disabled')
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

    def get_time(self):
        # Create a Toplevel window for time selection
        time_window = tk.Toplevel(self.root)
        time_window.title("Choose Time")

        # Create a Combobox for selecting the time
        time_combobox = ttk.Combobox(time_window, values=[f"{hour:02d}:{minute:02d}" for hour in range(24) for minute in range(0, 60, 15)])
        time_combobox.grid(row=0, column=0, padx=10, pady=10)

        # Button to confirm the selected time
        confirm_button = tk.Button(time_window, text="OK", command=lambda: self.set_selected_time(time_combobox.get()))
        confirm_button.grid(row=1, column=0, padx=10, pady=10)

        cancel_button = tk.Button(time_window, text="Cancel", command=time_window.destroy)
        cancel_button.grid(row=1, column=1, padx=10, pady=10)

    def set_selected_time(self, selected_time):
        self.event_time_entry.config(state='normal')
        self.event_time_entry.delete(0, tk.END)
        self.event_time_entry.insert(0, selected_time)
        self.event_time_entry.config(state='disabled')

    def exit_application(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EventPlannerApp(root)
    root.mainloop()
