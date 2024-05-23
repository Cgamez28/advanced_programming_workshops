from pydantic import BaseModel

class Engine(BaseModel):  
    """This class represents the behavior of a vehicle engine."""
    name: str
    type_: str  
    potency: int
    weight: float 

    def __str__(self):
        return f"Name: {self.name}   Type: {self.type_}\
            Potency: {self.potency}   Weight: {self.weight}"