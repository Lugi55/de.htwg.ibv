# QnA
1. Welche Aufnahmefehler sind in 01 und 03 zu erkennen? Woran ist dies im Histogramm erkennbar?
	- _Bild1:_ Unterbelichtet; sehr viele Pixel haben einen niedrigen Helligkeitswert; Bild erscheint dunkel; Informationen gehen im Schatten verloren
	- _Bild3:_ kaum Bildinformationen vorhanden; Überbelichtet; Es gibt keine niedrigen Grauwerte; Es gehen viele Bildinformationen verloren, da wir sehr viele weiße Pixel haben.
2. Bild01 ist das aufgenommene Bild. Bild02 wurde nachbearbeitet. Die Helligkeit wurde erhöht. Woran ist dies im Histogramm erkennbar? Welche Daten gehen dabei verloren?
	- Informationen gehen in den Spitzlichtern verloren; Im Histogram ist eine Verschiebung der Häufigkeitswerte nach rechts zu sehen und ein Turm im Bereich des höchsten Helligkeitswerts, d.h. diese Pixel sind weiß und beinhalten damit keine Informationen;
		Dynamikumfang wird voll ausgenutzt
3. Bild04 ist das aufgenommene Bild. Bild05 wurde einem Bearbeitungsschritt unterzogen. Was wurde in Bild05 verändert? Woran kann man dies in seinem Histogramm erkennen?
	- Der Schwarzwert des Bildes wurde angepasst. Das ist daran zu erkennen, dass der rechte Teil des Histrograms fast unbeeinflusst bleibt, der linke Teil aber eine Verschiebung zum Grauwert 0 hin aufweist. In Bild5 gibt es auch richtiges schwarz, in Bild4 ist das nicht der Fall.

4. In Aufgabe (3b) gingen Daten beim Aufhellen eines Bildes verloren. Wie könnte dies vermieden werden?
	- Die Funktion zum Aufhellen so implementieren, dass sich sich dem höchsten Helligkeitswert annähert, aber diesen niemals erlaubt; Die dunkleren Pixel mehr aufhellen, als die eh schon hellen
5. Damit beim Aufhellen von Bild01 keine Daten verloren gehen, soll eine Lookup-Tabelle verwendet werden. Versuchen Sie mit der Lookup-Tabelle die dunklen Bildbereiche des Bildes aufzuhellen ohne die hellen Bereiche zu stark zu verändern.
	- Lookup-Tabelle nach Funktion: 
\begin{equation}
f(x)=\frac{1}{2000}*(x-255)^2
\end{equation}
