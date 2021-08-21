import os

if __name__=='__main__':
    start()

# ======================================Funções Auxiliares==============================================
def finish():
    print(f'''{os.linesep}Espero ter te ajudado, até a pŕoxima!{os.linesep}''')


def continua(a):
    if a == '1':
            start()
    elif a == '2':
        finish()

    

def processar_resposta(resposta,nome):
    if resposta == '1':
        print(f'''{os.linesep}{nome}, Para solicitar certificado de Participação no PET, basta enviar um e-mail
         para pet_prograd@uece.br, informando Nome completo, Matrícula e a que grupo PET você
         pertence.{os.linesep}''')
        a = input(f'''{os.linesep}Digite 1 se deseja continuar e 2 se deseja parar: {os.linesep}''')
        continua(a)
        

    elif resposta == '2':
        print(f'''{os.linesep}{nome}, Para solicitar certificado de Participação no PROMAC, basta enviar um e-mail
         para promac_prograd@uece.br, informando Nome completo, Matrícula e nome da disciplina em
         que atuou.{os.linesep}''')
        a = input(f'''{os.linesep}Digite 1 se deseja continuar e 2 se deseja parar: {os.linesep}''')
        continua(a)
        

    else:
        print(f'''{os.linesep}No momento, temos apenas estas duas opções!{os.linesep}''')
        a = input(f'''{os.linesep}Digite 1 se deseja continuar e 2 se deseja parar: {os.linesep}''')
        continua(a)
    

# Apresentar o Chatbot
def start():
    print(f'''{os.linesep}Olá, seja bem vindo!''')
    # Pedir o nome
    nome = input('Digite o seu nome: ')
    # Pedir o e-mail
    email = input('Digite o seu E-mail: ')
    # Pedir resposta
    #loop = True
    #while True:
    resposta = input(
    f'''O que você deseja?{os.linesep}[1] - Solicitar o certificado PET?: 
    {os.linesep}[2] - Solicitar Certificado PROMAC?: ''')
    processar_resposta(resposta, nome)
    #    break
     