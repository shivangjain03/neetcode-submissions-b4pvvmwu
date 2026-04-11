class TimeMap:

    def __init__(self):
        self.dict1 = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict1:
            self.dict1[key].append([value,timestamp])
        else:
            self.dict1[key] = [[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict1:
            return ""
        else:
            low = 0
            lis = self.dict1[key]
            print(lis)
            high = len(self.dict1[key])-1
            res = ""

            while low<=high:
                mid = (low+high)//2

                if lis[mid][1] == timestamp:
                    return lis[mid][0]

                elif lis[mid][1]>timestamp:
                    high = mid-1
                else:
                    low = mid+1
                    res = lis[mid][0]
            return res
