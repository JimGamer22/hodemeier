# 📧 Email Generator für Hodemeier Hub

## 🎯 Was wurde erstellt?

Ein **vollständig funktionsfähiger Email-Generator** mit Dashboard für dein Hodemeier-Projekt. Das System ermöglicht es dir, schnell und professionell Emails zu generieren, zu verwalten und zu tracken.

### ✨ Highlights
- ✅ **5 vorgefertigte Email-Templates** (Willkommen, Benachrichtigung, Erinnerung, Bericht, Custom)
- ✅ **Integriertes Dashboard** mit Live-Metriken, Filtern und Suchfunktion
- ✅ **Google Sheets Integration** für Datenverwaltung
- ✅ **Email-Variablen** zur Personalisierung (`{recipient_name}`, `{company}`, etc.)
- ✅ **Vorschau-Funktion** vor dem Speichern
- ✅ **Status-Tracking** (Entwurf, geplant, gesendet)
- ✅ **Verwaltungstools** zum Löschen von Emails

---

## 📦 Bereitgestellte Dateien

### 1. **email_generator.py** (15 KB)
Die Hauptkomponente - enthält:
- 5 Email-Templates mit Variablen
- Email-Erstellungs-Interface
- Dashboard mit Filterfunktion
- Verwaltungs-Tools
- Google Sheets Integration

### 2. **main.py** (2.4 KB)
Aktualisierte Hauptdatei mit:
- Import des Email Generators
- Navigation zu neuem Email-Tab
- Routing-Logik

### 3. **QUICKSTART.md** (5 KB)
Schnellanleitung für 5-Minuten Setup:
- Installation in 3 Schritten
- Erste Email erstellen
- Häufige Fragen

### 4. **EMAIL_GENERATOR_GUIDE.md** (6.5 KB)
Detailliertes Manual mit:
- Vollständige Feature-Dokumentation
- API-Referenz
- Best Practices
- Troubleshooting

### 5. **INTEGRATION_SUMMARY.md** (11 KB)
Umfassende Übersicht mit:
- Workflow-Beispiele
- Datenspeicherung
- Nächste Schritte
- Erweiterte Features

### 6. **setup.py** (2.1 KB)
Optionales Setup-Script zum Initialisieren der Google Sheets Worksheets

### 7. **requirements.txt**
Abhängigkeiten (keine neuen Pakete nötig!)

---

## 🚀 Schnellstart

### Schritt 1: Datei kopieren
```bash
cp email_generator.py /dein/hodemeier/projekt/
```

### Schritt 2: main.py anpassen
Ersetze deine `main.py` mit der neuen Version ODER integriere manuell:

```python
# Am Anfang hinzufügen:
from email_generator import render_email_generator_tab

# Im pages Dictionary:
pages = {
    "📊  ApoRed Predictor": "predictor",
    "📧  Email Generator": "email",    # ← NEU
    "📧  Google Manager": "google",
}

# Im main-Block:
elif choice == "email":                # ← NEU
    render_email_generator_tab()
```

### Schritt 3: Google Sheets vorbereiten
Erstelle ein Worksheet mit dem Namen `emails` und diese Spalten:
- `email_id` | `sender` | `recipient` | `recipient_name` | `subject` 
- `body` | `template` | `status` | `created_at` | `sent_at`

**Fertig!** 🎉

---

## 📋 Features Überblick

### Tab 1: ✉️ Email erstellen
- Email-Template auswählen (5 vorgefertigte + Custom)
- Absender/Empfänger eingeben
- Betreff und Body anpassen
- Variablen verwenden: `{recipient_name}`, `{company}`, etc.
- Vorschau anzeigen vor Speicherung
- Status setzen (Entwurf/geplant/gesendet)
- In Google Sheets speichern

### Tab 2: 📋 Dashboard
- **Metriken**: Gesamte Emails, gesendet, Entwürfe, geplant
- **Filter**: Nach Status, Template, Name
- **Suchfunktion**: Nach Email-Adresse oder Name
- **Tabelle**: Alle Emails mit wichtigen Infos
- **Detailansicht**: Vollständige Email-Information

### Tab 3: 🗑 Verwalten
- Einzelne Emails löschen
- Alle Emails auf einmal löschen (mit Bestätigung)

---

## 🎯 5 Email-Templates

| Template | Icon | Best For |
|----------|------|----------|
| **Willkommen** | 🎉 | Neue Nutzer, Onboarding, Team-Mitglieder |
| **Benachrichtigung** | 🔔 | Wichtige Mitteilungen, Updates, System-Alerts |
| **Erinnerung** | ⏰ | Deadlines, Follow-ups, Task-Management |
| **Bericht** | 📊 | Monatliche Reports, Zusammenfassungen, Analytics |
| **Benutzerdefiniert** | ✍️ | Völlig freie Gestaltung, eigene Templates |

---

## 💡 Beispiel-Workflows

### Beispiel 1: Willkommens-Email an neuen Nutzer
```
1. Tab "Email erstellen" öffnen
2. Empfänger: max@example.com, "Max Mustermann"
3. Template: 🎉 Willkommen (wird automatisch gefüllt)
4. Status: "gesendet"
5. [💾 Speichern]
6. ✅ Email in Google Sheets gespeichert
7. Tab "Dashboard" → Email sichtbar in der Liste
```

### Beispiel 2: Personalisierte Erinnerung
```
Betreff: Erinnerung: Bericht von {recipient_name} fällig

Nachricht:
Hallo {recipient_name},

bitte reiche deinen Bericht ein!

{message}

Deadline: {deadline}

Viele Grüße
```

### Beispiel 3: Monatlicher Report
```
1. Template: 📊 Bericht
2. Für mehrere Empfänger kopieren & anpassen
3. Status für alle "geplant"
4. Im Dashboard filtern nach Template
5. Alle auf einmal verwalten
```

---

## 🔧 Verfügbare Variablen

Nutze diese Variablen in Betreff und Body - sie werden automatisch ersetzt:

```
{company}        → Unternehmensname (z.B. "Hodemeier GmbH")
{recipient_name} → Name des Empfängers (z.B. "Max Mustermann")
{title}          → Betreff/Titel (z.B. "Wichtige Ankündigung")
{message}        → Nachrichteninhalt
{deadline}       → Fälligkeitsdatum (z.B. "31.12.2024")
{month}          → Monat/Zeitraum (z.B. "Dezember 2024")
```

**Beispiel:**
```
Betreff: Willkommen bei {company}!
→ Wird zu: "Willkommen bei Hodemeier!"

Nachricht: Hallo {recipient_name}, ...
→ Wird zu: "Hallo Max, ..."
```

---

## 📊 Datenspeicherung

Jede Email wird in Google Sheets als Zeile gespeichert:

```json
{
  "email_id": "a1b2c3d4",
  "sender": "Hodemeier Team <noreply@hodemeier.de>",
  "recipient": "max@example.com",
  "recipient_name": "Max Mustermann",
  "subject": "Willkommen bei Hodemeier!",
  "body": "Hallo Max, willkommen...",
  "template": "🎉 Willkommen",
  "status": "gesendet",
  "created_at": "14.04.2024 14:30",
  "sent_at": "14.04.2024 14:31"
}
```

---

## ⚙️ Konfiguration

### Default-Werte ändern
In `email_generator.py` anpassen:

```python
# Zeile ca. 60-65:
sender_name = st.text_input("Absendername", value="HIER_ÄNDERN", ...)
sender_email = st.text_input("Absender Email", value="YOUR_EMAIL@domain", ...)
company_name = st.text_input("Unternehmensname", value="HIER_ÄNDERN", ...)
```

### Templates anpassen/hinzufügen
In `email_generator.py` um Zeile 6-30:

```python
EMAIL_TEMPLATES = {
    "mein_template": {
        "name": "🎨 Mein Template",
        "subject": "Mein Betreff",
        "body": "Mein Body mit {recipient_name} und {company}"
    },
    # ... weitere Templates
}
```

---

## 🔄 Integration mit anderen Features

### Mit ApoRed Predictor
Du kannst Emails senden, wenn eine Wette erfolgreich ist:
```python
if ev > 1.05 and kelly > 0:
    # Öffne Email-Tab und sende Erfolgs-Benachrichtigung
```

### Mit Google Manager
Zukünftig: Emails an mehrere Google-Accounts verwalten

---

## 📚 Dokumentation

Alle Details findest du in den mitgelieferten Dokumenten:

1. **QUICKSTART.md** - Schneller Einstieg (5 Min)
2. **EMAIL_GENERATOR_GUIDE.md** - Vollständiges Manual
3. **INTEGRATION_SUMMARY.md** - Detaillierte Übersicht
4. Diese README - Überblick

---

## 🐛 Häufige Probleme & Lösungen

### Problem: "Worksheet 'emails' nicht gefunden"
**Lösung:**
1. Öffne Google Sheets
2. Erstelle ein neues Worksheet
3. Nenne es exakt `emails` (kleinschreibung!)
4. App neustarten

### Problem: Emails werden nicht gespeichert
**Lösung:**
1. Überprüfe `secrets.toml` - Google Sheets Connection
2. Stelle sicher, dass die Spreadsheet-ID richtig ist
3. Überprüfe die Berechtigung deines Google-Accounts
4. Nutze optional `setup.py` zur Auto-Initialisierung

### Problem: Variablen werden nicht ersetzt
**Lösung:**
- Nutze Klammern: `{variable}` nicht `variable`
- Überprüfe die genaue Schreibweise
- Beispiel: `{recipient_name}` ✅ nicht `{recipient}` ❌

### Problem: Dashboard zeigt keine Emails
**Lösung:**
1. Hast du eine Email erstellt und gespeichert?
2. Tab wechseln und zurückwechseln (Cache refresh)
3. Browser-Cache leeren
4. App neustarten: `streamlit run main.py`

---

## 🚀 Nächste Schritte (Optional)

### Direkt nutzbar (sofort verfügbar)
✅ Email-Generator mit 5 Templates  
✅ Google Sheets Integration  
✅ Live Dashboard  
✅ Email-Variablen  
✅ Status-Tracking  

### Für die Zukunft (Optional)
🔜 SMTP Email-Versand Integration  
🔜 HTML-Email Templates  
🔜 Email-Anhänge  
🔜 Zeitgesteuerte Emails  
🔜 Template-Editor in der UI  
🔜 Email-Öffnung Tracking  

---

## ✅ Checkliste für Setup

- [ ] `email_generator.py` ins Projekt kopiert
- [ ] `main.py` aktualisiert oder mit neuer Version ersetzt
- [ ] Google Sheets Worksheet `emails` erstellt
- [ ] Alle 10 Spalten angelegt
- [ ] Streamlit App gestartet
- [ ] Navigation zu "📧 Email Generator" sichtbar
- [ ] Angemeldet (mit Passwort)
- [ ] Erste Test-Email erstellt
- [ ] Test-Email im Dashboard sichtbar
- [ ] Status "gesendet" angezeigt

---

## 📞 Technische Infos

### Dependencies
```
streamlit>=1.28.0
pandas>=2.0.0
altair>=5.0.0
st-gsheets-connection>=0.1.0
```

**Wichtig:** Keine neuen Pakete nötig! Nutzt bereits installierte Dependencies.

### File Structure
```
hodemeier/
├── main.py                      (aktualisiert)
├── email_generator.py           (NEU - 15 KB)
├── apored/
│   ├── __init__.py
│   └── predictor.py
├── google_manager/
│   ├── __init__.py
│   └── automation.py
├── auth.py
├── .gitignore
├── requirements.txt
└── README.md
```

### Google Sheets Schema
```
Sheet: emails
├── email_id           STRING  (Unique ID)
├── sender             STRING  (Name <email>)
├── recipient          STRING  (Email-Adresse)
├── recipient_name     STRING  (Personen-Name)
├── subject            STRING  (Email-Betreff)
├── body               STRING  (Email-Body)
├── template           STRING  (Template-Name)
├── status             STRING  (Entwurf|geplant|gesendet)
├── created_at         STRING  (Datetime)
└── sent_at            STRING  (Datetime)
```

---

## 🎓 Verwendete Technologien

- **Streamlit** - Web-UI Framework
- **pandas** - Datenverwaltung
- **Google Sheets Connection** - Cloud-Datenspeicherung
- **Altair** - (nicht genutzt im Email-Generator, aber verfügbar)

---

## 📝 Lizenz & Credits

- Erstellt für: **Hodemeier Hub**
- Datum: **14.04.2024**
- Status: **✅ Produktionsreif**
- Version: **1.0**

---

## 🎉 Viel Erfolg!

Dein Email-Generator ist fertig zum Einsatz!

**Nächste Schritte:**
1. Alle Dateien in dein Projekt kopieren
2. Google Sheets Worksheet erstellen
3. App hochfahren
4. Anmelden
5. Erste Email erstellen
6. Im Dashboard genießen! 📧

Bei Fragen siehe die detaillierte Dokumentation oder den Code-Kommentare in `email_generator.py`.

Happy Emailing! 🚀

---

*Fragen? Siehe QUICKSTART.md oder EMAIL_GENERATOR_GUIDE.md*
