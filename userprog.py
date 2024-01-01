"""userprog.py tests ability to import and use package mypackage.
"""
THIS_IS = 'userprog.py 11/28/23 D.C.'

from mypackage.mymod1 import twice

print(THIS_IS)
print(f'twice("foo") = {twice("foo")}')

