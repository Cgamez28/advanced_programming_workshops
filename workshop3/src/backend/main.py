from fastapi import FastAPI
from engines import Engine
from vehicles import Vehicle
from catalog_entry import CatalogEntry

app = FastAPI()

@app.get("/create_vehicle")
def create_vehicle(vehicle_type: str):   
    """
    This method lets create a new vehicle based on its type.

    Args:
    - vehicle_type (str): Vehicle type
    """
    return CatalogEntry.create_vehicle(vehicle_type)

@app.get("/create_engine")
def create_engine():   
    """
    This method lets create a new vehicle based on its type.
    """
    return CatalogEntry.create_engine()


@app.post("/show_engines")
def create_engine():   
    """
    This method show all available engines
    """
    return CatalogEntry.show_engines()


@app.post("/show_vehicles")
def show_vehicles():   
    """
    This method show all available engines
    """
    return CatalogEntry.show_vehicles()