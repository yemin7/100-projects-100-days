try:
    file = open("file.txt")
    dict1 = {"key": "testvalue"}
    print(dict1["key"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Testing123")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    # raise TypeError("This is an error that I made up.")
