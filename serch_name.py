from termcolor import colored

def pasports_1 (FIO):
    with open('src//pasports_1.csv', 'r', encoding='utf-8') as file:
        
        for line in file:
            data = line.strip().split('|')  
            if len(data) >= 8:
                if FIO in data[0]:
                    print(colored('┌──────────────────────────────────────────────────────', "green"))
                    print(colored('│Найдено в базе Паспортов(09.2022)', "green"))
                    print(colored('├──────────────────────────────────────────────────────', "green"))
                    print(colored('├' + data[0].strip(), "green"))
                    print(colored('├' + data[1].strip(), "green"))
                    print(colored('├' + data[2].strip(), "green"))
                    print(colored('├' + data[3].strip(), "green"))
                    print(colored('├' + data[4].strip(), "green"))
                    print(colored('├' + data[5].strip(), "green"))
                    print(colored('├' + data[6].strip(), "green"))
                    print(colored('├' + data[7].strip(), "green"))
                    print(colored('├' + data[8].strip(), "green"))
                    print(colored('└──────────────────────────────────────────────────────', "green"))
            
    print(colored(f"Номер телефона в 1 базе не найден :( ", "red"))