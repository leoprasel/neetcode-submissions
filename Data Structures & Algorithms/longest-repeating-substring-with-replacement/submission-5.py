class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        max_window_length = 0

        for r, letter in enumerate(s):
            freq[letter] = freq.get(letter,0) + 1
            max_freq = max(freq.values())

            window_length = r - l + 1
            if window_length - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            else:
                max_window_length = max(window_length,max_window_length)
        return max_window_length

          #  