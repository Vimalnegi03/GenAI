import tiktoken
encoder =tiktoken.encoding_for_model('gpt-4o')
print("vocab size",encoder.n_vocab)
text_input="The cat sat on the mat"
tokens=encoder.encode(text_input)
print("tokens ",tokens)
my_tokens= [976, 9059, 10139, 402, 290, 2450]
decoded_text=encoder.decode(my_tokens)
print(decoded_text)