class Vehicle(object):
  """A datastructure for storing information about a vehicle.

  Longer class information....
  Longer class information....

  Attributes:
    brand (str): The brand of the vehicle.
    owner (str): The owner of the vehicle.
    model (str): The model of the vehicle.
    category (str): The category of the vehicle.

  Methods:
    None
  """
  def __init__(self, brand, owner, model, category) -> None:
    """Initializes a Vehicle object with the given attributes.
    
    Args:
      brand (str): The brand of the vehicle.
      owner (str): The owner of the vehicle.
      model (str): The model of the vehicle.
      category (str): The category of the vehicle.
    """
    self.brand = brand
    self.owner = owner
    self.model = model
    self.category = category