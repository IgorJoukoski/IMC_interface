import PySimpleGUI as sg


sg.theme('DarkTeal9')

layout = [
    [sg.Text("IMC")],
    [sg.Text("Altura "),sg.Input(key='-MASS-',size=(5,1))],
    [sg.Text("Massa "),sg.Input(key='-HIGH-',size=(5,1))],
    [sg.Push(),sg.Button('Calcular') , sg.Push()]
  ] 

window = sg.Window ("IMC", layout=layout,font="Calibri 17")

while True:
  event, value = window.read()
  print(event,value)
  massa=float(value['-MASS-'])
  altura=float(value['-HIGH-'])
  imc = massa / (altura**2)
  sg.Popup(f'Seu imc é {imc:.2f}', font='26')
  if event == 'QUIT' or event == sg.WIN_CLOSED:
      break
    
