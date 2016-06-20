import requests


# Эта часть...
payload = {
	'j_password': 'здесь_действительный_пароль',
	'j_username': '7273731365',
	'sSubmit': 'ВХОД В КАБИНЕТ',
	'AuthType': '2',
	'form': '1'
}

with requests.Session() as s:
	
	# p = s.post('http://telecom.kz/auth20/login', data=payload)
	# if(p.json()['success']==True):
	# 	print('Hello!')
	# else:
	# 	print(p.json()['errors']['j_username'])

	d = {
		'phone': '7273731365'
	}

	cookies = {

		'session_name': 'rl1c304oll5gckrv9pgaj93dg7',
		'ym_uid': '1465230994695002506',
		'_gat': '1',
		'_ym_isad': '2',
		'_ym_visorc_26106261': 'w',
		'type_closed': 'b9e3304650de7b49cf876f1264ddd78ede238f69%7E0',
		'_ga': 'GA1.2.1500074302.1465230992'

	}


	p = s.post('http://telecom.kz/ajax/pay/phonedata', data = d, cookies=cookies)
	print(p.text)

	# p1 = s.post('http://telecom.kz/ajax/account/get_account_balance', cookies=p.cookies)

	# print("-------------------------")
	# # print(p.cookies['session_name'])
	# print(p1.text)

# payload = {
# 	'email': 'ura2178@gmail.com',
# 	'amount': '-2493.37',
# 	'guid': '1-',
# 	'phone': '727373136',
# 	'pay_type': 'phone'
# }

# with requests.Session() as s:
# 	p = s.get('http://telecom.kz/ajax/pay/create_order', data = payload)

# print(p.text)