import sys
#checking for file input through the terminal
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
    result += binaryCharacter
#print because I can't understand if you want us to print it or not......
print(result)
#make list containing strings of only 1 and only 0 respectively
list0 = result.split('1')
list1 = result.split('0')
#compare by length and print
print('Largest repetition of 0: ' + str( len( max(list0, key=len) )))
print('Largest repetition of 1: ' + str( len( max(list1, key=len) )))
