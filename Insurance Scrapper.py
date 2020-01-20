import requests
import json

if __name__ == "__main__":
	res = requests.get('https://www.ia.org.hk/en/supervision/reg_insurers_lloyd/insurers_list.php')
	data = json.loads(res.text)
	all_item = data['insurers']
	print(data)
	with open('test2.csv', 'w', encoding='utf_8_sig') as file:
		file.write("文件號碼,保險人姓名,註冊地點,業務類型,主要在香港業務,聯絡電話,傳真號碼,官方網站地址,電郵地址,注冊登記\n")
		for item in all_item:
			file.write("{},{},{},{},{},{},{},{},{},{}\n".format(
				item['no'],
				item['name'],
				item['place'],
				item["business"],
				item['address'],
				item['tel'],
				item['fax'],
				item['website'],
				item['email'],
				"https://www.ia.org.hk/tc/supervision/reg_insurers_lloyd/files/"+item['pdf']
				))
