class Solution:
    def solve(self, heights, k):
        ans = list()
        queue = list()
        for i in reversed(range(len(heights))):
            height = heights[i]

            if len(queue) > k:
                queue.pop(0)

            while queue and queue[0] < height:
                queue.pop(0)

            if not queue:
                ans.append(i)

            queue.append(height)
        
        return ans[::-1]
