z = 10  # Global variable z

def x(z):
    print(z)
    z = z + 1
    print(z)
    return z

x(z)



class Y:
    def yy(self):
        x()
        print("zxc")
        x()
        print("zxc")

# Create an instance of class Y
y_instance = Y()

# Call the some_function method of the Y instance
y_instance.yy()
