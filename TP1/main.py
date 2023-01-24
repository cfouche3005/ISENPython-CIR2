# EX1

def celcius_fahrenheit(celcius):
    return (celcius*9/5)+32


temperature_celsius = 22
temperature_fahrenheit = celcius_fahrenheit(temperature_celsius)
print(temperature_fahrenheit)

# EX2


def mention(note):
    out=""
    if note < 10:
        out = "insuffisant"
    elif note < 12:
        out = "passable"
    elif note < 14:
        out ="assez bien"
    elif note < 16:
        out = "bien"
    elif note <= 20:
        out ="très bien"
    return out

print(mention(13))
print(mention(20))

# EX3

def nombre_pairs(n):
    out = []
    for nb in range(0, n+1, 2):
        out.append(nb)
    return out


print(nombre_pairs(855))

# EX4

