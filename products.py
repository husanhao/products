# Read File
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if 'Product, Price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])	
print(products)

# Enter Data
while True:
	name = input ('Please enter product name: ')
	if name == 'q':
		break
	price = input ('Please enter product price: ')
	price = int(price)
	products.append([name, price])
print(products)

# Print Data
for p in products:
	print(p[0], 'price is', p[1])

# Write File
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Product, Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
