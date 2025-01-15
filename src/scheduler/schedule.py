class Schedule:
    def __init__(self):
        self.schedule = {}

    def add_shift(self, employee_id, shift):
        if employee_id not in self.schedule:
            self.schedule[employee_id] = []
        self.schedule[employee_id].append(shift)

    def remove_shift(self, employee_id, shift):
        if employee_id in self.schedule and shift in self.schedule[employee_id]:
            self.schedule[employee_id].remove(shift)

    def generate_schedule(self):
        # Logic to generate the schedule based on employee availability and shifts
        pass

    def get_schedule(self):
        return self.schedule

    def clear_schedule(self):
        self.schedule.clear()