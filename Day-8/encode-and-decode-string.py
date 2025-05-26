class Codec:
    # use non-ascii character as delimiter
    # TC: O(n) SC: O(n)
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return '◊'.join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('◊')


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

class Codec:
    # use comma as delimiter, with length mapping
    # TC: O(n) SC: O(n)

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""

        for s in strs:
            encoded_string = encoded_string + str(len(s)) + ',' + s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strings = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != ',':
                j += 1
            
            str_len = int(s[i:j])

            decoded_strings.append(s[j+1: j+1+str_len])

            i = j + 1 + str_len
        
        return decoded_strings
        
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))