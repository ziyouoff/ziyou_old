import os
from termcolor import colored



f_arg = [38028, 38000]
s_arg = [38029, 4444,4418,552 ,1657,
552,1657,552,1657,552,552,552,552,552,
552,552,552,552,552,552,1657,552,1657,
552,1657,552,552,552,552,552,552,552,
55, 255255255255255216575525525525525525525525525525525525525521683552552552165755216575521657552,
 16575521657,552, 1657, 552, 47175, 4444, 
4418,552,552,552,97137]

def FlipperNull():
    print(colored("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡠⠤⠤⠤⠤⠤⠤⠤⠤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠞⠛⠓⠒⠒⠒⠒⠢⠤⢄⣀⢀⠤⡪⠊⠉⠉⡹⠶⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠎⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡨⠩⡺⠒⠁⠀⣀⠔⠁⠠⢄⠙⢳⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡱⢮⡾⠀⠀⢀⠆⠀⠀⠁⡀⠀⠱⠀⣿⡆⠀⠀⢀⣰⡶⠶⠶⠶⢶⣄⣀⠀⠀⠀⠀
⠀⠀⠀⠀⣤⠇⠀⠀⠀⠀⠀⢀⠄⠐⣒⣒⣒⡒⠺⢮⡵⠀⠀⠀⡎⠀⠀⠑⠀⠈⢁⠤⠀⠉⡹⠶⠋⠉⠀⠀⠀⠀⣀⣀⣤⣭⡇⠀⠀⠀
⠀⠀⠀⣸⠛⠀⠀⠀⠀⢀⠜⢃⠜⠃⣀⣀⣀⡘⠛⢄⡐⢄⠀⠀⠘⢄⣀⣀⠤⠚⠃⣀⠀⠛⠀⠀⠀⠀⢀⣠⣼⣿⣿⣿⡿⠛⠀⠀⠀⠀
⠀⠀⣤⠇⠀⠀⠀⠀⠀⡜⡘⠃⣠⣾⡿⢿⣿⣿⣧⡀⠘⡘⡄⠀⠀⠀⠀⢀⡀⠀⠘⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⡿⠛⠀⠀⠀⠀⠀⠀
⠀⢀⠉⠀⠀⠀⠀⠀⠀⡇⡇⠀⣿⣿⣤⣼⣿⣿⣿⡇⠀⡇⡇⠀⣀⠤⠒⠊⠁⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠀⠀⠀⠀⢀⢀⡰⡇⢃⡀⢻⣿⣿⣿⣿⠛⠛⠃⢠⡇⠑⠂⠉⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡏⠀⠀⠀⠐⡕⡕⢪⢺⡌⠑⣤⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡇⠀⠀⠀⠠⡪⡪⢕⢕⢝⡳⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⣾⠟⠉⠉⠉⠉⠙⠛⠫⠭⣉⠉⠉⣉⡩⠭⠛⣶⠀⠀
⡼⠇⠀⠀⠀⠀⠈⠌⠣⠡⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣀⣀⣀⣤⣴⣿⣿⣿⣇⣀⣀⣀⣀⣀⣀⡠⠤⠤⠜⠛⠋⠀⠀⠀⣠⠟⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠛⠁⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⠤⠖⠚⠋⠉⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣶⣶⣾⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠢⢫⡝⡟⢻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⡰⡰⠄⣀⢎⠿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠁⠲⠱⠉⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""", "yellow"))

	print(colored("""  _____ _ _                       _   _       _ _  """, "yellow"))
	print(colored(""" |  ___| (_)_ __  _ __   ___ _ __| \ | |_   _| | | """, "yellow"))
	print(colored(""" | |_  | | | '_ \| '_ \ / _ \ '__|  \| | | | | | | """, "yellow"))
	print(colored(""" |  _| | | | |_) | |_) |  __/ |  | |\  | |_| | | | """, "yellow"))
	print(colored(""" |_|   |_|_| .__/| .__/ \___|_|  |_| \_|\__,_|_|_| """, "yellow"))
	print(colored("""           |_|   |_|                               """, "yellow"))
    for i in f_arg:
        for j in s_arg:
            print('termux-infrared-transmit -f', str(i), str(j))
            try:
                os.system('termux-infrared-transmit -f ' + str(i) + ' ' + str(j))
            except:
                print('[!]USE IK PORT BLYAT')


    