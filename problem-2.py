current_num = 1
prev_num = 1
total = 0

while current_num <= 4000000:
	
	current_num = current_num + prev_num
	prev_num = current_num - prev_num

	if current_num % 2 == 0:
		total += current_num

print(total)