import OpenHowNet

from .word_swap import WordSwap


class ChineseWordSwapHowNet(WordSwap):
    """Transforms an input by replacing its words with synonyms provided by
    WordNet."""

    def __init__(self):
        self.hownet_dict = OpenHowNet.HowNetDict(init_sim=True)
        self.topk = 10

    def _get_replacement_words(self, word):
        """Returns a list containing all possible words with N characters
        replaced by a homoglyph."""
        results = hownet_dict.get_nearest_words(word, language = "zh", K = topk)
        synonyms = []
        for key, synonyms in results.items():
          for w in synonyms:
            synonyms.append(w)
        else:
            return []
