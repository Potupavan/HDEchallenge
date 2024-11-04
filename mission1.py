def square(x):
    return x * x  if x >= 0 else 0

def negative_squares(numbers):
    return sum(map(square, map(int, numbers.split())))

def sum_squares(count, accumulator=[]):
    if count == 0:
        print('\n'.join(map(str, accumulator)))
        return
    
    num_count = int(input())
    numbers = input()
    current_sum =negative_squares(numbers)
    
    sum_squares(
        count - 1, 
        accumulator + [current_sum]
    )
N = int(input())
sum_squares(N)
