import hangman
import rules
import unittest

class TestHangmanGame(unittest.TestCase):
    def test_check_guess(self):
        guess, word, dashes, guesses_max = "a", "cat", "___", 5
        dashes, guesses_max = hangman.check_guess(guess, word, dashes, guesses_max)
        self.assertEqual(dashes, "_a_")
        self.assertEqual(guesses_max, 5)
    
    def test_update_dashes(self):
        word = "cat"
        dashes = "___"
        guess = "a"
        dashes = hangman.update_dashes(word, dashes, guess)
        self.assertEqual(dashes, "_a_")
    
    def test_minus_guesses(self):
        guesses_num = 10
        self.assertEqual(hangman.minus_guesses(guesses_num), 9)

    def test_choose_word(self):
        rand_word = rules.choose_word()
        self.assertIsNotNone(rand_word)

    def test_check_win(self):
        self.assertFalse(rules.check_win("purple","purp_e"))
        self.assertTrue(rules.check_win("calculus","calculus"))

    def test_check_lose(self):
        self.assertFalse(rules.check_lose(4))
        self.assertTrue(rules.check_lose(0))

    #integration tests
    #testing check_guess and update_dashes can work together
    def test_check_guess_and_update_dashes(self):
        guess, word, dashes, guesses_max = "p", "purple", "______", 5
        dashes, guesses_max = hangman.check_guess(guess, word, dashes, guesses_max)   
        self.assertEqual(dashes, "p__p__")
        dashes = hangman.update_dashes(word, dashes, "u")
        dashes, guesses_max = hangman.check_guess("r", word, dashes, guesses_max)
        self.assertEqual(dashes, "purp__")
    
    #testing check_guess and minus_guesses work together
    def test_check_guess_and_minus_guesses(self):
        guess, word, dashes, guesses_max = "z", "purple", "______", 5
        dashes, guesses_max = hangman.check_guess(guess, word, dashes, guesses_max) 
        self.assertEqual(dashes, "______")  
        self.assertEqual(guesses_max, 4)
        guesses_max = hangman.minus_guesses(guesses_max)
        self.assertEqual(guesses_max, 3)
    
    #testing choose_word and check_guess
    def test_choose_word_check_guess(self):
        random_w = rules.choose_word()
        dashes = "_" * len(random_w)  
        guess, guesses_max = "a", 5
        dashes, guesses_max = hangman.check_guess(guess, random_w, dashes, guesses_max)
        self.assertIsNotNone(random_w)
        self.assertIsNotNone(dashes)
        self.assertNotEqual(guesses_max, 0)

    #testing update dashes and check win
    def test_update_dashes_and_check_win(self):
        dashes = hangman.update_dashes("cat", "c_t", "a")
        self.assertTrue(rules.check_win("cat", dashes))

    #testing minus guesses and check lose
    def test_minus_guesses_and_check_lose(self):
        guesses_left = 1
        guesses_left = hangman.minus_guesses(guesses_left)
        self.assertTrue(rules.check_lose(guesses_left))

