#가변인자 argument

def add(*args):
  print(args) #모든 인자 출력
  
add(1,2,3,4,5)
add(1,2,3)

#매개변수가 n개인 덧셈 합
def add(*args):
  sum = 0
  for i in args:
    sum = sum + i
  print(sum)
  
add(1,2,3) #6
