'''
  INDENTATION FIXER
  Burak Kiper 390626
  Muhammed Halim Güleşen 348398
'''

from ArrayStack import *

S = ArrayStack()
space_count=0

def reverse(stack):
    items = []
    while not stack.is_empty():
        items.append(stack.pop())
    for item in items:
        stack.push(item)
    return stack

def find_bracket(line,space_count):
  if line.find('{') >= 0:
    new_line=space_count*' '+line
    S.push(new_line)
    space_count=space_count+4
  elif line.find('}') >= 0:
    space_count=space_count-4
    new_line=space_count*' '+line
    S.push(new_line)
  else:
    new_line=space_count*' '+line
    S.push(new_line)
  return space_count

sfile = "source.c"
original = open(sfile) 
    
for line in original:
  l = line.rstrip('\n')
  space_count=find_bracket(l,space_count)

original.close()

tfile = "target.c"
output = open(tfile, 'w') 
reverse_stack=reverse(S)  
while not S.is_empty():
  output.write(reverse_stack.pop() + '\n') 
output.close()
