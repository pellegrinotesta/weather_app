from flask import Flask, render_template, request
from src.cache_manager import WeatherService

app = Flask(__name__)
service = WeatherService()

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_results = []
    error = None
    
    if request.method == 'POST':
        citta_input = request.form.get('city')
        # Gestiamo input multipli (Roma, Milano)
        nomi = [n.strip() for n in citta_input.split(",") if n.strip()]
        
        for n in nomi:
            data = service.get_weather(n)
            if "error" in data:
                error = data["error"]
            else:
                weather_results.append(data)

    return render_template('index.html', results=weather_results, error=error)

if __name__ == '__main__':
    # Usiamo la porta 8080 e disattiviamo il reloader per un test pulito
    app.run(host='127.0.0.1', port=8080, debug=True)