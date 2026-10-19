# Anforderungen

## Aufgabe:
Der erste Teil des Projektes ist es, die Anforderungen richtig zu verstehen.

1. **Überleg dir Fragen und beantworte sie mithilfe der Webseite.** 
2. **Schreib eine kurze Zusammenfassung aller Informationen, die du gefunden hast.**

---

## Testobjekt:
> https://grocerymate.masterschool.com/

Webshop mit folgenden Grundfunktionen:

- Registrierung und Login
- Produktsuche mit Sortierfunktion (z. B. nach Preis), Kategorisierung von Produkten
- Produkte zu Favoriten hinzufügen
- Produkte in den Warenkorb legen
- Bestellabschluss: Eingabe von Rechnungs- und Versandinformationen, Auswahl der Zahlungsmethode, Preisberechnung (Gesamtsumme)

## **Neue Funktionen (Features)**

### **1. Bewertungssystem für Produkte**

**Ursprünglich vage formulierte Anforderung:**
Nutzer sollen Produkte mit einem 5-Sterne-System bewerten und zusätzlich schriftliches Feedback hinterlassen können.

---

### **2. Altersverifikation für alkoholische Produkte**

**Ursprünglich vage formulierte Anforderung:**
Alkoholische Produkte erfordern eine Altersverifikation. Beim Aufrufen der Kategorie soll ein Fenster erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

---

### **3. Änderungen bei den Versandkosten**

**Ursprünglich vage formulierte Anforderung:**
Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

## Offene Fragen:

#### Fünf-Sterne-System:
- **Wertebereich** (mit einem 5-Sterne-System bewerten):
  - zu klären: 0 Sterne-Vergabe erlaubt? Oder zählt es als dann als noch nicht bewertet?
- **Pflichtfelder:**
  -  zu klären: Ist die Vergabe von Sternen verpflichtend für die Abgabe einer Rezension (Nur Freitext auch möglich?)
  -  zu klären: muss User eingeloggt sein? Anonyme Bewertung möglich?
- **Limit:**
   - zu klären: kann nur maximal eine Rezension pro Produkt eingereicht werden?
   - zu klären: Muss das Produkt zuvor gekauft worden sein um es zu bewerten
- **Korrektur:**
  - Vor dem Absenden kann die eingabe und die Sternen vergabe sooft geändert werden wie der user möchte
  - zu klären: kann eine bereits veröffentlichte Bewertung nachträglich bearbeitet oder gelöscht werden vom User selbst

#### Freitext-Feedback:
- **Optional:**
  - Textfeld darf Leergelassen werden
- **Text:**
  - zu klären: Gibt es eine minimale Eingabelänge z.B. 5 Zeichen um sinnlose Eingaben zu minimieren?
  - zu klären: Gibt es eine maximale Zeichenzahl z.B. 500 Zeichen
  - zu klären: Welche Alphabete/Sprachen sollen unterstützt werden
- **Sicherheit und Moderation:**
  - zu klären gibt es automatischen “Schimpfwortbereinigung” oder eine Freigabe vorab
  - zu klären: gibt es einen Melden-Button für unangebrachte Kommentare
 
#### Anzeige & Darstellung (Produktseite):
- **Veröffentlichung:**
  - zu klären: Nach erfolgreichem Absenden erscheint die Bewertung direkt auf der Detailseite des jeweiligen Produkts oder erst Freigabe?
- **Durchschnittsberechnung:**
  - Der Gesamt-Mittelwert der Sterne sowie die Gesamtzahl der Stimmen werden auf der Produktseite dynamisch neu berechnet und angezeigt.
  - zu klären: Auf wie viel Stellen nach dem Komme runden? z.B. auf eine 4.5

## Detailierte Anforderung:

### **1. Bewertungssystem für Produkte**
Nutzer sollen Produkte mit einem 5-Sterne-System bewerten. 
Die Vergabe von mindestens 1 bis maximal 5 Sterne ist möglich, wenn der User eingeloggt ist und das Produkt zuvor auch gekauft hat.
Vor dem Absenden kann die Eingabe und die Sternen vergabe sooft geändert werden wie der User möchte.
Es ist nur eine Rezension pro Artikel pro User möglich. 
Der Kommentar kann nach dem Absenden bearbeitet oder gelöscht werden, wenn der User eingeloggt ist.
Für ein Rezension ist es Pflicht mindestens 1 Stern zu vergeben. Ist kein Stern vergeben kann die Eingabe nicht abgesendet werden.
Es ist möglich zusätzlich schriftliches Feedback abzugeben.
Der Freitext darf maximal 500 Zeichen habene, eine untere Grenze gibt es nicht. 
Es werden neben dem lateinischen Alphabet auch zusätzliche Zeichen aus europäischen Sprachen unterstützt. Eine genaue List muss erstellt werden.
Es ist weder eine automatische "Schimpfwortbereinigung" oder eine vorab Freigabe oder ein Melden-Button vorgesehen.*
Nach erfolgreichem Absenden erscheint die Bewertung direkt auf der Detailseite des jeweiligen Produkts.
Der Gesamt-Mittelwert der Sterne sowie die Gesamtzahl der Stimmen werden auf der Produktseite dynamisch neu berechnet und angezeigt.
Der Gesamt-Mittelwert wird in Form von ausgefüllten bzw. teilausgefüllten Sternen gezeigt. Die Gesammtzahl als Zahl in Klammern dahinter.

\* würde dem Team an dieser Stelle melden: Mir ist aufgefallen, dass wir weder Moderation noch einen Melde-Button vorsehen.
Durch den Digital Services Act (DSA) riskiert der Shop Abmahnungen oder Bußgelder, wenn rechtswidrige Kommentare gepostet werden.
Sollen wir ein Standard-Meldeformular als Acceptance Criteria mit aufnehmen oder das rechtlich prüfen lassen?
