'''
Projeto Integrador I => Calculadora de Gasto Energético Basal
'''

def gastoEnergetico(p):

        sexo = input('Você é:\nHomem (H)\nMulher (M)\n[H/M]?: ').upper()

        while sexo != 'H' and sexo != 'M':
                print('\n<<<ERRO: Sexo inválido, digite H ou M>>>\n')
                sexo = input('Você é:\nHomem (H)\nMulher (M)\n[H/M]?: ').upper()

        idadeValida = False
        while not idadeValida:
                try:
                        idade = int(
                                input('\nFavor, digite sua idade: ')
                        )
                        if idade <= 0:
                                print('<<<ERRO: Valor inválido, use APENAS números positivos>>>')
                        else:
                                idadeValida = True

                except ValueError:
                        print('<<<ERRO: Valor inválido, use APENAS números sem vírgula>>>')

        if (idade <= 3):
                if sexo == 'H':
                        gasto = (58.317 * p) - 31.1
                else:
                        gasto = (59.512 * p) - 30.4
        elif (3 < idade <= 10):
                if sexo == 'H':
                        gasto = (20.315 * p) + 485.9
                else:
                        gasto = (22.706 * p) + 504.3
        elif (10 < idade <= 18):
                if sexo == 'H':
                        gasto = (13.384 * p) + 692.6
                else:
                        gasto = (17.686 * p) + 658.2
        elif (18 < idade <= 30):
                if sexo == 'H':
                        gasto = (14.818 * p) + 486.6
                else:
                        gasto = (15.057 * p) + 692.2
        elif (30 < idade <= 60):
                if sexo == 'H':
                        gasto = (8.126 * p) + 845.6
                else:
                        gasto = (11.472 * p) + 873.1
        elif (idade > 60):
                if sexo == 'H':
                        gasto = (9.082 * p) + 658.5
                else:
                        gasto = (11.711 * p) + 587.7

        return gasto