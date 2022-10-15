# Вариант против бота

from random import randint


BOT_NAME = "(._. )"

def calculate_max_pick(current_value, max_value):
    if max_value > current_value:
        return current_value
    else:
        return max_value


def get_user_name(message:str, users: dict):
    while (True):
        name = input(message)
        if name in users or name == BOT_NAME:
            print("Name taken, please choose another!")
        else:
            users[name] = list()
            break

def get_input(name, count, max_pick):
    default_pick = calculate_max_pick(count, max_pick)
    
    while True:
        try:
            number = int(input(f"{name} take from 1 to {default_pick} candies: "))
        except:
            print("Please insert a correct number")
            continue
        
        if not default_pick >= number > 0:
            print("Please insert a correct number")
        else:
            break
        
    return number
    

def print_stats(users: dict, user_name: str):
    for name, total_pick in users.items():
        if name == user_name:
            print(f"{name} took the candies in {len(total_pick)} moves.")
            
def init_ai(users: dict): 
    users[BOT_NAME] = list()
    
def ai_input(count, user_input, max_step):
    key_number = max_step + 1
    
    if (count - (key_number - user_input)) % key_number == 0:
        step = key_number - user_input
    else:
        step = count % key_number
        
    if step == 0:
        step = randint(1, key_number-1)
        
    if step > count:
        step = count
    
    print(f"{BOT_NAME} took {step} candies")
    return step

def game_2021():
    users = dict()
    game = 2021
    max_step_pick = 280
    count = game
    
    get_user_name("Please insert your name: ", users)
    init_ai(users)
    
    print("Game started!")
    
    while count > 0:
        last_user_input = 0
        for name, _ in users.items():
            print(f"{count} candies left")
            if name == BOT_NAME:
                pick = ai_input(count, last_user_input, max_step_pick)
            else: 
                pick = get_input(name, count, max_step_pick)
                last_user_input = pick
               
            users[name].append(pick)
            count -= pick
            
            if count == 0:
                print(f"{name} won")
                print_stats(users, name)
                return
        

game_2021()