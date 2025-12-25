n = int(input('\n\tEnter val of N :'))

def iteration_ink(n):
    
    if n<100:
        for i in range(n+1):
            print(f'{i}th Iteration ---')
    else:
        print(f'what do you mean by {n}. Im too lazy to print!')
    
iteration_ink(n)  

