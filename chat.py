def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # -sig 為了去掉/ufeff
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue

		if person != None:
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f: # r-讀取  w-寫入 # utf-8編碼
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output1.txt',lines)

main()