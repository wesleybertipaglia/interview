# HackerRank - Week Preparation Kit (Mock Test Day 1)
# challenge-title: Find the Median
# challenge-url: https://www.hackerrank.com/interview/preparation-kits/one-week-preparation-kit/one-week-day-one/challenges

# Description:
# The median of a list of numbers is essentially its middle element after sorting. The same number of
# elements occur after it as before. Given a list of numbers with an odd number of elements, find the median?

def find_median(arr):
    arr.sort()
    med_pos = len(arr) // 2
    return arr[med_pos]