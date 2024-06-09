'''Number to text translation'''
ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = [
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
]
tens = [
    "Ten",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
]
over_thousand = {
    "Thousand ": 1000000,
    "Million ": 1000000000,
    "Billion ": 1000000000000,
    "Trillion ": 1000000000000000,
}


def number_to_text(num):
    '''Converts an integer number into its literal equivalent.'''
    if num < 10:
        return ones[num] + " "
    elif num == 10:
        return "Ten "
    elif num < 20:
        return teens[num - 11] + " "
    elif num < 100:
        return (
            tens[num // 10 - 1]
            + " "
            + ("" if num % 10 == 0 else (number_to_text(num % 10)))
        )
    elif num < 1000:
        return (
            ones[num // 100]
            + " Hundred "
            + ("" if num % 100 == 0 else ("and " + number_to_text(num % 100)))
        )

    for limit in over_thousand.values():
        if limit > num:
            return (
                number_to_text(num // (limit // 1000))
                + list(over_thousand.keys())[list(over_thousand.values()).index(limit)]
                + (
                    ""
                    if num % (limit // 1000) == 0
                    else (number_to_text(num % (limit // 1000)))
                )
            )


def main():
    '''Main module'''
    num = int(input("Enter a number: "))
    translation = number_to_text(num)
    print(translation)



main()
