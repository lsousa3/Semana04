import time
def countdown(t):
    while t:
        min, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Contagem Terminada!')


t = input("Digite o tempo em segundos:")
countdown(int(t))

