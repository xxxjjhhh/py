#키워드 가변인자 keyword argument

def kwlist(**kwargs):
  print(kwargs)
  

kwlist(a="kim", b="Lee", c="Jenong") #{'a': 'Kim', 'b': 'Lee', 'c': 'Jeong'}
