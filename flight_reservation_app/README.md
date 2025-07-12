# Flight Reservation Desktop App

A simple desktop application for booking and managing flight reservations, built with Tkinter and SQLite.

## Features
- Book new flights
- View all reservations
- Edit or delete reservations
- Modern, user-friendly interface
- Data stored locally in SQLite

## Requirements
- Python 3.x
- Tkinter (usually included with Python)

## Setup
1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd flight_reservation_app
   ```
2. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   python main.py
   ```

## Packaging as an EXE
1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Build the executable:
   ```
   pyinstaller --onefile main.py
   ```
3. The EXE will be in the `dist/` folder.

## File Structure
```
flight_reservation_app/
├── main.py
├── database.py
├── home.py
├── booking.py
├── reservations.py
├── edit_reservation.py
├── flights.db
├── requirements.txt
├── README.md
├── .gitignore
```

## License
MIT 