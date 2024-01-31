from pathlib import Path

path = Path()
# print(path.mkdir())
# print(path.exists())

for file in path.glob('*.py'):
    print(file) # print all files in the current directory