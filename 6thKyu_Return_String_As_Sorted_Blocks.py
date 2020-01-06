#### NOT OPTIMIZED

# You will receive a string consisting of lowercase letters, uppercase letters and digits as input. Your task is to return this string as blocks separated by dashes ("-"). The elements of a block should be sorted with respect to the hierarchy listed below, and each block cannot contain multiple instances of the same character.

# The hierarchy is:

# lowercase letters (a - z), in alphabetic order
# uppercase letters (A - Z), in alphabetic order
# digits (0 - 9), in ascending order
# Examples

# "21AxBz" -> "xzAB12" - since input does not contain repeating characters, you only need 1 block
# "abacad" -> "abcd-a-a" - character "a" repeats 3 times, thus 3 blocks are needed
# "" -> "" - an empty input should result in an empty output

import collections
def blocks(s):
  order_dict = {}
  result = ''

  for x in s:
    if x not in order_dict: 
      order_dict[x] = 1
    else:
      order_dict[x] += 1
  order_dict = collections.OrderedDict(order_dict.items())

  while sum(list(order_dict.values())) != 0:
    final, order_dict = print_dict_values(order_dict)
    if result == '':
      result += final
    else:
      result = result + '-' + final
  return result

def print_dict_values(order_dict):
  lower = ''
  upper = ''
  num = ''
  for k,v in order_dict.items():
    if order_dict[k] != 0:
      if k.islower():
        lower += k
        order_dict[k] -= 1
      elif k.isupper():
        upper += k
        order_dict[k] -= 1
      else:
        num += k
        order_dict[k] -= 1
    lower = ''.join(sorted(lower))
    upper = ''.join(sorted(upper))
    num = ''.join(sorted(num))
  final = lower + upper + num
  return final, order_dict


assert blocks("heyitssampletestkk") == "aehiklmpsty-ekst-est"
