def recomendar_plano(consumo):
   
    if consumo <= 10:
        return 'Plano Essencial Fibra - 50Mbps'
    elif consumo <= 20:
        return 'Plano Prata Fibra - 100Mbps'
    else:
        return 'Plano Premium Fibra - 300Mbps'


consumo_usuario = float(input(' '))
plano_recomendado = recomendar_plano(consumo_usuario)
print(f' {plano_recomendado}')


