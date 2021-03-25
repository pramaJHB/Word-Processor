
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """
    Converts a string into a list of words
        Parameters:
            text: the string to be converted into a list
        Return:
            A list of words
    """
    word_list = split(' ,.?;', text)
    return [words.lower() for words in word_list if len(words) > 0]


def words_longer_than(length, text):
    """
    Finds all words longer than a specified length from a string
        Parameters:
            text: the string which will be searched through
            length: the specified length of word
        Return:
            A list of words longer than the length
    """
    word_list = convert_to_word_list(text)
    return list(filter(lambda words: len(words) > length, word_list))


def words_lengths_map(text):
    """
    Finds how many words occur of each length in a string
        Parameters:
            text: the string which will be analysed
        Return:
            A dictionary of how many words occur of each length
    """
    word_list = convert_to_word_list(text)
    word_length = sorted(list(map(lambda words: len(words), word_list)))
    return dict((i, word_length.count(i)) for i in word_length)

def get_alphabet_characters():
    """
    Gets a list of each letter of the alphabet
        Return:
            A list of characters
    """
    import string
    return list(string.ascii_lowercase)


def letters_count_map(text):
    """
    Counts the number of times each letter occurs in a string
        Parameters:
            text: the string to be analysed
        Return:
            A dictionary of the numbers of occurrences of each letter
    """
    word_list = convert_to_word_list(text)
    word_list = ''.join(word_list)
    alphabet = get_alphabet_characters()
    return dict((alphabet[i], word_list.count(alphabet[i])) for i in range(len(alphabet)))


def most_used_character(text):
    """
    Finds the most used letter in a string
        Parameters:
            text: the string to be analysed
        Return:
            The most used letter of the string
    """
    letter_count_dict = letters_count_map(text)
    maxvalue = max(letter_count_dict.values())
    return None if maxvalue == 0 else \
        max(letter_count_dict, key=lambda i: letter_count_dict[i])
