from flask import Flask, render_template, request, send_file
import io

app = Flask(__name__)

def generate_art(text, style):
    if style == 'star':
        return f"*** {text} ***"
    elif style == 'box':
        border = '+' + '-' * (len(text) + 2) + '+'
        return f"{border}\n| {text} |\n{border}"
    elif style == 'wave':
        return '~'.join(text)
    elif style == 'mirror':
        return text + " | " + text[::-1]
    elif style == 'steps':
        return '\n'.join(text[i:] for i in range(len(text)))
    else:
        return text

@app.route('/', methods=['GET', 'POST'])
def index():
    art_result = ''
    text = ''
    style = 'star'
    if request.method == 'POST':
        text = request.form['text']
        style = request.form['style']
        art_resultcl = generate_art(text, style)
    return render_template('index.html', art_result=art_result, text=text, style=style)

@app.route('/download', methods=['POST'])
def download():
    text = request.form['text']
    style = request.form['style']
    art = generate_art(text, style)
    file_stream = io.BytesIO()
    file_stream.write(art.encode('utf-8'))
    file_stream.seek(0)
    return send_file(file_stream, as_attachment=True, download_name="art.txt", mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
