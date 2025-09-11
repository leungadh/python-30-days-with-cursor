import gradio as gr
from PIL import Image

def display_size(image):
    width=image.width
    height=image.height
    return(width,height)
    # try:
    #     with Image.open(image) as img:
    #         width, height = img.size
    #         print(f"Image dimensions of '{image}':")
    #         print(f"Width: {width} pixels")
    #         print(f"Height: {height} pixels")
    #         return(width,height)
    # except FileNotFoundError:
    #     print(f"Error: File '{image}' not found.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")



interface = gr.Interface(
        fn=display_size,
        inputs=gr.Image(type="pil",label="Upload a Text File"),
        outputs=[gr.Number(label="Width"),gr.Number(label="Height")]

)

interface.launch()