def fib(n):#функция чтобы не заморачиваться с подсчетом чисел
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

def solution(A):
    summa=0
    itog=0
    for i in range(1,A+1):#ищем максимум
        if fib(i)%2==0:
            summa+=fib(i)
            
    while(summa>0):#считаем сумму чисел максимума
        itog+=summa%10
        summa=summa//10
    return itog #не работает, доработай!
    #https://certification.mail.ru/lc/editor/5494f2bb-0c5f-448c-a1e0-47d58aea02e8/
