import random
import time


def RPS(word):
    lis=["rock","paper","scissor"]
    AI_choice=random.choice(lis)
    AI_choice=AI_choice.upper()  
    word=word.upper()
    
    if AI_choice=='ROCK':
        if word=='ROCK':
            print("mine was also ",AI_choice,"\n Comeon think different, you copycat.")
        elif word=='PAPER':
            print("I chose",AI_choice,"\n You win")
        elif word=='SCISSOR':
            print("Guess what\n",time.sleep(1),AI_choice,"\n 'HA HA' You just got Crushed.")

    elif AI_choice=='PAPER':
        if word=='ROCK':
            print("",AI_choice,"\n'HA HA' your boulder just got coverd ")          
        elif word=='PAPER':
            print("",AI_choice,"\n Stop it, you will never be me")
        elif word=='SCISSOR':
            print("",AI_choice,"\n AH!, it cut me deep") 


    elif AI_choice=='SCISSOR':
        if word=='ROCK':
            print("",AI_choice,"\n Man, those scissors were new.")
        elif word=='PAPER':
            print("",AI_choice,"\n Yeah!, I just tore you apart")
        elif word=='SCISSOR':
            print("",AI_choice,"\n We got to stop tinking same")



if __name__==__name__ == "__main__":
    while True:
        print("Wanna play       (Enter s to play  ,   n to exit)")
        ans=input()
        if ans=='s':
            print("Rock-Paper-Scissor    (pick yours)")
            choice=input()
            RPS(choice)
        elif ans=='n':
            break    