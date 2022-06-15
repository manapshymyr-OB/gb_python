###


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'stans', 'dsa','Manap'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]



def gen_of_people():
    i = 0
    tutors_len = len(tutors)
    klasses_len = len(klasses)
    while i < tutors_len:
        if i < klasses_len:
            yield (tutors[i], klasses[i])
            i += 1

        else:

            yield (tutors[i], None)
            i += 1

for gen in gen_of_people():
    print(gen)
