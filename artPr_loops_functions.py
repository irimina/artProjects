

'''
AIM: Modify programs using parameters and class constants to create original artworks.
Assessment: Complete an art project and “artist statement” justifying their programming choices
'''
#function definitions

def writeChars(ch,num):
  for i in range(1,num,1):
    print(ch, end =" ") # end ="" means that ch prints on the same line
  
# program starts

#write a line of 20 ='s
writeChars("=",18)

for i in range(1,10,1):# for 10 lines of pic(height)
  writeChars(">",i) #increate the number of '>'s in each line
  writeChars(' ',20-2*i)#decrease the number of characters in each line
  writeChars("<",i) # increase the number of "<" in each line
  print() # go to the next line before starting the body of the loop again

  
