class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        
        symbol_to_value = {
            "M":1000,#
            "CM":900,#
            "D":500,#
            "CD":400,#
            "C":100,#
            "XC":90,#
            "L":50,#
            "XL":40,#
            "X":10,#
            "IX":9,#
            "V":5,#
            "IV": 4,
            "I":1,
        }
        
        for key, value in symbol_to_value.items():
            count = s.count(key) * 2
            for key_i, _ in symbol_to_value.items():
                if key_i.count(key):
                    count -= s.count(key_i)
                print(key,key_i, count)
            
            output += (count * value)
        
        print(output)
        return output
        
        
        
        
solution = Solution()

solution.romanToInt("III")
        