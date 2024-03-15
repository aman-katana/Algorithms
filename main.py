class Solution(object):
    def checkRecord(self, s: str):
        """
        :type s: str
        :rtype: bool
        """
        absent = 0
        late = 0
        for i in s:
            if i == 'A':
                absent += 1
                late = 0
            elif i == 'L':
                late += 1
            else:
                late = 0
            if late == 3 or absent > 1:
                return False
        else:
            return True
