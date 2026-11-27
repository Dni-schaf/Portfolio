#### 1. Schreibe das XPath zu dem Login-Button.

> //*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]

oder

> //div[contains(@class,'social-icon-cont')]//div[contains(@class,'headerIcon')][1]


#### 2. Schreibe das XPath für alle Eingabefelder, die "Sign In"-Schaltfläche, den Link "Create a new account" und den Link "Go to Home".

> //input[@type='email']

> //input[@type='password']

> //button[@type='submit']

> //a[@class='switch-link']

> //a[@class='home-link']


#### 3. Schreibe das XPath für alle Eingabefelder und die "Sign Up"-Schaltfläche.

> //input[@placeholder='Full Name']

> //input[@type='email']

> //input[@type='password']

> //button[@type='submit']


#### 4. Schreibe das XPath der "Confirm"-Schaltfläche, die du im Modal sehen kannst.

> //div[@class='modal-content']//button[text()='Confirm']

#### 5. Schreibe das **XPath** für das **Mengeneingabefeld von Orangen**, die **"Add to cart"** Schaltfläche für Orangen und die **"Add to wish list"** Schaltfläche für Orangen.

> //p[contains(@class, 'lead') and text()='Oranges']/ancestor::div[contains(@class,'card')]//input[@type='number']

> //p[contains(@class, 'lead') and text()='Oranges']/ancestor::div[contains(@class,'card')]//button[contains(@class, 'btn-cart')]

> //p[contains(@class, 'lead') and text()='Oranges']/ancestor::div[contains(@class,'card')]//button[text()='❤']
