import binascii

# Set 1 - 1
def hex_to_base64(str):
	return str.decode("hex").encode("base64")

# Set 1 - 2
def xor_byte_strings(input_bytes_1, input_bytes_2):
	return ''.join([chr(a ^ b) for a,b in zip(input_bytes_1,input_bytes_2)])

# Set 1- 3
def xor_single_byte(str):
	nums = binascii.unhexlify(str)
	result = (''.join(chr(ord(num) ^ key) for num in nums) for key in range(256))
	print max(result, key=lambda s: s.count(' '))
