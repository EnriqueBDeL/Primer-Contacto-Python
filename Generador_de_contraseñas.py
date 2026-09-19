import gradio as gr
import random as r

minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["+", "-", "*", "@", "%", "&"]

def generar_contrasena(cantidad_letras,cantidad_numeros,cantidad_simbolos):

    resultado = ""

    for _ in range(cantidad_letras):
        resultado = resultado + r.choice(minusculas)

    for _ in range(cantidad_numeros):
        resultado = resultado + r.choice(numeros)

    for _ in range(cantidad_simbolos):
        resultado = resultado + r.choice(simbolos)

    return resultado

aplicacion = gr.Interface(
    fn=generar_contrasena,
    inputs=[
        gr.Slider(minimum=1, maximum=15, step=1, value=6, label="Cantidad de Letras"),
        gr.Slider(minimum=0, maximum=10, step=1, value=2, label="Cantidad de Números"),
        gr.Slider(minimum=0, maximum=10, step=1, value=2, label="Cantidad de Símbolos")
    ],
    outputs="text",
    title="Mi Generador de Contraseñas",
    description="Genera tu contraseña. Esta app colocará siempre primero las letras, luego los números y por último los símbolos.",
    submit_btn="Generar",
    clear_btn="Borrar",
    flagging_mode="never"
)

aplicacion.launch()
