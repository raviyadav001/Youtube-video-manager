file = open('youtube.txt','w')

try:
    file.write('Welcome to my Hub')
finally:
    file.close()

with open('youtube.txt','w') as file:
    file.write('welcome to my HUB')
