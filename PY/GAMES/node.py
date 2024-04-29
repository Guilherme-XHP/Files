class Node:
   def __init__(self, info):
      self.info = info
      self.next = None

   def __str__(self):
      return(f"Info: {self.info}")