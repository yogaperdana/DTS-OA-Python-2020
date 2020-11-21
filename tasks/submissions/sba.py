email = 'yogapp@gmail.com'

def fungsiIO():
	getin = input('Masukkan barisan angka dan pisahkan dengan spasi: ')
	if getin != '':
		listin = sorted(list(map(int, getin.split(' '))))
		for i in range(len(listin)):
			print(*['*' for n in range(listin[i])], sep='')

def caseShopia(txt):
	return ''.join([(txt[i].upper() if txt[i].islower() else txt[i].lower()) for i in range(len(txt)) if txt[i].isalpha()])

dcur2idr = {'USD': 14425, 'EUR': 16225, 'AUD': 9925, 'CAD': 10500, 'GBP': 17800, 'CHF': 15200, 'SGD': 10375, 'HKD': 1775, 'JPY': 132500, 'MYR': 3250, 'SAR': 3500, 'WON': 10750, 'IDR': 1}

def usd2eur(usd):
	return float(usd * dcur2idr['USD'] / dcur2idr['EUR'])

class MoneyChanger:
	def __init__(self, dcurrency, base='IDR', percent=2):
		self.dcurrency = {item: float(dcurrency[base] / dcurrency[item]) for item in dcurrency}
		self.base = base
		self.percent = percent
		
	def selling_price(self, nominal, curr):
		return float((nominal * self.dcurrency[self.base] / self.dcurrency[curr]) * ((100 + self.percent) / 100))
	
	def buying_price(self, nominal, curr):
		return float((nominal * self.dcurrency[self.base] / self.dcurrency[curr]) * ((100 - self.percent) / 100))

	def change_base(self, new_base):
		self.base = new_base
