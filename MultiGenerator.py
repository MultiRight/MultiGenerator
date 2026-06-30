# mimi is a nice cat 🐱

# github : https://github.com/MultiRight

# Copyright © 2026 MultiRight <https://github.com/MultiRight>

import secrets
import sys

if sys.platform == "win32":
    import os
    os.system("")
    

color_red = "\033[31m"
color_green = "\033[32m"
color_orange = "\033[33m"
color_light_blue = "\033[94m"
color_pink = "\033[95m"
color_reset = "\033[0m"


uprunning = True

print("\033c", end="")

try :

    while uprunning :

        running = True

        print(f"{color_light_blue}====================Welcome to multigenerator===================={color_reset}")
        print()
        user_q = input(f"{color_light_blue}Press enter to start use multigenerator : {color_reset}")
        print()

         
        while running :
            
            try :
                length = int(input(f"{color_pink}Enter password length(It should not be less than 16 or more than 32) : {color_reset}"))

                if length < 16 :
                    print()
                    print(f"{color_red}err102 : Invalid length. (A number greater than 32 or less than 16 was used.){color_reset}")
                elif length > 32 :
                    print()
                    print(f"{color_red}err102 : Invalid length. (A number greater than 32 or less than 16 was used.){color_reset}")
                else :
                    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*-_=+"

                    password = "".join(secrets.choice(chars) for i in range(length))

                    print()
                    print(f"{color_pink}Generated password is : {color_reset}")
                    print(f"{color_green}{password}{color_reset}")

                    while True :
                        print()
                        user_action = input(f"Type {color_green}'r'{color_reset} to restart or {color_green}'q'{color_reset} to quit : ")
                    
                        if user_action == "q" :
                            print()
                            print(f"{color_orange}Thank you for using multigenerator!{color_reset}")
                            print(f"{color_orange}Author : https://github.com/MultiRight{color_reset}")
                            print()
                            print(f"{color_orange}goodbye{color_reset}")
                            running = False
                            uprunning = False
                            break
                    
                    
                    
                        elif user_action == "r" :
                            print("\033c" , end="")
                    
                            uprunning = True
                            running = False
                            break
                    
                        else :
                            print(f"{color_red}err103 : Invalid action. (Choice is not 'r' or 'q'.){color_reset}")
            
            except ValueError :
                print(f"{color_red}err101 : Invalid input. (Letters/symbols entered instead of numbers.){color_reset}")
                print()

except KeyboardInterrupt :

                
    print("\n")

    print(f"{color_orange}Thank you for using multigenerator!{color_reset}")
    print(f"{color_orange}Author : https://github.com/MultiRight{color_reset}")
    print()
    print(f"{color_orange}goodbye{color_reset}")
                
