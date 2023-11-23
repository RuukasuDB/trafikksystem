class Vehicle(object):
  def __init__(self, brand, owner, model, category = {"el":False, "gas":False, "diesel":False}) -> None:
    self.brand = brand
    self.owner = owner
    self.model = model
    self.category = category