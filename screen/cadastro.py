from PySimpleGUI import PySimpleGUI as sg
import pyautogui as ag
from time import sleep


def automatic(nf, frota, fornecedor, responsavel, saude, educacao, outros, viagemSim, qtd, data, preco, obs, km):
    # saindo do automatizador e indo para o programa
    sleep(2)
    ag.keyDown('alt')
    ag.press('tab', presses=2)
    ag.keyUp('alt')

    # clicando no inserir e iniciando novo lançamento
    sleep(2)
    ag.click(x=137, y=170)
    sleep(3)
    ag.press('tab', presses=3)
    ag.press('enter')
    ag.press('down')
    ag.press('enter')

    # Colocando informanções para o lançamento
    sleep(3)
    ag.write(data)
    sleep(1)
    # virificando departamento e viagem
    if (saude == True):
        if (viagemSim == True):
            nf = f'sf{nf}'
        else:
            nf = f'S{nf}'
    elif(educacao == True):
        if (viagemSim == True):
            nf = f'ef{nf}'
        else:
            nf = f'E{nf}'
    elif(outros == True):
        if (viagemSim == True):
            nf = f'of{nf}'
        else:
            nf = f'O0{nf}'

    ag.click(x=713, y=256)
    ag.click(x=574, y=257)
    ag.write(nf)
    sleep(2)
    ag.press('tab', presses=3)
    ag.write(fornecedor)
    ag.press('tab', presses=2)
    sleep(2)
    ag.write(frota)
    sleep(2)

    # mensagem para confirmar motorista e veiculo para proseguir
    msg = sg.popup_yes_no('Confirme o veiculo e selecione o motorista e clique em Yes')  # Shows Yes and No buttons
    # se for Yes o programa continua
    if (msg == 'Yes'):
        sleep(1)
        ag.keyDown('alt')
        ag.press('tab')
        ag.keyUp('alt')
        sleep(1)

        ag.press('tab')
        ag.hotkey('ctrl', 'a')
        ag.write(responsavel)
        sleep(1)
        ag.press('enter', presses=2)

        # entra na parte de produtos
        sleep(2)
        ag.write(qtd)
        ag.press('tab')
        ag.write(preco)

        # se for motossera
        if (frota == 'motosse'):
            ag.press('tab', presses=8)
            sleep(1)
            ag.write(obs)
            sleep(1)
            #sg.click(x=1057, y=948)
            print('moto')
            return
        
        # se tiver com KM quebrado
        if (km == 'Q' or km == 'q'):
            ag.press('tab', presses=8)
            sleep(1)
            ag.write('KM quebrado')
            #sg.click(x=1057, y=948)
            print('quebrado')

        # se tiver com ND KM
        if (km == 'ND' or km == 'nd'):
            ag.press('tab', presses=8)
            sleep(1)
            ag.write('ND KM')
            #sg.click(x=1057, y=948)
            print('nd km')
        
        # se for de viagem
        if (viagemSim == True):
            ag.press('tab', presses=6)
            ag.write(km)
            sleep(1)
            ag.press('tab', presses=2)
            ag.write(obs)
            #sg.click(x=1057, y=948)
            print('viagem')

        
        if (viagemSim == False):
            ag.press('tab', presses=6)
            ag.write(km)
            sleep(1)
            #sg.click(x=1057, y=948)
            print('sem viagem')


    else: # se não ele para o programa
        sg.WIN_CLOSED



class screenCadastroNF:
    def __init__(self):
        sg.theme('DarkBlue12')
        layout = [
            [sg.Column([[sg.Text('',size=(3,0))]]), sg.Image(filename='logo.png')],
            [sg.Text('Data', size=(10, 0)), sg.Input(size=(15, 0), key='data'),
            sg.Text('Observação', size=(10, 0)), sg.Input(size=(15, 0), key='obs'),
            sg.Text('Odometro', size=(10, 0)), sg.Input(size=(15, 0), key='km')],
            [sg.Text('Nota Fiscal', size=(10, 0)), sg.Input(size=(15, 0), key='nf'),
             sg.Text('Frota', size=(10, 0)), sg.Input(size=(15, 0), key='frota'),
             sg.Text('Quantidade', size=(10, 0)), sg.Input(size=(15, 0), key='qtd')],
            [sg.Text('Fornecedor', size=(10, 0)), sg.Input(size=(15, 0), key='fornecedor'),
             sg.Text('Responsavel', size=(10, 0)), sg.Input(size=(15, 0), key='responsavel'),
             sg.Text('Preço', size=(10, 0)), sg.Input(size=(15, 0), key='preco')],
            [sg.Text('Qual Departamento?')],
            [sg.Radio('Saude', 'dep', key='saude'), sg.Radio(
                'Educação', 'dep',  key='educação'), sg.Radio('Outros', 'dep', key='outros')],
            [sg.Text('Viagem?')],
            [sg.Radio('Sim', 'Viagem', key='viagem'), sg.Radio(
                'Nao', 'Viagem', key='naoViagem')],
            [sg.Button('Enviar dados')],
            [sg.Button('Sair')],

        ]
        self.janela = sg.Window('Lançamento de NFs').layout(layout)

    def iniciarAuto(self):
        while True:
            self.button, self.values = self.janela.Read()

            if self.button == "Sair":
                sg.WIN_CLOSED
                break

            if self.button == "Enviar dados":
                data = self.values['data']
                preco = self.values['preco']
                km = self.values['km']
                obs = self.values['obs']
                nf = self.values['nf']
                frota = self.values['frota']
                qtd = self.values['qtd']
                fornecedor = self.values['fornecedor']
                responsavel = self.values['responsavel']
                saude = self.values['saude']
                educacao = self.values['educação']
                outros = self.values['outros']
                viagemSim = self.values['viagem']
                automatic(nf, frota, fornecedor, responsavel, saude, educacao, outros, viagemSim, qtd, data, preco, obs, km)


tela = screenCadastroNF()
tela.iniciarAuto()
