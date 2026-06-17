class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        first=a
        second =b
        if len(first)>len(second):
            second = ("0" * (len(first)-len(second))) + second
        else:
            first = ("0" * (len(second)-len(first))) + first 
        first = "00"+first
        second = "00"+second
        print( a,b)
        print( first,second)
        
        print( len(first),len(second))
        assert len(first)==len(second)
        carry = 0
        digits = []
        print("adding", first, second)
        first_reversed = "".join(reversed(first))
        second_reversed = "".join(reversed(second))

        for i in range(0, len(first)):
            # for char1 in reversed(first):
            #     for char2 in reversed(second):
            char1=first[i]
            char2=second[i]
            print(char1, char2, '...digits')
            
            if int(char1) + int(char2) + carry==2:
                print("carry 1")
                carry =1
                digits.append("0")
            elif int(char1) + int(char2) + carry==3:
                print("carry 2")
                carry =2
                digits.append("1")
            else:
                print("ordinary math, no carry")
                digits.append(str(int(char1) + int(char2)+carry))
                carry =0

            intermedite ="".join(reversed("".join(digits)))
            print(intermedite, "at column ", i)
        padded ="".join(reversed(digits))
        print(padded, '...final with padding')
        if padded:
            while padded[0]=="0":

                padded = padded[1:]
                print(padded, "trim 0")
        return padded
