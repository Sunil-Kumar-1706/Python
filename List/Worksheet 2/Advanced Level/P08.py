# Write a Python function to find the maximum sum sub-sequence in a list 
# (sub-sequence, not necessarily contiguous).

def fun(l):
    max_seq=[x for x in l if x>0]

    if max_seq:
        return sum(max_seq),max_seq
    else:
        max_ele = sum(l)
        return max_ele,[max_ele]
    
l=[2, -1, 2, 3, 4, -5]
max_sum,max_seq=fun(l)
print("Max_sum =",max_sum,"\nMax_seq =",max_seq)