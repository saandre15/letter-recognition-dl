class Letter:

  def __init__(self, _input: list<list<int>>, output: chr):
    val = ord(output)
    if(val <  65 || val > 122 || (val > 91 && val < 97))
      raise IndexError("Letter initialized without ASCII out of bound")
    self.input = _input
    self.output = output

  def outputAsInt(self):
    val = ord(self.output) 
    if(val < 91) return val - 65
    else return (val - 97) + 65