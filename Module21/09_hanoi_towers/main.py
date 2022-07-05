def move(n, init_stick, final_stick):
    if n == 1:
        print(f'Переложить диск {n} со стержня {init_stick} на стержень {final_stick}')
    else:
        temp_stick = (6 - init_stick) - final_stick
        move(n - 1, init_stick, temp_stick)
        print(f'Переложить диск {n} со стержня {init_stick} на стержень {final_stick}')
        print(f'Переложить диск {n - 1} со стрежня {temp_stick} на стержень {final_stick}')
        return


move(2, 1, 3)


# Оставлю решение, я его не сам решил :)
# Так что можешь на гугл не тратить время))
