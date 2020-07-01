from Bubble_Sort import bubble_sort
from Insertion_Sort import insertion_sort
from Selection_Sort import selection_sort
from Merge_Sort import merge_sort
from Heap_Sort import heap_sort
from Quick_Sort import quick_sort
import time
import random
randomlist= random.sample(range(0,1000000),1000000)
randomlist1=randomlist.copy()
randomlist2=randomlist.copy()
randomlist3=randomlist.copy()
randomlist4=randomlist.copy()
randomlist5=randomlist.copy()
randomlist6=randomlist.copy()
#print(randomlist)


# start_time = time.time()
# selection_sort(randomlist1)
# print("selection--- %s seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# bubble_sort(randomlist2)
# print("bubble--- %s seconds ---" % (time.time() - start_time))
#
#
# start_time = time.time()
# insertion_sort(randomlist3)
# print("insertion--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
merge_sort(randomlist4)
print("merge--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
heap_sort(randomlist5)
print("heap--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
quick_sort(randomlist6)
print("quick--- %s seconds ---" % (time.time() - start_time))