import json
import PySimpleGUI as sg

#--------------------------------------------
#Objeto desenvolvido
obj = [
    [sg.Column(
      [
        [
          sg.Button(
            "Home", 
            button_color="Green",
            size=(12, 1),
            key='changeLink-http://192.168.15.103:5000'
          ),
          sg.Text('', size=(1,1), text_color="Black",background_color="Black" ),
          sg.Button(
            "Sobre", 
            button_color="white on red",
            size=(12, 1),
            key='changeLink-http://192.168.15.103:5000/sobre',

          ),
          sg.Text('', size=(1,1), text_color="Black",background_color="Black" ),
          sg.Button(
            "Abacate", 
            button_color="black on yellow",
            size=(12, 1),
            key='changeLink-http://192.168.15.103:5000/abacate'
          ),
          sg.Text('', size=(1,1), text_color="Black",background_color="Black" ),
          sg.Button(
            "Sei lá", 
            button_color="white on blue",
            size=(12, 1),
            key='changeLink-http://192.168.15.103:5000/seila'
          )
        ]
      ],
      size=(845,40),
      background_color="Black")
     ],
    [sg.Column(
        [
        ],
        size=(600,450),
        background_color="Light Gray"
    )],
    [sg.Column([],size=(845,1),background_color="Black")],
    [sg.Text(
            'By: N. Wissenklaus',
            text_color="Black",
            background_color="White" ,
            size=(50,1)
        )
    ]
]

#--------------------------------------------

#--------------------------------------------
#Formatadores de objetos
def formatColumn(cSize,cBC,cRow):
  return {
    "size": cSize,
    "background_color": cBC,
    "conteudo": cRow
  }

def formatImage(iFile):
  return {"filename": iFile}

def formatButton(btn, btnC, btnS, btnK):
  return {
    "button_color": btnC,
    "size": btnS,
    "key": btnK,
    "texto": btn
  }

def formatText(txt, txtC, txtS, txtBC):
  return {
      "text_color": txtC,
      "size": txtS,
      "texto": txt,
      "background_color": txtBC
    }

#--------------------------------------------

#--------------------------------------------
#Conversor recursivo de sg obj > json
def convertEs(tela):
  listaFinal = []
  for linha in tela:
    l = []
    e = []
    for elemento in linha:
      if elemento.Type == "column":
        et = "column"
        atr = formatColumn(
          [elemento.Size[0],elemento.Size[1]],
          elemento.BackgroundColor,
          convertEs(elemento.Rows)
        )
        e = [et,atr]
      if elemento.Type == "image":
          et = "image"
          atr = formatImage(elemento.Filename)
          e = [et,atr]
      if elemento.Type == "button":
          et = "button"
          atr = formatButton(
            elemento.ButtonText, 
            elemento.ButtonColor, 
            [elemento.Size[0],elemento.Size[1]], 
            elemento.Key
          )
          e = [et,atr]
      if elemento.Type == "text":
          et = "text"
          atr = formatText(
              elemento.DisplayText, 
              elemento.TextColor, 
              [elemento.Size[0],elemento.Size[1]], 
              elemento.BackgroundColor
            )
          e = [et,atr]
      l.append(e)
    listaFinal.append(l)
  return listaFinal

#--------------------------------------------

#--------------------------------------------
#Salva o modelo
convertido = convertEs(obj)
nomeArquivo = input("arquivo> ")
nomeArquivo += ".json"
f = open(nomeArquivo, "w")
f.write(json.dumps(convertido))
f.close()

#--------------------------------------------