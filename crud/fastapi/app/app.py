from fastapi import FastAPI

# Initialize an instance of the FastAPI class
# This is the main entry point for the FastAPI application
# The FastAPI instance is the main application object that will handle incoming requests
app = FastAPI()

# Here we start adding operations to the FastAPI instance
# Define a root endpoint that returns a simple JSON response
# The root endpoint is the default endpoint that is accessed when the base URL is requested
# The @app.get decorator is used to define a GET request handler for the root endpoint
# The tags parameter is used to group the endpoint in the OpenAPI documentation
# the async def keyword is used to define an asynchronous function
# The function returns a dictionary that will be automatically converted to JSON
# The response will be returned with a 200 OK status code
@app.get("/", tags=["root"])
async def root() -> dict:
    return {"message": "Hello World"}

# Define a list of to-do items
# This is a simple in-memory list of dictionaries representing to-do items
todos = [
    {"id": 1, "task": "Learn FastAPI", "completed": False},
    {"id": 2, "task": "Build a REST API", "completed": False},
    {"id": 3, "task": "Write a blog post about it", "completed": False},
]


# GET --> Read To Do

# Define an endpoint to retrieve a list of to-do items
# The @app.get decorator is used to define a GET request handler for the /todo endpoint
# The return type is specified as a dictionary
# The function returns the list of to-do items as a JSON response
@app.get("/todo", tags=["todos"])
async def get_todo() -> dict:
    return {"data": todos}


# POST --> Create To Do

# Define an endpoint to create a new to-do item
# The @app.post decorator is used to define a POST request handler for the /todo endpoint
# The function takes a dictionary representing the new to-do item as input
# The function appends the new to-do item to the list of to-do items
@app.post("/todo", tags=["todos"])
async def create_todo(todo: dict) -> dict:
    # Add the new to-do item to the list
    todos.append(todo)
    # Return the newly created to-do item
    return {
        "data": "A new task has been added"
        }


# PUT --> Update To Do

# Define an endpoint to update an existing to-do item
# The @app.put decorator is used to define a PUT request handler for the /todo endpoint
# The function takes an ID and a dictionary representing the updated to-do item as input
# The function updates the corresponding to-do item in the list
@app.put("/todo/{id}", tags=["todos"])
async def update_todo(id: int, todo: dict) -> dict:
    for existing_todo in todos:
        if existing_todo["id"] == id:
            existing_todo.update(todo)
            return {
                "data": f"The task with id {id} has been updated"
                }
    return {
        "error": f"The task with id {id} was not found"
        }


# DELETE --> Delete To Do

# Define an endpoint to delete a to-do item
# The @app.delete decorator is used to define a DELETE request handler for the /todo endpoint
# The function takes an ID as input
# The function removes the corresponding to-do item from the list
@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for existing_todo in todos:
        if existing_todo["id"] == id:
            todos.remove(existing_todo)
            return {
                "data": f"The task with id {id} has been deleted"
                }
    return {
        "error": f"The task with id {id} was not found"
        }