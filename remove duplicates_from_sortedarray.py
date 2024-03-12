class Solution(object):
  def removeDuplicates(self, nums):
    """

    Args:
        nums: A sorted list of integers.

    Returns:
        The number of unique elements (up to two occurrences each) in the first part of the array.
    """

    k = 0  
    for num in nums:
      if k < 2 or num != nums[k - 2]:  # Checking for at most two duplicates
        nums[k] = num
        k += 1
    return k
