class Solution(object):
    def maxSum(self, matrix):  
        """
        Finds the maximum sum of an hourglass in the given matrix.

        Args:
            matrix: A list of lists containing integers, representing the matrix.

        Returns:
            The maximum sum of an hourglass in the matrix.
        """

        m = len(matrix)
        n = len(matrix[0])
        max_sum = -float('inf') 

        
        for i in range(m - 2):
            for j in range(n - 2):
                current_sum = sum([matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
                                   matrix[i + 1][j + 1],
                                   matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]])
                max_sum = max(max_sum, current_sum)

        return max_sum
