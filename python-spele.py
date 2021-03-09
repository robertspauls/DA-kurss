list1 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

def error():
    print('Neatbilstoša vērtība!')

def error2():
    print('Lauciņš ir aizņemts!')

def test_input(a):
    try:
        a = int(a)
    except:
        return True
    if a > 3 or a < 1:
        return False
    else: return True

def test_gajiens(b):
    if list1[b] == '_':
        return True

def uzvaretajs(e):
    print('Uzvarēja spēlētājs ' + e + '!')

def test_uzvara1(c):
    if list1[0] == list1[1] == list1[2] == c: return True
    elif list1[3] == list1[4] == list1[5] == c: return True
    elif list1[6] == list1[7] == list1[8] == c: return True
    elif list1[0] == list1[3] == list1[6] == c: return True
    elif list1[1] == list1[4] == list1[7] == c: return True
    elif list1[2] == list1[5] == list1[8] == c: return True
    elif list1[0] == list1[4] == list1[8] == c: return True
    elif list1[2] == list1[4] == list1[6] == c: return True

def printet():
    print(list1[0],list1[1],list1[2])
    print(list1[3],list1[4],list1[5])
    print(list1[6],list1[7],list1[8])

def main_funkcija():

    printet()

    for i in range(1,10):
        print('---------------')
        if i % 2 == 1:
            print('Gājiens spēlētājam X')
            d = 'X'
            while d == 'X':
                while d == 'X':
                    line1 = input('Ievadiet rindu (1-3):')
                    test_input(line1)
                    if test_input(line1):
                        break
                    error()

                while d == 'X':
                    kolona1 = input('Ievadiet kolonu (1-3):')
                    test_input(line1)
                    if test_input(line1):
                        break
                    error()

                gajiens = (int(line1) - 1) * 3 + int(kolona1) - 1
                if test_gajiens(gajiens):
                    break
                error2()

            list1[gajiens] = d
            if test_uzvara1(d):
                uzvaretajs(d)
                break
            printet()

        else:
            print('Gājiens spēlētājam 0')
            d = '0'
            while d == '0':
                while d == '0':
                    line1 = input('Ievadiet rindu (1-3):')
                    test_input(line1)
                    if test_input(line1):
                        break
                    error()

                while d == '0':
                    kolona1 = input('Ievadiet kolonu (1-3):')
                    test_input(line1)
                    if test_input(line1):
                        break
                    error()

                gajiens = (int(line1) - 1) * 3 + int(kolona1) - 1
                if test_gajiens(gajiens):
                    break
                error2()

            list1[gajiens] = d


            if test_uzvara1(d):
                uzvaretajs(d)
                break
            printet()
    if i == 9:
        print('Spēle beidzās neizšķirti!')
    else: print('Error')

if __name__ == '__main__':
    main_funkcija()
