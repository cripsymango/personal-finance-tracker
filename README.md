# Project Title: My Personal Finance Tracker

## Overview of the Project
This is a simple, beginner-friendly Python application created to help users track their daily money. It uses a clean command-line menu where users can log incomes, record expenses, and generate instant financial reports. It was built using core Python concepts like Object-Oriented Programming, lists, and file handling.

## Features
*   **Add Records:** Quickly log new incomes and expenses.
*   **Live Balance:** Automatically calculates total money earned, total spent, and the remaining balance.
*   **Category Analysis:** Groups expenses by category (like Food or Rent) to show where money is going.
*   **Search & Delete:** Easily find specific past transactions or delete mistakes.
*   **Local Saving:** Uses Python's built-in JSON library to save data automatically.

## Technologies/Tools Used
*   **Python 3:** The main programming language.
*   **json module:** Used to save and load user data to a local file.
*   **unittest module:** Used to run automated tests on the math logic.
*   **Command Line Interface (CLI):** The text-based menu used to interact with the app.

## Steps to Install & Run the Project
1. Make sure Python 3 is installed on your computer.
2. Open your terminal or command prompt.
3. Navigate to the folder where you saved this project.
4. Run the main script by typing: `python3 main.py`

## Instructions for Testing
To prove the math and logic work correctly without manually entering data, you can run the automated tests. 
1. Open your terminal in the project folder.
2. Type this command: `python3 -m unittest discover -s tests -v`
3. Press Enter, and you will see the test results printed on the screen. 
