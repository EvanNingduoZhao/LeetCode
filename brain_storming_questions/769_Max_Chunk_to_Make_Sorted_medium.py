class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_seen_so_far=0
        num_of_chunks=0
        for i in range(len(arr)):
            max_seen_so_far=max(max_seen_so_far,arr[i])
            if i==max_seen_so_far:
                num_of_chunks+=1
        return num_of_chunks