email = 'yogapp@gmail.com'

class titik2d:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def ambiltitik(self):
		return (self.x, self.y)
	
	def tambahkan(self, titik):
		self.x += titik.x
		self.y += titik.y

def run():
	return titik2d(*tuple(map(int, input('Masukkan 2 angka, pisahkan dengan spasi: ').split(' '))))

if __name__ == '__main__':
	t1 = run()
	print('Titik 1:', t1.ambiltitik())
	t2 = run()
	t2.tambahkan(t1)
	print('Titik 2:', t2.ambiltitik())
