from rag_model import generate_response_with_cot

# Define the user query you want to test
user_query = "What is the capital of the France?"

# Call the generate_response_with_cot function with the user query
response = generate_response_with_cot(user_query)

# Print the generated response
print(f"Query: {user_query}")
print(f"Response: {response}")