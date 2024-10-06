import tkinter as tk
from dataclasses import dataclass



def Button_Clicked():
    print("Button Clicked")
    print(var.get())

window = tk.Tk()
window.minsize(400, 400)
window.title("Subnet Calculator")
#  -- Widget  --  #
"Do not move the frame over the Tk window."
frame = tk.Tk()
greeting = tk.Label(frame,text="Hello, This is a subnet calculator\n"
                                      "This is a basic project to calculate the subnet of a given IP address\n"
                                      "İf you want upgrade this project, you can contact me via email:emirgundayy@gmail.com",
                                      foreground="white",
                                      background="black",
                                      width=100,
                                      height=10)
greeting.pack()
frame.mainloop
"If you are reading this, don't make the same mistake I made in this stupid code. "
"I couldn't get the correct data from the radiobox because I didn't open the widget as a separate frame from the beginning. (Im not sure about that)"
"It was solved with just 2 lines, I feel both happy and stupid at the same time. Don't make the same mistake."
# -- End  -- #


frame1 = tk.Frame(window)
frame1.pack()
tk.Label(frame1, text="IP address").grid(row=0, column=0)

var = tk.IntVar()
frame2 = tk.LabelFrame(window, text='Don\'t be greedy.')
frame2.pack()
tk.Radiobutton(frame2, text='Any Class', variable=var, value=1).grid(row=0, column=0)
tk.Radiobutton(frame2, text='Class A', variable=var, value=2).grid(row=0, column=1)
tk.Radiobutton(frame2, text="Class B", variable=var, value=3).grid(row=1, column=0)
tk.Radiobutton(frame2, text="Class C", variable=var, value=4).grid(row=1, column=1)

name_TF = tk.Entry(frame1)
name_TF.grid(row=0, column=1)

tk.Button(frame2, text="Submit", command=Button_Clicked, padx=50, pady=5).grid(row=2, column=0, columnspan=2, pady=5)

window.mainloop()