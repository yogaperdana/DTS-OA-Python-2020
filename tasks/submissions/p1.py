priority = 1
email = 'yogapp@gmail.com'

def letter_catalog(items, letter='A'):
	return [i for i in items if i.find(letter, 0, 1) != -1]

def counter_item(items):
	return {i: items.count(i) for i in items}

fruits = ['Apple', 'Avocado', 'Banana', 'Blackberries', 'Blueberries', 'Cherries', 'Date Fruit', 'Grapes', 'Guava', 'Jackfruit', 'Kiwifruit']
prices = [6, 5, 3, 10, 12, 7, 14, 15, 8, 7, 9]
chart = ['Blueberries', 'Blueberries', 'Grapes', 'Apple', 'Apple', 'Apple', 'Blueberries', 'Guava', 'Jackfruit', 'Blueberries', 'Jackfruit']

fruit_price = {fruits[n]: prices[n] for n in range(len(fruits))}

def total_price(dcounter, fprice):
	c = {k: (v * fprice[k]) for k, v in dcounter.items()}
	return sum(c.values())

def discounted_price(total, discount, minprice=100):
	if total >= minprice: total -= (discount / 100) * total
	return total

def print_summary(items, fprice):
	cart = counter_item(items)
	for item in sorted(cart):
		print(cart[item], item, ':', cart[item] * fprice[item])
	print('total :', total_price(counter_item(items), fprice))
	print('discount price :', discounted_price(total_price(counter_item(items), fprice), 10, minprice=100))
