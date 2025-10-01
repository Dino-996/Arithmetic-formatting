Ecco un README.md strutturato in modo chiaro e accademico per il progetto **Arithmetic Formatter**:

---

````markdown
# 📐 Arithmetic Formatter

## Descrizione
Gli studenti delle scuole elementari spesso dispongono i problemi aritmetici in colonna per semplificare i calcoli.  
Questo progetto implementa la funzione **`arithmetic_arranger`**, che riceve una lista di stringhe rappresentanti operazioni aritmetiche e le restituisce formattate verticalmente, affiancate tra loro.  

La funzione supporta inoltre un parametro opzionale che, se impostato a `True`, mostra anche i risultati delle operazioni.

---

## 🔧 Funzionalità
- Accetta una lista di problemi aritmetici in formato stringa (es. `"32 + 698"`).
- Supporta **solo addizione e sottrazione**.
- Restituisce le operazioni scritte verticalmente, con gli operandi e il risultato (opzionale) allineati.
- Gestisce errori di input in maniera esplicita e leggibile.

---

## 📋 Regole e Vincoli
1. **Numero massimo di problemi:**  
   - Al massimo **5 operazioni** contemporaneamente.  
   - In caso contrario:  
     ```
     Error: Too many problems.
     ```

2. **Operatori consentiti:**  
   - Solo `+` e `-`.  
   - Se viene usato `*` o `/`:  
     ```
     Error: Operator must be '+' or '-'.
     ```

3. **Validità degli operandi:**  
   - Devono contenere **solo cifre**.  
   - In caso contrario:  
     ```
     Error: Numbers must only contain digits.
     ```

4. **Dimensione massima degli operandi:**  
   - Ogni numero deve avere **al massimo 4 cifre**.  
   - In caso contrario:  
     ```
     Error: Numbers cannot be more than four digits.
     ```

5. **Formattazione dell’output:**  
   - Operandi allineati a destra.  
   - Lo spazio tra operatore e operando deve rispettare la larghezza del numero più lungo.  
   - Quattro spazi tra un problema e l’altro.  
   - Riga di trattini (`-`) lunga quanto l’operazione.  
   - Se richiesto, visualizzazione del risultato allineato.

---

## 💻 Esempi di utilizzo

### Esempio 1 (senza risultati)
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
````

Output:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

---

### Esempio 2 (con risultati)

```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:

```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

---

## 📦 Installazione e utilizzo

1. Clona il repository o scarica i file.
2. Importa la funzione nel tuo progetto Python:

   ```python
   from arithmetic_formatter import arithmetic_arranger
   ```
3. Passa una lista di stringhe contenenti le operazioni:

   ```python
   print(arithmetic_arranger(["123 + 49", "45 - 32"], True))
   ```

---

## 🧪 Test

La funzione è stata progettata per gestire sia casi corretti che input non validi.
Si consiglia di provare vari scenari, inclusi errori di input, per verificare la robustezza della soluzione.

---

## 📖 Note

Questo progetto fa parte di un esercizio di programmazione introduttiva, utile per consolidare:

* Manipolazione di stringhe
* Gestione di eccezioni ed errori
* Allineamento di testo in output

```

---

```