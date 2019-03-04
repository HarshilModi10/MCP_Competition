class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ''
        string1 = ["", "I", "II","III", "IV", "V", "VI", "VII", "VIII", "IX", "X" ]
        string2 = ["", "X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C" ]
        string3 = ["", "C", "CC","CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M" ]
        string4 = ["", "M", "MM", "MMM" ]
        
        roman += string4[int(num/1000)] + string3[int((num%1000)/100)] + string2[int((num%100)/10)] + string1[num%10]
        return roman
