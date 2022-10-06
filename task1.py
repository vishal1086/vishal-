#Getting choice  from user

def area_of_circle(radius):
    area=3.14*radius*radius
    print("area of  a circle is  ", area)
def area_of_rectangle(length, width):
    area=length*width
    print("area of  a rectangle =", area)

def area_of_triangle(height, base):
    area = (height*base)/2
    print("area of triangle =", area)

print("Geometry calculator")
print("1. calculate area of a circle ")
print("2. calculate area of a retangle ")
print("3. calculate area of a triangle ")
print("4. quit ")
while True:

    option = int(input("Enter Your choice(1-4): "))


    if option == 1:
        radius = int(input(" enter radius of  a circle"))
        area_of_circle(radius)


    elif option == 2:
        length=int(input("enter length of a rectangle:"))
        width = int(input("enter width of a rectangle:"))
        area_of_rectangle(length, width)

    elif option == 3:
        height = int(input("enter height of a triangle"))
        base = int(input("enter base length of a triangle"))
        area_of_triangle(height, base)

    elif option == 4:
        break

    else:
        print("Invalid Option")