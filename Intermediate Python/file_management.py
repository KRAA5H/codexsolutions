file = open("diaries.txt", "w")

file.write("sanam re")
file.write("\n sanam ree")

file_path = "diaries.txt"

try:
    file = open(file_path, "r")
finally:
    file.close()

with open(file_path, "r") as file:
    content = file.read()
    print(content)

with open(file_path, "r") as file:
    file.seek(10)
    content = file.read()
    print(content)

with open(file_path, "a") as file:
    file.truncate(7)
