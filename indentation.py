from ArrayStack import *

S = ArrayStack()
space_count=0

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
while not S.is_empty():
  output.write(S.pop() + '\n')  
output.close()