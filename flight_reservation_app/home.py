import tkinter as tk
from tkinter import ttk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = ttk.Label(self, text="Welcome to Flight Reservation System", font=("Arial", 20))
        label.pack(pady=40)
        book_btn = ttk.Button(self, text="Book Flight", width=20,
                              command=lambda: controller.show_frame("BookingPage"))
        book_btn.pack(pady=20)
        view_btn = ttk.Button(self, text="View Reservations", width=20,
                              command=lambda: controller.show_frame("ReservationsPage"))
        view_btn.pack(pady=10) 