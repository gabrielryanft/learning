# Notes i take while i read [Mictosoft's introduction to A.I.] (https://learn.microsoft.com/en-us/training/modules/introduction-large-language-models/)

## Tokens

Tokens are what llms use to "understand" the input given. 

They transform the input, lets use text, as the input for this example:

The words car and internet, are very common words so if you transform they in tokens, you get 1 token per word. But, if you take words like blueberry and tokenizer, you get more than one token per word, in this case, you get two tokens per word.

In the article, they, recommend using the openAI tokenizer to see a visual representation of the process: https://platform.openai.com/tokenizer.

## letter-by-letter geneartion

A LLM makes generations in a word-by-word way, seeing what is more probable to go next based on what it has recived.

> A letter-by-letter text generation could easily result in gibberish.

## GPT meaning

Generative pre-trained transformer
