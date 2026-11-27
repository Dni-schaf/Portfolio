#### 1. Schreibe das XPath, um das Haupt-**h1**Element zu finden.
> //h1[@id='mainTitle']

#### 2. Schreibe das XPath, um den Navigationslink **About Us** auszuwählen.
> //a[@href = '#about']

#### 3. Schreibe das XPath, um den Dropdown-Link **Graphic Design** auszuwählen.
> //a[@href = '#graphicdesign']

#### 4. Schreibe das XPath, um den Namen des Teammitglieds **Jane Smith** auszuwählen.
> //h4[text()='Jane Smith']

#### 5. Schreibe das XPath, um die Beschreibung (die sich im Absatz befindet) der **SEO Services** auszuwählen.
> //h3[text()='SEO Services']/ancestor::div[contains(@class,'service-item')]//p

#### 6. Schreibe einen XPath-Ausdruck, um alle Service-Elemente im Abschnitt "**Our Services**" auszuwählen.
> //section[@id='services']//div[contains(@class,'service-item')]

#### 7. Wie lautet das XPath, um das **E-Mail-Eingabefeld** im Kontaktformular auszuwählen?
> //input[@id='email']

#### 8. Wie würdest du ein XPath schreiben, um das **gesamte Kontaktformular** auszuwählen?
> //section[@id='contact']//form

#### 9. Gib das XPath an, um das **Footer-Absatz-Element** auszuwählen.
> //footer//p[contains(text(),'Company Name')]

#### 10. Was ist das XPath, um den Namen (`<h4>`) des **ersten Teammitglieds** auszuwählen?
> //div[@class='team']//li[1]//h4

#### 11. Wie kannst du mit XPath die Beschreibung des **zweiten Service-Elements** auswählen?
> //section[@id='services']//div[contains(@class,'service-item')][2]//p

#### 12. Was ist das XPath, um die Überschrift der Sektion **"Contact Us"** (`<h2>`Element) auszuwählen?
> //section[@id='contact']//h2

#### 13. Schreibe einen XPath-Ausdruck, um alle Links innerhalb des Dropdowns unter dem Navigationspunkt **"Services"** auszuwählen.
> //a[@href='#services']/following-sibling::ul[@class='dropdown']//a

#### 14. Was ist das XPath, um das erste `<li>` im Abschnitt **"Our Team"** auszuwählen?
> //h3[text()='Our Team']//li[1]

#### 15. Gib das XPath an, um die Schaltfläche **"Send Message"** im Kontaktformular zu finden.
> //input[@type='submit']
