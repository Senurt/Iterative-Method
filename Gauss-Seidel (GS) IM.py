# Gauss Seidel Iteration Method for solving systems of linear equations

# Define the equations to be solved in diagonally dominant form
f1 = lambda x, y, z: (17 - y + 2 * z) / 20
f2 = lambda x, y, z: (-18 - 3 * x + z) / 20
f3 = lambda x, y, z: (25 - 2 * x + 3 * y) / 20

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Read the tolerable error
e = float(input("Enter tolerable error: "))

# Implementation of Gauss Seidel Iteration
print("\nCount\tx\ty\tz\n")
condition = True
while condition:
    x1 = f1(x0, y0, z0)
    y1 = f2(x1, y0, z0)
    z1 = f3(x1, y1, z0)
    print(f"{count}\t{x1:.4f}\t{y1:.4f}\t{z1:.4f}\n")

    e1 = abs(x0 - x1)
    e2 = abs(y0 - y1)
    e3 = abs(z0 - z1)

    count += 1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > e and e2 > e and e3 > e

print(f"\nSolution: x={x1:.3f}, y={y1:.3f}, and z={z1:.3f}\n")
