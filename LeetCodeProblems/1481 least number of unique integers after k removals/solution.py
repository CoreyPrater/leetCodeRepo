class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:



         # Count the frequency of each number

        frequency = {}

        for num in arr:

            frequency[num] = frequency.get(num, 0) + 1



        # Sort the numbers based on their frequencies in ascending order

        sorted_nums = sorted(frequency.keys(), key=lambda x: frequency[x])



        # Remove elements with the lowest frequencies until k becomes 0

        for num in sorted_nums:

            if k >= frequency[num]:

                k -= frequency[num]

                del frequency[num]

            else:

                break

        return len(frequency)