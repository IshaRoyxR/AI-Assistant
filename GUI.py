from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#71E809")

# ask function
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User ---> ' + user_val + "\n")
    if bot_val is not None:
        text.insert(END, "Bot  <--- " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

# delete function
def delete_text():
    text.delete("1.0", "end")

# send function
def send():
    send_val = entry.get()
    bot_val = action.Action(send_val)
    text.insert(END, "Me   ---> " + send_val + "\n")
    if bot_val is not None:
        text.insert(END, "Bot  <--- " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

# Configure columns
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Frame for heading and image
Frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raise", bg="#71E809")
Frame.grid(row=0, column=1, pady=20)

# Title label
text_label = Label(Frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#71E809")
text_label.grid(row=0, column=0, columnspan=3, pady=10)

# Load and resize image
image_path = "image/assistant.jpeg"
original_image = Image.open(image_path)
resized_image = original_image.resize((300, 300), Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(resized_image)

# Image label
image_label = Label(Frame, image=image, bg="#71E809")
image_label.image = image
image_label.grid(row=1, column=1, pady=10)

# Text box
text = Text(root, font=('courier 10 bold'), bg="#15BE0D")
text.place(x=100, y=420, width=375, height=100)

# Entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=535, width=350, height=30)

# Ask Button
Button1 = Button(root, text="ASK", bg="#15BE0D", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=590)

# Delete Button (fixed name)
Button2 = Button(root, text="Delete", bg="#15BE0D", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete_text)
Button2.place(x=220, y=590)

# Send Button (fixed name)
Button3 = Button(root, text="Send", bg="#15BE0D", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button3.place(x=380, y=590)

root.mainloop()
