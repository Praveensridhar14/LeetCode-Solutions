class Solution:
    def romanToInt(self, s: str) -> int:
        dict_value = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000, "IV" : 4, "IX" : 9, "XL": 40, "XC" : 90, "CD":400, "CM":900}
        output_sum = 0
        if len(s) >= 1 and len(s) <=15:
            if "IV" in s:
                IV_count = s.count("IV")
                output_sum += (IV_count * dict_value["IV"])
                s = s.replace("IV", "")
            if "IX" in s:
                IX_count = s.count("IX")
                output_sum += (IX_count * dict_value["IX"])
                s = s.replace("IX", "")
            if "XL" in s:
                XL_count = s.count("XL")
                output_sum += (XL_count * dict_value["XL"])
                s = s.replace("XL", "")
            if "XC" in s:
                XC_count = s.count("XC")
                output_sum += (XC_count * dict_value["XC"])
                s = s.replace("XC", "")
            if "CD" in s:
                CD_count = s.count("CD")
                output_sum += (CD_count * dict_value["CD"])
                s = s.replace("CD", "")
            if "CM" in s:
                CM_count = s.count("CM")
                output_sum += (CM_count * dict_value["CM"])
                s = s.replace("CM", "")
            for i in s:
                if i in dict_value and i in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
                    output_sum += dict_value[i]
            if output_sum >= 1 and output_sum <= 3999:
                return output_sum
        