result = ''
file = open('lorem.txt', 'r')
data = file.readlines()[0]
#take 1 character from the string at the time
for i in data:
    #convert to binary and remove 0b
    binaryCharacter = str(bin(ord(i))).replace('0b', '')
    #add 0s in the front to make it a 7bit
    binaryCharacter = '0'*( 7 - len(binaryCharacter) ) + binaryCharacter
    result += binaryCharacter
print(result)
#make list containing strings of only 1 and only 0 respectively
list0 = result.split('1')
list1 = result.split('0')
#compare by length and print
print('Largest repetition of 0: ' + str( len( max(list0, key=len) )))
print('Largest repetition of 1: ' + str( len( max(list1, key=len) )))
