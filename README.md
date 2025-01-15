# ICC Scheduler

## Overview
The ICC Scheduler is a Python application designed to manage employee scheduling efficiently. It provides a user-friendly graphical interface for adding and editing employee availability, creating and managing shifts, and generating schedules based on the input data.

## Features
- Add and edit employee information and availability.
- Create and manage shifts for employees.
- Generate schedules based on employee availability and shifts.
- Intuitive GUI for easy navigation and operation.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/icc-scheduler.git
   ```
2. Navigate to the project directory:
   ```
   cd icc-scheduler
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Directory Structure
```
icc-scheduler
├── src
│   ├── main.py                # Entry point of the application
│   ├── scheduler
│   │   ├── __init__.py        # Scheduler module initialization
│   │   ├── employee.py         # Employee management
│   │   ├── shifts.py           # Shift management
│   │   └── schedule.py         # Schedule generation
│   └── assets
│       └── ICC Logo Inverse2.png # Logo asset
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.