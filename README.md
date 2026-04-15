# Python Weather App (Open-Meteo)
Una semplice ma potente applicazione Python da riga di comando che fornisce dati meteorologici in tempo reale. Il sistema utilizza l'API di geocodifica per trovare le coordinate di qualsiasi città e recupera i dati atmosferici correnti tramite Open-Meteo.

🚀 Panoramica del Progetto
L'applicazione permette agli utenti di inserire il nome di una città e ricevere istantaneamente le condizioni meteo principali. È progettata con un'architettura a prova di errore, gestendo input non validi e problemi di rete, mantenendo al contempo un registro storico delle operazioni tramite un file di log dedicato.

🛠️ Installazione
Clona il repository:

Bash
git clone https://github.com/pellegrinotesta/weather_app.git
cd weather-app
Crea un ambiente virtuale (consigliato):

Bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
Installa le dipendenze:
Questa app utilizza la libreria requests.

Bash
pip install requests
📖 Guida all'Uso
Avvia lo script principale:

Bash
python main.py
Segui le istruzioni a schermo:

Inserisci il nome della città quando richiesto.

Visualizza i dati (Temperatura, Vento, Umidità).

Controlla il file weather_app.log per lo storico delle chiamate e gli eventuali errori registrati.

📊 Output di Esempio
JSON
{
  "citta": "Milano, IT",
  "temperatura_c": 18.5,
  "velocita_vento_kmh": 12.3,
  "umidita_relativa": 65,
  "descrizione": "Parzialmente nuvoloso"
}
✨ Funzionalità
Geocodifica Intelligente: Converte i nomi delle città in coordinate geografiche precise (Lat/Lon).

Dati in Tempo Reale: Recupera temperatura, velocità del vento e umidità relativa.

Gestione Errori: Gestisce città inesistenti, assenza di connessione internet e timeout delle API.

Sistema di Logging: Registra ogni richiesta e errore su un file locale per facilitare il debugging.

Nessuna Chiave API: Utilizza Open-Meteo, rendendo l'app pronta all'uso senza configurazioni complesse.

🔮 Miglioramenti Futuri
[ ] Previsioni a 5 giorni: Aggiungere un grafico delle temperature settimanali.

[ ] Interfaccia Grafica (GUI): Implementare una finestra user-friendly con Tkinter o PyQt.

[ ] Supporto Multi-lingua: Permettere all'utente di scegliere la lingua delle descrizioni meteo.

[ ] Esportazione Dati: Salvare i risultati in formato CSV o Excel.

Note Tecniche
L'app sfrutta i seguenti endpoint:

Geocoding: https://geocoding-api.open-meteo.com/

Weather: https://api.open-meteo.com/v1/forecast
