#Zadanie 1 (5 b.) - odovzdanie v druhom týždni semestra
##Pripojte sa na kameru na vašom PC a vytvorte aplikáciu, ktorá s využitím opencv:
• Zosnímat’ 4 snímky po stlaˇcení medzerníka a následne snímky uloží to vami definovaného prieˇcinku [0,5 b.].
• Vytvorí mozaiku zo 4 roch snímok vo formáte 2 x 2 a zobrazí ju pomocou príkazu ”imshow” a uloží ju na vami definované miesto – pozor nie použitie funkcie "subplot" ale
vytvorenie vlastného obrázka [2 b.].
• Na prvom obrázku z mozaiky aplikujete funkciu kernel masky na každý pixel (v rozmere
3x3) - operáciu realizujte už v existujúcej mozaike [1 b.].
• Druhú snímku otoˇcte o 90° pomocou využitia for cyklu. [0,5 b.].
• Na tret’om obrázku zobrazte z RGB len ˇcervený kanál [ 0,5 b.].
• Do terminálu vypíšete základné informácie o obraze (dátový typ, rozmer, vel’kost’) [0,5
b.].
##Pomôcky:
• Pre pripojenie kamery využite ukážkový program v PyCharme – kamera už má nainštalovaný driver
• Potrebné návody na vypracovanie jednotlivých úloh nájdete na stránke
– Open CV doc - tutorial pre prácu s ukladaním obrázku, zobrazovaním a nahrávaním
– Open CV doc - Python pre získanie špecifického farebného kanála z obrázku a získanie vlastností obrázku a vytvorenie subplotu
– Open CV - mask operations pre maskovacie operácie na obraze
– Vysvetlenie formátu MAT v C++ Open CV C++ MAT
