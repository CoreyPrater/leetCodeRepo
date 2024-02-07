class Solution:
    def frequencySort(self, s: str) -> str:
        #count char using counters
        count = Counter(s)

        # Sort chars by freq in desc order using rever = true. 
        sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Build the result string based on sorted characters and their frequencies
        result = ''.join(char * freq for char, freq in sorted_chars)

        return result