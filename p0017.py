to_9: list[str] = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
to_90_by_10 = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
to_99: list[str] = [
    *to_9,
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    *to_90_by_10,
    *[f"{tens}{ones}" for tens in to_90_by_10 for ones in to_9],
]
to_999: list[str] = [
    *to_99,
    *[f"{hundreds}hundred" for hundreds in to_9],
    *[f"{hundreds}hundredand{ones}" for hundreds in to_9 for ones in to_99],
]
to_1000: list[str] = [
    *to_999,
    "onethousand",
]
print(sum(map(len, to_1000)))
