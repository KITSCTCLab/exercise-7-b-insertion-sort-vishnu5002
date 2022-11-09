from typing import List

def insertionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(size):
    min = i
    for j in range(i + 1, size):
      if array[min] > array[j]:
        min = j;
    array[i], array[min] = array[min], array[i]
  return array

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data, len(data)))
