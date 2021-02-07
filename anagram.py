def anagram_checker(str1, str2):
    # constraints: strings only, single words, len < 50 chars
    # return True, False
    # example: tone, note

    if str1.sort() == str2.sort():
        return True
    else:
        return False


# a celebrity is a person who knows noone but everyone knows
# given people[], identify the celebrity (one exists)

