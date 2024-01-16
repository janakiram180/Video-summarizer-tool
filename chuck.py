import nltk


def re_chunks(input, tokenizer):
    sentences = nltk.tokenize.sent_tokenize(input)

    # initialize
    length = 0
    chunk = ""
    chunks = []
    count = -1

    for sentence in sentences:
        count += 1
        # add the no. of sentence tokens to the length counter
        combined_length = len(tokenizer.tokenize(sentence)) + length
        if combined_length <= 500:  # if it doesn't exceed
            chunk += sentence + " "  # add the sentence to the chunk
            length = combined_length  # update the length counter

            # if it is the last sentence
            if count == len(sentences) - 1:
                chunks.append(chunk.strip())  # save the chunk

        else:
            chunks.append(chunk.strip())  # save the chunk

            # reset
            length = 0
            chunk = ""

            # take care of the overflow sentence
            chunk += sentence + " "
            length = len(tokenizer.tokenize(sentence))

    return chunks
