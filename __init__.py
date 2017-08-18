string = ""

_data = {"str": string,"name": "Parsing Object"}
_keywords = {}
_groups = []

class PolyObject:
  def __init__(str=string,name="Parsing Object"):  # Can be used either PolyObject(str="name",name="name")
    # Define system data.
    _data["str"] = str
    _data["name"] = name
    
  def Keyword(name,alias)
    _keywords.update(name: alias)
    print("".join([name," has been added to keywords list."]))
    
  def Group()
