def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # -sig 為了去掉/ufeff
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	allen_words_count = 0
	viki_words_count = 0
	allen_stickers_count = 0
	viki_stickers_count = 0
	allen_images_count = 0
	viki_images_count = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_stickers_count += 1
			elif s[2] == '圖片':
				allen_images_count += 1
			else:
				for m in s[2:]:
					allen_words_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_stickers_count += 1
			elif s[2] == '圖片':
				viki_images_count += 1
			else:
				for m in s[2:]:
					viki_words_count += len(m)
	print('allen說了', allen_words_count, '個字')
	print('allen傳了', allen_stickers_count, '張貼圖')
	print('allen傳了', allen_images_count, '張圖片')
	print('viki說了', viki_words_count, '個字')
	print('allen傳了', viki_stickers_count, '張貼圖')
	print('allen傳了', viki_images_count, '張圖片')

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f: # r-讀取  w-寫入 # utf-8編碼
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output1.txt',lines)

main()