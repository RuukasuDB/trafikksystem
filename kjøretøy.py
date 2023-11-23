class Kjøretøy(object):
  def __init__(self, merke, eier, modell, kategori = {"el":False, "bensin":False, "diesel":False}) -> None:
    self.merke = merke
    self.eier = eier
    self.modell = modell
    self.kategori = kategori