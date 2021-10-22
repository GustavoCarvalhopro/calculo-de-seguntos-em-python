seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = seg//60//60//24
horas = (seg//60//60)%24
minutos = (seg//60)%60
segundos = seg%60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
