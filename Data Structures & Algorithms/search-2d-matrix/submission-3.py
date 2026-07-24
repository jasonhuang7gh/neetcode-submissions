class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Searching in 2D matrix is like searching in 1D array
        # except the coordinates are modded by matrix dimensions.
        # Time: O(log(m * n)) / Space: O(1)
        # WIP


        # Locate the list where target is within and then do binary search.
        # More space efficient because binary search is in-place.
        # Time: O(m + log(n)) / Space: O(1)
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                i, j = 0, len(row) - 1
                while(i <= j):
                    k = (i + j) // 2
                    # if the midpoint is the target, index has been found
                    if target == row[k]:
                        return True
                    # if target in upper half, set i as midpoint (non-inclusive)
                    elif row[k] < target:
                        i = k + 1
                    # if target in lower half, set j as midpoint (non-inclusive)
                    else:
                        j = k - 1
        # after binary search of whole array, target is not found
        return False


        # # Append all lists into one list for regular binary search.
        # # Time: O(m + log(m * n)) / Space: O(m * n)
        # combined = []
        # for i in range(len(matrix)):
        #     combined += matrix[i]
        # # i is the lower boundary, j is the upper boundary
        # # at the start, i is the first element and j is the last
        # i, j = 0, len(combined) - 1
        # while(i <= j):
        #     k = (i + j) // 2
        #     # if the midpoint is the target, index has been found
        #     if target == combined[k]:
        #         return True
        #     # if target in upper half, set i as midpoint (non-inclusive)
        #     elif combined[k] < target:
        #         i = k + 1
        #     # if target in lower half, set j as midpoint (non-inclusive)
        #     else:
        #         j = k - 1
        # # after binary search of whole array, target is not found
        # return False
