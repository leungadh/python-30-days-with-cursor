#Pick a number between 0 and 100
#Use a slider to pick a number
#Use a button to submit the number
#Use a label to display the number
#Use a slider to pick a number
#Use a button to submit the number
#Use a label to display the number

import gradio as gr

def square_number(number):
    return number * number  

interface = gr.Interface(fn=square_number, 
    inputs=gr.Slider(minimum=0, maximum=100, step=1, label="Number"), 
    outputs=gr.Number(label="Result"),
    title="Square a Number",
    description="Square a number between 0 and 100",
    theme="dark",
    examples=[
        [1],
        [2],
        [3],
        [4],
        [5]])

interface.launch()