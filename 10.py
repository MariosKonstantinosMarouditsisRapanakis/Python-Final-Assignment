import sys
#checking for file input through the cmd
filename = ''
filename = sys.argv[1] if len(sys.argv) > 1 else 'two_cities_ascii.txt'
#getting data from the file
file = open(filename, 'r')
data = ''.join(file.readlines())
file.close()

result = ''
#take 1 character from the string at the time
for i in data:
    #convert to binary and remove 0b
    binaryCharacter = str(bin(ord(i))).replace('0b', '')
    #add 0s in the front to make it a 7bit
    binaryCharacter = '0'*( 7 - len(binaryCharacter) ) + binaryCharacter
    #get 2 first and 2 last digits
    result += binaryCharacter[:2] + binaryCharacter[-2:]
resultList = [ result[16*j:(j+1)*16] for j in range(int(len(result)/16)) ]
#initiating count variables
count2or5 = 0
count3 = 0
count7 = 0
#iterating
for i in range(len(resultList)):
    count2or5+=1 if int(resultList[i])%2 == 0 else 0
    count3+=1 if int(resultList[i])%3 == 0 else 0
    count7+=1 if int(resultList[i])%7 == 0 else 0
print(f' Even numbers: {str(100*count2or5/len(resultList))[:5]}%\n Dividable by 3: {str(100*count3/len(resultList))[:5]}%\n Dividable by 5: {str(100*count2or5/len(resultList))[:5]}%\n Dividable by 7: {str(100*count7/len(resultList))[:5]}%\n')
