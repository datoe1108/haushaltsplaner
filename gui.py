import customtkinter as ctk

# Liste der Einträge
eintraege = []

# Label für Gesamtsummen
gesamt_label = None


# -------------------------------------------------------------
#  Funktion: Neues Eintrag-Fenster
# -------------------------------------------------------------
def eintrag_hinzufuegen_fenster(parent, list_frame):
    popup = ctk.CTkToplevel(parent)
    popup.title("Neuen Eintrag hinzufügen")
    popup.geometry("450x400")
    popup.attributes('-topmost', True) #Pop-Up Fenster immer im Vordergrund

    # Name
    label_name = ctk.CTkLabel(popup, text="Name des Eintrags:")
    label_name.pack(pady=(20, 5))
    entry_name = ctk.CTkEntry(popup, width=200)
    entry_name.pack()

    # Betrag
    label_betrag = ctk.CTkLabel(popup, text="Betrag in Euro:")
    label_betrag.pack(pady=(20, 5))
    entry_betrag = ctk.CTkEntry(popup, width=200)
    entry_betrag.pack()

    # Typ
    label_typ = ctk.CTkLabel(popup, text="Typ:")
    label_typ.pack(pady=(20, 5))
    dropdown_typ = ctk.CTkOptionMenu(popup, values=["Ausgabe", "Einnahme"])
    dropdown_typ.set("Ausgabe")
    dropdown_typ.pack()

    # Speichern-Funktion
    def speichern():
        name = entry_name.get()
        betrag = entry_betrag.get()
        typ = dropdown_typ.get().lower()

        if name.strip() == "" or betrag.strip() == "":
            print("Bitte beide Felder ausfüllen.")
            return

        try:
            betrag = float(betrag)
        except ValueError:
            print("Betrag muss eine Zahl sein.")
            return

        eintraege.append({"name": name, "betrag": betrag, "typ": typ})
        eintraege_anzeigen(list_frame)

        popup.destroy()

    button_speichern = ctk.CTkButton(popup, text="Speichern", command=speichern, height=30)
    button_speichern.pack(pady=20, padx=20)


# -------------------------------------------------------------
#  Funktion: Eintrag bearbeiten
# -------------------------------------------------------------
def eintrag_bearbeiten_fenster(frame, index):
    eintrag = eintraege[index]

    popup = ctk.CTkToplevel(frame) 
    popup.title("Eintrag bearbeiten")
    popup.geometry("350x300")
    popup.attributes('-topmost', True) # Pop-Up Fenster immer im Vordergrund

    # Name
    label_name = ctk.CTkLabel(popup, text="Name des Eintrags:")
    label_name.pack(pady=(20, 5))
    entry_name = ctk.CTkEntry(popup, width=200)
    entry_name.pack()
    entry_name.insert(0, eintrag["name"])

    # Betrag
    label_betrag = ctk.CTkLabel(popup, text="Betrag in Euro:")
    label_betrag.pack(pady=(20, 5))
    entry_betrag = ctk.CTkEntry(popup, width=200)
    entry_betrag.pack()
    entry_betrag.insert(0, str(eintrag["betrag"]))

    # Typ
    label_typ = ctk.CTkLabel(popup, text="Typ:")
    label_typ.pack(pady=(20, 5))
    dropdown_typ = ctk.CTkOptionMenu(popup, values=["Ausgabe", "Einnahme"])
    dropdown_typ.pack()
    dropdown_typ.set(eintrag["typ"].capitalize())

    # Speichern-Funktion
    def speichern():
        name = entry_name.get()
        betrag = entry_betrag.get()
        typ = dropdown_typ.get().lower()

        if name.strip() == "" or betrag.strip() == "":
            print("Bitte beide Felder ausfüllen.")
            return

        try:
            betrag = float(betrag)
        except ValueError:
            print("Betrag muss eine Zahl sein.")
            return

        eintraege[index] = {"name": name, "betrag": betrag, "typ": typ}
        eintraege_anzeigen(frame)
        popup.destroy()

    button_speichern = ctk.CTkButton(popup, text="Speichern", command=speichern, height=30)
    button_speichern.pack(pady=20, padx=20)


# -------------------------------------------------------------
#  Funktion: Einträge anzeigen
# -------------------------------------------------------------
def eintraege_anzeigen(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    if not eintraege:
        leer_label = ctk.CTkLabel(frame, text="Keine Einträge vorhanden.")
        leer_label.pack(pady=10)
        update_gesamt()
        return

    for i, eintrag in enumerate(eintraege):
        name = eintrag["name"]
        betrag = eintrag["betrag"]
        typ = eintrag["typ"]

        row_frame = ctk.CTkFrame(frame)
        row_frame.pack(fill="x", pady=5, padx=5)

        # Eintrag-Label mit Typ
        label_text = ctk.CTkLabel(row_frame, text=f"{i+1}. [{typ[0].upper()}] {name}: {betrag} €")
        label_text.pack(side="left", padx=10, pady=5)

        # Bearbeiten-Button
        button_edit = ctk.CTkButton(row_frame, text="Bearbeiten", width=80,
                                    command=lambda idx=i: eintrag_bearbeiten_fenster(frame, idx))
        button_edit.pack(side="right", padx=(0,15), pady=5)

        # Löschen-Button
        button_delete = ctk.CTkButton(row_frame, text="Löschen", width=80,
                                      command=lambda idx=i: (eintraege.pop(idx), eintraege_anzeigen(frame)))
        button_delete.pack(side="right", padx=(0,5), pady=5)

    update_gesamt()


# -------------------------------------------------------------
#  Funktion: Gesamtsummen & Saldo
# -------------------------------------------------------------
def update_gesamt():
    if gesamt_label is None:
        return
    gesamt_ausgaben = sum(e["betrag"] for e in eintraege if e["typ"] == "ausgabe")
    gesamt_einnahmen = sum(e["betrag"] for e in eintraege if e["typ"] == "einnahme")
    saldo = gesamt_einnahmen - gesamt_ausgaben
    gesamt_label.configure(
        text=f"Einnahmen: {gesamt_einnahmen:.2f} €  |  Ausgaben: {gesamt_ausgaben:.2f} €  |  Saldo: {saldo:.2f} €"
    )


# -------------------------------------------------------------
#  Hauptfenster
# -------------------------------------------------------------
def main():
    global gesamt_label, list_frame

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    fenster = ctk.CTk()
    fenster.title("Haushaltsplaner")
    fenster.geometry("600x550")

    # Titel
    titel = ctk.CTkLabel(fenster, text="Haushaltsplaner", font=ctk.CTkFont(size=24, weight="bold"))
    titel.pack(pady=10)

    # Button oben
    buttons_frame = ctk.CTkFrame(fenster)
    buttons_frame.pack(pady=10)

    button_add = ctk.CTkButton(buttons_frame, text="Eintrag hinzufügen",
                               command=lambda: eintrag_hinzufuegen_fenster(fenster, list_frame))
    button_add.pack(padx=10)

    # Scrollbare Liste
    list_frame = ctk.CTkScrollableFrame(fenster, width=550, height=350)
    list_frame.pack(pady=15)

    # Label für Gesamtsummen
    gesamt_label = ctk.CTkLabel(fenster, text="Einnahmen: 0.00 €  |  Ausgaben: 0.00 €  |  Saldo: 0.00 €",
                                 font=ctk.CTkFont(size=16))
    gesamt_label.pack(pady=10)

    # Initial laden
    eintraege_anzeigen(list_frame)

    fenster.mainloop()


if __name__ == "__main__":
    main()
