import PySimpleGUI as sg

#home
objHome = [
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
    [sg.Image('im.png')],
    [sg.Column(
        [
            [sg.Column([],size=(500,25),background_color="Light Gray")],
            [sg.Text(
                """Teste """,
                text_color="Black",
                background_color="Light Gray",
                size=(550,400)
            )]
        ],
        size=(600,450),
        background_color="Light Gray"
    ),
    sg.Column(
        [],
        size=(235,400),
        background_color="Blue"
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

#sobre
objSobre = [
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
            [sg.Column([],size=(500,25),background_color="Light Gray")],
            [sg.Text(
                """
                Criador: Nikola Wissenklaus;
                Nome: Ningyo;
                Tipo: Browser;
                Versão: 1.0
                Diferencial: Não usa HTML ou CSS, usa json + PySimpleGUI;
                Inspiração: Vozes da minha cabeça;
                """,
                text_color="Black",
                background_color="Light Gray",
                size=(550,400)
            )]
        ],
        size=(840,450),
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

#abacate
objAbacate = [
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
            [sg.Image('aba.png')]
        ],
        size=(660,450),
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

#seila
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
    [sg.Column(obj, scrollable=True,  vertical_scroll_only=True, size=(900, 500), background_color="White")]
]

window = sg.Window(
    'Ningyo', 
    interface, 
    size=(900, 500)
)

while True:

    event, values = window.read() 
    if event == sg.WIN_CLOSED:
        break
    print(event)
    print(values)

window.close()
