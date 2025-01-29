import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from datetime import datetime, timedelta
from yahoo_fin import stock_info as si
import yfinance as yf
import pandas as pd

def getCurrentPrice(ticker):
	# Compute Current Price
  current_price = si.get_live_price(ticker)
  return current_price

def get12MonthMovingAvg(ticker):
  start_date = datetime.now() - timedelta(days=364.167)
  end_date = datetime.now()
	
  data = yf.download(ticker, start=start_date, end=end_date)
  var_12SMA = data["Close"].mean()
  return var_12SMA

def get3MonthPrice(ticker):
  # Set the start and end dates
  start_date = (datetime.now() - timedelta(days=91)).strftime('%Y-%m-%d')
  end_date = datetime.now().strftime('%Y-%m-%d')
  
  # Get the historical stock prices
  stock_data = si.get_data(ticker, start_date, end_date)
  
  # Compute 3 Month Ago Price
  closing_prices = stock_data['close']
  three_month_ago_price = closing_prices.iloc[0]
  
  return three_month_ago_price
  

def get3MonthPercentageChange(current_price, three_month_ago_price):
  # Compute the 3 Month % Change
  three_month_percentage_change = (current_price - three_month_ago_price) / three_month_ago_price * 100
  rounded_three_month_percentage_change = round(three_month_percentage_change, 2)
  return rounded_three_month_percentage_change
  
def getCycleRecommendation(ticker, cycle):
  return cycle_recommendation

def getRecommendBuySell():
  return recommended_buysell

def getTotalPoints(ticker):
  return total_points
  
def MyFunction(ticker):
	
	# Set the start and end dates
	start_date = (datetime.now() - timedelta(days=91)).strftime('%Y-%m-%d')
	end_date = datetime.now().strftime('%Y-%m-%d')
	
	# Get the historical stock prices
	ticker_symbol = ticker # Replace with your desired ticker symbol
	stock_data = si.get_data(ticker_symbol, start_date, end_date)

	# Compute Current Price
	current_price = si.get_live_price(ticker_symbol)
	
	# Compute 3 Month Ago Price
	closing_prices = stock_data['close']
	three_month_ago_price = closing_prices.iloc[0]

	# Compute the 3 Month % Change
	three_month_precentage_change = (current_price-three_month_ago_price)/three_month_ago_price*100

	if("SPY" == ticker):
		# Compute the 12 Month Moving Average
		start_date = datetime.now() - timedelta(days=364.167)
		end_date = datetime.now()
	
		data = yf.download(ticker_symbol, start=start_date, end=end_date)
		avg_price = data["Close"].mean()

	# Print the result
	# print(ticker_symbol, "Current Price: ", current_price)
	# print(ticker_symbol, "10 Month Moving Average: ", avg_price)
	# print(ticker_symbol, "3 Month Ago Price: ", three_month_ago_price)
	# print(ticker_symbol, "3 Month % Change: ", three_month_precentage_change,"%")
	return three_month_precentage_change

my_symbols = []
my_3monthpercentagechange = []
data = {"XLK": MyFunction("XLK"),
        "XLC": MyFunction("XLC"),
        "XLP": MyFunction("XLP"),
        "XLI": MyFunction("XLI"),
        "XLE": MyFunction("XLE"),
        "XLB": MyFunction("XLB"),
        "XLV": MyFunction("XLV"),
        "XLU": MyFunction("XLU"),
        "XLY": MyFunction("XLY"),
        "XLF": MyFunction("XLF"),
        "XLRE": MyFunction("XLRE")}

sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=False)
top_3_buy_stocks = sorted_data[:11]

for x in top_3_buy_stocks:
  print("Buy", x[0])
  my_symbols.append(x[0])
  my_3monthpercentagechange.append(x[1])

print("\n")


data = {'Symbol': my_symbols,
       '3 Month % Change': my_3monthpercentagechange}
df = pd.DataFrame(data)

print(df)

### Integrating the data into automated email system ###

# import smtplib
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText

# # instance of MIMEMultipart
# msg = MIMEMultipart()

# # storing the sender's email address
# msg['From'] = 'TNTHARMjrsmf@gmail.com'

# # storing the receiver's email address
# msg['To'] = 'xkjazzfunk@gmail.com'

# # storing the subject
# msg['Subject'] = 'Email using Python'

# # Store the body of the mail
# message = 'Buy XLK Buy XLC Buy XLP Symbol  3 Month % Change 0    XLK          9.151434 1    XLC          7.415443 2    XLP          5.723302'

# # attach the body with the msg instance
# msg.attach(MIMEText(message))

# # creates SMTP session
# mailserver = smtplib.SMTP('smtp.gmail.com', 587)

# # identify ourselves to smtp gmail client
# mailserver.ehlo()

# # secure our email with tls encryption
# mailserver.starttls()

# # re-identify ourselves as an encrypted connection
# mailserver.ehlo()

# # Authentication
# mailserver.login('TNTHARMjrsmf@gmail.com', "PASSWORD GOES HERE")

# mailserver.sendmail('TNTHARMjrsmf@gmail.com', 'xkjazzfunk@gmail.com', msg.as_string())

# mailserver.quit()