Struktura:
- dane: dane wejściowe, m.in. pliki csv z jadojade, liczba kursów obsługujących dany przystanek etc.
- infografiki: zwizualizowane mapy, wykorzystywane do promocji
- skrypty: oprogramowanie do obróbki danych
- warstwy: warstwy ESRI shapefile (shp) do projektu QGISa

Używane formaty:
- qgs - projekt QGISa
- csv w formacie WKT
- json/geojson
- shp - ESRI shapefile (zbiór pięciu plików, w shp trzymane są współrzędne, w dbf parametry)

Skrypty:
- clustering_jakdojade - ładuje pliki z danym z jakdojade, tworzy klastry i zlicza połączenia między nimi. Generuje trzy pliki w formacie WKT: centers.csv (centra klastrów), points.csv (punkty przypisane do klastrów), lines.csv (połączenia między klastrami); nazwa pliku wejściowego w linii 80 ;), dzielnikiem w linii 18 regulujemy średnią wielkość klastra

Używamy układu współrzędnych ETRS89 / Poland CS2000 zone 6 (na Śląsku i Zagłębiu; inne strefy: https://pl.wikipedia.org/wiki/Uk%C5%82ad_wsp%C3%B3%C5%82rz%C4%99dnych_2000). Ustawiamy go we właściwościach projektu. Tam też włączamy reprojekcję w locie. Współrzedne geograficzne długość/szerokość to układ WGS84 (EPSG:4236). Pamiętajmy o tym ładując inne warstwy.

Po załadowaniu warstwy do QGIS z pliku innego niż shp, bądź za pomocą wtyczki QuickOSM, należy warstwę od razu zapisać do formatu ESRI Shapefile (shp; prawy przyscik na warstwie -> Zapisz jako...), pamiętając o zmianie układu współrzędnych. Dodawanie warstwy WKT do projektu QGIS: Warstwa -> Dodaj warstwę -> Dodaj warstwę tekstową CSV.

Jako podkładu najlepiej użyć jednej z rastrowych map stworzonych na podstawie OpenStreetMaps (np. OCM Public Transport). Służy do tego wtyczka OpenLayers.

Kilka użytecznych funkcji warstw. Prawy przycisk:
- powiększ do warstwy
- tabela atrybutów (baza danych z pliku dbf)
- właściwości -> styl - symbol stopniowy (nadanie różnych atrybutów kolorom i kształtom obiektom w zależności od jednego z pól z bazy danych)

Warstwy:
- GOP_gęstość_zaludnienia (gęstość zaludnienia w siatce kilometrowej; dane z http://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/population-distribution-demography)
- jakdojade_*, jakdojade_3_* (dane z jakdojade po clusteringu, dla wszystkich połączeń z jednego dnia i dla połączeń z dwoma lub więcej przesiadkami z trzech tygodni)
- przystanki_KZK_GOP (przystanki KZK GOP z liczą obsługiwanych połączeń jednego dnia roboczego)

Tworzenie nowych wydruków za pomocą 