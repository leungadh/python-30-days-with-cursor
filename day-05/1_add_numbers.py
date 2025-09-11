import gradio as gr

def add_numbers(a, b):
    return a + b

#gr.Interface(fn=add_numbers, inputs=["number", "number"], outputs="number").launch()

interface = gr.Interface(fn=add_numbers, 
        inputs=[gr.Number(label="First Number"), gr.Number(label="Second Number")], 
        outputs=gr.Number(label="Sum"),
        title="Add Numbers",
        description="Add two numbers together",
        theme="dark",
        examples=[
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10]])

interface.launch()