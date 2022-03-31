import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        count += 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
                     # the last print is 1
    return count
  
def lineGraph(num = 0):
  max_so_far = 0
  grapher = turtle.Turtle()
  writer = turtle.Turtle()
  writer.up()
	
  myscreen = turtle.Screen()
  
  for i in range(1, num + 1):
    result = seq3np1(i)
    if result > max_so_far:
      max_so_far = result 
      myscreen.setworldcoordinates(0, 0, i + 5, max_so_far + 5)
      maximum = "\nMaximum is: " + str(max_so_far)
      print(maximum)
      writer.clear()
      writer.up()
      writer.goto(0, max_so_far)
      writer.down()
      writer.write(maximum)
    myscreen.setworldcoordinates(0, 0, i + 10, max_so_far + 10)
    grapher.goto(i, result)

  myscreen.exitonclick()
  
def main():
  
  upper = int(input("Upper bound value: "))
  if upper > 0:
    for i in range(1, upper + 1):
      print("\nStarting value: ", i)
      print("Return value: ", seq3np1(i))
    lineGraph(upper)
    
  else:
    exit()
  
main()