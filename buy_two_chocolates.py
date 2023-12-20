# Question_Link - https://leetcode.com/problems/buy-two-chocolates/

class Solution:
  def buyChoco(self: prices: List[int],money: int)->int:
    min1=min2=float("inf")
    for p in prices:
      if p < min1:
        min1, min2= p,min1
      elif p< min2:
        min2=p
    total_cost= min1+min2

    if total_cost>money:
      return money
    else:
      return money - total_cost
