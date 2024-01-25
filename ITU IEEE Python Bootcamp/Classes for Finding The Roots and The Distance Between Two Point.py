import math 

#Class for solving Quadric Equations
class QuadraticEquation:
   def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
#The function taking the discriminant
   def discriminant(self):
    delta = self.b**2 -4*self.a*self.c
    return delta
     
#Find roots of the equation
   def solve(self):
     if (self.discriminant() > 0):
       x1 = (-self.b + math.sqrt(self.discriminant()))/(2*self.a)
       x2 = (-self.b - math.sqrt(self.discriminant()))/(2*self.a)
       return x1, x2 
     elif(0 == self.discriminant()):
       x = -self.b/(2*self.a)
       return x
     else:
       r =-self.b/(2*self.a)
       j=math.sqrt(abs(self.discriminant())) / (2*self.a)
       return complex(r,j),complex(r,-j)

#Class for finding distance between two points
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance(self,other_point):
    distance_x=self.x-other_point.x
    distance_y=self.y-other_point.y
    return math.sqrt(distance_x**2+distance_y**2)


def main():
  print("Select an operation:")
  print("1.Solve Quadratic Equation")
  print("2.Calculate Distance between Two Points\n") 
  choice=int(input("Your Choice: "))
  
  #Mapping the coefficients and find roots of the equation
  if choice==1:
    a, b, c=map(float,input("Enter Coefficients a,b,c for the Quadratic Equation(ax^2+bx+c): ").split())
    equation =QuadraticEquation(a, b, c)
    return equation.solve()
    
  #Mapping the coefficients for distance between two points
  elif choice==2:

    x1, y1=map(float,input("Enter the coordinates of the first point(x,y): ").split())
    x2, y2=map(float,input("Enter the coordinates of the second point(x,y): ").split())
    
    point1=Point(x1,y1)
    point2=Point(x2,y2)
    print("The distance between the points is:")
    return point1.distance(point2)

print(main())