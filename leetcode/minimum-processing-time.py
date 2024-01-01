class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        _max = float('-inf')
        for i in range(len(processorTime)):
            for j in range((i*4),(i + 1)*4):
                _max = max(_max, tasks[j] + processorTime[i])
        return _max

        