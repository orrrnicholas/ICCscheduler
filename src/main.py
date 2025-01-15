# FILE: /icc-scheduler/icc-scheduler/src/main.py

import tkinter as tk
import customtkinter as ctk
from scheduler.employee import Employee
from scheduler.shifts import Shift
from scheduler.schedule import Schedule

def open_employee_availability_window():
    # Function to open the employee availability window
    pass

def create_shifts():
    # Function to create or edit shifts
    pass

def generate_schedule_with_ilp():
    # Function to generate the schedule using ILP
    pass

# Initialize the main application window
app = ctk.CTk()
app.title("ICC Scheduler")
app.geometry("800x600")

# Create a scrollable frame
scrollable_frame = ctk.CTkScrollableFrame(app)
scrollable_frame.pack(fill="both", expand=True)

# Configure rows in the scrollable frame
for i in range(20):
    scrollable_frame.grid_rowconfigure(i, weight=1)

# Add a frame at the top for the logo and buttons
top_frame = ctk.CTkFrame(scrollable_frame, fg_color="white")
top_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=2)

# Load and display the logo
logo = ctk.CTkImage("assets/ICC Logo Inverse2.png", size=(75, 75))
logo_label = ctk.CTkLabel(top_frame, image=logo, bg="white")
logo_label.grid(row=0, column=0, padx=5, pady=2)

# Add buttons to the top frame
add_employee_button = ctk.CTkButton(top_frame, text="Add/Edit Employee", command=open_employee_availability_window)
add_employee_button.grid(row=0, column=1, padx=5, pady=2)

create_shifts_button = ctk.CTkButton(top_frame, text="Create/Edit Shifts", command=create_shifts)
create_shifts_button.grid(row=0, column=2, padx=5, pady=2)

generate_schedule_button = ctk.CTkButton(top_frame, text="Generate Schedule", command=generate_schedule_with_ilp)
generate_schedule_button.grid(row=0, column=3, padx=5, pady=2)

# Start the application
app.mainloop()