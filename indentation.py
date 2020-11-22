from ArrayStack import *

S = ArrayStack()

sfile = "source.c"
original = open(sfile) 
    
for line in original:
  l = line.rstrip('\n')
  S.push(l)
original.close()

tfile = "target.c"
output = open(tfile, 'w')
while not S.is_empty():
  output.write(S.pop() + '\n')  
output.close()