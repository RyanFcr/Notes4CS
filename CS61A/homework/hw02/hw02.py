HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x <10 and x == 8:
        return 1
    elif x >=10:
        if x % 10 == 8: 
            return num_eights(x//10)+1
        else:
            return num_eights(x//10)
    else:
        return 0


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(18)
    2
    >>> pingpong(19)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(38)
    2
    >>> pingpong(48)
    8
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # 以下代码复杂度太高了，会超时
    # if n == 1:
    #     return 1
    # elif n == 2 :
    #     return 2
    # elif (num_eights(n-1) != 0) or ((n-1) % 8 == 0):
    #     return pingpong(n - 2)
    # else:
    #     return 2 * pingpong(n-1)-pingpong(n-2) 
    # 这种方法好像因为没有递归而不行
    # def pp(n):
    #     if(n <8):
    #         return n,1
    #     else:
    #         re,re_dir=pp(n-1)
        
    #     if (num_eights(n)!=0)or n %8 ==0:
    #         return re+re_dir,-re_dir
    #     else:
    #         return re+re_dir,re_dir
    

    # r,r_dir=pp(n)    
    # return r


    def helper(index,ppn,dir):
        if(index == n):
            return ppn
        elif(num_eights(index)!=0)or((index)%8==0):
            return helper(index+1,ppn-dir,-dir)
        else:
            return helper(index+1,ppn+dir,dir)
    return helper(1,1,1)

    # index = 1
    # ppn = 1
    # dir =1
    # while(index!=n):
    #     index+=1
    #     ppn+=dir
    #     if(num_eights(index)!=0)or((index)%8==0):
    #         dir = -dir
    # return ppn
    

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    missing_sum = 0
    num1 = n % 10
    num2 = (n//10) % 10
    if n < 10:
        return 0
    elif num1 == num2:
        return missing_digits(n//10)
    else:
        return missing_digits(n//10) + (n%10)-1-(n//10)%10


def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    def last_largest_coin(n):
        y = 0
        if(n == 1):
            return 0
        elif(n ==5):
            return 1
        elif(n == 10):
            return 5
        elif( n == 25):
            return 10

    def count_coins_helper(index,max):
        if index < 0:
            return 0
        elif max == 0:
            return 0
        elif max == 1 or index == 0:
            return 1
        else:
            return count_coins_helper(index-max,max)+count_coins_helper(index,last_largest_coin(max))

    if(total >= 25):
        return count_coins_helper(total,25)
    elif(total >= 10):
        return count_coins_helper(total,10)
    elif(total >= 5):
        return count_coins_helper(total,5)
    else:
        return count_coins_helper(total,1)
from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))
    # 主要参考了 https://blog.csdn.net/qq_42103298/article/details/123773235

