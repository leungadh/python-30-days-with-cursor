import gradio as gr

def your_choice(selected):
    if selected:
            return f"You've chosen: {','.join(selected)}"
    else:
            return "You didn't select any crusine"


interface = gr.Interface(
        fn=your_choice,
        inputs=gr.CheckboxGroup(
            choices=["Chinese","Western","India","Asian"],
            label="Which type of crusine do you like?"
        ),
        outputs=gr.Textbox(label="You Choose:")
)

interface.launch()