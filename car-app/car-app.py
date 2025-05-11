# The line below imports the FastAPI class from the fastapi module.
# The FastAPI class is used to create an instance of a FastAPI application.
from fastapi import FastAPI
from schemas import load_car_data

# The line below creates an instance of the FastAPI class.
# This instance will be used to define the API endpoints and handle requests.
# The instance is stored in the variable 'app'.
# The FastAPI instance is the main entry point for the application.
app = FastAPI()

# A list named 'car_data' is defined to store information about cars.
# The keys of the list are car IDs, and the values are dictionaries containing car details.
car_data = load_car_data("cars.json")

# The following code defines a simple FastAPI application with a single endpoint.
# The endpoint returns a welcome message when accessed.
# The @app.get("/") decorator defines an attribute for the app defined in the FastAPI instance.
@app.get("/")
async def welcome(name):
    """Return a friendly welcome message."""
    return {"message": f"Hello, {name}! Welcome to the Car Sharing service!"}

# The following code defines an endpoint to retrieve car data.
# The endpoint is accessed via a GET request to "/cars".
@app.get("/cars")
async def get_cars(make: str|None = None, model: str|None = None, year: int|None = None) -> list:
    """Return a list of cars."""
    # If the make, model, or year parameters are provided, filter the car_data list.
    result = car_data
    if make:
        result = [car for car in result if car.make == make]
    if model:
        result = [car for car in result if car.model == model]
    if year:
        result = [car for car in result if car.year == year]
    # If no filters are applied, return the entire car_data list.
    return result

# The following code defines an endpoint to retrieve a specific car by its ID.
# The endpoint is accessed via a GET request to "/cars/{car_id}".
@app.get("/cars/{car_id}")
async def get_car(car_id: int) -> dict:
    """Return a car by ID."""
    # Find the car with the specified ID in the car_data list.
    for car in car_data:
        # Access the 'id' attribute using dot notation
        if car.id == car_id:
            # Convert the Car object to a dictionary if needed
            return car.__dict__
    # If the car is not found, return a 404 error.
    return {"error": "Car not found"}