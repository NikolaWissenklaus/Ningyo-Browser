import PySimpleGUI as sg
import requests
import base64
import os

#http://192.168.15.103:5000

tela = []

interface = [
    [
        sg.Input(
            '',
            key='linkBuscado',
            size=(110, 10)
        ), 
        sg.Button(
            'Buscar', 
            key='buscarLink'
        )
    ],
    [sg.Column([[sg.Text('',size=(2,0))]], key="rrrrrrrr")],
    [sg.Column(
      tela, 
      scrollable=True,  
      vertical_scroll_only=True,
      background_color="White", 
      size=(900, 500),
      key="mainC"
    )]
]
#Conversor recursivo de json > sg obj
imagens = []
def convertInter(obj):
    listaFinal = []
    for linha in obj:
        l = []
        e = []
        for elemento in linha:
            if elemento[0] == "column":
                e = sg.Column(
                    convertInter(elemento[1]["conteudo"]),
                    size=(elemento[1]["size"][0],elemento[1]["size"][1]),
                    background_color=elemento[1]["background_color"]
                )
            if elemento[0] == "image":
                e = sg.Image(elemento[1]["filename"])
                imagens.append(elemento[1]["filename"])
            if elemento[0] == "button":
                e = sg.Button(
                    elemento[1]["texto"], 
                    button_color=elemento[1]["button_color"],
                    size=(elemento[1]["size"][0],elemento[1]["size"][1]),
                    key=elemento[1]["key"]
                )
            if elemento[0] == "text":                
                e = sg.Text(
                    text=elemento[1]["texto"],
                    text_color=elemento[1]["text_color"], 
                    background_color=elemento[1]["background_color"],
                    size=(elemento[1]["size"][0],elemento[1]["size"][1])
                )
            l.append(e)
        listaFinal.append(l)
    return listaFinal

def update_tela(linkTela):
    global window
    response = requests.get(linkTela)
    novaTela = response.json()
    novaTela = convertInter(novaTela)
    interface = [
        [
            sg.Input(
                '',
                key='linkBuscado',
                size=(110, 10)
            ), 
            sg.Button(
                'Buscar', 
                key='buscarLink'
            )
        ],
        [sg.Column([[sg.Text('',size=(2,0))]], key="rrrrrrrr")],
        [sg.Column(
        novaTela if len(novaTela)>=1 else [],
        scrollable=True,  
        vertical_scroll_only=True,
        background_color="White", 
        size=(900, 500),
        key="mainC"
        )]
    ]
    if len(imagens) >= 1:
        for i in imagens:
            lt = "http://" + linkTela.split("http://")[1].split("/")[0]
            response = requests.get(lt+"/imagem",params={"img": i})
            arquivo = response.json()
            f = open(i, 'wb')
            f.write(base64.b64decode(arquivo["arq"].encode()))
            f.close()

    window.close()

    window = sg.Window(
    'Ningyo',
    size=(900, 500)
    ).Layout(interface)

window = sg.Window('Ningyo',size=(900, 500)).Layout(interface)

while True:
    event, values = window.read() 
    if event == sg.WIN_CLOSED:
        break
    if event == "buscarLink":#layout
        if len(values["linkBuscado"].strip()) > 0:
            update_tela(values["linkBuscado"])
    if event.split("-")[0] == "changeLink":#layout
        if len(event.split("-")[1].strip()) > 0:
            update_tela(event.split("-")[1])

for imgD in os.listdir(os.getcwd()):
    try:
        if not imgD == "ningyo.py":
            os.remove(imgD)
    except:
        pass
window.close()

