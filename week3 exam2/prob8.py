class pair_of_sum:
  def twoSum(self, nums, target):
       index = {}
       for i, num in enumerate(nums):
           if target - num in index:
               return (index[target - num], i+1 )
           index[num] = i+1
print("index1=%d, index2=%d" % pair_of_sum().twoSum((20,10,40,50,60,70),50))

