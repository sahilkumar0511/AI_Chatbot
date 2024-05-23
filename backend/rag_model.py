from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
from datasets import load_dataset
import os
import warnings

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Suppress Deprecation Warning
warnings.filterwarnings("ignore", category=FutureWarning)

tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
dataset = load_dataset("wiki_dpr",  "psgs_w100.nq.exact", trust_remote_code=True)
retriever = RagRetriever.from_pretrained(
    "facebook/rag-sequence-nq",
    index_name="legacy", passages_path=dataset['train']['passages'])
rag_model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)

def generate_response_with_cot(user_query):
    inputs = tokenizer(user_query, return_tensors="pt")
    initial_response = rag_model.generate(inputs['input_ids'])
    # Implement Chain of Thought processing here if necessary
    response_text = tokenizer.batch_decode(initial_response, skip_special_tokens=True)[0]
    return response_text