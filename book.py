import random
import numpy as np 

class TrainTicketBooking:
    def __init__(self, train_id, name, age, sex, from_station, to_station, seat_class):
        self.train_id = train_id
        self.name = name
        self.age = age
        self.sex = sex
        self.from_station = from_station
        self.to_station = to_station
        self.seat_class = seat_class
        self.pnr = random.randint(100000, 999999)

    def book(self):
        self._alloted_berth_and_coach()
        self._set_fare()
        self._print_ticket()

    def _alloted_berth_and_coach(self):
        self.berth_num = random.randint(1, 72)  
        coach_codes = {'AC': 'A', 'Sleeper': 'S', 'Unreserved': 'U'}
        prefix = coach_codes.get(self.seat_class, 'U')
        self.coach_num = prefix + str(random.randint(1, 10))

    def _set_fare(self):
        fare_table = {'AC': 1575, 'Sleeper': 815, 'Unreserved': 325}
        self.fare_cost = fare_table.get(self.seat_class, 300)

    def _print_ticket(self):
        print("\t Thankyou for booking! here is your ticket status:")
        print("------------------------------------------")
        print(f"PNR No.: {self.pnr}")
        print(f"Train No.: {self.train_id}")
        print(f"Passenger: {self.name}")
        print(f"Age/Gender: {self.age}/{self.sex}")
        print(f"From: {self.from_station} To: {self.to_station}")
        print(f"Class: {self.seat_class}")
        print(f"Coach: {self.coach_num}")
        print(f"Berth No.: {self.berth_num}")
        print(f"Total Fare: ₹{self.fare_cost}")
        print("------------------------------------------")
        print("Wishing you a happy journey!")

def get_valid_input(prompt, valid_choices):
    while True:
        ans = input(prompt).strip()
        if ans in valid_choices:
            return ans
        else:
            print(f"Oops, please enter one of these: {', '.join(valid_choices)}")

if __name__ == "__main__":
    print("Welcome to the Train Ticket Booking!")
    train_no = input("Please enter the train number: ").strip()
    passenger_name = input("Passenger Full Name: ").strip()

    while True:
        try:
            passenger_age = int(input("Age (in years): ").strip())
            break
        except ValueError:
            print("That doesn’t look like a valid age. Please enter a number.")

    gender = get_valid_input("Gender (M/F): ", ['M', 'F'])
    departure = input("Departure Station: ").strip()
    arrival = input("Destination Station: ").strip()
    seat_class = get_valid_input("Choose class (AC/Sleeper/Unreserved): ", ['AC', 'Sleeper', 'Unreserved'])

    booking = TrainTicketBooking(
        train_id=train_no,
        name=passenger_name,
        age=passenger_age,
        sex=gender,
        from_station=departure,
        to_station=arrival,
        seat_class=seat_class
    )
    booking.book()
