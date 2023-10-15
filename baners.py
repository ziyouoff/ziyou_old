import os

try:
  from termcolor import colored
except:
   os.system('pip install termcolor')
   from termcolor import colored

try:
    from pystyle import Center
    from pystyle import Add
except:
    os.system('pip install pystyle')
    from pystyle import Center
    from pystyle import Add

import random

def soft_info():
    print(f'''В КС 3 займусь фиксом''')

Bye_Bye = f'''
_______________________________________________
    ____                     ____              
    /   )                    /   )             
---/__ /-----------__-------/__ /-----------__-
  /    )   /   / /___)     /    )   /   / /___)
_/____/___(___/_(___ _____/____/___(___/_(___ _
             /                        /        
         (_ /                     (_ /         
'''

setings_big = '''
          _____                    _____                _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \              /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \            /::\    \                /::\    \                /::\____\                /::\    \                /::\    \        
       /::::\    \              /::::\    \           \:::\    \               \:::\    \              /::::|   |               /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \           \:::\    \               \:::\    \            /:::::|   |              /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \           \:::\    \               \:::\    \          /::::::|   |             /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \           \:::\    \               \:::\    \        /:::/|::|   |            /:::/  \:::\    \        /:::/__\:::\    \    
    \:::\   \:::\    \      /::::\   \:::\    \          /::::\    \              /::::\    \      /:::/ |::|   |           /:::/    \:::\    \       \:::\   \:::\    \   
  ___\:::\   \:::\    \    /::::::\   \:::\    \        /::::::\    \    ____    /::::::\    \    /:::/  |::|   | _____    /:::/    / \:::\    \    ___\:::\   \:::\    \  
 /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \      /:::/\:::\    \  /\   \  /:::/\:::\    \  /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\  /\   \:::\   \:::\    \ 
/::\   \:::\   \:::\____\/:::/__\:::\   \:::\____\    /:::/  \:::\____\/::\   \/:::/  \:::\____\/:: /    |::|   /::\____\/:::/____/  ___\:::|    |/::\   \:::\   \:::\____\ 
\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /   /:::/    \::/    /\:::\  /:::/    \::/    /\::/    /|::|  /:::/    /\:::\    \ /\  /:::|____|\:::\   \:::\   \::/    /
 \:::\   \:::\   \/____/  \:::\   \:::\   \/____/   /:::/    / \/____/  \:::\/:::/    / \/____/  \/____/ |::| /:::/    /  \:::\    /::\ \::/    /  \:::\   \:::\   \/____/ 
  \:::\   \:::\    \       \:::\   \:::\    \      /:::/    /            \::::::/    /                   |::|/:::/    /    \:::\   \:::\ \/____/    \:::\   \:::\    \     
   \:::\   \:::\____\       \:::\   \:::\____\    /:::/    /              \::::/____/                    |::::::/    /      \:::\   \:::\____\       \:::\   \:::\____\    
    \:::\  /:::/    /        \:::\   \::/    /    \::/    /                \:::\    \                    |:::::/    /        \:::\  /:::/    /        \:::\  /:::/    /    
     \:::\/:::/    /          \:::\   \/____/      \/____/                  \:::\    \                   |::::/    /          \:::\/:::/    /          \:::\/:::/    /     
      \::::::/    /            \:::\    \                                    \:::\    \                  /:::/    /            \::::::/    /            \::::::/    /      
       \::::/    /              \:::\____\                                    \:::\____\                /:::/    /              \::::/    /              \::::/    /       
        \::/    /                \::/    /                                     \::/    /                \::/    /                \::/____/                \::/    /        
         \/____/                  \/____/                                       \/____/                  \/____/                                           \/____/         
                                                                                                                                                                           
'''

setings_smol = '''
███████╗███████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
██╔════╝██╔════╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
███████╗█████╗     ██║   ██║██╔██╗ ██║██║  ███╗███████╗
╚════██║██╔══╝     ██║   ██║██║╚██╗██║██║   ██║╚════██║
███████║███████╗   ██║   ██║██║ ╚████║╚██████╔╝███████║
╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                       
'''

telegram_logo = f'''
@@@@@@@@@@@@@@@@@@%%**+=-------------++*%%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#+=------------------------=+#@@@@@@@@@@@@@@@
@@@@@@@@@@@@#=--------------------------------=#%@@@@@@@@@@@
@@@@@@@@@%=--------------------------------------=#@@@@@@@@@
@@@@@@@%+------------------------------------------=%@@@@@@@
@@@@@@+----------------------------------------------+%@@@@@
@@@@#=-------------------------------------------------#@@@@
@@@*----------------------------------------------------*@@@
@@*------------------------------------------------------*@@
@#-----------------------------------:..   .--------------*@
@=------------------------------:..         ---------------%
#--------------------------::.             .---------------+
-----------------------:.         ..       :----------------
------------------::.          .:-.        -----------------
-------------::.            .:--.          -----------------
-----------:             .:---.           .-----------------
------------:..       .:---:.             ------------------
------------------:::-----.               ------------------
#------------------------:               :-----------------+
@=-------------------------:.            ------------------%
@#----------------------------:.         -----------------*@
@@*------------------------------:.     :----------------*@@
@@@*--------------------------------:..:----------------*@@@
@@@@#=------------------------------------------------=#@@@@
@@@@@%+----------------------------------------------+%@@@@@
@@@@@@@%+------------------------------------------=%@@@@@@@
@@@@@@@@@%+--------------------------------------+#@@@@@@@@@
@@@@@@@@@@@%#=--------------------------------=#%@@@@@@@@@@@
@@@@@@@@@@@@@@@#+=------------------------=+#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@%%**+=------------==**%%@@@@@@@@@@@@@@@@@@

'''

baner_1 = '''.
⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⠟⠋⠉⠁⠁⠁⠀⠀⣄⣀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⠿⠛⠛⠋⠉⠉⠛⠟⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡇⠀⠀⣀⣄⠀⢹⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣿⣿⣿⣿
⠛⢀⣠⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠀⠀⠀⢿⣷⣶⣾⣿⣿⣿⡟⠁⠸⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢤⡄⠀⢲⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣸⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠊⠂⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⠀⣀⣀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡄⠀⠘⠉⢡⣄⡈⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣄⠀⠀⠀⣠⠀⠀⠀⠀⣤⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⡀⠛⠋⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣿⣿⣿⣆⠀⢸⣿⣶⠀⠀⣠⡿⠦⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣷⣤⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣷⣾⣿⣧⠀⠀⠋⠀⠀⠃⡾⠻⠿⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⡀⠀⠀⠀⢳⢤⠀⠀⠹⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⡘⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠁⠀⠁⠈⣶⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣼⣅⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣁⣀⣀⣤⡀⠀⠀⢀⣼⣿⣿⠛
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⣶⣿⠟⠋⢉⣤
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿
'''

baner_2 = '''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░▒░░▒░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒░░░▒░░░░░░░░░░░░░░░░░░░▒░░▒░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒░░░▒████▓░░░░░░▓███▓▒░░░▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒░░▓██████▓░░░░███████▓░░▓░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒░░░▒██████▒░▓▓░▒▓█████▒░░▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒░░░░▒▒▒░░░▒██▒░░░░░░░░░░▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▒░░░▓▒░░░░█▓██░░░░░▓▒▒▒░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒░██▒░░░▒░░▒░░░░▒█▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒░▓█░░░░░░░░░░░░▓█▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒░░▒▒▒░░░░░░░▒▒░██░▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▒░░░░░░▒▒░▒░░░░░░░▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░▒░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''
    
baner_3 = '''
░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░
░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░
░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░░░
░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░
░░░░░░▒▒▒▒▒▒▒▒▒▓▓▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▓▓▒▒▒▒▒▒▒▒▒░░░░░░
░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░
░░░▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒░░░
░░▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▓▓▓▒▒░░░▒▒▒▒▒▒▒▒▒▒░░░▒▒▓▓▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒░░
░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒░░▒▒▒▒▒▒▒▒░░▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░
░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░
░▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒░▒▒▒▒▒▒▒▒▒▒▒▒░
░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░▒▒▒▒▒▓▓▓▒▒▓▓▓▒▒▒▒▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░▒▒▒▒▒▒▒▒▒▓▒▒▒▒░░░░▒▒▒▒▓▓██████████▓▓▒▒▒▒░░░░▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒
░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▓███▓▓▓▒▒▓▓▓███▓▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒░
░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓███▓▓▒▒▒▒▒▒▒▒▓▓███▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓███▓▓▓▒░▒▓█▓▓█▓░░▒▓▓▓███▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▓████▓▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░▒▓████▓▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░
░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▓████▓▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░
░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▓████▓▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░
░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒████▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░
░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░
░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░
░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░

'''

baner_4 = f'''
                                                            
                                                            
                                                            
                                                            
                                                            
                          .-  :                             
                           :*.:*.                           
                    .+-.:=. .#+-%=                          
                 =%##%%%%%%%*+%%*#%-                        
              =#%%%%%%%%%%%%%%%%%%%%%=                      
             -*%%%%#=-:...:-+#%%%%%%%%%+                    
            -#%%%%:            -#%%%%%%%%-                  
            +%%%@:               :#%%%%  %=                 
           :-%%%@.                 +%%%%%%%+                
            :@%%%*                   -*%%%%*.               
            ::*%%%#:                    =%%%%+.             
              .%*%%%*-                    +%%%%:            
                  =#%%%*-                  %%#:             
                     -+#%%#+-.             -.               
                         :=*%%#+:                           
                             .=*%#-                         
                                 -##.                       
                                   -%.                      
                                    :*                      
                                     =                      
                                                            
                                                            


'''

baner_5 = f'''
                  ..::--=====================-.             
           .-+**#%%#***+++==--:::...::.   ..:=##:           
        -**=::::.................:::::::::     :%#          
      =%=     ..:::::.       .......::-=-:::.    #%         
      %.    :.      .:       -          ..:.      #*        
     *%       .:::.  -        -+*+%@@%#*-          #*       
   +@+.::.  :%@%%@@@#= .    =@=.:=%@@@@##@..-:   .:-#%*.    
 .@#===       ..::-=*@#=    -##*=:. +-  :: :-+#*+++: .-+*.  
 =%-.-.+#*+#*-:=     @:              =*+++*#*=.+.  =#. .:@. 
 -%- :   -+.+==.  :*#=       ++=.          :=*#%%=. +* : #+ 
  **::: .@%    .:%@#     .=+=-.#+.... .-+%@*-  +%=+:%- : @- 
   *#:- #%@#=..    -#=-=  :..:-+::=***+==@. .=#@=   :.=:%+  
    #+ .@@++#*##+=--:=+---=++++*#@.   .-%@@#+@%.    .=#*.   
    -% :@@+%+ +%.::-@*-::**     :@+*%@@##@..#*      *#.     
    :@ .@@@@@@@@##**@#***%%**#%@@@@+=:  .%#@-      **       
    -%  %@@@@@@@@@@@@@@@@@@@+=-: :@.   -#%=       +%        
    **  :@#@-#*:##.:*@..  +%      +@=#%*:       :#*         
    %=   .*%##@+=@+..%=...+@--=+*##+-::..:=-::+#+.          
   .@.       :--==++++++++==--:.  ::-=----=*#+:             
   -@  ..  :--:..  ..::......::-=-:::-=*#*-.                
   -@    ----::................  .=##+-                     
    **.                   :-::=*#+-                         
     :*#+-:.     ..:-=+#%%#*+-:                             

'''



ziyou_1 = '''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░______░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░|__   (_)_   _  ___  _   _ ░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░/ /| | | | |/ _ \| | | |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░/ /_| | |_| | (_) | |_| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░/____|_|\__, |\___/ \__,_|░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░|___/░Version 1.4.3░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄Telegtam: @ziyouoff▄
                    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
'''

ziyou_2 = '''



          _____                    _____                _____                   _______                   _____          
         /\    \                  /\    \              |\    \                 /::\    \                 /\    \         
        /::\    \                /::\    \             |:\____\               /::::\    \               /::\____\        
        \:::\    \               \:::\    \            |::|   |              /::::::\    \             /:::/    /        
         \:::\    \               \:::\    \           |::|   |             /::::::::\    \           /:::/    /         
          \:::\    \               \:::\    \          |::|   |            /:::/~~\:::\    \         /:::/    /          
           \:::\    \               \:::\    \         |::|   |           /:::/    \:::\    \       /:::/    /           
            \:::\    \              /::::\    \        |::|   |          /:::/    / \:::\    \     /:::/    /            
             \:::\    \    ____    /::::::\    \       |::|___|______   /:::/____/   \:::\____\   /:::/    /      _____  
              \:::\    \  /\   \  /:::/\:::\    \      /::::::::\    \ |:::|    |     |:::|    | /:::/____/      /\    \ 
_______________\:::\____\/::\   \/:::/  \:::\____\    /::::::::::\____\|:::|____|     |:::|    ||:::|    /      /::\____\ 
\::::::::::::::::::/    /\:::\  /:::/    \::/    /   /:::/~~~~/~~       \:::\    \   /:::/    / |:::|____\     /:::/    /
 \::::::::::::::::/____/  \:::\/:::/    / \/____/   /:::/    /           \:::\    \ /:::/    /   \:::\    \   /:::/    / 
  \:::\~~~~\~~~~~~         \::::::/    /           /:::/    /             \:::\    /:::/    /     \:::\    \ /:::/    /  
   \:::\    \               \::::/____/           /:::/    /               \:::\__/:::/    /       \:::\    /:::/    /   
    \:::\    \               \:::\    \           \::/    /                 \::::::::/    /         \:::\__/:::/    /    
     \:::\    \               \:::\    \           \/____/                   \::::::/    /           \::::::::/    /     
      \:::\    \               \:::\    \                                     \::::/    /             \::::::/    /      
       \:::\____\               \:::\____\                                     \::/____/               \::::/    /       
        \::/    /                \::/    /                                      ~~                      \::/____/        
         \/____/                  \/____/                                                                ~~              
          telegram: @ziyouoff                                                                        version: 1.4.3                             
'''

ziyou_3 = '''
 ______     __     __  __     ______     __  __    
/\___  \   /\ \   /\ \_\ \   /\  __ \   /\ \/\ \   
\/_/  /__  \ \ \  \ \____ \  \ \ \/\ \  \ \ \_\ \  
  /\_____\  \ \_\  \/\_____\  \ \_____\  \ \_____\ 
  \/_____/   \/_/   \/_____/   \/_____/   \/_____/ 
   telegram: @ziyouoff             version: 1.4.3
                                                   
'''

ziyou_4 = '''
███████╗██╗██╗   ██╗ ██████╗ ██╗   ██╗
╚══███╔╝██║╚██╗ ██╔╝██╔═══██╗██║   ██║
  ███╔╝ ██║ ╚████╔╝ ██║   ██║██║   ██║
 ███╔╝  ██║  ╚██╔╝  ██║   ██║██║   ██║
███████╗██║   ██║   ╚██████╔╝╚██████╔╝
╚══════╝╚═╝   ╚═╝    ╚═════╝  ╚═════╝ 
telegram: @ziyouoff   version: 1.4.3                                     
'''

ziyou_5 = '''
▒███████▒ ██▓▓██   ██▓ ▒█████   █    ██ 
▒ ▒ ▒ ▄▀░▓██▒ ▒██  ██▒▒██▒  ██▒ ██  ▓██▒
░ ▒ ▄▀▒░ ▒██▒  ▒██ ██░▒██░  ██▒▓██  ▒██░
  ▄▀▒   ░░██░  ░ ▐██▓░▒██   ██░▓▓█  ░██░
▒███████▒░██░  ░ ██▒▓░░ ████▓▒░▒▒█████▓ 
░▒▒ ▓░▒░▒░▓     ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ 
░░▒ ▒ ░ ▒ ▒ ░ ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░ 
░ ░ ░ ░ ░ ▒ ░ ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░ 
  ░ ░     ░   ░ ░         ░ ░     ░     
░             ░ ░                  
telegram: @ziyouoff      version: 1.4.3      
'''

ziyou_6 = '''
 ▄███████▄   ▄█  ▄██   ▄    ▄██████▄  ███    █▄  
██▀     ▄██ ███  ███   ██▄ ███    ███ ███    ███ 
      ▄███▀ ███▌ ███▄▄▄███ ███    ███ ███    ███ 
 ▀█▀▄███▀▄▄ ███▌ ▀▀▀▀▀▀███ ███    ███ ███    ███ 
  ▄███▀   ▀ ███▌ ▄██   ███ ███    ███ ███    ███ 
▄███▀       ███  ███   ███ ███    ███ ███    ███ 
███▄     ▄█ ███  ███   ███ ███    ███ ███    ███ 
 ▀████████▀ █▀    ▀█████▀   ▀██████▀  ████████▀  
  telegram: @ziyouoff           version: 1.4.3   
                                                 
'''

ziyou_7 = '''
_      ___      ___   __   ____     ___    ___    _
(___   ) (_    _) (  (  )  )   )   (   |  |   |  | 
   /  /    |  |    \  \/  /   /     \  |  |   |  | 
  /  /     |  |     \    /   (       ) |  |   |  | 
 /  /__   _|  |_     )  /     \     /  |   \_/   | 
(      )_(      )___/  (_______)   (____\       /__
 telegram: @ziyouoff                version: 1.4.3 
'''

def print_start():
    try:
      import pickle
      with open('data.pkl', 'rb') as file:
          data = pickle.load(file)      
    except:
       import main
       main.setings()
    
    r_baner = random.randint(1, 5)
    r_ziyou = random.randint(1, 7)

    if data['devise'] == 'M':
      if r_baner == 1: print(Center.XCenter(colored(baner_1, "blue")))
      elif r_baner == 2: print(Center.XCenter(colored(baner_2, "white")))
      elif r_baner == 3: print(Center.XCenter(colored(baner_3, "white")))
      elif r_baner == 4: print(Center.XCenter(colored(baner_4, "blue")))
      elif r_baner == 5: print(Center.XCenter(colored(baner_5, "white")))


      if r_ziyou == 1: print(Center.XCenter(colored(ziyou_1, "yellow")))
      elif r_ziyou == 2: print(Center.XCenter(colored(ziyou_2, "yellow")))
      elif r_ziyou == 3: print(Center.XCenter(colored(ziyou_3, "cyan")))
      elif r_ziyou == 4: print(Center.XCenter(colored(ziyou_4, "red")))
      elif r_ziyou == 5: print(Center.XCenter(colored(ziyou_5, "green")))
      elif r_ziyou == 6: print(Center.XCenter(colored(ziyou_6, "white")))
      elif r_ziyou == 7: print(Center.XCenter(colored(ziyou_7, "white")))
    
    elif data['devise'] == 'P':
       print(Center.XCenter(Add.Add(colored(baner_4, "blue"), colored(ziyou_2, "blue"))))

def print_telegram_logo(): print(Center.XCenter(colored(telegram_logo, "blue")))
def print_bye_bye(): print(Center.XCenter(Bye_Bye))

def print_ascll_setings():
    try:
      import pickle
      with open('data.pkl', 'rb') as file:
        data = pickle.load(file)  

      if data['devise'] == 'M':
        print(Center.XCenter(colored(setings_smol, 'yellow')))

      elif data['devise'] == 'P':
        print(Center.XCenter(colored(setings_big, 'yellow')))
    except:
       pass