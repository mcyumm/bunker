import random
x = int(input())
y = random.randint(0, 6)
disaster = random.choice(open('disaster.txt').readlines())
bunker = (open(f'Бункер{y}.txt'))
h = open('Катастрофа.txt', 'w')
h.write(disaster)
h.close()
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


    f = open(f'Игрок {i+1}.txt', 'w')
    if sex == 1:
        f.write(f'Пол: Мужской, {str(age)}')
    else:
        f.write(f'Пол: Женский, {str(age)}')
    if cf == 1:
        f.write("\nЧайлдфри")
    f.write(f"\nТелосложение: {weight}".rstrip())
    f.write(f"\nРост: {height}".rstrip())
    if sex == 1:
        f.write(f"\nЧеловеческая черта: {ht}".rstrip() )
    else:
        f.write(f"\nЧеловеческая черта: {htf}".rstrip())
    f.write(f"\nЗдоровье: {health}".rstrip())
    f.write(f"\nРабота: {job}" .rstrip() + f" {exp}".rstrip())
    f.write(f"\nФобия: {fear}".rstrip())
    f.write(f"\nИнвентарь: {item}".rstrip())
    f.close()