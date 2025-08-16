MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
import random
ROWS = 3
COLS = 3

symbols_count = {
    "🍒":7,
    "💎":4,
    "🔔":6,
    "😍":5
}
symbols_values = {
    "🍒":5,
    "💎":4,
    "🔔":3,
    "😍":2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings+= values[symbol]*bet
            winning_lines.append(line+1)
    return winnings , winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
## symbols is a dictionary like {"🍒": 4, "💎": 2, "🔔": 3,"😍":4}.
    ## This loop creates a flat list all_symbols with each symbol repeated according to its count.
    ## Example output of all_symbol: ["🍒", "🍒", "🍒", "🍒", "💎", "💎", "🔔", "🔔", "🔔"]

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns = []
    for _ in range(cols):
        column = []

    ### Suppose current Symbol: {current_symbol = ["🍒", "🍒", "💎", "💎", "🔔", "🔔"]
###  random.choice(current_symbol) → picks "💎"
     ###  Remove "💎" → current_symbol = ["🍒", "🍒", "💎", "🔔", "🔔"]
     ###  column = ["💎"]
###  random.choice(current_symbol) -> Picks "🔔"
     ###  Remove "🔔" → current_symbol = ["🍒", "🍒", "💎", "🔔"]
     ###  column = ["💎", "🔔"]
### random.choice(current_symbol) -> Picks "🍒"
    ###  Remove "🍒" → current_symbol = ["🍒", "💎", "🔔"]
    ###  column = ["💎", "🔔", "🍒"]


        ##MAKING COPY OF ALL SYMBOLS
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column) ###  This generates a single row / COLUMN like ["💎", "🔔", "🍒"]
        # After filling one column, add it to the columns list.

    return columns
    ### This column will represent full grind of 3 * 3 matrix.
    ###[["💎", "🔔", "🍒"],
    ###["🔔", "💎", "🍒"],
    ### "🔔", "🍒", "💎"] i.e., It's a list of list



def print_slot_machine(columns):
    ## INPUT
    ## PRINT TRANSPOSE OF A MATRIX
    ###[[""💎, "🔔", "🍒"],
    ###["🔔", "💎", "🍒"],
    ### "🔔", "🍒", "💎"]
    for row in zip(*columns):
        print(" | ".join(row))
   ### 💎 | 🔔 | 🔔
   ### 🔔 | 💎 | 🍒
   ### 🍒 | 🍒 | 💎



### FUNCTION TO DEPOSIT BALANCE
def deposit():
    # Works until user enters valid amount
    while True:
       amount = input("What Would you like to deposit ? $")
       #check if amount is number
       if amount.isdigit():
           amount = int(amount)

           #check number is greater than zero
           if amount > 0:
               break
           else:
               print("Amount must be greater than 0")
       else:
           print("Please enter a number")

    return amount

### FUNCTION TO GET NUMBER OF LINES IN SLOT MACHINE
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        # check if amount is number
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
    else:
        print("Please enter a number")

    return lines

####FUNCTION TO GET BET
def get_bets():
    while True:
        amount = input("What would you like to bet on each line? $ ")
        # check if amount is number
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between 1 and " + str(MAX_BET))
        else:
            print("Please enter a number")


    return amount

###MAIN METHOD
def main():
    balance = deposit()
    lines = get_number_of_lines()
    is_playing = True

    while is_playing:
        while True:
            print(f"\nCurrent Balance: ${balance}")
            bets = get_bets()
            total_bet = bets * lines

            if total_bet > balance:
                print("You don't have enough money, your current balance is $" + str(balance))
            else:
                print(f"You are betting ${bets} on {lines} lines. Total bet: ${total_bet}")
                break

        # Deduct the total bet first
        balance -= total_bet

        # Spin the slot machine
        slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
        print("\n🎰 Slot Machine Result:")
        print_slot_machine(slots)

        # Check winnings
        winnings, winning_lines = check_winnings(slots, lines, bets, symbols_values)
        balance += winnings  # Add winnings to balance

        print(f"\nYou won ${winnings} on lines: {winning_lines if winning_lines else 'None'}")
        print(f"Updated Balance: ${balance}")

        if balance < MIN_BET:
            print("You don't have enough balance to continue playing. Game over!")
            break

        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice != "y":
            is_playing = False
            print("🎉 Thank you for playing!")


main()


main()