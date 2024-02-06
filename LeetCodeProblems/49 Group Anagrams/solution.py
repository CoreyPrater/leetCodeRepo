class Solution(object):
    def groupAnagrams(self, strs):
        sorted_dict = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str in sorted_dict:
                sorted_dict[sorted_str].append(string)
            else:
                sorted_dict[sorted_str] = [string]
        final_array = list(sorted_dict.values())
        return final_array