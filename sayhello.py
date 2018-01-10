with open('name.txt') as f:
	full_text = f.read()

with open('hello.txt', 'w') as f:
	f.write('hello my name is ' + full_text)

