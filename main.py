import deepl
import pandas as pd
import re
import json

# WICHTIG: Ersetze dies durch deinen echten Key (und halte ihn geheim!)
AUTH_KEY = "3364d381-797f-4c04-a2d5-9e1855be1905:fx" 

def translate_and_save(text, excel_file="result.xlsx", json_file="result.json"):
    # 1. Text teilen (nach Punkt, Komma, Semikolon)
    gefilterter_text = re.sub(r'([.,;?])\s*', r'\1\n', text)
    zeilen = [z.strip() for z in gefilterter_text.split('\n') if z.strip()]

    # 2. DeepL Setup
    translator = deepl.Translator(AUTH_KEY)
    
    print(f"Starte Batch-Übersetzung von {len(zeilen)} Zeilen...")

    # 3. Batch-Übersetzung (IT -> DE)
    results = translator.translate_text(zeilen, source_lang="IT", target_lang="DE")
    
    # 4. Daten für JSON und Excel vorbereiten
    # Hier nutzen wir direkt "it" und "de" als Keys
    daten = []
    for original, result in zip(zeilen, results):
        daten.append({
            "it": original,
            "de": result.text
        })

    # 5. Als JSON speichern
    # 'ensure_ascii=False' sorgt dafür, dass Umlaute/Sonderzeichen korrekt bleiben
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)
    
    # 6. Als Excel speichern (für die Übersicht)
    df = pd.DataFrame(daten)
    # Wir benennen die Spalten für Excel kurz um, damit sie schöner aussehen
    df.columns = ["Italienisch", "Deutsch"]
    df.to_excel(excel_file, index=False)

    print(f"Fertig!")
    print(f"-> JSON gespeichert unter: {json_file}")
    print(f"-> Excel gespeichert unter: {excel_file}")


MEIN_TEXT = """ciao"""


translate_and_save(MEIN_TEXT)