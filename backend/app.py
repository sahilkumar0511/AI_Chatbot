from flask import Flask, request, jsonify
from embeddings import generate_embeddings, update_vector_database
from rag_model import generate_response_with_cot

app = Flask(__name__)

@app.route('/update-embeddings', methods=['POST'])
def update_embeddings():
    data = request.json
    text = data['text']
    post_id = data['post_id']
    embeddings = generate_embeddings(text)
    update_vector_database(post_id, embeddings)
    return jsonify({"status": "success"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_query = data['query']
    previous_context = data.get('context', [])
    response = generate_response_with_cot(user_query, previous_context)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
