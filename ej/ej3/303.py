def calc(s):
    dic = {'ZER':'0', 'ONE':"1", "TWO":"2", "THR":"3", "FOU":"4", "FIV":"5", "SIX":"6","SEV":"7", "EIG":"8", "NIN":"9"}
    if '+' in s:
        parts = s.split("+")
    elif '*' in s:
        parts = s.split('*')
    elif '-' in s:
        parts = s.split('-')

    for i in range(0, len(s), 3):
        part = s[i:i+3]
