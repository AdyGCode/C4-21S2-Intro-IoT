# This assumes the class Measurement exists
class Measurements:
    def __init__(self):
        self.measurements = list()

    def add_measurement(self, measurement):
        """Add new measurement to the list."""
        self.measurements.append(measurement)

    def clear_all(self):
        """Clear all measurements in the list."""
        for item in self.measurements:
            item.clear()
