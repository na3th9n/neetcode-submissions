class TimeMap:

    def __init__(self):
        # double hashmap?
        # array for keys
        # hassmap with a value as an array, index of the array will be for the timestamp

        self.keys = {} # key = string, value = [list of [values, timestamp]]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []

        self.keys[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keys.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1

            else:
                r = m - 1
                
        return res

        

                
