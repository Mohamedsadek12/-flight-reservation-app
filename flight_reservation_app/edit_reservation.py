import tkinter as tk
from tkinter import ttk, messagebox
import database

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Edit Reservation", font=("Arial", 18))
        label.pack(pady=20)

        self.form_frame = ttk.Frame(self)
        self.form_frame.pack(pady=10)
        labels = ["Name", "Flight Number", "Departure", "Destination", "Date (YYYY-MM-DD)", "Seat Number"]
        self.entries = {}
        for i, text in enumerate(labels):
            ttk.Label(self.form_frame, text=text+":").grid(row=i, column=0, sticky="e", pady=5, padx=5)
            entry = ttk.Entry(self.form_frame, width=30)
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[text] = entry

        update_btn = ttk.Button(self, text="Update", width=15, command=self.update_reservation)
        update_btn.pack(pady=15)
        back_btn = ttk.Button(self, text="Back", width=10, command=lambda: controller.show_frame("ReservationsPage"))
        back_btn.pack()

    def refresh(self):
        res_id = self.controller.selected_reservation_id
        if res_id is None:
            return
        res = database.get_reservation_by_id(res_id)
        if not res:
            messagebox.showerror("Error", "Reservation not found.")
            self.controller.show_frame("ReservationsPage")
            return
        # res: (id, name, flight_number, departure, destination, date, seat_number)
        for entry, value in zip(self.entries.values(), res[1:]):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def update_reservation(self):
        res_id = self.controller.selected_reservation_id
        values = [e.get().strip() for e in self.entries.values()]
        if not all(values):
            messagebox.showerror("Error", "All fields are required.")
            return
        database.update_reservation(res_id, *values)
        messagebox.showinfo("Success", "Reservation updated!")
        self.controller.show_frame("ReservationsPage") 