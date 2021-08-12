# greeter-1.py
# from "package" import "class"
from measurement import Measurement
from measurements import Measurements

if __name__ == "__main__":
    perth_reading = Measurement(29.5, "Perth")
    bunbury_reading = Measurement(26.5, "Bunbury")
    sydney_reading = Measurement(18.7, "Sydney")
    readings = Measurements()
    readings.add_measurement(perth_reading)
    readings.add_measurement(bunbury_reading)
    readings.add_measurement(sydney_reading)
    print("Readings added")
    for a_reading in readings.measurements:
        print(a_reading)
    readings.clear_all()
    print("Readings cleared")
    for a_reading in readings.measurements:
        print(a_reading)
    perth_reading.clear()
    bunbury_reading.clear()
    sydney_reading.clear()
