from flask import Flask, render_template, request, session
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_sessao'  # Necessário para usar sessões no Flask

# Configuração do modelo e chave de API
genai.configure(api_key="AIzaSyCk-u-JNCWlX0-G5omIdhictzVNW8bEZbM")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=(
        "Baymax: Assistente Virtual e Sistema de Gestão de Campus\n"
    )
)


@app.route('/')
def home():
    # Recupera o histórico da sessão, ou inicializa uma lista vazia
    chat_history = session.get('chat_history', [])
    return render_template('IA.html', chat_history=chat_history)


@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']

    # Gera a resposta da IA
    response = model.generate_content([user_input])

    # Recupera o histórico da sessão
    chat_history = session.get('chat_history', [])

    # Adiciona a nova interação (pergunta e resposta)
    chat_history.append({'user_input': user_input, 'ai_response': response.text})

    # Atualiza o histórico na sessão
    session['chat_history'] = chat_history

    return render_template('IA.html', chat_history=chat_history)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
