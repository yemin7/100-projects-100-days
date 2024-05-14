line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input().lower()  # Where do you want to put the treasure?

letters = ["a", "b", "c"]
column = letters.index(position[0])
row = int(position[1])-1

map[row][column] = "X"

print(f"{line1}\n{line2}\n{line3}")
