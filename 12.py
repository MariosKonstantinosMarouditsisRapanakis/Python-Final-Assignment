import requests
result= ""
#get latest round
round = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'}).json()['round']
for i in range(100):
    value = requests.get(f'https://drand.cloudflare.com/public/{round - i}', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'}).json()['randomness']
    value = bin(int(value, 16)).replace('0b', '')
    result += str(value)
#make list containing strings of only 1 and only 0 respectively
list0 = result.split('1')
list1 = result.split('0')
#compare by length and  print
print('Largest repetition of 0: ' + str( len( max(list0, key=len) )))
print('Largest repetition of 1: ' + str( len( max(list1, key=len) )))
