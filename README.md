# Subword-Tokenization-with-Byte-Pair-Encoding-BPE

In this project, I implemented a variation of the Byte-Pair Encoding (BPE) algorithm for subword tokenization using only Python’s built-in re and codecs libraries.

The program is divided into two main components:

- Token Learner

Takes a raw training corpus (as a string or UTF-8 encoded file)

Learns a vocabulary, a list of merge operations, and produces a tokenized version of the corpus

Returns a triple: (Merges, Vocabulary, TokenizedCorpus)

Supports an optional maximum merge count parameter (default = 10)

- Token Segmenter

Takes any new input text (as a string)

Applies the learned merges to tokenize the text consistently with the vocabulary induced by the learner

Key Constraints:

Only re and codecs libraries were used.

Designed to process UTF-8 encoded text files or direct input strings.

Emphasis was on algorithmic correctness, minimal dependencies, and modular design.

Through this project, I gained a deeper understanding of unsupervised tokenization techniques and the internal workings of subword-based language models.
