#Calculator App
from cProfile import label
import gradio as gr
#from gradio import Interface

def calculator(number1, number2, operation):
    
    if operation == "Addition":
        return number1 + number2
    elif operation == "Subtraction":
        return number1 - number2
    elif operation == "Multiplication":
        return number1 * number2
    elif operation == "Division":
        if number2 != 0:
           return number1 / number2
        else: 
            return "Error: Divison by zero"


interface = gr.Interface(
    fn=calculator,
    inputs=[
        gr.Number(label="First Number"),
        gr.Number(label="Second Number"),
        gr.Dropdown(choices=["Addition",
                             "Subtraction",
                             "Multiplication",
                             "Division"], label="Operation")
    ],
    outputs = gr.Number(label="Result")
)

interface.launch()