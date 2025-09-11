from code import interact
from fastapi import UploadFile
import gradio as gr

def count_word(uploadfile):
    try:
        with open(uploadfile, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return(f"Total number of words: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{uploadfile}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


interface = gr.Interface(
        fn=count_word,
        inputs=gr.File(label="Upload a Text File"),
        outputs=gr.Textbox(label="Word Count")
)

interface.launch()