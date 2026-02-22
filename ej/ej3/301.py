def val_check(x):
    while x != 0:

        if (x % 10) % 2 != 0:
            print('Not valid')
            return
        x //= 10
        
    print('Valid')

jo = int(input())
val_check(jo)

    
