import time
print("Rosalind Problems: Rabbits and Recurrence Relations")
def rabbit_recurrence(months, offsprings):
    parent, child= 1,1
    for i in range(months- 1):
        child, parent= parent, parent+ (child*offsprings)
    return child
tic= time.process_time()
print(rabbit_recurrence(int(input("pleasen enter months: ")), int(input("pleasen enter number of offsprings: "))))
toc= time.process_time()
print("time taken is: "+str((toc-tic)*1000)+"ms")

def rabbit_recursive(months, offsprings):
    if months<2:
        return months
    else:
        return rabbit_recursive(months-1, offsprings)+ rabbit_recursive(months-2, offsprings)*offsprings

def rabbit_iterative(months, offsprings):
    parent_1, parent_2 = 1, 1
    parent = 1  # Just a place holder in case n is too small
    for _ in range(2, months):
        parent = parent_1 + parent_2*offsprings
        parent_2, parent_1 = parent_1, parent
    return parent

def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)

# print(fib(6,2))
# Fn-1 + Fn-2 - Fn-(m+1)