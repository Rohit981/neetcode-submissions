class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for n in range(len(strs)):
            #To get the len of the strings
            stringlen = len(strs[n])

            #Create 5#Hello5#world
            encoded.append(f"{stringlen}#{strs[n]}")
        
        encoded_str = "".join(encoded)
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        start = 0
        extracted_word = []

        while start < len(s):
            length_accumulator = ""
            while s[start] != '#':
                length_accumulator += s[start]
                start +=1
            
            token_length = int(length_accumulator)

            start +=1

            word = s[start:start+token_length]
            extracted_word.append(word)

            start +=token_length
        return extracted_word
