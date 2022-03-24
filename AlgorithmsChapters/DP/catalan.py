# recursive solution
def catalan(n):
   if n < 1 :
      return 1

   catn = 0
   for i in range(n):
      catn += catalan(i) * catalan(n-i-1)
   return catn

print (catalan(11))

# dynamic programming solution
def catalan2(n):  
   catn = [0]*(n + 1)
   catn[0] = 1 # Base case

   # recursion
   for i in range(1, n + 1):
      for j in range(i):
         catn[i] += catn[j] * catn[i-j-1]
   return catn[n]

print(catalan2(11))

"""
58786
58786
"""