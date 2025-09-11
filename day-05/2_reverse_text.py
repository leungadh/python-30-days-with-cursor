from gradio import Interface

def reverse_text(text):
    return text[::-1]

interface = Interface(fn=reverse_text, inputs="text", outputs="text")
interface.launch()


"""Explanation:
text[::-1] uses Python slicing to reverse the string.
text[start:stop:step] is the general slicing format.
[::-1] means:
Start from the end of the string,
Move backwards one character at a time,
Until the beginning is reached."""