import json

from pydantic import BaseModel


# This is a Pydantic model for a car
class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int


def load_car_data(file_path: str) -> list[Car]:
    """Load car data from a JSON file."""
    with open("cars.json") as file:
        data = json.load(file)
    return [Car(**car) for car in data]