class Shift:
    def __init__(self, shift_id, employee_id, start_time, end_time):
        self.shift_id = shift_id
        self.employee_id = employee_id
        self.start_time = start_time
        self.end_time = end_time

    def edit_shift(self, start_time=None, end_time=None):
        if start_time:
            self.start_time = start_time
        if end_time:
            self.end_time = end_time

    def get_shift_details(self):
        return {
            "shift_id": self.shift_id,
            "employee_id": self.employee_id,
            "start_time": self.start_time,
            "end_time": self.end_time
        }