with open("file.txt") as file:
    content = file.read()
    print(content)
    file.close()

with open("file.txt", mode="a") as file:
    content = file.write("\nNew text.")