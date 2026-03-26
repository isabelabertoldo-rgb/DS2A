valor_hora = float(input("quanto voce ganha por hora?"))
horas_trabalhada = floar(input("quantas horas voce trabalhou nessa semana"))

if horas_trabalhadas>40:
    horas_extra = horas_trabalhada - 40
    pagamenti_extra = hora s_extra * (valor_hora * 1.5)
    total = (40 * valor_hora) + pagamenti_extra
    print (f"voce fez {horas_extra} horas_extra")
else:
    total = horas_trabalhadas * valor_hora
    print ("sem horas extras essa semana")

print (f"o valor bruto a reveber é: R$ {total}")
                          