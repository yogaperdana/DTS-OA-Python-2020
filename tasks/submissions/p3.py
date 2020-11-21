priority = 0
email = 'yogapp@gmail.com'

def caesar_encript(txt, shift):
	result = ''
	for i in range(len(txt)):
		if txt[i].isalpha():
			alpha = 'a' if txt[i].islower() else 'A'
			result += chr((ord(txt[i]) + shift - ord(alpha)) % 26 + ord(alpha))
		else:
			result += txt[i]
	return result

def caesar_decript(chiper, shift):
	return caesar_encript(chiper, -shift)

def shuffle_order(txt, order):
	return ''.join([txt[i] for i in order])

def deshuffle_order(sftxt, order):
	txt = list(sftxt)
	for i in range(len(order)):
		txt[order[i]] = sftxt[i]
	return ''.join(txt)

def send_batch(txt, batch_order, shift=3):
	encrypted = caesar_encript(txt, shift)
	text_length = len(txt)
	batch_length = len(batch_order)
	batches = []
	for i in range(0, len(encrypted), batch_length):
		i_max = i + batch_length
		batch = encrypted[i:i_max]
		if i_max > text_length:
			batch += '_' * (i_max - text_length)
		batches.append(shuffle_order(batch, batch_order))
	return batches

def receive_batch(batch_cpr, batch_order, shift=3):
	batch_txt = [caesar_decript(deshuffle_order(i, batch_order), shift) for i in batch_cpr]
	return ''.join(batch_txt).strip('_')
