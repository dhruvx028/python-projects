import os
f = os.listdir('FILES')
x = 0
y = 0
z = 0

for name in f:
    source = os.path.join('FILES', name)
    if os.path.isdir(source):
        continue
    elif name.endswith('.txt'):
        file = os.path.getsize(source)
        x = x + file
    elif name.endswith('.csv'):
        file = os.path.getsize(source)
        y = y + file
    elif name.endswith('.py'):
        file = os.path.getsize(source)
        z = z + file

print (f'Total size of .txt files: {x} bytes')        
print (f'Total size of .csv files: {y} bytes')
print (f'Total size of .py files: {z} bytes')