import random


def enviroment():
    disaster = random.choice(open('disaster.txt').readlines())
    return disaster


def bunker():
    random_bunker = random.choice(open('bunker.txt').readlines())
    return random_bunker


def generate(x):
    for i in range(x):
        sex = random.randint(0,1)
        age = random.randint(14,100)
        cf = random.randint(0,6)
        weight = random.choice(open('weight.txt').readlines())
        height = str(random.randint(155,199))
        ht = random.choice(open('htrait.txt').readlines())
        htf = random.choice(open('htrait(f).txt').readlines())
        health = random.choice(open('health.txt').readlines())
        job = random.choice(open('job.txt').readlines())
        exp = random.choice(open('exp.txt').readlines())
        fear = random.choice(open('fear.txt').readlines())
        item = random.choice(open('item.txt').readlines())


        f = open(f'Player{i+1}.txt', 'w')
        if sex == 1:
            f.write(f'Пол: Мужской, {str(age)}')
        else:
            f.write(f'Пол: Женский, {str(age)}')
        if cf == 1:
            f.write(" Чайлдфри")
        f.write(f". Телосложение: {weight}".rstrip())
        f.write(f". Рост: {height}".rstrip())
        if sex == 1:
            f.write(f". Человеческая черта: {ht}".rstrip() )
        else:
            f.write(f". Человеческая черта: {htf}".rstrip())
        f.write(f". Здоровье: {health}".rstrip())
        f.write(f". Работа: {job}" .rstrip() + f" {exp}".rstrip())
        f.write(f". Фобия: {fear}".rstrip())
        f.write(f". Инвентарь: {item}".rstrip())
        f.close()