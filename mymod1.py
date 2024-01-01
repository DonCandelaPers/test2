"""Module mymod1.py is part of the toy package mypackage, used to test
various things.
"""
THIS_IS = 'mymod1.py 11/28/23 D.C.'

def twice(x):
    return x+x

if __name__=='__main__':
    print(f'Running {THIS_IS}')
    print(f'twice(3) = {twice(3)}')
