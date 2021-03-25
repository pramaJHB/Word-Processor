import unittest
import word_processor


class MyTestWords(unittest.TestCase):
	def test_convert_to_word_list_empty(self):
		output = word_processor.convert_to_word_list('')
		self.assertEqual([], output)

	
	def test_convert_to_word_list_with_delimiters(self):
		output = word_processor.convert_to_word_list('this .is a test? ;   for splitting text, with,.? delimiters.;')
		self.assertEqual(['this', 'is', 'a', 'test', 'for', 'splitting', 'text', 'with', 'delimiters'], output)

	
	def test_convert_to_word_list_camelcase(self):
		output = word_processor.convert_to_word_list('ThiS IS my CaMElcASE teSt')
		self.assertEqual(['this', 'is', 'my', 'camelcase', 'test'], output)


	def test_words_longer_than_0(self):
		output = word_processor.words_longer_than(0, 'Will this test return all these words as a list?')
		self.assertEqual(['will', 'this', 'test', 'return', 'all', 'these', 'words', 'as', 'a', 'list'], output)


	def test_words_longer_than_5(self):
		output = word_processor.words_longer_than(5, 'This test should only return words longer than; 5 Characters.')
		self.assertEqual(['should', 'return', 'longer', 'characters'], output)


	def test_words_longer_than_5_empty(self):
		output = word_processor.words_longer_than(5, '')
		self.assertEqual([], output)


	def test_words_longer_than_100(self):
		output = word_processor.words_longer_than(100, 'This test will return an empty list!')
		self.assertEqual([], output)


	def test_words_length_map(self):
		output = word_processor.words_lengths_map('I hope this works...')
		self.assertEqual({1: 1, 4: 2,5: 1}, output)

	
	def test_words_length_map_empty(self):
		output = word_processor.words_lengths_map('')
		self.assertEqual({}, output)

	
	def test_words_length_map_again(self):
		output = word_processor.words_lengths_map('a aa aaa aaaa aaaaa aaaaaa aaaaa aaa a')
		self.assertEqual({1: 2, 2: 1, 3: 2, 4: 1, 5: 2, 6: 1}, output)


	def test_get_alphabet_characters(self):
		output = word_processor.get_alphabet_characters()
		self.assertEqual(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
			'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], output)

	
	def test_letters_count_map_empty(self):
		output = word_processor.letters_count_map('')
		self.assertEqual({'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, \
             'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}, output)


	def test_letters_count_map(self):
		output = word_processor.letters_count_map('The quick brown fox jumps over the lazy dog.')
		self.assertEqual({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 3, 'f': 1, 'g': 1, 'h': 2, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1,\
             'o': 4, 'p': 1, 'q': 1, 'r': 2, 's': 1, 't': 2, 'u': 2, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}, output)
	

	def test_most_used_character_empty(self):
		output = word_processor.most_used_character('')
		self.assertIsNone(output)
	

	def test_most_used_character(self):
		output = word_processor.most_used_character('yy.y?yyy yy')
		self.assertEqual('y', output)


	def test_most_used_character_again(self):
		output = word_processor.most_used_character('I wonder what the most used character is in this sentence?')
		self.assertEqual('e', output)



if __name__ == '__main__':
    unittest.main()