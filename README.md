# Znenie zadania
V zadaní budete pracovať s 2D kamerou od spoločnosti Ximea. Cieľom zadania je pochopiť
princípom kalibrácie kamery a kalibrovať si svoju vlastnú kameru pre ďalšiu prácu s obrazom. Taktiež je cieľom zadania naučiť sa orientovať v technickej dokumentácií a manuáloch
OpenCV.
## Úlohy:
1. Pripravte sa na zadanie a dohľadajte potrebné postupy pre realizáciu zadania v zmysle
úloh nižšie na stránke dokumentácie k OpenCV. Prezentujte vami nájdené postupy a
riešenie [1,5 b.].
2. Realizujte kalibráciu kamery pomocou šachovnice a zistite jej vnútorné parametre fx ,
fy , cx , cy [2,5 b.].
3. Využite už existujúcu implementáciu na stránke OpenCv pre Houghovu transformáciu
na detekciu kružníc a vytvorte program ktorý bude vedieť detegovať a kruhom označovať kružnice na stene v miestnosti D 618 (Pri odovzdávaní môže byť zadanie testované
aj na iných kruhoch!) [2,5 b.].
4. Urobte si poriadok na vašom GIT repozitári aby každé zadanie bolo v samostatnom priečinku s názvom "Zadanie_<čislozadania>” a všetky údaje ste mali v branch master [0,5
b.].
5. Zdokumentujte svoj postup a dosiahnuté výsledky. Dokumentáciu k zadaniu odovzdávajte v PDF [1 b.].
## Užitočné odkazy:
• Návod na kalibráciu kamery pomocou OpenCV knižnice:
https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html

• Práca s trackbarmi:
https://docs.opencv.org/4.x/d9/dc8/tutorial_py_trackbar.html

• Houghove kruhy: OpenCV - Hough Circle Transform
https://docs.opencv.org/4.x/da/d53/tutorial_py_houghcircles.html

# Dokumentacia
## Kalibracia kamery
Na pracu s kamerou sme ju najprv potrebovali spravne nakalibrovat. Toho sme dosiahli tak, ze sme si nastudovali [navod](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html) na kalibraciu a kameru kalibrovali pomocou sachovnice.<br>
Pouzili sme obe metody:<br>
-undistortion<br>
-remapping<br>
pred:<br>
<p align="center">
  <img src="https://github.com/DaverSVK/ComputerImageProcessing/blob/Zadanie_2/Recources/test8.jpg" width="250" height="250">
</p> <br>
po:<br>
<p align="center">
<img src="https://github.com/DaverSVK/ComputerImageProcessing/blob/Zadanie_2/calibresult.png" width="250" height="250">
</p><br>
po:(druha metoda)<br>
<p align="center">
<img src="https://github.com/DaverSVK/ComputerImageProcessing/blob/Zadanie_2/calibresult2.png" width="250" height="250">
</p><br>
tiez sme vdaka tomuto zistili parametre fx, fy, cx, cy pre kameru a to 126.142, 132.542, 95.555, 39.175. 

## Hladanie kruhov
Z kniznice openCV sme pouzili uz dostupnu implementaciu Houghovej trasformacie, kde nastavujeme hodnoty parameter1 a parameter2, kde:<br>
-dp je stupen redukcie rozlisenia<br>
-minDist je minimalna vzdialenost medzi stredmi detekovanych kruhov<br>
-parameter1 je vyuzuty na redukciu sumu pri detekcii vyraznych hran ktore by mohli byt sucastou kruhu, cize nastavuje hornu hranicu -canny edge detectora a teda zalezi na kontraste kruhu s pozadim<br>
parameter2 je vyuzity ako citlivost na velkost detekovanych kruhov (center detector) kde pri malej hodnote mozme dosiahnut mnozstvo falsepositives a pri vysokom cisle dosiahneme velku presnost pri detekovani kruhov avsak nemusime detekovat vsetky.<br>
-minRadius je minimalna hodnota polomeru detekovanych kruhov<br>
-maxRadius je maximalna hodnota polomeru detekovanych kruhov<br>
Pre nastavenie hodnot tychto parametrov vyuzivame slidre, ktore su sucastou obrazku<br>
Priklad:<br>
<p align="center">
  <img src="https://github.com/DaverSVK/ComputerImageProcessing/blob/Zadanie_2/HoughCirclesParam.png">
</p> <br>


