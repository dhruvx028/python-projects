import os
f = os.listdir('FILES')
x = 0
y = 0
z = 0


for file in f:
    if file.endswith('.txt'):
        x += 1
    elif file.endswith('.csv'):
        y += 1
    else:
        z += 1

print (f'Number of .txt files: {x}')
print (f'Number of .csv files: {y}')
print (f'Number of other files: {z}')