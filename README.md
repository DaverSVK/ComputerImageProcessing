# Zadanie 1 (5 b.) - odovzdanie v druhom týždni semestra
## Pripojte sa na kameru na vašom PC a vytvorte aplikáciu, ktorá s využitím opencv:

• Zosnímať 4 snímky po stlčení medzerníka a následne snímky uloží to vami definovaného priečinku [0,5 b.].

• Vytvorí mozaiku zo 4 roch snímok vo formáte 2 x 2 a zobrazí ju pomocou príkazu ”ims-how” a uloží ju na vami definované miesto – pozor nie použitie funkcie "subplot" ale
vytvorenie vlastného obrázka [2 b.].

• Na prvom obrázku z mozaiky aplikujete funkciu kernel masky na každý pixel (v rozmere 3x3) - operáciu realizujte už v existujúcej mozaike [1 b.].

• Druhú snímku otočte o 90° pomocou využitia for cyklu. [0,5 b.].

• Na treťom obrázku zobrazte z RGB len červený kanál [ 0,5 b.].

• Do terminálu vypíšete základné informácie o obraze (dátový typ, rozmer, veľkosť) [0,5 b.].

## Pomôcky:
• Pre pripojenie kamery využite ukážkový program v PyCharme – kamera už má nainštalovaný driver
• Potrebné návody na vypracovanie jednotlivých úloh nájdete na stránke

– Open CV doc - tutorial pre prácu s ukladaním obrázku, zobrazovaním a nahrávaním
https://docs.opencv.org/4.7.0/db/deb/tutorial_display_image.html

– Open CV doc - Python pre získanie špecifického farebného kanála z obrázku a získanie vlastností obrázku a vytvorenie subplotu
https://docs.opencv.org/4.7.0/d3/df2/tutorial_py_basic_ops.html

– Open CV - mask operations pre maskovacie operácie na obraze
https://docs.opencv.org/4.7.0/d7/d37/tutorial_mat_mask_operations.html

– Vysvetlenie formátu MAT v C++ Open CV C++ MAT
https://docs.opencv.org/4.x/d6/d6d/tutorial_mat_the_basic_image_container.html
