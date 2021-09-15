from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(ind):
    inf_list = content.split('ID')
    for code in inf_list:
        if ind in code:
            return float(code.replace('/', '').split('<Value>')[-2].replace(',', '.'))


print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('GBP'))
print(currency_rates('vjefbvjb'))
