import pandas as pd
import os
import sys

def readExcel():
    cheatSheet = cheatSheet=pd.read_excel(
        os.path.join("Draft Cheat Sheet 2021.xlsx"),
        engine='openpyxl',
    )
    return cheatSheet

def promptUser(cheatSheet, myTeam):
    while True:
        command = input('Enter your command: ').split()
        if len(command) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Enter a valid command")
        elif command[0] == "quit":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif command[0] == "help":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("List of arguments:")
            print("'help' gives you a list of the possible command line arguments")
            print("'top <number>' shows you the top <number> of players available for each position")
            print("'drafted <player>' shows that <player> was taken by another team")
            print("'idrafted <player>' shows that you drafted <player>")
            print("'myTeam' shows you your team")
            print("'quit' quits the program")
        elif command[0] == "top":
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                topPlayersNumber = int(command[1])
                df1 = cheatSheet.sort_values(by='Differential_Value',ascending = False).groupby('Position').head(topPlayersNumber)
                # df1 = df1.sort_values(by='Position', ascending = False)
                print(df1)
            except:
                print("Second argument must be a number. Try again.")
        elif command[0] == "drafted":
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                if len(command) == 2:
                    playerName = command[1]
                    cheatSheet = cheatSheet[cheatSheet.Player != playerName]
                elif len(command) == 3:
                    playerName = command[1] + ' ' + command[2]
                    cheatSheet = cheatSheet[cheatSheet.Player != playerName]
                elif len(command) == 4:
                    playerName = command[1] + ' ' + command[2] + ' ' + command[3]
                    cheatSheet = cheatSheet[cheatSheet.Player != playerName]
                else:
                    print("Enter a valid player")
            except:
                print("Name doesn't exist. Try again.")
        elif command[0] == "idrafted":
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                if len(command) == 2:
                    playerName = command[1]
                    entry = cheatSheet.loc[cheatSheet['Player'] == playerName]
                    myTeam = myTeam.append(entry)
                    cheatSheet = cheatSheet[cheatSheet.Player != playerName]
                elif len(command) == 3:
                    playerName = command[1] + ' ' + command[2]
                    entry = cheatSheet.loc[cheatSheet['Player'] == playerName]
                    myTeam = myTeam.append(entry)
                    cheatSheet = cheatSheet[cheatSheet.Player != playerName]
                elif len(command) == 4:
                    playerName = command[1] + ' ' + command[2] + ' ' + command[3]
                    entry = cheatSheet.loc[cheatSheet['Player'] == playerName]
                    myTeam = myTeam.append(entry)
                    cheatSheet = cheatSheet[cheatSheet.Player != playerName]
                else:
                    print("Enter a valid player")   
            except:
                print("Name doesn't exist. Try again.")
        elif command[0] == "myTeam":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(myTeam)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bad arguments. Try again.")

def main():
    cheatSheet = readExcel()
    myTeam = pd.DataFrame(data=None, columns=cheatSheet.columns)
    promptUser(cheatSheet, myTeam)

main()

