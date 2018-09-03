def xor_byte_strings(input_bytes_1, input_bytes_2):
	return ''.join([chr(a ^ b) for a,b in zip(input_bytes_1,input_bytes_2)])

input1 = bytearray.fromhex('1c0111001f010100061a024b53535009181c')
input2 = bytearray.fromhex('686974207468652062756c6c277320657965')
print (xor_byte_strings(input1,input2)).encode('hex')
