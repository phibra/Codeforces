input = [16, 16, 1]
i = 0
j = 0

while (i * input[2] < input[0]):
    i += 1
    
while (j * input[2] < input[1]):
    j += 1

print(i*j)
