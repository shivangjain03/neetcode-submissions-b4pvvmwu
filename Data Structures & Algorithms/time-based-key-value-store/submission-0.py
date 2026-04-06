class TimeMap:
    # For get fucntionality we need to get the value using binary search
    # In order to use binary search we have to make sure to get value in increasing timestamp only


    def __init__(self):
        # Initialising a dict 
        self.maindict = {}
        # Value = [val,timestamp]
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.maindict:
            self.maindict[key].append([value,timestamp])
        else:
            self.maindict[key] = [[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.maindict:
            return ""
        else:
            temp_l = self.maindict[key]
            l = 0
            r = len(temp_l)-1
            res = ""
            while l<=r:
                mid = (l+r)//2
                if temp_l[mid][1] == timestamp:
                    return temp_l[mid][0]

                elif temp_l[mid][1]<timestamp:
                    l = mid+1
                    res = temp_l[mid][0]
                else:
                    r = mid-1
            return res

