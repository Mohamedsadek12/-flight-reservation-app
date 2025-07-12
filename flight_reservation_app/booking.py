import tkinter as tk
from tkinter import ttk, messagebox
import database

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Book a Flight", font=("Arial", 18))
        label.pack(pady=20)

        form_frame = ttk.Frame(self)
        form_frame.pack(pady=10)

        labels = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
        self.entries = {}
        for i, text in enumerate(labels):
            ttk.Label(form_frame, text=text+":").grid(row=i, column=0, sticky="e", pady=5, padx=5)
            entry = ttk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[text] = entry

        submit_btn = ttk.Button(self, text="Submit", width=15, command=self.submit)
        submit_btn.pack(pady=15)
        back_btn = ttk.Button(self, text="Back", width=10, command=lambda: controller.show_frame("HomePage"))
        back_btn.pack()

    def submit(self):
        values = [e.get().strip() for e in self.entries.values()]
        if not all(values):
            messagebox.showerror("Error", "All fields are required.")
            return
        database.add_reservation(*values)
        messagebox.showinfo("Success", "Reservation booked!")
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.controller.show_frame("ReservationsPage") 