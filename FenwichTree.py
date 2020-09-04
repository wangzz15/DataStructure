class FenwichTree:
    def __init__(self, nums):
        self.arr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.arr[i + 1] = nums[i]
        for i in range(1, len(self.arr)):
            j = i + (i & -i)
            if j < len(self.arr):
                self.arr[j] += self.arr[i]

    def update(self, i, delta):
        i += 1
        while i < len(self.arr):
            self.arr[i] += delta
            i += (i & (-i))
            
    def setVal(self, i, val):
        i += 1
        self.update(i, val - self.arr[i])

    def prefix(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.arr[i]
            i -= (i & (-i))
        return res

    def intervalSum(self, i, j):
        return self.prefix(j) - self.prefix(i - 1)