# AND                        # OR                           # NO
# false + false = false      # false + false = false        # true  = false 
# true  + false = false      # true  + false = true         # false = true 
# false + true  = false      # false + true  = true 
# true  + true  = true       # true  + true  = true

# Dica: crtl + k + c para comentar tudo


# AND
idade = 15
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode participar do evento? ' + str(resultado)

print(msg)


# OR
# Programa de disparo de alarme
porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = ('Alarme disparado? ' + str(alarme))
print(msg)

# NO
tem_dinheiro = False
tem_dinheiro = not tem_dinheiro
msg = 'Tem dinheiro? ' + str(tem_dinheiro)
print(msg)