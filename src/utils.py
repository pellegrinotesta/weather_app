def interpret_wmo_code(code):
    """Converte i codici numerici WMO in descrizioni leggibili."""
    mapping = {
        0: "Cielo sereno",
        1: "Prevalentemente sereno", 2: "Parzialmente nuvoloso", 3: "Nuvoloso",
        45: "Nebbia", 51: "Pioggerellina", 61: "Pioggia debole", 95: "Temporale"
    }
    return mapping.get(code, "Condizioni variabili")

def format_side_by_side(weather_results):
    """
    Prende una lista di risultati meteo e li formatta affiancati.
    """
    if not weather_results:
        return "Nessun dato da visualizzare."

    # Definiamo le righe della nostra "scheda"
    headers = []
    temps = []
    conditions = []
    winds = []

    for res in weather_results:
        if "error" in res:
            city_name = "Errore"
            temp = "N/A"
            cond = "N/D"
            wind = "N/D"
        else:
            city_name = res['citta'][:15] # Tronchiamo nomi troppo lunghi
            temp = f"{res['temp']}°C"
            cond = res['desc'][:15]
            wind = f"{res['vento']}km/h"

        # Creiamo colonne di larghezza fissa (es. 20 caratteri)
        headers.append(f"{city_name:<20}")
        temps.append(f"Termo: {temp:<13}")
        conditions.append(f"Meteo: {cond:<13}")
        winds.append(f"Vento: {wind:<13}")

    # Uniamo le liste in stringhe singole separate da uno spazio o pipe
    separator = " | "
    output = [
        separator.join(headers),
        separator.join(["-"*20 for _ in weather_results]),
        separator.join(temps),
        separator.join(conditions),
        separator.join(winds),
        separator.join(["-"*20 for _ in weather_results])
    ]

    return "\n".join(output)

def format_weather_report(data):
    """Crea una stringa formattata ed elegante per i dati meteo."""
    report = [
        f"📍 LOCALITÀ: {data['citta'].upper()}",
        f"{'='*35}",
        f"🌡️  Temperatura:    {data['temp']:>5}°C",
        f"☁️  Condizioni:     {data['desc']}",
        f"{'-'*35}",
        f"💧  Umidità:       {data['umidita']:>5}%",
        f"🌬️  Vento:         {data['vento']:>5} km/h",
        f"🌧️  Precipitazioni: {data['precipitazioni']:>5} mm",
        f"{'='*35}"
    ]
    return "\n".join(report)