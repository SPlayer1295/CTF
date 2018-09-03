import binascii


def xor_single_byte(str):
	nums = binascii.unhexlify(str)
	result = (''.join(chr(ord(num) ^ key) for num in nums) for key in range(256))
	print max(result, key=lambda s: s.count(' '))

xor_single_byte('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')