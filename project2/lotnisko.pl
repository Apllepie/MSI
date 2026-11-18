% -----------------------------------------------------
% 1. LOTY
% lot(Numer, Miasto, Godzina, Typ, Status, Linia, Samolot)
% -----------------------------------------------------

% O D L O T Y

lot(lo101, warszawa, 800, odlot, planowy, lot, boeing737).
lot(lo102, londyn, 830, odlot, opozniony, wizzair, airbusa320).
lot(lo103, berlin, 900, odlot, planowy, lufthansa, airbusa320).
lot(lo104, paryz, 930, odlot, odwolany, airfrance, boeing737).
lot(lo105, rzym, 1000, odlot, opozniony, lot, boeing787).
lot(lo106, madryt, 1030, odlot, planowy, ryanair, boeing737).
lot(lo107, praga, 1100, odlot, planowy, lot, embraer195).
lot(lo108, oslo, 1130, odlot, opozniony, wizzair, airbusa321).
lot(lo117, ateny, 1200, odlot, planowy, ryanair, boeing737).
lot(lo118, amsterdam, 1230, odlot, planowy, klm, boeing737).
lot(lo119, barcelona, 1300, odlot, opozniony, lufthansa, airbusa320).
lot(lo120, helsinki, 1330, odlot, planowy, finnair, airbusa320).

% P R Z Y L O T Y

lot(lo109, warszawa, 810, przylot, planowy, lot, boeing737).
lot(lo110, londyn, 850, przylot, opozniony, wizzair, airbusa320).
lot(lo111, berlin, 920, przylot, planowy, lufthansa, airbusa320).
lot(lo112, paryz, 950, przylot, planowy, airfrance, boeing737).
lot(lo113, rzym, 1010, przylot, odwolany, lot, boeing787).
lot(lo114, madryt, 1040, przylot, planowy, ryanair, boeing737).
lot(lo115, praga, 1110, przylot, opozniony, lot, embraer195).
lot(lo116, oslo, 1140, przylot, planowy, wizzair, airbusa321).
lot(lo121, ateny, 1210, przylot, opozniony, ryanair, boeing737).
lot(lo122, amsterdam, 1240, przylot, planowy, klm, boeing737).
lot(lo123, barcelona, 1310, przylot, planowy, lufthansa, airbusa320).
lot(lo124, helsinki, 1340, przylot, odwolany, finnair, airbusa320).

% -----------------------------------------------------
% 2. BRAMKI I TERMINALE
% bramka(NumerLotu, Terminal, NumerBramki)
% -----------------------------------------------------

bramka(lo101, t1, g1).
bramka(lo102, t1, g2).
bramka(lo103, t1, g3).
bramka(lo104, t2, g4).
bramka(lo105, t2, g5).
bramka(lo106, t2, g6).
bramka(lo107, t1, g1).
bramka(lo108, t1, g2).
bramka(lo109, t1, g3).
bramka(lo110, t2, g4).
bramka(lo111, t2, g5).
bramka(lo112, t2, g6).
bramka(lo113, t1, g1).
bramka(lo114, t1, g2).
bramka(lo115, t1, g3).
bramka(lo116, t2, g4).
bramka(lo117, t2, g5).
bramka(lo118, t2, g6).
bramka(lo119, t1, g1).
bramka(lo120, t1, g2).
bramka(lo121, t1, g3).
bramka(lo122, t2, g4).
bramka(lo123, t2, g5).
bramka(lo124, t2, g6).

% -----------------------------------------------------
% 3. LINIE LOTNICZE
% linia(Kod, Nazwa, Kraj)
% -----------------------------------------------------

linia(lot, 'LOT Polish Airlines', polska).
linia(wizzair, 'Wizz Air', wegry).
linia(lufthansa, 'Lufthansa', niemcy).
linia(airfrance, 'Air France', francja).
linia(ryanair, 'Ryanair', irlandia).
linia(klm, 'KLM', holandia).
linia(finnair, 'Finnair', finlandia).

% -----------------------------------------------------
% 4. SAMOLOTY
% samolot(Model, Producent, LiczbaMiejsc, Zasieg)
% -----------------------------------------------------

samolot(boeing737, boeing, 189, 5600).
samolot(boeing787, boeing, 330, 14000).
samolot(airbusa320, airbus, 180, 6100).
samolot(airbusa321, airbus, 220, 7400).
samolot(embraer195, embraer, 132, 4300).

% -----------------------------------------------------
% 5. MIASTA
% miasto(Nazwa, Kraj, Kontynent)
% -----------------------------------------------------

miasto(warszawa, polska, europa).
miasto(londyn, wielka_brytania, europa).
miasto(berlin, niemcy, europa).
miasto(paryz, francja, europa).
miasto(rzym, wlochy, europa).
miasto(madryt, hiszpania, europa).
miasto(praga, czechy, europa).
miasto(oslo, norwegia, europa).
miasto(ateny, grecja, europa).
miasto(amsterdam, holandia, europa).
miasto(barcelona, hiszpania, europa).
miasto(helsinki, finlandia, europa).

% -----------------------------------------------------
% 6. LICZBA PASAZEROW
% pasazerowie(NumerLotu, LiczbaPasazerow)
% -----------------------------------------------------

pasazerowie(lo101, 150).
pasazerowie(lo102, 175).
pasazerowie(lo103, 160).
pasazerowie(lo104, 0).
pasazerowie(lo105, 280).
pasazerowie(lo106, 180).
pasazerowie(lo107, 110).
pasazerowie(lo108, 190).
pasazerowie(lo109, 145).
pasazerowie(lo110, 170).
pasazerowie(lo111, 155).
pasazerowie(lo112, 165).
pasazerowie(lo113, 0).
pasazerowie(lo114, 175).
pasazerowie(lo115, 120).
pasazerowie(lo116, 180).
pasazerowie(lo117, 185).
pasazerowie(lo118, 170).
pasazerowie(lo119, 160).
pasazerowie(lo120, 150).
pasazerowie(lo121, 175).
pasazerowie(lo122, 165).
pasazerowie(lo123, 155).
pasazerowie(lo124, 0).


%Reguły
lot_do(Miasto, Lot ) :- lot(Lot, Miasto, _,przylot , _, _, _   ).
lot_z(Miasto, Lot ) :- lot(Lot, Miasto, _,odlot , _, _, _   ).
