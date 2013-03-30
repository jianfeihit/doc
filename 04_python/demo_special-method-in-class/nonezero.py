#-*-coding:utf-8-*-
'''
Created on 2013-3-30

@author: jianfeihit
'''
class NonzeroTestor(object):
    def __nonzero__(self):
        print 'nonzero is called'
        return True
    
if __name__ == '__main__':
    t = NonzeroTestor()
    print bool(t)