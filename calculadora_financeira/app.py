from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)

def jsimp(inicial, taxa, tempo):
    taxa = taxa / 100
    montante = inicial + inicial * taxa * tempo
    return montante

def jcompCD(inicial, taxa, tempo, fc=1):
    taxa = taxa / (100 * fc)
    tempo = tempo * fc
    montante = inicial * ((1 + taxa) ** tempo)
    return montante

def jcompCC(inicial, taxa, tempo):
    taxa = taxa / 100
    montante = inicial * np.exp(taxa * tempo)
    return montante

def japort(inicial, taxa, tempo, aporte):
    taxa = taxa / 100
    montante = (aporte / taxa) * (np.exp(taxa * tempo) - 1) + inicial * np.exp(taxa * tempo)
    return montante

@app.route('/', methods=['GET', 'POST'])
def index():
    inicial = 10000
    taxa = 15
    tempo = 15
    aporte = 1000
    fc = 1
    img_base64 = None

    if request.method == 'POST':
        inicial = float(request.form['inicial'])
        taxa = float(request.form['taxa'])
        tempo = float(request.form['tempo'])
        aporte = float(request.form['aporte'])
        fc = float(request.form['fc'])

        t = np.linspace(0, tempo, 100)
        v = jsimp(inicial, taxa, t)
        w = jcompCD(inicial, taxa, t, fc=fc)
        x = jcompCC(inicial, taxa, t)
        y = japort(inicial, taxa, t, aporte)

        plt.figure(figsize=(10, 6))
        plt.plot(t, v, label='Juros Simples')
        plt.plot(t, w, label='Juros Compostos Discreto')
        plt.plot(t, x, label='Juros Compostos Contínuo')
        plt.plot(t, y, label='Juros Compostos com Aportes')
        plt.title('Crescimento do Montante com Diferentes Regimes de Juros')
        plt.xlabel('Tempo (anos)')
        plt.ylabel('Montante')
        plt.grid(True)
        plt.legend()

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
        plt.close()

    return render_template('index.html', inicial=inicial, taxa=taxa, tempo=tempo, aporte=aporte, fc=fc, img_base64=img_base64)

if __name__ == '__main__':
    app.run(debug=True)