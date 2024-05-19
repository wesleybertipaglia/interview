# HackerRank - Week Preparation Kit
# challenge-title: Diagonal Difference
# challenge-url: https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/

# Description:
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(n, matrix):
    dia_primary = 0
    dia_secondary = 0

    for i in range(0, len(matrix)):
        dia_primary += matrix[i][i]
        dia_secondary += matrix[i][n - 1 - i]
    
    return abs(dia_primary - dia_secondary)