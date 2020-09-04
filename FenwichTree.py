class FenwichTree:
    def __init__(self, nums):
        self.BIT_arr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.BIT_arr[i + 1] = nums[i]
        for i in range(1, len(self.BIT_arr)):
            j = i + (i & -i)
            if j < len(self.BIT_arr):
                self.BIT_arr[j] += self.BIT_arr[i]

    def update(self, i, delta):
        i += 1
        while i < len(self.BIT_arr):
            self.BIT_arr[i] += delta
            i += (i & (-i))
            
    def setVal(self, i, val):
        i += 1
        self.update(i, val - self.BIT_arr[i])

    def prefix(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.BIT_arr[i]
            i -= (i & (-i))
        return res

    def intervalSum(self, i, j):
        return self.prefix(j) - self.prefix(i - 1)