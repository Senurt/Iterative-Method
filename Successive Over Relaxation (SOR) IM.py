f1 = lambda x, y, z: (-1 + y - z) / 3
f2 = lambda x, y, z: (7 + x + z) / 3
f3 = lambda x, y, z: (-7 - x + y) / 3

# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input("Enter tolerable error: "))

# Reading relaxation factor
w = float(input("Enter relaxation factor: "))

# Implementation of successive over-relaxation
print("\nCount\tx\ty\tz\n")
condition = True
while condition:
    x1 = (1 - w) * x0 + w * f1(x0, y0, z0)
    y1 = (1 - w) * y0 + w * f2(x1, y0, z0)
    z1 = (1 - w) * z0 + w * f3(x1, y1, z0)
    print(f"{count}\t{x1:.4f}\t{y1:.4f}\t{z1:.4f}\n")

    e1 = abs(x0 - x1)
    e2 = abs(y0 - y1)
    e3 = abs(z0 - z1)

    count += 1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > e and e2 > e and e3 > e

print(f"\nSolution: x = {x1:.3f}, y = {y1:.3f}, and z = {z1:.3f}\n")


