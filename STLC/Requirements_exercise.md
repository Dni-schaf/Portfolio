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

### **2. Altersverifikation für alkoholische Produkte**

**Ursprünglich vage formulierte Anforderung:**
Alkoholische Produkte erfordern eine Altersverifikation. Beim Aufrufen der Kategorie soll ein Fenster erscheinen, in dem Nutzer ihr Alter angeben müssen (18+), bevor sie Zugriff erhalten.

### **3. Änderungen bei den Versandkosten**

**Ursprünglich vage formulierte Anforderung:**
Versandkosten entfallen ab einem bestimmten Bestellwert. Darunter fallen Versandkosten an.

## Offene Fragen:

#### Fünf-Sterne-System:
- **Wertebereich** (mit einem 5-Sterne-System bewerten):
  - Ist 0 Sterne-Vergabe erlaubt? Oder zählt es als dann als noch nicht bewertet?
- **Pflichtfelder:**
  -  Ist die Vergabe von Sternen verpflichtend für die Abgabe einer Rezension (Nur Freitext auch möglich?)
  -  Muss User eingeloggt sein? Anonyme Bewertung möglich?
- **Limit:**
   - Kann nur maximal eine Rezension pro Produkt eingereicht werden?
   - Muss das Produkt zuvor gekauft worden sein um es zu bewerten
- **Korrektur:**
  - Vor dem Absenden kann die eingabe und die Sternen vergabe sooft geändert werden wie der user möchte
  - zu klären: kann eine bereits veröffentlichte Bewertung nachträglich bearbeitet oder gelöscht werden vom User selbst

#### Freitext-Feedback:
- **Optional:**
  - Textfeld darf Leergelassen werden
- **Text:**
  - Gibt es eine minimale Eingabelänge z.B. 5 Zeichen um sinnlose Eingaben zu minimieren?
  - Gibt es eine maximale Zeichenzahl z.B. 500 Zeichen
  - Welche Alphabete/Sprachen sollen unterstützt werden
- **Sicherheit und Moderation:**
  - Gibt es automatischen “Schimpfwortbereinigung” oder eine Freigabe vorab
  - Gibt es einen Melden-Button für unangebrachte Kommentare
 
#### Anzeige & Darstellung (Produktseite):
- **Veröffentlichung:**
  - Nach erfolgreichem Absenden erscheint die Bewertung direkt auf der Detailseite des jeweiligen Produkts oder erst Freigabe?
- **Durchschnittsberechnung:**
  - Der Gesamt-Mittelwert der Sterne sowie die Gesamtzahl der Stimmen werden auf der Produktseite dynamisch neu berechnet und angezeigt.
  - Auf wie viel Stellen nach dem Komme runden? z.B. auf eine 4.5
 
#### Altersverifikation:
- **Eingabe:**
  - In welchen Format soll das Alter angegeben werden Beispiel DD-MM-JJJJ
  - Gibt es eine Validierung der Eingabe. Werden unsinniger Eingaben Bspw. die in der Zukunft liegen oder Menschen die angeblich über 150 Jahre alt sind abgelehnt?
- **Kategorien:**
  - Bei welchen Kategorien ist eine Altersfreigabe erforderlich
- **Datenspeicherung:**
  - Wie wird die Altersinformation im Profil gespeichert 
    - ist nach dem aus und wieder einloggen noch gültig?
    - oder ist die Freigabe nur für die aktuelle Sitzung gültig?
    - oder muss die Eingabe pro Aktikel aus der Katergorie durchgeführt werden?
- **Verhalten bei Ablehnung:**
  - Was passiert, wenn der User unter 18 ist?
    - Wird man zurück zu Startseite geleitet.
    - Kann man die Produkte sehen, aber nicht in den Warenkorb legen.
    - Wird man auf eine Seite geleitet, wo diese +18 Katergorien ausgeblendet sind?
- **Sicherheit:**
  - Reicht rechtlich die reine Alterseingabe aus?
  - Kann er man das Fenster schießen und die Eingabe wiederholen? Bypass-Gefahr
  - Was ist wenn man nicht über die Kategorie kommt, sondern über einen Direktlink. Kommt dennoch die Sicherheitsabfrage?

#### Änderungen bei den Versandkosten:
- **Ausgangswerte:**
  - Wie hoch sind die Versandkosten normalerweise.
  - Sind die Versandkosten weltweit gleich oder unterscheiden sie sich beispielsweise für In- und Ausland, EU oder Weltweit
  - Gibt es Zuschläge? gekühlte Wahre, Expresslieferung, hohes Gewicht bei Beispielsweise Getränkelieferungen
- **Schwellenwert**
  - Ab welche Betrag entfallen die Versandkosten.
  - Was dient als Berechnungsgrundlage? Brutto oder Netto, vor Rabatt- oder Gutschein-Codes oder danach?
  - Zählen Zuschläge, wie zum Beispiel Expresskosten und Pfand mit zum Erreichen des Grenzwertes oder nur der reine Produktpreis?
  - Was passiert, wenn nach der Bestellung ein Teil stoniert wird und die Bestellung wieder unter den Grenzwert sinkt?
- **Sonderregelunge:**
  - Gibt es Sonderregelungen für Sperrgut oder gekühlte waren, die trotz des erreichten Schwellenwerts Versandkosten zahlen müssen
- **UI/UX Hinweise**
  - Wird darauf hingewiesen, ab wann keine Versandkosten anfallen, wenn ja wo?
  - Ändert sich die Anzeige im Warenkorb in echtzeit?

## Detailierte Anforderung:

### **1. Bewertungssystem für Produkte**
Nutzer sollen Produkte mit einem 5-Sterne-System bewerten. 
- Die Vergabe von mindestens 1 bis maximal 5 Sterne ist möglich, wenn der User eingeloggt ist und das Produkt zuvor auch gekauft hat.
- Vor dem Absenden kann die Eingabe und die Sternen vergabe sooft geändert werden wie der User möchte.
- Es ist nur eine Rezension pro Artikel pro User möglich. 
- Für ein Rezension ist es Pflicht mindestens 1 Stern zu vergeben. Ist kein Stern vergeben kann die Eingabe nicht abgesendet werden.
Es ist möglich zusätzlich schriftliches Feedback abzugeben.
- Der Freitext darf maximal 500 Zeichen habene, eine untere Grenze gibt es nicht. 
- Es werden neben dem lateinischen Alphabet auch zusätzliche Zeichen aus europäischen Sprachen unterstützt. Eine genaue List muss erstellt werden.
- Es ist weder eine automatische "Schimpfwortbereinigung" oder eine vorab Freigabe oder ein Melden-Button vorgesehen.*
- Nach erfolgreichem Absenden erscheint die Bewertung direkt auf der Detailseite des jeweiligen Produkts.
- Der Gesamt-Mittelwert der Sterne sowie die Gesamtzahl der Stimmen werden auf der Produktseite dynamisch neu berechnet und angezeigt.
- Der Gesamt-Mittelwert wird in Form von ausgefüllten bzw. teilausgefüllten Sternen gezeigt. Die Gesammtzahl als Zahl in Klammern dahinter.
- Der Kommentar kann nach dem Absenden bearbeitet oder gelöscht werden, wenn der User eingeloggt ist.

\* würde dem Team an dieser Stelle melden: Mir ist aufgefallen, dass wir weder Moderation noch einen Melde-Button vorsehen.
Durch den Digital Services Act (DSA) riskiert der Shop Abmahnungen oder Bußgelder, wenn rechtswidrige Kommentare gepostet werden.
Sollen wir ein Standard-Meldeformular als Acceptance Criteria mit aufnehmen oder das rechtlich prüfen lassen?

### **2. Altersverifikation für alkoholische Produkte**
Nutzer unter 18 Jahren dürfen Produkte der Kategorien Alkohol nicht kaufen.
- Hat der User sich eingeloggt und klickt auf den Button "Shop", geht ein Popup auf, das zum eintragen des Geburtsdatums im Format DD-MM-JJJJ auffordert*
- Klickt ein nicht eingeloggter User auf den Button "Shop" geht ebenfalls das Popup auf.
- Unsinnige Eingaben, wie etwa ein Datum nach dem aktuellen Datum sollte abgelehnt werden, ebenso wie Daten, die ergeben, das der User über 150 Jahre alt wäre oder die nicht im erlaubten Bereich liegen. (bei Tagen 1-31, bei Monaten 1-12).
- Bei eine unsinnigen Eingabe wird der User mit einem roten Text unter dem Eingabefeld, um ein gültiges Datum gebeten.
- Die Geburtstagseingabe wird im Profil gespeichert und ist auch nach dem aus und wieder einloggen gesichert.
- Die Geburtstagseingabe kann nach dem initialen eingeben nicht mehr geändert werden.
- ist der User unter 18 Jahre kann er Produkte der Kathegorie Alkohol weder in der Alle Produktlitse noch in der Kathegorie Alkohol sehen
- Auch ein Direktlink zu einer Detailseite eines Produktes der Kategorie Alkohol sollte nicht angezeigt werden, wenn der User unter 18 ist.

\* würde dem Team an dieser Stelle melden: Das Jugendschutzgesetz (JuSchG) verlangt beim Online-Handel mit Alkohol eine zweistufige Prüfung, um sicherzustellen, dass die Ware weder bestellt noch an Minderjährige übergeben wird.

### **3. Änderungen bei den Versandkosten**
- 5 Euro sind die Versandkosten normalerweise.
- Ab >=20 Euro Warenwert(Netto) entfallen die Versandkosten.
- Werden Produkte aus dem Warenkorb gelöscht und die Produktsumme fällt unter 20 Euro werden die Versandkosten wieder auf 5 Euro erhöht.
- Die Versandkosten sind weltweit gleich.
- Versandkosten sind nicht abhängig von Art des Produktes oder dem Gesamtgewicht.
- Es gibt keine Expresslieferung, Rapatt- oder Gutscheincodes.
- Die Anzeige im Warenkorb ändert sich in Echtzeit. 
- Im Warenkorb wird darauf hingewiesen: "ab 20 Euro Warenwert entfallen die Versandkosten."
- Ab >=20 Euro Warenwert(Netto) gibt es keinen Hinweis mehr. Bei Versandkosten steht 0 Euro.
