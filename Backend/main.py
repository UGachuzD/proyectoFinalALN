from flask import Flask, jsonify, request
from flask_cors import CORS
from langdetect import detect, DetectorFactory
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel
from googletrans import Translator

DetectorFactory.seed = 0

app = Flask(__name__)
CORS(app)

class MLPClassifier(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(MLPClassifier, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.softmax = nn.Softmax(dim=1)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return self.softmax(x)

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
transformer = AutoModel.from_pretrained('bert-base-uncased')

def get_embeddings(text, tokenizer, transformer):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = transformer(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings


input_dim = 768
hidden_dim = 256
output_dim = 2
model = MLPClassifier(input_dim, hidden_dim, output_dim)


model.load_state_dict(torch.load('modelo_entrenado.pth'))
model.eval()

def use_model(embedding, model):
    with torch.no_grad():
        prediction = model(embedding).argmax(dim=1)
    return prediction.item()  # 0 para humano, 1 para máquina

# Traductor google trans
translator = Translator()

# endpoints
@app.route('/')
def home():
    return "Welcome to text analyzer"

@app.route('/api/analyzeText', methods=['POST'])
def analizerText():
    if not request.json or 'text' not in request.json:
        return jsonify({'message': 'Entrada vacia', 'status': 'error'}), 400

    text = request.json['text']

    try:
        # Detecta el idioma
        detected_language = detect(text)

        # El modelo solo funciona en inglés. Si está en español, traducimos al inglés.
        if detected_language == 'es':
            translated_text = translator.translate(text, src='es', dest='en').text
            print("Texto traducido:", translated_text) # Para debuggear
            text_to_use = translated_text
        else:
            text_to_use = text  # Asumiendo que esta en ingles, no se traduce

        
        embeddings = get_embeddings(text_to_use, tokenizer, transformer)

        
        prediction = use_model(embeddings, model)  # 0 (humano) o 1 (máquina)

        
        classification = "humano" if prediction == 0 else "máquina" #

        # Mensaje final
        if detected_language == 'es':
            idiom = 'español'
        else:
            idiom = 'inglés'
        message = f"Idioma = {idiom} \nSe detectó que el texto es hecho por '{classification}'"

        return jsonify({
            'message': message,
            'status': 'success'
        }), 200
    
    except Exception as e:
        return jsonify({
            'message': 'Procesando...',
            'error': str(e),
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
