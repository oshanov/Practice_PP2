import re


products = list()
amount = None
time = None
me1hod = None
with open('raw.txt', encoding='utf-8') as file:
    for i in file:
        i = i.rstrip()

        if re.match('ИТОГО:', i):
            amount = next(file).strip()
            
        if re.match(r'\d+\.$', i):
            need = next(file).strip()
            products.append(need)

        if re.search(r'Время: (\d{2}\.\d{2}\.\d{4}\s\d{2}\:\d{2}\:\d{2})', i):
            time = i
        




prices = set()
with open("raw.txt", encoding="utf-8") as f:
    for i in f:
        i = i.rstrip()
    
        found = re.findall(r'x (\d[\d ]+,\d{2})', i)
        for j in found:
            prices.add(j)
        
        if re.search('Наличный расчёт: ', i) or re.search('Банковская карта:', i):
            me1hod = i[:len(i)-1]


   
print("Стоимость товаров:")
for price in prices:
    print("-", price)
    
print("Наименования товаров:")
for product in products:
    print("-", product)

print('Общая стоимость покупки:', amount)

print(time)

print("Метод оплаты -", me1hod)




