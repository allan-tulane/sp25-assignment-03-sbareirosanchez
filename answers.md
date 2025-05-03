# CMPS 2200 Assignment 3
## Answers

**Name:** Sofia Bareiro 


Place all written answers from `assignment-03.md` here for easier grading.

1a) Start with the largest coin denomination <= N. Use as many of that coin as possible. Substract the total value of those coins from N. Repeat with the next smaller denomination until N=0. 

1b) Greedy-Choice property: at every step, the algorithm chooses the largest power of 2 that fits into the remaining amount. Since powers of 2 are non-overlapping and can only be summed uniquely (binary representation), using the largest coin doesn't prevent an optimal solution for the remainder. Optimal strubstructure: once the largest coin is chosen, the problem reduces to a smaller subproblem of the same structure: making change for N-coin. The optimal solution to the full problem includes the optimal solution to this subproblem. In conclusion, this greedy algorithm produces the binary representation of N, where each power-of-2 coin corresponds to a 1 in a binary digit. Thus, it is provably optimal. 

1c) Work: The total number of steps corresponds to the number of 1s in the binary representation of N. In the worst case (all bits are 1), this is O(log N) additions to the result list. Span: since each coin decision depends on the current N only and updates it, the operations are inherently sequential. So, Span = O(log N) in worst-case time (each subtraction and append is constant time but done log N times in worst case).

2a) The greedy algorithm from Part 1 fails in Fortuito due to the arbitrary nature of the coin denominations. A simple counterexample demonstrates this failure: consider the coin denominations {1,2,3} and a target of N=6. A greedy approach would first pick the largest denomination not exceeding 6, which is 4, leaving a remainder of 2. Then it would pick two 1s, totaling three coins. However, the optimal solution is to use two 3s, which sums to 6 using only two coins. This example clearly shows that the greedy algorithm does not always produce the minimal number of coins when denominations are arbitrary.

2b) Even though the greedy algorithm doesn’t always work in this problem, we can still say that it has optimal substructure. This means that the best way to make change for an amount N depends on the best ways to make change for smaller amounts like N-Di, where Di is any coin value. In other words, if we already know the minimum number of coins needed for smaller amounts, we can use that information to find the best solution for N. This works because combining the best smaller solutions always gives us the best overall answer. 

2c) We can use dynamic programming to solve this problem by building up solutions from smaller amounts. We create a list where each spot represents the smallest number of coins needed to make that amount. We start from 0 and go up to N, trying every coin to see which one gives the best result. For each amount, we choose the option that gives the fewest coins. This way, we avoid repeating the same calculations. The total work is O(N*k), where k is the number of coin types, and the span is also O(N*k) since we go through each amount step by step. 

