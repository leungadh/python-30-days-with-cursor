import gradio as gr

def your_choice(option):
    if option == "Chinese":
        return "You should try Li's Garden"
    elif option == "Western":
        return "McDonald is your Favorite!"
    elif option == "India":
        return "LiLa is not a bad choice!"
    elif option == "Asian":
        return "Try the Haina Chicken Rice."


interface = gr.Interface(
        fn=your_choice,
        inputs=gr.Radio(
            choices=["Chinese","Western","India","Asian"],
            label="Which type of crusine do you like?"
        ),
        outputs=gr.Textbox(label="You Choose:")
)

interface.launch()