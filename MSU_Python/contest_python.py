inp=input().split()
amount=int(inp[0])
period=int(inp[1])*12
rate=float(inp[2])/12

labels=[]
labels.append('Месяц')
labels.append('Сумма на вкладе')
labels.append('Начислениe')

with open('output.csv', 'w') as csv_file:
	print(f'{labels[0]},{labels[1]},{labels[2]}',file=csv_file)
	for i in range(1,period+1):
		income=amount*rate*0.01
		amount+=income
		print(f'{i},{amount:.2f},{income:.2f}',file=csv_file)