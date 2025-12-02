# Haushaltsplaner mit Python & CustomTkinter

Ein einfacher, moderner Haushaltsplaner in Python mit grafischer Oberfläche (GUI) mithilfe von **CustomTkinter**.  
Mit diesem Tool kannst du **Einnahmen und Ausgaben** verwalten, Einträge bearbeiten oder löschen und den **Saldo** automatisch berechnen lassen.

---

## **Features**

- Einnahmen und Ausgaben hinzufügen  
- Bearbeiten oder Löschen von Einträgen  
- Automatische Berechnung von Gesamtausgaben, Gesamteinnahmen und Saldo  
- Scrollbare Liste für viele Einträge  
- Moderner Look dank **CustomTkinter**

---

## **Installation**

1. **Python 3.10+ installieren**  
   (Download: [https://www.python.org/downloads/](https://www.python.org/downloads/))

2. **CustomTkinter installieren**, falls noch nicht vorhanden:

```bash
pip install customtkinter
```

## **Benutzung**
1. *Neuen Eintrag hinzufügen*
    - Name des Eintrags eingeben
    - Betrag in Euro eingeben
    - Typ auswählen: "Einnahme" oder "Ausgabe"
    - Auf 'Speichern' klicken
2. *Eintrag bearbeiten*
    - Auf den 'Bearbeiten-Button' neben dem Eintrag klicken
    - Daten ändern und speichern
3. *Eintrag löschen*
    - Auf den 'Löschen-Button' neben dem Eintrag klicken
4. *Saldo & Gesamtsumme* werden automatisch aktualisiert

## **Ausblick/ Erweiterungen**

- Daten persistent speichern (JSON, CSV)
- Filtern nach Einnahmen und Ausgaben
- Sortierung nach Betrag und/oder Datum
- Farbige Kennzeichnungen für Einnahmen und Ausgaben
- Erweiterungen der GUI mit Diagrammen (z.B Einnahmen vs. Ausgaben pro Monat)
