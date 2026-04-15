# Email Generator - Integration Guide

## 📋 Überblick

Der Email Generator ermöglicht es dir, schnell und effizient Emails zu generieren und zu verwalten. Alle Emails werden in Google Sheets gespeichert und können im Dashboard verwaltet werden.

## 🚀 Installation

### 1. Dateien hinzufügen

Kopiere diese Datei in dein Projekt:
- `email_generator.py` → Hauptverzeichnis

### 2. main.py aktualisieren

Ersetze deine `main.py` mit der aktualisierten Version oder integriere manuell:

```python
from email_generator import render_email_generator_tab

# Im pages-Dictionary:
pages = {
    "📊  ApoRed Predictor": "predictor",
    "📧  Email Generator": "email",    # ← Neu
    "📧  Google Manager": "google",
}

# Im main-Teil:
elif choice == "email":
    render_email_generator_tab()
```

### 3. Google Sheets vorbereiten

**Wichtig:** Erstelle ein neues Worksheet in deinem Google Sheet namens `emails` mit folgenden Spalten:

| email_id | sender | recipient | recipient_name | subject | body | template | status | created_at | sent_at |
|----------|--------|-----------|---|---------|------|----------|--------|-----------|---------|
| abc12345 | Name <email> | user@example.com | Max Mustermann | Betreff | Nachricht... | 🎉 Willkommen | gesendet | 01.01.2024 12:30 | 01.01.2024 12:31 |

## 🎯 Features

### 📧 Email-Templates

Der Generator kommt mit 5 vorgefertigten Templates:

1. **🎉 Willkommen** - Für neue Nutzer/Team-Mitglieder
2. **🔔 Benachrichtigung** - Für wichtige Mitteilungen
3. **⏰ Erinnerung** - Für Deadlines und Aufgaben
4. **📊 Bericht** - Für regelmäßige Reports
5. **✍️ Benutzerdefiniert** - Komplett frei gestaltbar

### ✉️ Tab 1: Email erstellen

- **Template auswählen** - Vorgefertigte oder eigene Vorlagen nutzen
- **Variablen verwenden** - `{company}`, `{recipient_name}`, `{message}`, etc.
- **Vorschau anzeigen** - Vor dem Speichern prüfen
- **Status setzen** - Entwurf, geplant oder gesendet

**Verfügbare Variablen:**
- `{company}` - Unternehmensname
- `{recipient_name}` - Name des Empfängers
- `{title}` - Titel/Thema
- `{message}` - Nachrichteninhalt
- `{deadline}` - Termin/Deadline
- `{month}` - Monat/Zeitraum

### 📋 Tab 2: Dashboard

**Dashboard-Metriken:**
- Gesamtanzahl Emails
- Anzahl gesendeter Emails
- Anzahl Entwürfe
- Anzahl geplanter Emails

**Filteroptionen:**
- Nach Status filtern (Entwurf, geplant, gesendet)
- Nach Template filtern
- Nach Email/Name suchen

**Detailansicht:**
- Vollständige Email-Informationen anzeigen
- Absender, Empfänger, Template, Status
- Zeitstempel (erstellt, gesendet)

### 🗑 Tab 3: Verwaltung

- **Email löschen** - Einzelne Emails entfernen
- **Alle Emails löschen** - Vollständiger Reset (mit Bestätigung)

## 💡 Beispiele

### Beispiel 1: Willkommens-Email

**Template:** 🎉 Willkommen
**Betreff:** Willkommen bei {company}!
**Nachricht:** (Standard aus Template)
**Variablen:**
- {company} = "Hodemeier GmbH"
- {recipient_name} = "Max Mustermann"

### Beispiel 2: Erinnerungs-Email

**Template:** ⏰ Erinnerung
**Betreff:** Erinnerung: Projekt Deadline
**Nachricht:**
```
Hallo {recipient_name},

dies ist eine freundliche Erinnerung für dich:

{message}

Bitte handle bis zum {deadline}.

Viele Grüße,
Das Team
```

**Variablen:**
- {recipient_name} = "Anna Schmidt"
- {message} = "Dein Projektbericht muss eingereicht werden"
- {deadline} = "31.12.2024"

### Beispiel 3: Benutzerdefinierte Email

**Template:** ✍️ Benutzerdefiniert
**Betreff:** Individuelle Email
**Nachricht:** Komplett frei gestalten

## 📊 Datenstruktur

Jede Email hat folgende Eigenschaften:

```json
{
  "email_id": "abc12345",           // Eindeutige ID
  "sender": "Name <email@domain>",  // Absender
  "recipient": "user@example.com",  // Empfänger Email
  "recipient_name": "Max Mustermann", // Empfänger Name
  "subject": "Betreff",              // Email-Betreff
  "body": "Nachricht...",            // Email-Body
  "template": "🎉 Willkommen",       // Verwendetes Template
  "status": "gesendet",              // Status
  "created_at": "01.01.2024 12:30",  // Erstellungszeit
  "sent_at": "01.01.2024 12:31"      // Sendezeit
}
```

## ⚙️ Konfiguration

### Standardwerte ändern

In `email_generator.py` kannst du folgende Defaults anpassen:

```python
sender_name = st.text_input("Absendername", value="DEIN_NAME", ...)
sender_email = st.text_input("Absender Email", value="DEINE_EMAIL@domain.com", ...)
company_name = st.text_input("Unternehmensname", value="DEIN_UNTERNEHMEN", ...)
```

### Templates anpassen

Ändere die `EMAIL_TEMPLATES` dictionary in `email_generator.py`:

```python
EMAIL_TEMPLATES = {
    "welcome": {
        "name": "🎉 Willkommen",
        "subject": "Dein Custom Betreff",
        "body": "Dein Custom Body..."
    },
    # ...
}
```

## 🔗 Integration mit anderen Features

Der Email Generator lässt sich leicht mit anderen Tools verbinden:

### Mit ApoRed Predictor
```python
# Sende automatisch eine Email, wenn eine Wette erfolgreich ist
if ev > 1.05:
    render_email_generator_tab()  # Email-Generator öffnen
```

### Mit Google Manager
```python
# Verbinde Email-Versand mit Account-Verwaltung
# (Placeholder für zukünftige Integration)
```

## 🛠 Troubleshooting

### Problem: "Worksheet 'emails' nicht gefunden"
**Lösung:** Erstelle das Worksheet `emails` in Google Sheets mit den richtigen Spalten.

### Problem: Emails werden nicht gespeichert
**Lösung:** Überprüfe die Google Sheets Connection im `secrets.toml`:
```toml
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"
```

### Problem: Variablen werden nicht ersetzt
**Lösung:** Stelle sicher, dass du die Variablen in Klammern schreibst: `{variable_name}`

## 📝 Best Practices

1. **Immer Vorschau anzeigen** - Vor dem Speichern mit "Email-Vorschau" prüfen
2. **Klare Betreffzeilen** - Nutze sprechende Betreffzeilen
3. **Variablen verwenden** - Personalisiere Emails mit `{recipient_name}`
4. **Status setzen** - Unterscheide zwischen Entwurf, geplant und gesendet
5. **Regelmäßig aufräumen** - Lösche alte Emails im Tab "Verwalten"

## 🚀 Zukünftige Features

- [ ] Automatischer Email-Versand via SMTP
- [ ] HTML-Email-Support
- [ ] Email-Anhänge
- [ ] Geplante Emails (zeitgesteuert)
- [ ] Email-Vorlagen-Editor
- [ ] Automatische Erinnerungen
- [ ] Email-Template-Duplikation
- [ ] Batch-Email-Versand

---

**Version:** 1.0  
**Letzte Aktualisierung:** 14.04.2024
