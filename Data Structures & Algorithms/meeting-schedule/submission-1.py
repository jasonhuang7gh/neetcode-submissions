"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by start time and then look for a conflict
        # Time: O(n * log(n)) / Space: O(1)

        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            end_1 = intervals[i-1].end
            start_2 = intervals[i].start
            if start_2 < end_1:
                return False
        return True