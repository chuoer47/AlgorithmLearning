size = set()
for red in range(0, 255 + 1):
    for green in range(0, 255 + 1):
        for blue in range(0, 255 + 1):
            if blue > red and blue > green:
                size.add((red, green, blue))
print(len(size))
