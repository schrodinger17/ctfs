# 0x04, 0x66, 0x08, 0x32, 0x04, 0x4E, 0x08, 0x33, 0x04, 0xA9, 0x08, 0x34, 0x04, 0xFD, 0x08, 0x35, 0x04, 0x3C, 0x08, 0x36, 0x04, 0x55, 0x08, 0x37, 0x04, 0x90, 0x08, 0x38, 0x04, 0x24, 0x08, 0x39, 0x04, 0x57, 0x08, 0x3A, 0x04, 0xF6, 0x08, 0x3B, 0x04, 0x5D, 0x08, 0x3C, 0x04, 0xB1, 0x08, 0x3D, 0x04, 0x01, 0x08, 0x3E, 0x04, 0x20, 0x08, 0x3F, 0x04, 0x81, 0x08, 0x40, 0x04, 0xFD, 0x08, 0x41, 0x04, 0x36, 0x08, 0x42, 0x04, 0xA9, 0x08, 0x43, 0x04, 0x1F, 0x08, 0x44, 0x04, 0xA1, 0x08, 0x45, 0x04, 0x0E, 0x08, 0x46, 0x04, 0x0D, 0x08, 0x47, 0x04, 0x80, 0x08, 0x48, 0x04, 0x8F, 0x08, 0x49, 0x04, 0xCE, 0x08, 0x4A, 0x04, 0x77, 0x08, 0x4B, 0x04, 0xE8, 0x08, 0x4C, 0x04, 0x23, 0x08, 0x4D, 0x04, 0x9E, 0x08, 0x4E, 0x04, 0x27, 0x08, 0x4F, 0x04, 0x60, 0x08, 0x50, 0x04, 0x2F, 0x08, 0x51, 0x04, 0xA5, 0x08, 0x52, 0x04, 0xCF, 0x08, 0x53, 0x04, 0x1B, 0x08, 0x54, 0x04, 0xBD, 0x08, 0x55, 0x04, 0x32, 0x08, 0x56, 0x04, 0xDB, 0x08, 0x57, 0x04, 0xFF, 0x08, 0x58, 0x04, 0x28, 0x08, 0x59, 0x04, 0xA4, 0x08, 0x5A, 0x04, 0x5D, 0x08, 0x5B, 
arr1 =  [102, 78, 169, 253, 60, 85, 144, 36, 87, 246, 93, 177, 1, 32, 129, 253, 54, 169, 31, 161, 14, 13, 128, 143, 206, 119, 232, 35, 158, 39, 96, 47, 165, 207, 27, 189, 50, 219, 255, 40, 164, 93]
# 0x01, 0x08, 0x64, 0x01, 0x08, 0x65, 0x01, 0x08, 0x66, 0x01, 0x08, 0x67, 0x01, 0x08, 0x68, 0x01, 0x08, 0x69, 0x01, 0x08, 0x6A, 0x01, 0x08, 0x6B, 0x01, 0x08, 0x6C, 0x01, 0x08, 0x6D, 0x01, 0x08, 0x6E, 0x01, 0x08, 0x6F, 0x01, 0x08, 0x70, 0x01, 0x08, 0x71, 0x01, 0x08, 0x72, 0x01, 0x08, 0x73, 0x01, 0x08, 0x74, 0x01, 0x08, 0x75, 0x01, 0x08, 0x76, 0x01, 0x08, 0x77, 0x01, 0x08, 0x78, 0x01, 0x08, 0x79, 0x01, 0x08, 0x7A, 0x01, 0x08, 0x7B, 0x01, 0x08, 0x7C, 0x01, 0x08, 0x7D, 0x01, 0x08, 0x7E, 0x01, 0x08, 0x7F, 0x01, 0x08, 0x80, 0x01, 0x08, 0x81, 0x01, 0x08, 0x82, 0x01, 0x08, 0x83, 0x01, 0x08, 0x84, 0x01, 0x08, 0x85, 0x01, 0x08, 0x86, 0x01, 0x08, 0x87, 0x01, 0x08, 0x88, 0x01, 0x08, 0x89, 0x01, 0x08, 0x8A, 0x01, 0x08, 0x8B, 0x01, 0x08, 0x8C, 0x01, 0x08, 0x8D, 
arr2 = list(input()) # len = 41
# 0x04, 0x00, 0x06, 0x00, 0x05, 0x00, 0x04, 0x07, 0x16, 0x56, 
var1 = 0 
for j in range(7):
# 0x04, 0x00, 0x06, 0x01, 0x05, 0x01, 0x04, 0x06, 0x16, 0x42, 
	for i in range(6):
		var1 = arr2[6*j+i]
		var1 = ~var1
		var1 &= (i + 2) * j
		var2 = arr2[6*j + i]
		var2 &= ~((i + 2) * j)
		var1 |= var2
		arr3[i * 7 + j] = var
# arr2 ==> arr3
	# push vm_block[0] #j
	# push  6, 
	# BINARY_MULTIPLY 

	# push vm_block[1] #i
	# BINARY_ADD 

	# push  100, 	arr --> arr2
	# BINARY_ADD 	arr 偏移一百的位置就是arr2的位置。
			# arr2[j * 6 + i]

	# vm_stack[vm_sp] = vm_arr[vm_stack[vm_sp]]
	# vm_stack[vm_sp] = ~vm_stack[vm_sp]
						# var1 = arr2[6*j+i]   (最初 var1 = 0 )
						# var1 = ~var1

	# push vm_block[0] #j 
	# push vm_block[1] #i
	# push  2
	# BINARY_ADD 
			# i+2
	# BINARY_MULTIPLY 
			# (i+2) * j
	# BINARY_AND
						# var1 &= (i+2) * j

	# push  100, 
	# push vm_block[0]
	# push  6, 
	# BINARY_MULTIPLY 
			# j * 6
	# push vm_block[1]
	# BINARY_ADD 
	# BINARY_ADD 
			# j* 6 + i + 100 : arr --> arr2
	# vm_stack[vm_sp-1] = vm_arr[vm_stack[vm_sp-1]]
						# var2 = arr2[j * 6 + i]

	# push vm_block[0]
	# push vm_block[1]
	# push  2, 
	# BINARY_ADD 
	# BINARY_MULTIPLY 
			# (i + 2) * j
	# vm_stack[vm_sp] = ~vm_stack[vm_sp]
	# BINARY_AND
					# var2 &= ~((i + 2) * j)
	# BINARY_OR
					# var1 |= var2
	# push vm_block[1]
	# push  7, 
	# BINARY_MULTIPLY 
		# i * 7
	# push vm_block[0]
	# BINARY_ADD 
		# i * 7 + j
	# vm_arr[vm_stack[vm_sp]] = vm_stack[vm_sp-1]
					# arr3[i*7+j] = var1

	# push vm_block[1]
	# push  1, 
	# BINARY_ADD
	# push 1, 
	# vm_block[vm_stack[vm_sp]] = vm_stack[vm_sp-1]
			# block[1] = block[1] + 1
	# jump $+0xBC,  #其实应该是减法， 是个回跳-循环  $ - 68 , 回到本文件ln 11， 

	# 0x05, 0x00, 0x04, 0x06, 0x0B, 0x05, 0x01, 0x09, 0x04, 0x64, 0x09, 
	# 0x19, 0x12, 0x05, 0x00, 0x05, 0x01, 0x04, 0x02, 0x09, 0x0B, 0x0F, 0x04, 0x64, 0x05, 0x00, 0x04, 0x06, 0x0B, 0x05, 0x01, 0x09, 0x09, 0x19, 0x05, 0x00, 0x05, 0x01, 0x04, 0x02, 0x09, 0x0B, 0x12, 0x0F, 0x10, 0x05, 0x01, 0x04, 0x07, 0x0B, 0x05, 0x00, 0x09, 0x1A, 0x05, 0x01, 0x04, 0x01, 0x09, 0x04, 0x01, 0x1C, 0x1D, 0xBC, 
	# 0x05, 0x00, 0x04, 0x01, 0x09, 0x04, 0x00, 0x1C, 0x1D, 0xA8, 
# 0x04, 0x01, 0x06, 0x00, 0x05, 0x00, 0x04, 0x2A, 0x16, 0x34, 
for i in range(1, 42):	
# 0x05, 0x00, 0x04, 0x02, 0x0D, 0x04, 0x00, 0x14, 0x0F, 
	if i % 2 == 0:
		# arr[i] += arr[i-1] 
		# 注意还会进行高位舍去
		arr[i] = (arr[i] + arr[i-1]) & 0xff
# arr3 ==> arr4  (i % 2 == 0)
	# push i 
	# vm_stack[vm_sp-1] = vm_arr[vm_stack[vm_sp-1]]
			# var1 = arr[i]

	# push i 
	# push  0x01, 
	# BINARY_SUBTRACT
			# i - 1

	# vm_stack[vm_sp-1] = vm_arr[vm_stack[vm_sp-1]]
			# var2 = arr[i-1]

	# BINARY_ADD
			# var2 += var1

	# push i 
	# vm_arr[vm_stack[vm_sp]] = vm_stack[vm_sp-1] 
			# arr[i] = var2

	# push i 
	# opcode
	# 0x05, 0x00, 0x19, 0x05, 0x00, 0x04, 0x01, 0x0A, 0x19, 0x09, 0x05, 0x00, 0x1A, 
	
# 0x05, 0x00, 0x04, 0x02, 0x0D, 0x04, 0x01, 0x14, 0x0B, 
	if i % 2 == 1:
		arr[i] = (arr[i] * 0x6b) & 0xff
# arr3 ==> arr4  (i % 2 == 1)
	# push 0x6B, 
	# push i
	# vm_stack[vm_sp-1] = vm_arr[vm_stack[vm_sp-1]]
		# var = arr2[i]
	# BINARY_MULTIPLY, 
		# var *= 0x6b
	# push i
	# vm_arr[vm_stack[vm_sp]] = vm_stack[vm_sp-1], 
		# arr[i] = var
	# push i
	# push  0x01, 
	# BINARY_ADD, 
	# push  0x00, 
	# vm_block[vm_stack[vm_sp]] = vm_stack[vm_sp-1], 
		# i += 1
	# jump  $ -  53   回跳 形成循环。 回到ln 99

	# opcode 
	# 0x04, 0x6B, 0x05, 0x00, 0x19, 0x0B, 0x05, 0x00, 0x1A, 0x05, 0x00, 0x04, 0x01, 0x09, 0x04, 0x00, 0x1C, 0x1D, 0xCA, 
for i in range(0x29):
	if arr[i] != arr1[i] :
		print('n')
		return 0
	print('y')
	return 0
	# 最后的判断位置了。
# check

	# push 0x00, 
	# vm_block[0] = vm_stack[vm_sp] 
	# push i
	# push 0x29, 
	# if  v0x29 < i:
	# 		jump $ + 27, 

	# push i
	# vm_stack[vm_sp-1] = vm_arr[vm_stack[vm_sp-1]]
	# push 0x32, 
	# push i
	# BINARY_ADD
	# vm_stack[vm_sp-1] = vm_arr[vm_stack[vm_sp-1]] 
	#  if  vm_stack[vm_sp] == vm_stack[vm_sp-1]:
	#  			jump $+0x0C, 
	# push i
	# push 0x01, 
	# BINARY_ADD
	# push 0x00, 
	# vm_block[vm_stack[vm_sp]] = vm_stack[vm_sp-1]
					# i += 1
	# 		jump $ -26,  回跳构成循环，到ln 160的位置

	# push 0x6E, 'n'
	# 0x02, print
	# 0x1E, return 
	# push 0x79, 'y'
	# 0x02, print
	# 0x1E return 

	# opcode ::
	# 0x04, 0x00, 0x06, 0x00, 0x05, 0x00, 0x04, 0x29, 0x18, 0x04, 
	# 0x1D, 0x1B, 
	# 0x05, 0x00, 0x19, 0x04, 0x32, 0x05, 0x00, 0x09, 0x19, 0x14, 0x0C, 0x05, 0x00, 0x04, 0x01, 0x09, 0x04, 0x00, 0x1C, 
	# 0x1D, 0xE5, 0x04, 0x6E, 0x02, 0x1E, 0x04, 0x79, 0x02, 0x1E