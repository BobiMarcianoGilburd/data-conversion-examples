with open('name.txt') as f:
	full_text = f.read()

with open('hello.txt', 'w') as f:
	f.write('My name is ')
	f.write(full_text) 

