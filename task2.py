def square(length):
    print("perimeter of square is :",4*length,"cm")
    print("area of square is :",   length* length, "cm^2")
def rectangle(length,breadth):
    print("perimeter of rectangle is :",(2*length)+(2*breadth),"cm")
    print("area of rectangle is :",   length* breadth, "cm^2")
def circle(radius):
    print("circumference of circle is :",2*3.14*radius,"cm")
    print("area of  circle is :",   3.14*radius*radius, "cm^2")


print("shapes")
print("1.Square")
print("2.rectangle")
print("3.circle")
print("4.quit")
while True:
    shape=(int(input("enter your choice")))
    if shape==1:
        length=int(input("enter the length of square in cm:"))
        square(length )
    elif shape == 2:
        length = int(input("enter the length of rectangle in cm:"))
        breadth = int(input("enter the breadth of breadth in cm:"))
        rectangle(length, breadth)
    elif shape == 3:
        radius= int(input("enter the radius of circle in cm:"))
        circle(radius)

    elif shape==4:
        break
    else:print("invalid option")

