# CMPS 2200 Assignment 3
## Answers

**Name:** Sofia Bareiro 


Place all written answers from `assignment-03.md` here for easier grading.

1a) Start with the largest coin denomination <= N. Use as many of that coin as possible. Substract the total value of those coins from N. Repeat with the next smaller denomination until N=0. 

1b) Greedy-Choice property: at every step, the algorithm chooses the largest power of 2 that fits into the remaining amount. Since powers of 2 are non-overlapping and can only be summed uniquely (binary representation), using the largest coin doesn't prevent an optimal solution for the remainder. Optimal strubstructure: once the largest coin is chosen, the problem reduces to a smaller subproblem of the same structure: making change for N-coin. The optimal solution to the full problem includes the optimal solution to this subproblem. In conclusion, this greedy algorithm produces the binary representation of N, where each power-of-2 coin corresponds to a 1 in a binary digit. Thus, it is provably optimal. 

1c) Work: The total number of steps corresponds to the number of 1s in the binary representation of N. In the worst case (all bits are 1), this is O(log N) additions to the result list. Span: since each coin decision depends on the current N only and updates it, the operations are inherently sequential. So, Span = O(log N) in worst-case time (each subtraction and append is constant time but done log N times in worst case).

2a) The greedy 

