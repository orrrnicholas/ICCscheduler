class Employee:
    def __init__(self, name, availability=None):
        self.name = name
        self.availability = availability if availability is not None else []

    def add_availability(self, time_slot):
        if time_slot not in self.availability:
            self.availability.append(time_slot)

    def edit_availability(self, old_time_slot, new_time_slot):
        if old_time_slot in self.availability:
            index = self.availability.index(old_time_slot)
            self.availability[index] = new_time_slot

    def remove_availability(self, time_slot):
        if time_slot in self.availability:
            self.availability.remove(time_slot)

    def get_availability(self):
        return self.availability

    def __str__(self):
        return f"Employee: {self.name}, Availability: {self.availability}"