class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]
        if end >= start: # no cycle
            return list(range(start, end + 1))
        else: # cycle
            return list(range(1, end + 1)) + list(range(start, n + 1))