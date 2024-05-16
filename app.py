from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/registra_medico', methods=['GET', 'POST'])
def registra_medico():
    return render_template('registra_medico.html')
@app.route('/registra_infermiere', methods=['GET', 'POST'])
def registra_infermiere():
    return render_template('registra_infermiere.html')
@app.route('/registra_paziente', methods=['GET', 'POST'])
def registra_paziente():
    return render_template('registra_paziente.html')

@app.route('/accesso_medico', methods=['GET', 'POST'])
def accesso_medico():
    return render_template('accesso_medico.html')
@app.route('/accesso_infermiere', methods=['GET', 'POST'])
def accesso_infermiere():
    return render_template('accesso_infermiere.html')
@app.route('/accesso_paziente', methods=['GET', 'POST'])
def accesso_paziente():
    return render_template('accesso_paziente.html')

@app.route('/prenota_visita', methods=['GET', 'POST'])
def prenota_visita():
    return render_template('prenota_visita.html')

@app.route('/submit_registration', methods=['GET', 'POST'])
def submit_registration():
    def _registra_medico() : 
        username = request.form['username']
        password = request.form['password']
        cognome = request.form['cognome']
        nome = request.form['nome']
        codice_fiscale = request.form['codice_fiscale']
        specialita = request.form.getlist('specialita')

        print("Username:", username)
        print("Password:", password)
        print("Cognome:", cognome)
        print("Nome:", nome)
        print("Codice Fiscale:", codice_fiscale)
        print("Specialità:", specialita)
    
        string = f'Username: {username}<br> Password: {password}<br> Cognome: {cognome}<br> Nome: {nome}<br> Specialità: {specialita}<br> Codice Fiscale: {codice_fiscale}<br>' 
        return string
    def _registra_infermiere() : 
        username = request.form['username']
        password = request.form['password']
        cognome = request.form['cognome']
        nome = request.form['nome']

        print("Username:", username)
        print("Password:", password)
        print("Cognome:", cognome)
        print("Nome:", nome)

        string = f'Username: {username}<br> Password: {password}<br> Cognome: {cognome}<br> Nome: {nome}<br>' 
        return string
    def _registra_paziente() :
        username = request.form['username']
        password = request.form['password']
        cognome = request.form['cognome']
        nome = request.form['nome']
        codice_fiscale = request.form['codice_fiscale']
        data_nascita = request.form['data_nascita']
        luogo_nascita = request.form['luogo_nascita']
        
        print("Username:", username)
        print("Password:", password)
        print("Cognome:", cognome)
        print("Nome:", nome)
        print("Codice Fiscale:", codice_fiscale)
        print("Data di Nascita:", data_nascita)
        print("Luogo di Nascita:", luogo_nascita)

        string = f'Username: {username}<br> Password: {password}<br> Cognome: {cognome}<br> Nome: {nome}<br> Codice Fiscale: {codice_fiscale}<br> Data di Nascita: {data_nascita}<br> Luogo di Nascita: {luogo_nascita}' 
        return string
    
    if(request.referrer.endswith('/registra_medico')) : string = _registra_medico()
    if(request.referrer.endswith('/registra_infermiere')) : string = _registra_infermiere()
    if(request.referrer.endswith('/registra_paziente')) : string = _registra_paziente()

    return string

@app.route('/prenotazione_visita', methods=['GET', 'POST'])
def prenotazione_visita():
    patientType = request.form['patientType']
    date = request.form['date']
    time = request.form['time']
    doctor = request.form['doctor']
    regime = request.form['regime']
    urgency = request.form['urgency']

    string = f'Paziente: {patientType}<br>Data: {date}<br>Ora: {time}<br>Medico: {doctor}<br>Regime: {regime}<br>Urgenza: {urgency}<br>'

    return string

if __name__ == '__main__':
    app.run(debug=True)

