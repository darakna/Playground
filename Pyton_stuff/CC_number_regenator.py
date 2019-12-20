part_number = "42560353245833ab"


def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )



def get_numbs():
    for a in range(0,9):
        for b in range (0,9):
            s1 = part_number.replace("a", str(a))
            s2 = s1.replace("b", str(b))
            result = cardLuhnChecksumIsValid(s2)
            if result:
                print(s2)
get_numbs()