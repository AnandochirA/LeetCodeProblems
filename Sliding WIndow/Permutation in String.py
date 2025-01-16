class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Frequency dictionary for s1
        target_count = {}
        for char in s1:
            target_count[char] = target_count.get(char, 0) + 1

        # Sliding window frequency dictionary
        window_count = {}
        for i in range(len(s1)):
            char = s2[i]
            window_count[char] = window_count.get(char, 0) + 1

        # Check if the initial window matches
        if window_count == target_count:
            return True

        # Slide the window
        for end in range(len(s1), len(s2)):
            # Add the new character to the window
            char_to_add = s2[end]
            window_count[char_to_add] = window_count.get(char_to_add, 0) + 1

            # Remove the character going out of the window
            char_to_remove = s2[end - len(s1)]
            if window_count[char_to_remove] == 1:
                del window_count[char_to_remove]
            else:
                window_count[char_to_remove] -= 1

            # Check if the current window matches the target
            if window_count == target_count:
                return True

        return False
