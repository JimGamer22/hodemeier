# 📧 Email Generator - Quick Start

## 🚀 Schnelleinstieg (5 Minuten)

### 1️⃣ Installation

```bash
# Email Generator Datei in dein Projekt kopieren
cp email_generator.py /dein/projekt/

# requirements.txt hat bereits alle nötigen Packages
# Nichts zu updaten!
```

### 2️⃣ main.py anpassen

Füge diese 2 Zeilen am Anfang von `main.py` ein:
```python
from email_generator import render_email_generator_tab  # ← NEU
```

Und im `pages` Dictionary:
```python
pages = {
    "📊  ApoRed Predictor": "predictor",
    "📧  Email Generator": "email",    # ← NEU
    "📧  Google Manager": "google",
}
```

Und im `if choice == ...` Block:
```python
elif choice == "email":              # ← NEU
    render_email_generator_tab()     # ← NEU
```

### 3️⃣ Google Sheets vorbereiten

Erstelle ein neues **Worksheet** (nicht Spreadsheet!) mit dem Namen `emails`:

| email_id | sender | recipient | recipient_name | subject | body | template | status | created_at | sent_at |
|---|---|---|---|---|---|---|---|---|---|

Das war's! Die Spalten werden automatisch gefüllt.

## 📋 Templates

| Template | Icon | Verwendung |
|----------|------|-----------|
| Willkommen | 🎉 | Neue Nutzer/Team-Mitglieder |
| Benachrichtigung | 🔔 | Wichtige Mitteilungen |
| Erinnerung | ⏰ | Deadlines, Aufgaben |
| Bericht | 📊 | Monatliche Reports |
| Benutzerdefiniert | ✍️ | Komplett frei gestalten |

## 🎯 3 Reiter im Email Generator

### Tab 1: ✉️ Email erstellen
- Email-Betreff & Nachricht eingeben
- Template und Status auswählen
- Variablen wie `{recipient_name}` verwenden
- Vorschau anzeigen → Speichern

### Tab 2: 📋 Dashboard
- 📊 Dashboard-Metriken (Gesamt, gesendet, Entwürfe)
- 🔍 Nach Status/Template filtern
- 📧 Suche nach Email/Name
- 👁️ Detailansicht einzelner Emails

### Tab 3: 🗑 Verwalten
- 🗑️ Einzelne Emails löschen
- 🗑️ Alle Emails auf einmal löschen

## 💡 Beispiele

### Email 1: Willkommen
```
Template: 🎉 Willkommen
Absender: John Doe <john@example.com>
Empfänger: max@example.com
Empfängername: Max Mustermann
Betreff: Willkommen bei Hodemeier!
→ Speichern → Dashboard → Fertig!
```

### Email 2: Erinnerung mit Variablen
```
Template: ⏰ Erinnerung
Betreff: Erinnerung: Bericht abgeben
Nachricht:
  Hallo {recipient_name},

  Bitte reiche deinen Bericht bis {deadline} ein.
  
  Viele Grüße,
  Das Team

Variablen werden automatisch ersetzt!
```

## 🔧 Nützliche Variablen

```
{company}        → Unternehmensname
{recipient_name} → Empfängername
{title}          → Betreff/Titel
{message}        → Nachrichtentext
{deadline}       → Fälligkeitsdatum
{month}          → Monat/Zeitraum
```

## ⚡ Status-Codes

| Status | Icon | Bedeutung |
|--------|------|-----------|
| Entwurf | 📝 | Noch nicht gesendet |
| geplant | ⏱️ | Soll später gesendet werden |
| gesendet | ✅ | Bereits gesendet |

## 🔗 Integration mit anderen Tabs

### Mit ApoRed Predictor
```python
# Sende Email wenn Wette erfolgreich ist
if ev > 1.05:
    # Email-Tab öffnen
```

### Mit Google Manager
```python
# Emails an mehrere Google-Accounts
```

## 🐛 Häufige Probleme

**Problem:** Worksheet nicht gefunden
→ Stelle sicher, dass Worksheet `emails` existiert (nicht Spreadsheet!)

**Problem:** Emails werden nicht gespeichert
→ Überprüfe Google Sheets Connection in `secrets.toml`

**Problem:** Variablen werden nicht ersetzt
→ Verwende Klammern: `{variable}` nicht `variable`

## 📊 Dashboard-Metriken

```
┌─────────────────┬──────────┬──────────┬──────────┐
│ Gesamt Emails   │ Gesendet │ Entwürfe │ Geplant  │
│       42        │    28    │    10    │    4     │
└─────────────────┴──────────┴──────────┴──────────┘
```

## 🎨 UI Elemente

- ✉️ Tabs: Email-Erstellung, Dashboard, Verwaltung
- 📊 Metriken: Live-Übersicht der Emails
- 🔍 Filter: Nach Status, Template, Name suchen
- 👁️ Vorschau: Email vor dem Speichern prüfen
- 📋 Tabelle: Alle Emails auf einen Blick
- 📄 Details: Vollständige Email-Information

## 🚀 Was ist möglich?

✅ Emails generieren & speichern
✅ Multiple Templates verwenden
✅ Mit Variablen personalisieren
✅ Alle Emails im Dashboard verwalten
✅ Filtern & Suchen
✅ Löschen & Bearbeiten

❌ (Noch nicht möglich) Automatischer SMTP-Versand
❌ (Noch nicht möglich) HTML-Emails
❌ (Noch nicht möglich) Anhänge

## 📞 Support

Falls etwas nicht funktioniert:
1. Überprüfe `secrets.toml` (Google Sheets Connection)
2. Prüfe Worksheet-Namen: `emails` (nicht `Emails`!)
3. Lösche `.streamlit/` Cache und reload
4. Siehe EMAIL_GENERATOR_GUIDE.md für Details

---

**⏱ Setup-Zeit:** ~2 Minuten
**📦 Dependencies:** 0 neue (nutze bestehende)
**🎯 Features:** 5 Templates, Dashboard, Filter, Verwaltung
