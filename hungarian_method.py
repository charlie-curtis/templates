# https://leetcode.com/problems/minimum-time-to-break-locks-ii/

from scipy.optimize import linear_sum_assignment
import numpy as np
class Solution:
    def hungarian(self, adj: List[int]) -> int:
        
        cost_matrix = np.array(adj)

        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        optimal_cost = cost_matrix[row_ind, col_ind].sum()

        return int(optimal_cost)
