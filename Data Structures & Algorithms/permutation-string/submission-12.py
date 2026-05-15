class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s2_dict = {}
        def string_counter(string):
            string_dict = {}
            for s in string:
                string_dict[s] = string_dict.get(s,0) + 1
            return string_dict
        
        s1_dict = string_counter(s1)

        for r, char_s2 in enumerate(s2):

            s2_dict[char_s2] = s2_dict.get(char_s2,0) + 1

            if r - l + 1 > len(s1):
                s2_dict[s2[l]] = s2_dict[s2[l]] -1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l += 1  
                
            if s1_dict == s2_dict:
                return True
            



        return False
            