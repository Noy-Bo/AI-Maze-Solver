import fibheap

heap1 = fibheap.makefheap()

num_list1 = [1,4,2]

for num in num_list1:
    fibheap.fheappush(heap1, num)

heap1.delete(4)
pass
# fuck fibonacci