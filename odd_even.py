def even(num):
    if num % 2 == 0:
        return f"{num} is Even."
    else:
        return f"{num} is Odd."
    
num = 2
ans = even(num)
print(ans) #Output: 2 is Even.