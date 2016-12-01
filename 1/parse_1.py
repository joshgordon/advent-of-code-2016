

with open("input_1.txt") as f:
    directions = f.read()[:-1]
directions.strip()
directions = directions.split(', ')
print directions
