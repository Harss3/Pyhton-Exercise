def merge_the_tools(string, k):
  n = len(string)
  new = []
  if n % k != 0:
      seq = int(n/k) + 1
  else:
      seq = int(n/k)

  for i in range(seq):
      t = set(string[i*k:k*(i+1)])   # create a substring from given and prevent each character from being duplicated
      new.append(''.join(t))         # merge all obtained substring and put them into new list

  [print(x) for x in new]            # print out all substring on each line

if __name__=='__main__':
  s = input()
  k = int(input())
  merge_the_tools(s, k)
