"""Car Rental API. Start using python run.py and open /docs."""
from datetime import date
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from storage import load_records, save_records
from domain import Customer, Car, Insurance, Rental

app = FastAPI(title="Car Rental IS API", description="Customer / Car / Insurance / Rental")

class RentalRequest(BaseModel):
    customer_id: int
    license_plate: str
    insurance_id: int
    start_date: date
    end_date: date

def lookup(filename, key, value):
    for item in load_records(filename):
        if item[key] == value:
            return item
    raise HTTPException(status_code=404, detail=f"{key} not found: {value}")

@app.get("/")
def welcome():
    return {"message": "Car Rental IS API", "documentation": "/docs"}

@app.get("/customers")
def list_customers():
    return load_records("customers.json")

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return lookup("customers.json", "customer_id", customer_id)

@app.get("/cars")
def list_cars():
    return load_records("cars.json")

@app.get("/cars/{license_plate}")
def get_car(license_plate: str):
    return lookup("cars.json", "license_plate", license_plate)

@app.get("/insurance")
def list_insurance():
    return load_records("insurance.json")

@app.get("/insurance/{insurance_id}")
def get_insurance(insurance_id: int):
    return lookup("insurance.json", "insurance_id", insurance_id)

@app.get("/rentals")
def list_rentals():
    return load_records("rentals.json")

@app.get("/rentals/{rental_id}")
def get_rental(rental_id: int):
    return lookup("rentals.json", "rental_id", rental_id)

@app.post("/rentals", status_code=201)
def create_rental(request: RentalRequest):
    customer_data = lookup("customers.json", "customer_id", request.customer_id)
    car_data = lookup("cars.json", "license_plate", request.license_plate)
    insurance_data = lookup("insurance.json", "insurance_id", request.insurance_id)
    customer = Customer(**customer_data)
    car = Car(**car_data)
    insurance = Insurance(**insurance_data)
    records = load_records("rentals.json")
    next_id = max((r["rental_id"] for r in records), default=0) + 1
    rental = Rental(next_id, customer, car, insurance, request.start_date.isoformat(), request.end_date.isoformat())
    if not rental.validate_rental_period():
        raise HTTPException(status_code=400, detail="End date must be after start date")
    if customer.calculate_age(request.start_date) < 18:
        raise HTTPException(status_code=400, detail="Customer must be at least 18 on rental start date")
    if not car.is_available(request.start_date, request.end_date, records):
        raise HTTPException(status_code=409, detail="Car is unavailable for the requested period")
    record = rental.to_record()
    records.append(record)
    save_records("rentals.json", records)
    return record
