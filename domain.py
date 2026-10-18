"""Domain classes reflecting the car rental UML model."""
from datetime import date
from decimal import Decimal

YOUNG_DRIVER_SURCHARGE = Decimal("50.00")  # Assumption: CHF 50 per rental

class Customer:
    def __init__(self, customer_id, name, phone, licence_no, date_of_birth):
        self.customer_id, self.name, self.phone = customer_id, name, phone
        self.licence_no = licence_no
        self.date_of_birth = date.fromisoformat(date_of_birth)

    def calculate_age(self, on_date):
        return on_date.year - self.date_of_birth.year - ((on_date.month, on_date.day) < (self.date_of_birth.month, self.date_of_birth.day))

class Car:
    def __init__(self, license_plate, type, colour, daily_price):
        self.license_plate, self.type, self.colour = license_plate, type, colour
        self.daily_price = Decimal(str(daily_price))

    def is_available(self, start_date, end_date, rentals):
        return all(r["license_plate"] != self.license_plate or
                   not (start_date < date.fromisoformat(r["end_date"]) and
                        end_date > date.fromisoformat(r["start_date"])) for r in rentals)

class Insurance:
    def __init__(self, insurance_id, insurance_type, daily_cost):
        self.insurance_id, self.insurance_type = insurance_id, insurance_type
        self.daily_cost = Decimal(str(daily_cost))

class Rental:
    def __init__(self, rental_id, customer, car, insurance, start_date, end_date):
        self.rental_id, self.customer, self.car, self.insurance = rental_id, customer, car, insurance
        self.start_date, self.end_date = date.fromisoformat(start_date), date.fromisoformat(end_date)

    def validate_rental_period(self):
        return self.end_date > self.start_date

    def calculate_rental_days(self):
        return (self.end_date - self.start_date).days

    def apply_young_driver_surcharge(self):
        return YOUNG_DRIVER_SURCHARGE if self.customer.calculate_age(self.start_date) < 23 else Decimal("0.00")

    def calculate_total_price(self):
        if not self.validate_rental_period():
            raise ValueError("End date must be after start date")
        days = self.calculate_rental_days()
        return (days * (self.car.daily_price + self.insurance.daily_cost) + self.apply_young_driver_surcharge()).quantize(Decimal("0.01"))

    def to_record(self):
        return {"rental_id": self.rental_id, "customer_id": self.customer.customer_id,
                "license_plate": self.car.license_plate, "insurance_id": self.insurance.insurance_id,
                "start_date": self.start_date.isoformat(), "end_date": self.end_date.isoformat(),
                "rental_days": self.calculate_rental_days(), "customer_age": self.customer.calculate_age(self.start_date),
                "young_driver_surcharge": float(self.apply_young_driver_surcharge()),
                "total_price": float(self.calculate_total_price())}
