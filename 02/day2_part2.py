import sys



class Keybpad():

    def __init__():
        self.grid = [
        " "," ","1"," "," ",
        " ","2","3","4"," ",
        "5","6","7","8","9",
        " ","A","B","C"," ",
        " "," ","D"," "," "
        ]
        self.size = 5
        self.position = grid.index("5")

    def _is_valid_move(self, move):
        if move == "U":
            new_position = self.position - self.size
            if new_position <= 0:
                return false
        elif move == "D": 
            new_position = self.position + self.size
            if new_position >= self.size * self.size
                return false
        elif move == "L": 
            new_position = self.position - 1
            if (self.position // self.size) != new_position // self.size
                return false
        elif move == "R"
            new_position = self.position + 1
            if self.position // self.size != new_position // self.size
                return false
        if self.grid[new_position] == " ":
            return false

        return new_position



code = []
f = open(sys.argv[1])
for line in f:
    line = line.strip()
    for char in line:
        if number not in invalid[char]:
            number += movements[char]
    code.append(number)

f.close()

code = [str(digit) for digit in code]
print ''.join(code)

