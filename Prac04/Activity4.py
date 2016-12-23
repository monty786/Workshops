__author__ = 'jc437351'

def list_avg(L):
    try:
     avg= sum(L)/len(L)
    except TypeError:
        print("Not all elements numeric")
        return None
    except ZeroDivisionError:
        print("List is empty")
        return None
    except:
        print("Unknown Error")
        return avg()
print(list_avg([1,2,3]))
#print(list_avg([1,'a',3]))
#print(list_avg([]))