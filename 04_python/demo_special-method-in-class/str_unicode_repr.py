#-*-coding:utf-8-*-
'''
Created on 2013-3-30

@author: jianfeihit
'''
class StrTestor(object):
    def __repr__(self):
        print 'repr is called'
        return 'repr'
    
    def __str1__(self):
        print 'str is called'
        return 'str'
    
    def __unicode__(self):
        print 'unicode is called'
        return 'unicode'
    
if __name__ == '__main__':
    t = StrTestor()
    print t
    print str(t)
    print unicode(t)