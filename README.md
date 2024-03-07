# Znenie zadania
V zadaní budete pracovať s 2D kamerou od spoločnosti Ximea. Cieľom zadania je pochopiť
princípom kalibrácie kamery a kalibrovať si svoju vlastnú kameru pre ďalšiu prácu s obrazom. Taktiež je cieľom zadania naučiť sa orientovať v technickej dokumentácií a manuáloch
OpenCV.
## Úlohy:
1. Pripravte sa na zadanie a dohľadajte potrebné postupy pre realizáciu zadania v zmysle
úloh nižšie na stránke dokumentácie k OpenCV. Prezentujte vami nájdené postupy a
riešenie [1,5 b.].
2. Realizujte kalibráciu kamery pomocou šachovnice a zistite jej vnútorné parametre fx ,
f y , cx , cy [2,5 b.].
3. Využite už existujúcu implementáciu na stránke OpenCv pre Houghovu transformáciu
na detekciu kružníc a vytvorte program ktorý bude vedieť detegovať a kruhom označovať kružnice na stene v miestnosti D 618 (Pri odovzdávaní môže byť zadanie testované
aj na iných kruhoch!) [2,5 b.].
4. Urobte si poriadok na vašom GIT repozitári aby každé zadanie bolo v samostatnom priečinku s názvom "Zadanie_<čislozadania>” a všetky údaje ste mali v branch master [0,5
b.].
5. Zdokumentujte svoj postup a dosiahnuté výsledky. Dokumentáciu k zadaniu odovzdávajte v PDF [1 b.].
## Užitočné odkazy:
• Návod na kalibráciu kamery pomocou OpenCV knižnice:
[1]: https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html

• Práca s trackbarmi:
https://docs.opencv.org/4.x/d9/dc8/tutorial_py_trackbar.html

• Houghove kruhy: OpenCV - Hough Circle Transform
https://docs.opencv.org/4.x/da/d53/tutorial_py_houghcircles.html

# Dokumentacia
## Kalibracia kamery
Na pracu s kamerou sme ju najprv potrebovali spravne nakalibrovat. Toho sme dosiahli tak, ze sme si nastudovali [navod][1]
