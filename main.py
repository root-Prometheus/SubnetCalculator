import tkinter as tk
from dataclasses import dataclass
import re
import ipaddress

@dataclass
class IP:
    Ip: str
    Class: str
    Subnet: str
    Network_address: str
    Broadcast_address: str
    First_host: str
    Last_host: str
    Total_host: str


#def Button_Clicked():
    # ip = name_TF.get()
    # raw_ip = ip
    # ip = ip.replace("."," ")
    # data = re.split("\s",ip)
    # if var.get() == 0:
    #     Warning = tk.Label(frame1, text="Please select a class", foreground="red").grid(row=3, column=0, columnspan=2)
    # else:
    #     try:
    #         frame1.winfo_children()[2].destroy()
    #     except(IndexError):
    #         pass
    #     if var.get() == 1:
    #         try:
    #             slash_notation = re.split("/",data[3])
    #             IP.Class = slash_notation[1]
    #         except(IndexError):
    #             Warning = tk.Label(frame1, text="Please enter a valid subnet", foreground="red").grid(row=3, column=0, columnspan=2)
    #         if int(IP.Class) < 32:
    #             try:
    #                 frame1.winfo_children()[2].destroy()
    #             except(IndexError):
    #                 pass
    #             IP.Subnet = "255." * (int(IP.Class) // 8) + str(256 - (2 ** (8 - (int(IP.Class) % 8))))
    #             if int(IP.Class) // 8 < 4:
    #                 IP.Subnet = IP.Subnet + ".0" * (3 - int(IP.Class) // 8)
    #             raw_ip = raw_ip[:raw_ip.index('/')]
    #             ip_range = list(ipaddress.ip_network(str(raw_ip),(str("/"+slash_notation[1]))).hosts())
    #             print(ip_range)
    #         else:
    #             Warning = tk.Label(frame1, text="Please enter a valid subnet", foreground="red").grid(row=3, column=0, columnspan=2)


"I want that part without using ipaddress module"
"Because I want to learn how to do it manually"
"actually I did some part but not finished yet"
"so I will use ipaddress module for now"  

def Button_Clicked():
    ip = name_TF.get()
    try:
        try:
            for index,widget in enumerate(frame1.winfo_children()):
                if index > 1:
                    widget.destroy()
                else:
                    pass
        except(IndexError):
            pass
        if var.get() == 0:
            tk.Label(frame1, text="Please select a class", foreground="red").grid(row=3, column=0, columnspan=2)
            
        if var.get() == 1:
            ip_interface = ipaddress.ip_interface(ip)
            network = ip_interface.network
            IP_info = IP(
                Ip = str(ip_interface.ip),
                Class = str(network.network_address),
                Subnet = str(network.netmask),
                Network_address = str(network.network_address),
                Broadcast_address = str(network.broadcast_address),
                First_host = str(list(network.hosts())[0]),
                Last_host = str(list(network.hosts())[-1]),
                Total_host = str(network.num_addresses)
            )
        if var.get() == 2:
            if  int(ip[int(ip.find("/"))+1:]) >= 8:
                tk.Label(frame1, text="Please enter a valid subnet", foreground="red").grid(row=3, column=0, columnspan=2)
            ip_interface = ipaddress.ip_interface(ip)
            network = ip_interface.network
            IP_info = IP(
                Ip = str(ip_interface.ip),
                Class = str(network.network_address),
                Subnet = str(network.netmask),
                Network_address = str(network.network_address),
                Broadcast_address = str(network.broadcast_address),
                First_host = str(list(network.hosts())[0]),
                Last_host = str(list(network.hosts())[-1]),
                Total_host = str(network.num_addresses)
            )
        if var.get() == 3:
            if  int(ip[int(ip.find("/"))+1:]) >= 16:
                tk.Label(frame1, text="Please enter a valid subnet", foreground="red").grid(row=3, column=0, columnspan=2)
            ip_interface = ipaddress.ip_interface(ip)
            network = ip_interface.network
            IP_info = IP(
                Ip = str(ip_interface.ip),
                Class = str(network.network_address),
                Subnet = str(network.netmask),
                Network_address = str(network.network_address),
                Broadcast_address = str(network.broadcast_address),
                First_host = str(list(network.hosts())[0]),
                Last_host = str(list(network.hosts())[-1]),
                Total_host = str(network.num_addresses)
            )
        if var.get() == 4:
            if  int(ip[int(ip.find("/"))+1:]) >= 24:
                tk.Label(frame1, text="Please enter a valid subnet", foreground="red").grid(row=3, column=0, columnspan=2)
            ip_interface = ipaddress.ip_interface(ip)
            network = ip_interface.network
            IP_info = IP(
                Ip = str(ip_interface.ip),
                Class = str(network.network_address),
                Subnet = str(network.netmask),
                Network_address = str(network.network_address),
                Broadcast_address = str(network.broadcast_address),
                First_host = str(list(network.hosts())[0]),
                Last_host = str(list(network.hosts())[-1]),
                Total_host = str(network.num_addresses)
            )
        
        Info = {
                tk.Label(frame1, text=f"IP address: {IP_info.Ip}").grid(row=3, column=0, columnspan=2),
                tk.Label(frame1, text=f"Class: {IP_info.Class}").grid(row=4, column=0, columnspan=2),
                tk.Label(frame1, text=f"Subnet: {IP_info.Subnet}").grid(row=5, column=0, columnspan=2),
                tk.Label(frame1, text=f"Network address: {IP_info.Network_address}").grid(row=6, column=0, columnspan=2),
                tk.Label(frame1, text=f"Broadcast address: {IP_info.Broadcast_address}").grid(row=7, column=0, columnspan=2),
                tk.Label(frame1, text=f"First host: {IP_info.First_host}").grid(row=8, column=0, columnspan=2),
                tk.Label(frame1, text=f"Last host: {IP_info.Last_host}").grid(row=9, column=0, columnspan=2),
                tk.Label(frame1, text=f"Total host: {IP_info.Total_host}").grid(row=10, column=0, columnspan=2)
        }
    except ValueError:
        Warning = tk.Label(frame1, text="Invalid IP address or subnet!", foreground="red").grid(row=3, column=0, columnspan=2)


window = tk.Tk()
frame = tk.Tk()
window.minsize(400, 400)
window.title("Subnet Calculator")
#  -- Widget  --  #
"Do not move the frame over the Tk window."
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