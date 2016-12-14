import sys


instructions = []
# instruction pointer. (yes, eip. My old assembly class is leaking out.)
eip = 0
reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

def inc (arg):
  global eip
  reg[arg] += 1
  eip += 1

def dec(arg):
  global eip
  reg[arg] -= 1
  eip += 1

def cpy(*args):
  global eip
  if type(args[0]) is int:
    reg[args[1]] = args[0]
  else:
    reg[args[1]] = reg[args[0]]
  eip += 1

def jnz(compare, amount):
  global eip
  if type(compare) is int:
    if compare != 0:
      eip += amount
    else:
      eip += 1
  else:
    if reg[compare] != 0:
        eip += amount
    else:
      eip += 1

cmds = {'inc': inc, 'dec': dec, 'cpy': cpy, 'jnz': jnz}

with open(sys.argv[1]) as infile:
  for line in infile:
    instructions.append(line.strip().split(' '))

for instruction in instructions:
  for i in range(len(instruction)):
    try:
      instruction[i] = int(instruction[i]);
    except:
      pass

while eip < len(instructions):
  cmds[instructions[eip][0]](*instructions[eip][1:])

print reg
