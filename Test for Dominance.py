equations = [
    [[], False],  # [0, 1]
    [[], False],  # [0, 1]
    [[], False]  # [0, 1]
]


# Method for getting input
def getInput():
    print("X: ")
    x = int(input())  # get only integers

    print("Y:")
    y = int(input())  # get only integers

    print("Z:")
    z = int(input())  # get only integers

    # we need the x, y, z
    return x, y, z


try:
    # first equation
    print("Enter first equation below:")
    x, y, z = getInput()
    equations[0][0] = [x, y, z]

    sum = y + z
    if x > sum:
        equations[0][1] = True
        print("x is dominant")

    else:
        print("x is not dominant")

    # second equation
    x, y, z = getInput()
    equations[1][0] = [x, y, z]

    sum = x + z
    if y > sum:
        equations[1][1] = True
        print("y is dominant")
    else:
        print("y is not dominant")

    # third equation
    x, y, z = getInput()
    sum = x + y
    if z > sum:
        equations[2][1] = True
        print("z is dominant")
    else:
        print("x is not dominant")

    equations[2][0] = [x, y, z]

except Exception:
    print("enter only numbers")


def gauss_jacobi():
    # all the jacobi stuff
    pass  # remove this when u have code


def gauss_sidel():
    # all the sidel stuff
    pass  # remove this when u have code


trues: int = 0

# go through each equation and
# see if they are True or False
for i in range(len(equations)):
    bool = equations[i][1]  # True or False
    if bool:  # If it's true, we increment our number of trues
        trues = trues + 1

# Check if all of them are True
if trues == len(equations):
    print("Methods: Gauss Jacobi/Gauss Sidel")
    print("Choose method: (GJ/GS):")
    method = input()
    method = method.upper()

    # Make them choose a method.
    if method == "GJ":
        gauss_jacobi()
    elif method == "GS":
        gauss_sidel()


    # In case the user didn't pick a correct
    # method.
    else:
        print("i said choose GJ or GS")

# If one is False,
# Use Gauss Stidel
else:
    gauss_sidel()