# mimi is a nice cat 🐱

# github : https://github.com/MultiRight

# Copyright © 2026 MultiRight <https://github.com/MultiRight>

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.


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

running = True

print("\033c", end="")

try :

    print(f"{color_light_blue}====================Welcome to MultiGenerator===================={color_reset}")
    print()
    user_q = input(f"{color_light_blue}Press enter to start use MultiGenerator or enter '--help' to help for use MultiGenerator : {color_reset}")
    print()

    if user_q == "--help" :
        print(f"{color_orange}Welcome to MultiGenerator help page :{color_reset}")
        print(f"{color_orange}It seems you are having trouble using the application, even though it is a simple application :){color_reset}")
        print()
        print(f"{color_light_blue}How to use{color_reset}")
        print()
        print(f"{color_orange}It's easy, just enter the password length you want.{color_reset}")
        print(f"{color_orange}The number must not be less than 16 or greater than 32.{color_reset}")
        print(f"{color_orange}Please do not use letters or symbols in place of numbers, only whole numbers.{color_reset}")
        print()
        print(f"{color_light_blue}Explanation of error messages{color_reset}")
        print()
        print(f"{color_orange}err101 : Invalid input. (Letters/symbols entered instead of numbers).{color_reset}")
        print(f"{color_orange}err102 : Invalid length. (A number greater than 32 or less than 16 was used.).{color_reset}")
        print(f"{color_orange}err103 : Invalid action. (Choice is not 'r' or 'q'){color_reset}")
        print()
        input(f"{color_light_blue}Press Enter to start MultiGenerator...{color_reset}")
        print()

            
    while running :
            
        try :
            length = int(input(f"{color_pink}Enter password length(It should not be less than 16 or more than 32) : {color_reset}"))

            if length < 16 :
                print()
                print(f"{color_red}err102 : your input is invalid please try again{color_reset}")
            elif length > 32 :
                print()
                print(f"{color_red}err102 : your input is invalid please try again{color_reset}")
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
                        print(f"{color_orange}Thank you for using MultiGenerator!{color_reset}")
                        print(f"{color_orange}Author : https://github.com/MultiRight{color_reset}")
                        print()
                        print(f"{color_orange}goodbye{color_reset}")
                        running = False
                        break
                
                
                
                    elif user_action == "r" :
                        print("\033c" , end="")
                
                        running = True
                        break
                
                    else :
                        print(f"{color_red}err103 : your input is invalid please try again{color_reset}")
            
        except ValueError :
                print(f"{color_red}err101 : your input is invalid please try again{color_reset}")
                print()

except KeyboardInterrupt :

                
    print("\n")

    print(f"{color_orange}Thank you for using MultiGenerator!{color_reset}")
    print(f"{color_orange}Author : https://github.com/MultiRight{color_reset}")
                
