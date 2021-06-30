# A. Fair Playoff
# time limit per test
# 2 seconds
# memory limit per test
# 256 megabytes
# input
# standard input
# output
# standard output

# Four players participate in the playoff tournament. The tournament is held according to the following scheme: the first player will play with the second, and the third player with the fourth, then the winners of the pairs will play in the finals of the tournament.

# It is known that in a match between two players, the one whose skill is greater will win. The skill of the i
# -th player is equal to si and all skill levels are pairwise different (i. e. there are no two identical values in the array s

# ).

# The tournament is called fair if the two players with the highest skills meet in the finals.

# Determine whether the given tournament is fair.
# Input

# The first line contains a single integer t
# (1≤t≤104

# ) — the number of test cases.

# A single line of test case contains four integers s1,s2,s3,s4
# (1≤si≤100

# ) — skill of the players. It is guaranteed that all the numbers in the array are different.
# Output

# For each testcase, output YES if the tournament is fair, or NO otherwise.
# Example
# Input
# Copy

# 4
# 3 7 9 5
# 4 5 6 9
# 5 3 8 1
# 6 5 3 2

# Output
# Copy

# YES
# NO
# YES
# NO
def main():
    n = int(input())

    for _ in range(n):
        skills = [int(i) for i in input().split()]
        p1, p2 = skills[:2], skills[2:]
        # 3 7 9 5 -> 9 and 5 advance -> YES
        # 4 5 6 9 -> NO -> 6 does not advance
        best = sorted(skills, reverse=True)[:2]
        if (set(p1) == set(best)) or (set(p2) == set(best)):
            print('NO')
        else:
            print("YES")

if __name__ == "__main__":
    main()


