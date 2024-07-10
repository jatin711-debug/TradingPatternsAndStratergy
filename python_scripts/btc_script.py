import time
import requests
import winsound
import threading

# Set the target price for the alarm
target_price = 60000  # example target price, change as needed

# Function to get the current BTC/USD price
def get_btc_price():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    data = response.json()
    price = data['bpi']['USD']['rate_float']
    return price

# Function to play the alarm sound continuously
def play_alarm():
    duration = 1000  # milliseconds
    freq = 440  # Hz
    while True:
        winsound.Beep(freq, duration)

# Function to start the alarm in a separate thread
def start_alarm():
    alarm_thread = threading.Thread(target=play_alarm)
    alarm_thread.daemon = True
    alarm_thread.start()

while True:
    try:
        # Get the current BTC price
        current_price = get_btc_price()
        print(f"Current BTC/USD price: {current_price}")
        
        # Check if the price hits the target price
        if current_price >= target_price:
            print("Target price reached! Playing alarm...")
            start_alarm()
            while True:  # Keep the program running
                time.sleep(1)
            
        # Wait for 900 milliseconds before checking the price again
        time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        break
