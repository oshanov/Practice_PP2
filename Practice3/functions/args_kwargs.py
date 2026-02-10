def my_func(*args):                 #args is tuple
    print("Type:", type(args))
    print('first:', args[0])
    print('second:', args[1])
    print('third:', args[2])

my_func("Linear Algebra", 'Dicrete math', 'Calculus')

##########################

def greetings(greet, *names):
    for x in names:
        print(greet, x)

greetings('Hi', 'Didar', 'Ali', 'Asa', 'Mansur')

#########################

def sum_calc(*numbers):
    s = 0
    for x in numbers:
        s += x
    return s

print(sum_calc(1,2,3,4,5))
print(sum_calc(0,9,8,7,6,))

###########################

def max_finder(*nums):
    if len(nums) == 0:
        return None
    max_num = nums[0]
    for x in nums:
        if x > max_num:
            max_num = x
    return max_num

print(max_finder(1,5,2,8,3,76,441,7889,345,1223,76,-4353457))

#####################################
def fun_func(**kids):                           #kwargs is dictionary, available only by key arguments value
    print('his last name is', kids['surname'])

fun_func(fname = 'tobias', surname = 'kirk')

#################################

def uga_buga(**info):
    print('type:', type(info))
    print('name:', info['name'])
    print('surname:', info['sname'])
    print('all', info)

uga_buga(title = 'Sir', name = "Alex", sname = "Ferguson")

#################################

def profile_info(user, **table):
    print('Hello,', user)
    print('additional info:')

    for x,y in table.items():
        print( f'\t{x}: {y}')

profile_info('mqxdali', experience = "12 years", games_played = 12315, won_percentage = "34%" )