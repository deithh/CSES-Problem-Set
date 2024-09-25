# seq = input()
# pattern = input()

# bad_match_table = {}
# count = 0


# for ind, i in enumerate(pattern):
#     bad_match_table[i] = max(1, len(pattern) - ind - 1)

# i = len(pattern) - 1
# while i< len(seq):
#     if seq[i] != pattern[-1]:
#         i += bad_match_table.get(seq[i], len(pattern))
#     else:
#         for ind, j in enumerate(reversed(pattern)):
#             if j != seq[i-ind]:
#                 break
#         else:
#             count += 1
#         i+= 1
    
# print(count)

# edgecases to slow KMP algorithm inc...