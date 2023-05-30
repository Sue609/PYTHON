from pathlib import Path

#Absolute path
#Relative path

path = Path("emails")
print(path.exists())
print(path.mkdir())
print(path.rmdir())

path = Path()
for file in path.glob('*.py'): #search for files in a directory
    print(file)
    