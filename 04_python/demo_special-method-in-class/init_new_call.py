#-*-coding:utf-8-*-
'''
Created on 2013-3-27

@author: jianfeihit
'''
class Testor(object):
    def __call__(self):
        print "__call__ method is called"
        
    def __init__(self):
        print "__init__ method is called"
    
    """
        将new1修改为new的时候，t1()将会展现不同的风格
    """
    def __new1__(self):
        print "__new__ method is called"
        return self
        
if __name__ == '__main__':
    t1 = Testor()
    t1()
        