
# Importar
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Conteúdo da página
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinâmicas e formulário de feedback
@app.route('/', methods=['POST'])
def process_form():
    # Botões dos projetos
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')

    # Dados do formulário
    print("FORMULÁRIO RECEBIDO!")
    print(request.form)
    
    email = request.form.get('email')
    comentario = request.form.get('text')

    if email and comentario:
        print("Novo feedback recebido!")
        print("E-mail:", email)
        print("Comentário:", comentario)

        return redirect('/')

    return render_template(
        'index.html',
        button_python=button_python,
        button_discord=button_discord,
        button_html=button_html,
        button_db=button_db
    )


if __name__ == "__main__":
    app.run(debug=True)
