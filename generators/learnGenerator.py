def listcomprehension_style_generator():
	doubles = list(2 * n for n in range(50))
	print doubles

def genarators_using_yield(till):
    current_num = 0
    while current_num < till:
        yield current_num
        current_num += 1


listcomprehension_style_generator()	

for value in genarators_using_yield(10):
	print(value)