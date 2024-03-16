class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
      #using two pointers
        left, right = 0, n - 1

      #compare adjacent elements using the left pointer.
      #If any adjacent pair violates the non-decreasing order, we return 0. 
      #Otherwise, we continue moving the left pointer until we reach the end of the array, and then return 1 if no violations are found.
        while left < right:
            if arr[left] > arr[left + 1]:
                return 0
            left += 1

        return 1
