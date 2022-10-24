from PySimpleGUI import  PySimpleGUI as sg


class screenCadastroNF:
    def __init__(self):
        sg.theme('DarkBlue12')
        layout = [
            [sg.Image(filename='logo.png')],
            [sg.Text('Nota Fiscal', size=(10,0)), sg.Input(size=(15,0), key='nf'),
            sg.Text('Frota', size=(10,0)), sg.Input(size=(15,0), key='frota')],
            [sg.Text('Fornecedor', size=(10,0)), sg.Input(size=(15,0), key='fornecedor'), 
            sg.Text('Responsavel', size=(10,0)), sg.Input(size=(15,0), key='responsavel')],
            [sg.Text('Qual Departamento?')],
            [sg.Radio('Saude', 'dep', key='saude'), sg.Radio('Educação', 'dep',  key='educação'), sg.Radio('Outros', 'dep', key='outros')],
            [sg.Text('Viagem?')],
            [sg.Radio('Sim', 'Viagem', key='viagem'), sg.Radio('Nao', 'Viagem', key='naoViagem')],
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
                nf = self.values['nf']
                frota = self.values['frota']
                fornecedor = self.values['fornecedor']
                responsavel = self.values['responsavel']
                saude = self.values['saude']
                educação = self.values['educação']
                outros = self.values['outros']
                viagemSim = self.values['viagem']
                viagemNao = self.values['naoViagem']
                print(f'NF: {nf}')
                print(f'Frota: {frota}')
                print(f'Fornecedor: {fornecedor}')
                print(f'Responsavel: {responsavel}')
                print(f'Saude: {saude}')
                print(f'Educação: {educação}')
                print(f'Outros: {outros}')
                print(f'Viagem: {viagemSim}')
                print(f'Não é de viagem: {viagemNao}')

tela = screenCadastroNF()
tela.iniciarAuto()