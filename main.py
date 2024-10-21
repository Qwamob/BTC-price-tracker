import requests
import tkinter as tk
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


times = []
prices = []

def update_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        data = response.json()

        price = data["bpi"]["USD"]["rate_float"]  
        updated_time = data["time"]["updated"]

        
        current_time = datetime.now().strftime('%H:%M:%S') 
        times.append(current_time)
        prices.append(price)

       
        labelPrice.config(text="Price: $" + str(round(price, 2)) + "\nUpdated at: " + updated_time)

        
        update_graph()

    except Exception as e:
        labelPrice.config(text="Error fetching data")

    
    canvas.after(10000, update_price)

def update_graph():
    
    ax.clear()

    
    ax.plot(times, prices, marker='o', linestyle='-', color='b')

    
    ax.set_title("Bitcoin Price Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price (USD)")

    if len(times) > 1:
        ax.set_xticks([times[0], times[-1]])  
        ax.set_xticklabels([times[0], times[-1]], rotation=45, ha='right')

    
    graph_canvas.draw()

canvas = tk.Tk()
canvas.geometry("800x800")
canvas.title("BTC Price Tracker")

# Font styles
f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(canvas, text="BTC Price", font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)


fig, ax = plt.subplots(figsize=(5, 4), dpi=100)

graph_canvas = FigureCanvasTkAgg(fig, master=canvas)
graph_canvas.get_tk_widget().pack()

update_price()
canvas.mainloop()
