# input
# customers: an array of positive integers representing the queue. Each integer represents a customer,
# and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.
#
# Important
# Please look at the examples and clarifications below, to ensure you understand the task correctly :)
#
# Examples
# queue_time([5,3,4], 1)
# # should return 12
# # because when n=1, the total time is just the sum of the times
#
# queue_time([10,2,3,3], 2)
# # should return 10
# # because here n=2 and the 2nd, 3rd, and 4th people in the
# # queue finish before the 1st person has finished.
#
# queue_time([2,3,10], 2)
# # should return 12
# Clarifications
# There is only ONE queue serving many tills, and
# The order of the queue NEVER changes, and
# The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
# N.B. You should assume that all the test input will be valid, as specified above.


def queue_time(customers, n):
    tills = [0] * n
    for customer in customers:
        tills[tills.index(min(tills))] += customer
    return max(tills)


# print(queue_time([5, 3, 4], 1))
print(queue_time([2, 3, 10], 2))