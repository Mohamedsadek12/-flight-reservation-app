import tkinter as tk
from tkinter import ttk, messagebox
import database

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="All Reservations", font=("Arial", 18))
        label.pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("id", "name", "flight_number", "departure", "destination", "date", "seat_number"), show="headings")
        for col in ("id", "name", "flight_number", "departure", "destination", "date", "seat_number"):
            self.tree.heading(col, text=col.replace('_', ' ').title())
            self.tree.column(col, width=100, anchor="center")
        self.tree.pack(pady=10, fill="x", expand=True)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        edit_btn = ttk.Button(btn_frame, text="Edit Selected", width=15, command=self.edit_selected)
        edit_btn.grid(row=0, column=0, padx=5)
        del_btn = ttk.Button(btn_frame, text="Delete Selected", width=15, command=self.delete_selected)
        del_btn.grid(row=0, column=1, padx=5)
        back_btn = ttk.Button(btn_frame, text="Back", width=10, command=lambda: controller.show_frame("HomePage"))
        back_btn.grid(row=0, column=2, padx=5)

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for res in database.get_all_reservations():
            self.tree.insert("", "end", values=res)

    def get_selected_id(self):
        selected = self.tree.selection()
        if not selected:
            return None
        return self.tree.item(selected[0])["values"][0]

    def edit_selected(self):
        res_id = self.get_selected_id()
        if res_id is None:
            messagebox.showwarning("No selection", "Please select a reservation to edit.")
            return
        self.controller.set_selected_reservation(res_id)

    def delete_selected(self):
        res_id = self.get_selected_id()
        if res_id is None:
            messagebox.showwarning("No selection", "Please select a reservation to delete.")
            return
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?"):
            database.delete_reservation(res_id)
            self.refresh() 