def funkcija():
    import random

    list1 = []

    for i in range(2):
        list0 = ''
        for i in range(random.randint(5,25)):
            text = str(random.randint(0,20)) + ','
            list0 += text
        list0 = list0.rstrip(',')
        list1.append(list0)


    rindas = [line.rstrip('\n') for line in list1]
    rindu_max = []

    for i in range(len(rindas)):
        line0 = rindas[i].split(',')
        s = 0
        for j in range(len(line0)):
            if int(line0[j])>s: s = int(line0[j])
        rindu_max.append(s)

    print('Sarakstu max:')
    print(rindu_max)



if __name__ == '__main__':
    funkcija()