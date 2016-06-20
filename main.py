import requests

with requests.Session() as s:

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