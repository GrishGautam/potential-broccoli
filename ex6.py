ok = input("enter some numbers")

digit_mapping = {
	"1" : "one",
	"2" : "two",
	"3" : "Three",
	"4" : "Four",
	"5" : "five",
	"6" : "six",
	"7" : "seven",
	"8" : "eight",
	"9" : "nine",
	"0" : "zero",
	":)" : "😀"
	":(" : "😔"
}
lol = ""
output = ""
for ch in ok:
	output += digit_mapping.get(ch,"!") + " "
print(output)
