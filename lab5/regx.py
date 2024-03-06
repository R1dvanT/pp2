#1
import re


#we have string that have a or ab or abb and etc
p = re.compile(".*[ab*].*")
# "a" -> a
# "abbb" -> abbb
# "abbab" -> abb
# "as,nd,abb" -> a
# "nvjfvabb" -> nvjfvabb
# "nvanv" -> nvanv


m = input("String: ")
m = re.match(p, m)

if m == None:
    print("It not statisfy")
else:
    print(m.group())

#2
    
import re
#we have string where we have abb or abbb
pattern = re.compile("ab{2,3}")
"""
123abb123 -> abb
123abbbb321 -> abbb
123ab123 -> no

"""
m = input("String: ")

m = re.findall(pattern, m)

if len(m) == 0:
    print("It is no statisfy")
else: 
    print(m)

#3
    
import re
#there we need one underscore and at least one lowercase letters before "_" and after "_"
p = "[a-z]+_[a-z]+"
"""
ab_cd -> ab_cd
ab_cd_ef_gh -> [ab_cd, ef_gh]
AB_CDef_gh_F -> ef_gh
"""
m = input("String: ")

m = re.findall(p, m)

print(m)

#4

import re
#we need one Uppercase then at least one lower case letters
p = re.compile("[A-Z][a-z]+")

m1 = re.findall(p, "Abcd")
m2 = re.findall(p, "aAbcB")
m3 = re.findall(p, "aa1i31rf012=-AbcdfajfSjdna")
m4 = re.findall(p, "abdac1203rfk")

print(m1)
print(m2)
print(m3)
print(m4)

#5

import re
#we have string where we have "a" followed by something and end by "b"
p = re.compile(".*a.+b$")

m1 = re.match(p, "acb")
m2 = re.match(p, "vacgfhb")
m3 = re.match(p, "12a123bm") #error
print(m1.group())
print(m2.group())
print(m3.group())

#6
import re

m = "My name is Ridvan, I'm 18 years old. There will be three ':'- ,.}"

m = re.sub(r"\s|,|[.]", ":", m)

print(m)