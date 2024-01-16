from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from chuck import re_chunks


def summarize_text(text_to_summarize):

    # declearing the model to summarize
    model_name = "google/pegasus-cnn_dailymail"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # breaking the hugh text to chunks
    chunks = re_chunks(str(text_to_summarize), tokenizer)
    print(chunks[0])
    summary = ''
    inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]

    # summarizing the text
    for input in inputs:
        output = model.generate(**input)
        summary += tokenizer.decode(*output, skip_special_tokens=True)

    return summary
