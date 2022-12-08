import os
import time
import ctypes
import subprocess
import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt
from pyfiglet import Figlet

# Resize the terminal window
if os.name == "posix":
    subprocess.run(['resize', '-s', '22', '43'])
elif os.name == "nt":
    os.system("mode con: cols=43 lines=22")

# Rename terminal window
ctypes.windll.kernel32.SetConsoleTitleW("Power to the Players")

# Banner
custom_fig = Figlet(font='isometric1')
asci_banner = custom_fig.renderText("GME")

# Print the banner to the console
print(asci_banner + ("-" * 43) + "\n")

# Get the stock data for GameStop
gme = yf.Ticker("GME")

# Option Menu
print("1. Get the current price of GME.")
print("2. Get the historical data of GME.")
print("3. Plot the historical data of GME.")
print("4. View the GME DD library.")
print("5. Visit HQ r/Superstonk.")
print("6. Exit\n")

# Get the user's choice
choice = int(input("Enter your choice: "))

# Handle the user's choice
try:
    if choice == 1:
        # Get the current price of the stock
        os.system("start python3 price.py")
        os.system("python3 main.py")

    elif choice == 2:
        os.system("start python3 historical.py")
        os.system("python3 main.py")

    elif choice == 3:
        # Get the historical data for the stock
        data = gme.history(period="1y")

        # Plot the data
        mpf.plot(data, type="candle", style="charles", volume=True, title="GameStop (GME)")

        # Show the plot
        plt.show()
        os.system("python3 main.py")

    elif choice == 4:
        # Open the subreddit in a new window
        os.system("start http://www.gme.fyi")
        os.system("python3 main.py")

    elif choice == 5:
        # Open the subreddit in a new window
        os.system("start https://www.reddit.com/r/Superstonk/")
        os.system("python3 main.py")
    
    elif choice == 6:
        # Exit the program
        print("""\n
        Hedgies R' Fuk.
        
        Ken Griffin lied under oath.
        
        DTCC committed international 
        securities fraud.
        
        DRS your shares!\n""")
        time.sleep(5)
    os.system("cls")
    exit()

except (KeyboardInterrupt, SystemExit, ValueError, TypeError):
    exit()
