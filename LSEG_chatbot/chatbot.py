import json


def load_stock_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Stock data file '{file_name}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in stock data file '{file_name}'.")
        return None

def display_chatbot_menu():
    print("\nHello! Welcome to LSEG. I'm here to help you:\n")
    print("Please select a Stock Exchange.")
    print("London Stock Exchange (LSE)")
    print("New York Stock Exchange (NYSE)")
    print("Nasdaq (NASDAQ)")
    print("Exit")
    print()

def display_stock_menu(stock_Exchange, stocks):
    print(f"\nStocks traded on {stock_Exchange}:\n")
    for i, stock in enumerate(stocks, 1):
        print(f"{i}. {stock['stockName']} ({stock['code']})")

def get_stock_price(stock_code, stock_data):
    for exchange_info in stock_data:
        for stock in exchange_info['topStocks']:
            if stock['code'] == stock_code:
                return stock['price']
    return None

    
def main():
    stock_data = load_stock_data("./LSEG_chatbot/stock_data.json")

    abbreviations = {
        "LSE": "London Stock Exchange",
        "NYSE": "New York Stock Exchange",
        "NASDAQ": "Nasdaq"
    }

    while True:
        display_chatbot_menu()
        choice = input('Enter your choice: ').strip()

        if choice == 'Exit':
            print('\nExiting the chatbot. Goodbye!')
            break
        elif choice in ('LSE','NYSE','NASDAQ'):
            if choice in abbreviations:
                stock_Exchange = abbreviations[choice]
            else:
                stock_Exchange = choice
            
            stocks = []
            for exchange_info in stock_data:
                if exchange_info['stockExchange'] == stock_Exchange:
                    stocks = exchange_info['topStocks']
                    break
            if not stocks:
                print("Error: No stock data available for the selected exchange.")
                continue
            
            while True:
                display_stock_menu(stock_Exchange, stocks)
                stock_choice = input("\nEnter the stock code (or 'B' to go back): ").strip().upper()
                print()
                if stock_choice == 'B':
                    break

                selected_stock = None
                for stock in stocks:
                    if stock['code'] == stock_choice:
                        selected_stock = stock
                        break
                
                if selected_stock is None:
                    print("\nInvalid input. Please enter a valid stock code.")
                    continue

                price = get_stock_price(selected_stock['code'], stock_data)
                if price is not None:
                    print(f"The current price of {selected_stock['stockName']} ({selected_stock['code']}) is ${price}")
        else:
            print("\nInvalid choice. Please select from the provided options.")


if __name__ == "__main__":
    main()
