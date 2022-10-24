from PySimpleGUI import  PySimpleGUI as sg

class screenMain:
    def __init__(self):
        sg.theme('DarkBlue12')
        layout = [
            [sg.Image(filename='logo.png')],
            [sg.Column([[sg.Text('',size=(23,0))]]), sg.Button('Entrada de Produtos', size=(18,3))],
            [sg.Column([[sg.Text('',size=(23,0))]]), sg.Button('Saida de Produtos', size=(18,3))],
            [sg.Column([[sg.Text('',size=(23,0))]]), sg.Button('Lançamento de notas fiscais', size=(18,3))],
            [sg.Button('Sair', size=(8,2))],
        ]

        self.janela = sg.Window('Main').layout(layout)
        

    def opcProdutos(self):
        while True:
                self.event, self.values = self.janela.read()

                if self.event == "Sair":
                    sg.WIN_CLOSED
                    break
                
                if self.event == "Lançamento de notas fiscais":
                    from screen import cadastro as cd
                    break
                    tela = cd.screenCadastroNF()
                    tela.iniciarAuto()
                    
                    

                if self.event == "Entrada de Produtos":
                    from screen import entProdutos
                    break


screen = screenMain()
screen.opcProdutos()