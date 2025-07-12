import tkinter as tk
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class FlightReservationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("700x500")
        self.resizable(False, False)
        self.frames = {}
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("HomePage")
        self.selected_reservation_id = None  # For editing

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if hasattr(frame, 'refresh'):
            frame.refresh()

    def set_selected_reservation(self, res_id):
        self.selected_reservation_id = res_id
        self.show_frame("EditReservationPage")

if __name__ == "__main__":
    app = FlightReservationApp()
    app.mainloop() 