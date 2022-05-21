from math import floor
saque=float(input('Valor do Saque: '))
div100=floor(saque/100)
div50=floor((saque-100*div100)/50)
div20=floor((saque-(div100*100+div50*50))/20)
div10=floor((saque-(div100*100+div50*50+div20*20))/10)
print("Entregar {} Notas de R$ 100, {} Notas de R$ de 50, {} Notas de R$ de 20 ,{} Notas de 10".format(div100,div50,div20,div10))