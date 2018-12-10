import os
import time

def SayHello(name):
    if name:
        print("Hello " + name)
    else:
        name = raw_input("Vous devez saisir un: ")
        SayHello(name)

        SayHello('')

def main():
        SayHello("Michel")
        time.sleep(2)
        os.system('Calc.exe')

main()
