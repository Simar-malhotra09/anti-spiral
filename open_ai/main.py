
text = """Within the realm of transformer networks, the process of tokenization assumes a pivotal role in fragmenting text into smaller units known as tokens.
Tokenizers
Tokenization is the first step to building a model, which involves splitting text into smaller units called tokens that become the basic building blocks for LLMs. These extracted tokens are used to build a vocabulary index mapping tokens to numeric IDs, to numerically represent text suitable for deep learning computations. During the encoding process, these numeric tokens are encoded into vectors representing each token’s meaning. During the decoding process, when LLMs perform generation, tokenizers decode the numeric vectors back into readable text sequences.  
The process begins with normalization to process lowercase, pruning punctuation and whitespaces, stemming, lemmatization, handling contractions, and ‌removing accents. Once the text is cleaned up, the next step is to segment the text by recognizing word and sentence boundaries. Depending on the boundary, tokenizers can be at word, sub-word, or character-level granularity. 
Although word and character-based tokenizers are prevalent, there are challenges with these. Word-based tokenizers lead to a large vocabulary size and words not seen during the tokenizer training process cause many out-of-vocabulary tokens. Character-based tokenizers lead to long sequences and less meaningful individual tokens. 
Due to these shortcomings, subword-based tokenizers have gained popularity. The focus of subword tokenization algorithms is to split rare words into smaller, meaningful subwords, based on common character n-grams and patterns. For This technique enables the representation of rare and unseen words via known subwords, resulting in a reduced vocabulary size. During inference, it also handles out-of-vocabulary words effectively reducing vocabulary size, while handling out-of-vocabulary words gracefully during inference. 
Popular subword tokenization algorithms include Byte Pair Encoding (BPE), WordPiece, Unigram, and SentencePiece. 
BPE starts with character vocabulary and iteratively merges frequent adjacent character pairs into new vocabulary terms, achieving text compression with faster inference at decoding time by replacing most common words with single tokens. 
WordPiece is similar to BPE in doing merge operations, however, this leverages the probabilistic nature of the language to merge characters to maximize training data likelihood. 
Unigram starts with a large vocabulary, calculates the probability of tokens, and removes tokens based on a loss function until it reaches the desired vocabulary size. 
SentencePiece learns subword units from raw text based on language modeling objectives and uses Unigram or BPE tokenization algorithms to construct the vocabulary. 
Attention Mechanisms
As ‌traditional seq-2-seq encoder-decoder language models like Recurrent Neural Networks (RNNs) don’t scale well with the length of the input sequence, the concept of attention was introduced and has proved to be seminal. The attention mechanism enables the decoder to use the most relevant parts of the input sequence weighted by the encoded input sequence, with the most relevant tokens being assigned the highest weight. This concept improves the scaling of input sequence lengths by carefully selecting ‌tokens by importance. 
This idea was furthered with self-attention and introduced in 2017 with the transformer model architecture, removing the need for RNNs. Self-attention mechanisms create representations of the input sequence relying on the relationship between different words in the same sequence. By enhancing the information content of an input embedding through the inclusion of input context, self-attention mechanisms play a crucial role in ‌transformer architectures.
Computational steps in self-attention.
Figure 2. Self-attention architecture (source: Understanding and Coding the Self-Attention Mechanism of Large Language Models From Scratch)
Self-attention is called scaled-dot product attention because of how it achieves context-aware input representation. Each token in the input sequence is used to project itself into Query (Q), Key (K), and Value (V) sequences using their respective weight matrices. The goal is to compute an attention-weighted version of each input token given all the other input tokens as its context. By computing a scaled dotduct of Q and K matrices with relevant pairs determined by the V matrix getting higher weights, the self-attention mechanism finds a suitable vector for each input token (Q) given all key-value pairs that are other tokens in the sequence. """

''' counter at 4664'''
counter = 0
for i in text:
    counter +=1
#print("text" + str(counter))
    
import nltk

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


''' Filter '''
text = word_tokenize(text)
stop_words = set(stopwords.words('english'))
text= [word for word in text if word.lower() not in stop_words]
filtered_text= ' '.join(text)

''' counter at 3883'''
counter = 0
for i in filtered_text:
    counter +=1
#print("filtered_text" + str(counter))
    




from openai import OpenAI
import os
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": """ In the context of the given text 
      what is meanings of the term 'token'? How does the author use tokens to explain complex concepts? Can you recommend a concise and 
      easy-to-understand explanation of tokens in the context of text analysis?"""
     
    },
    {
      "role": "user",
      "content": filtered_text
    }
  ],
  temperature=0.1,
  max_tokens=200,
  top_p=1
)
print(response.choices[0].message.content
)