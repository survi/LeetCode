class MyCalendar(object):

    def __init__(self):
        self.booklist = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        end = end - 1
        for bl in self.booklist:
            if start >= bl[0] and start <=bl[1]:
                return False
            elif start <= bl[0] and end >= bl[1]:
                return False
            elif end >= bl[0] and end <= bl[1]:
                return False
        self.booklist.append([start,end])
        return True