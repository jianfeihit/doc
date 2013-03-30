'''
Created on 2013-3-30

@author: jianfeihit
'''
#下列引用一旦开启将会调用truediv
from __future__ import division

class ValueTestor(object):
    def __div__(self,other):
        print 'div is called'
        return 1
    
    def __floordiv__(self,other):
        print 'floordiv is called'
        return 2
    
    def __truediv__(self,other):
        print 'truediv is called'
        return 3

if __name__ == '__main__':
    t = ValueTestor()
    print t/1
    print t//1
