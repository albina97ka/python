import random
    #cherepaxa = (turtle.shape('turtle'), turtle.forward(50), turtle.left(90), turtle.forward(50), turtle.left(90), turtle.forward(50), turtle.right(90), turtle.forward(50), turtle.right(90), turtle.forward(50))
def hangman():
    import turtle
    print ('Привет! Добро пожаловать в игру Виселица')
    print ('ПРАВИЛА ИГРЫ:')
    print ('Компьютер загадывает слово, которое вы должны угадать, используя буквы алфавита и возможность совершить ограниченное количество ошибок.. Вы вписываете букву, после чего, в случае присутствия данной буквы в загаданном слове, она отображается вместо подчеркивания . Если в слове данная буква встречается несколько раз, то показываются все случаи присутствия этой буквы в слове. Если указана неверная буква, то на экране рисуется деталь виселицы. Как только все детали виселицы будут нарисованы, то вы больше не может угадывать слово в данном раунде.')
    #(turtle.shape('turtle'), turtle.forward(50), turtle.left(90), turtle.forward(50), turtle.left(90), turtle.forward(50), turtle.right(90), turtle.forward(50), turtle.right(90), turtle.forward(50))
    wordlist = ['мандарин', 'яблоко', 'груша', 'ананас', 'апельсин', 'манго', 'киви', 'авокадо', 'абрикос', 'нектарин', 'маракуйя', 'папайя', 'персик', 'грейпфрут']
    print('Тема: Фрукты')
    secret = random.choice(wordlist)
    guesses = '-'
    turns = 5

    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_',end=' ')
                missed += 1
        if missed == 0:
            print ('Ты выйграл!')
            break

        guess = input('Назови букву:')
        guesses += guess
        if guess not in secret:
            turns -= 1
            print('не угадал')
            print('Осталось попыток: ', turns)
            if turns < 5: turtle.reset(), turtle.tracer(1), turtle.width(3), turtle.down(), turtle.forward(170), turtle.up(), turtle.backward(25), turtle.down(), turtle.left(90), turtle.forward(150), turtle.right(90), turtle.forward(5), turtle.up(), turtle.left(180), turtle.forward(5), turtle.down(), turtle.forward(80), turtle.up(), turtle.backward(7), turtle.down(), turtle.left(90), turtle.forward(50), turtle.up(), turtle.goto(0,0), turtle.left(90), turtle.forward(125), turtle.left(45), turtle.down(), turtle.forward(25), turtle.up(), turtle.goto(165,0), turtle.left(90), turtle.down(), turtle.forward(25), turtle.up(), turtle.goto(145,115), turtle.down(), turtle.forward(50)
            if turns < 4: turtle.up(), turtle.goto(80,97), turtle.down(), turtle.circle(12.360)
            if turns < 3: turtle.up(), turtle.goto(72,75), turtle.left(180), turtle.down(), turtle.forward(20), turtle.up(), turtle.backward(20), turtle.right(90), turtle.down(), turtle.forward(20)
            if turns < 2: turtle.up(), turtle.goto(72,75), turtle.left(45), turtle.down(), turtle.forward(35)
            if turns < 1: turtle.left(45), turtle.forward(20), turtle.up(), turtle.backward(20), turtle.right(90), turtle.down(), turtle.forward(20), print('Вы проиграли! (￢_￢;)')

ans = 'да'
while ans == 'да':
    hangman()
    print('Хочешь сыграть снова? (да или нет)')
    ans = input()