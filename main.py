import random
x = int(input())
for i in range(x):


    sex = random.randint(0,1)
    age = random.randint(14,100)
    cf = random.randint(0,4)
    weight = random.choice(open('weight.txt').readlines())
    height = str(random.randint(155,199))
    ht = random.choice(open('htrait.txt').readlines())
    htf = random.choice(open('htrait(f).txt').readlines())
    health = random.choice(open('health.txt').readlines())
    job = random.choice(open('job.txt').readlines())
    exp = random.choice(open('exp.txt').readlines())
    fear = random.choice(open('fear.txt').readlines())
    item = random.choice(open('item.txt').readlines())


    f = open(f'player{i+1}.txt', 'w')
    if sex == 1:
        f.write(f'Пол: Мужской, {str(age)}')
    else:
        f.write(f'Пол: Женский, {str(age)}')
    if cf == 1:
        f.write("\nЧайлдфри")
    f.write(f"\nТелосложение: {weight}".rstrip())
    f.write(f"\nРост: {height}")
    if sex == 1:
        f.write(f"\nЧеловеческая черта: {ht}" )
    else:
        f.write(f"\nЧеловеческая черта: {htf}")
    f.write("Здоровье: " + health)
    f.write(f"Работа: {job}" .rstrip() + f" {exp}")
    f.write(f"Фобия: {fear}".rstrip())
    f.write(f"\nИнвентарь: {item}".rstrip())
    f.close()