# QnA
4. Berechnen Sie das Histogramm von den Bildern 01 bis 05. Sie werden zum einen Aufnah-mefehler (Belichtungsfehler) in deren Histogrammen erkennen können. Zum anderen werden Sie die Bearbeitungsschritte in zwei bearbeiteten Bild anhand des Histogramms erkennen können.
	1. Welche Aufnahmefehler sind in 01 und 03 zu erkennen? Woran ist dies im Histogramm erkennbar?
		- _Bild1:_ Unterbelichtet; sehr viele Pixel haben einen niedrigen Helligkeitswert; Bild erscheint dunkel; Informationen gehen im Schatten verloren
		- _Bild2:_ Überbelichtet; an bin_hist ist zu erkennen, dass sehr viele Pixel im oberen Bereich sind; Kontrast in der Aufnahme ist zu hoch; Informationen gehen in den Spitzlichtern verloren
		- _Bild3:_ Nur Pixel, die einen Helligkeitswert der über 150 liegt haben; kaum Bildinformationen vorhanden; Überbelichtet
	2. Bild01 ist das aufgenommene Bild. Bild02 wurde nachbearbeitet. Die Helligkeit wurde erhöht. Woran ist dies im Histogramm erkennbar? Welche Daten gehen dabei verloren?
		- Informationen gehen in den Spitzlichtern verloren; Im Histogram ist eine Verschiebung der Häufigkeitswerte nach rechts zu sehen und ein Turm im Bereich des höchsten Helligkeitswerts, d.h. diese Pixel sind weiß und beinhalten damit keine Informationen
	3. Bild04 ist das aufgenommene Bild. Bild05 wurde einem Bearbeitungsschritt unterzogen. Was wurde in Bild05 verändert? Woran kann man dies in seinem Histogramm erkennen?
		- Der Kontrast wurde erhöht; Das ist an der Häufung der Pixel im oberen und unteren Helligkeitbereich zu erkennen. Außerdem wurde der Schwarzwert angepasst, sodass jetzt auch schwarze Töne im Bild zu finden sind.

6. Implementieren Sie eine Funktion, die eine Punktoperation mithilfe einer Lookup-Tabelle zum Aufhellen eines Bildes durchführt.
	1. In Aufgabe (3b) gingen Daten beim Aufhellen eines Bildes verloren. Wie könnte dies vermieden werden?
		- Die Funktion zum Aufhellen so implementieren, dass sich sich dem höchsten Helligkeitswert annähert, aber diesen niemals erlaubt; Die dunkleren Pixel mehr aufhellen, als die eh schon hellen
	2. Damit beim Aufhellen von Bild01 keine Daten verloren gehen, soll eine Lookup-Tabelle verwendet werden. Versuchen Sie mit der Lookup-Tabelle die dunklen Bildbereiche des Bildes aufzuhellen ohne die hellen Bereiche zu stark zu verändern.
