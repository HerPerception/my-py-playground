/*============================================================================================
RECURSION is when a function calls itself. It should always have a base case or a stop condition
to avoid an infinite recursion.

The example is implememnted in Python.
==============================================================================================*/

def tri_recursion(k):
  if k > 0:
    result = k + tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result
