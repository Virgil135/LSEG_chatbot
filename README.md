# Introduction
    This chatbot application is intentionally designed to minimize reliance on frameworks and libraries. It operates seamlessly within the terminal/console.


# Getting Started

## Installation process

Requirements:

- `git` (to download the repository)
- `python 3.10.12 +` (It can be downloaded from: `https://www.python.org/downloads/` )

Recommended development environment is: Ubuntu 22+ with VSCode.

## Step 1: setup the project directory structure (Only once)
    Navigate to the desired location where you want to create the project directory and download the repository from Git: 
    
 Ex: - ~/Virgil_Nedelcu/LSEG_chatbot/LSEG_chatbot

## Running app:
  To start the application, you can either click on `Run Python File` within VSCode or open a terminal, navigate to the directory containing the .py file, and execute the following command: `python3 chatbot.py`

 After launching the application, a chatbot menu will appear, offering greetings, a list of stock exchanges, and an option to exit the application if desired.

 ** Important Note!
    When selecting an option from the stock exchange list, ensure that you use capital letters for the abbreviations. The input is not case-sensitive. Failure to do so will result in a message error and home menu will be displayed again.

    Ex:
        "Hello! Welcome to LSEG. I'm here to help you:

        Please select a Stock Exchange.
        London Stock Exchange (LSE)
        New York Stock Exchange (NYSE)
        Nasdaq (NASDAQ)
        Exit

        Enter your choice: lse

        Invalid choice. Please select from the provided options."

 Upon selecting the stock exchange, a list of stocks will be presented. You can select the desired stock by entering its abbreviation, which is case-insensitive. Subsequently, the price will be displayed, and you will be given the option to select another stock or return to the main menu by pressing the "B/b" key.

 To close the application, simply type 'Exit', and the program will terminate.