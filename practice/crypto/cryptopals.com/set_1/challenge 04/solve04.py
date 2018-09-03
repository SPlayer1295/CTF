import binascii


def xor_single_byte(str):
	nums = binascii.unhexlify(str)
	for key in range(256):
		result = ''.join(chr(ord(b) ^ key) for b in nums)
		if result.isprintable():
			print(result)

def main():
	with open("4.txt") as f:
		for line in f:
			xor_single_byte(line.strip())

if __name__ == '__main__':
	main()
