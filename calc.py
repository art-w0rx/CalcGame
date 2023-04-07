import random
import os

a = list(range(0,50))
b = list(range(0,50))
c = ['+', '-',]
os.system('clear')
score = int()

def rnd_gen():
    global aa, bb, cc, rnd_c, highscore
    file = open("score.nfr", 'r')
    highscore = int(file.read())
    file.close()
    rnd_a = random.randint(1, len(a))
    rnd_b = random.randint(1, len(b))
    rnd_c = random.randint(1, len(c))
    aa = a[rnd_a-1]
    bb = b[rnd_b-1]
    cc = c[rnd_c-1]
    if aa < bb:
        rnd_gen()
    prt_gen()
        
def prt_gen():
    global w
    print("\033[33m")
    print(aa, cc, bb, "= ?")
    print("\033[31m\n'Q' - выход")
    print("\033[32m\nРешено задач:", highscore)
    w = input("\033[36m\n\nОтвет: \033[0m")
    if rnd_c == 1:
        op_plus()
    if rnd_c == 2:
        op_minus()
    
def op_plus():
    global score
    if w == 'q' or w == 'Q':
        os.system('clear')
        exit()
    else:
        try:
            ww = int(w)
            if ww == aa + bb:
                print("\033[32mверно")
                score += 1
                if score > highscore:
                    file = open('score.nfr', 'w')
                    file.write(str(score))
                    file.close()
                print("Счет: ", score)
                rnd_gen()
            else:
                print("\033[31mневерно")
                prt_gen()
        except ValueError:
            print("\033[31mПопробуйте еще раз")
            prt_gen()
        
def op_minus():
    global score
    if w == 'q' or w == 'Q':
        os.system('clear')
        exit()
    else:
        try:
            ww = int(w)
            if ww == aa - bb:
                print("\033[32mверно")
                score += 1
                if score > highscore:
                    file = open('score.nfr', 'w')
                    file.write(str(score))
                    file.close()
                print("Счет: ", score)
                rnd_gen()
            else:
                print("\033[31mневерно")
                prt_gen()
        except ValueError:
            print("\033[31mПопробуйте еще раз")
            prt_gen()
        
rnd_gen()
