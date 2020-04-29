import random
suites = ['♡', '♢', '♤', '♧']
values = [2,3,4,5,6,7,8,9,10,"J", "Q", "K","A"]

def get_random_card(list_suites, list_values):
    # your code here
    rand_num = values[random.randint(0,len(list_values))]
    rand_suite = suites[random.randint(0,len(list_suites))]
    
    return str(rand_num) + rand_suite
    
print(get_random_card(suites, values))