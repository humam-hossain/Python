#  Jorge is a physicist who has published many research papers and wants to know how 
# much impact they have had in the academic community. To measure impact, 
# he has developed a metric, H-index, to score each of his papers based on the number of
#  times it has been cited by other papers. Specifically, the H-index score of a researcher is 
# the largest integer H such that the researcher has H papers with at least H citations each.
# 
# Jorge has written N papers in his lifetime. The i-th paper has Ci citations. 
# Each paper was written sequentially in the order provided, and the number of citations that 
# each paper has will never change. Please help Jorge determine his H-index score after 
# each paper he wrote. 

# 2
# 3
# 5 1 2
# 6
# 1 3 3 2 2 15
# Case #1: 1 1 2
# Case #2: 1 1 2 2 2 3

def each_h_index(n, citations):
  # citations = [5 1 2]
  N = len(list(citations)) #3

  temp = [0 for _ in range(N+1)]
  # temp = [0 0 0 0]

  for cit in citations:
    if cit>N:
      temp[N] += 1
    else:
      temp[cit] += 1
  # temp = [0 1 1 1]

  total = 0
  for i in range(N, -1, -1): # i = 3 2 1 0
    # print(i)
    total += temp[i] # temp[2] = 1
    # total = 3

    if total >= i: # total = 3
      return i
    

def h_index(n, citations):
  ans = []
  citations = list(citations)

  for i in range(1, n+1):
    ans.append(each_h_index(i, citations[:i]))
  return ans


if __name__ == '__main__':
  t = int(input())

  for test_case in range(1, t + 1):
    n = int(input())                      # The number of papers
    citations = map(int, input().split()) # The number of citations for each paper
    h_index_scores = h_index(n, citations)
    print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))
