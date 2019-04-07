products = []
while True:
	name = input('請輸入商品名稱：')
	if name =='q':
		break
	price = input('請輸入商品價格：')
	p = []
	p.append(name)
	p.append(price)   #可以寫成 p = [name, price]
	products.append(p)
	#可以簡化成 products.append([name, price])  就不用7-10行
print(products)

