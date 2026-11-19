from multiprocessing import Value


class ArrTrack():
 
    def __init__(self,arr) -> None:  
        self.arr = arr
        self.comparison = 0 
        self.arrayAccess = 0
        self.write = [None]
        self.access = [None]
        self.arrayAccesses = [0]
        self.comparisons = [0]
        self.snapshots = [arr.copy()]

    def track(self,arr,key, acess_type=None):
        if acess_type == "get":
            self.write.append(None)
            self.access.append(key)
        else:
            self.access.append(None)
            self.write.append(key)
        self.snapshots.append(arr.copy()) 
        self.arrayAccesses.append(self.arrayAccess)
        self.comparisons.append(self.comparison)

    def __getitem__(self,key):
        self.arrayAccess += 1 
        self.track(self.arr,key,"get")
        return self.arr[key]
        
    def __setitem__(self,key,value):
        self.arrayAccess += 1
        self.arr[key] = value
        self.track(self.arr,key,"set")

    
    def greater(self, i, value):
        self.comparison += 1 
        self.track(self.arr, i, "get")
        return self[i] > value

    def less(self,i,value):
        self.comparison += 1 
        self.track(self.arr, i, "get")
        return self[i] < value

    def __len__(self):
        return len(self.arr)

class ArrTrackForPivots(ArrTrack):

    def __init__(self, arr) -> None:
        super().__init__(arr)
        self.pivot = [None]
        self.current_pivot = None

    def track(self,arr,key, acess_type):
        self.pivot.append(self.current_pivot)
        super().track(arr,key,acess_type)

    def p(self, key):
        self.current_pivot = key
        self.arrayAccess += 1
        self.track(self.arr,key,"get")
        return self.arr[key]
