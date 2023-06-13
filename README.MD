# MasterGrimoire

- Projekt za kolegij Poslovni informacijski sustavi
- Autor: *Juraj Štern-Vukotić*
- JMBAG: 0303106940
- <img src="https://upload.wikimedia.org/wikipedia/hr/e/eb/Unipu-logo-lat.png"  width="4%" height="4%"> Sveučilište: Sveučilište Jurja Dobrile u Puli 

- <img src="https://media.discordapp.net/attachments/773704240987635722/1116841660190564372/Untitled.png?width=475&height=460"  width="4%" height="4%"> Fakultet: Fakultet informatike u Puli
___
## Upute za lokalno pokretanje:

### ***!!! OVE UPUTE PRETPOSTAVLJAJU DA IMATE DOCKER DESKTOP INSTALIRAN I POSTAVLJEN NA WINDOWSU 10 TE DA IMATE GIT BASH INSTALIRAN !!!***

1. Napraviti novi folder gdje ćete klonirati projekt.
2. Otvoriti git bash (desni klik -> git bash here) u folderu.
3. Kopirati sljedeću komandu za kloniranje repozitorija: ```git clone https://github.com/JurajSternVukotic/InstaGrimoire```
4. Sačekati da se repozitorij klonira, trebali bi ste vidjeti zadnje: ```instagrimoire-backend-1   | Press CTRL+C to quit``` i onda nakon toga opet input.
5. Upisati komandu ```cd InstaGrimoire```
6. Upisati komandu ```docker-compose up``` te sačekati da se sve setuppira i pokrenu kontejneri (može potrajati od par sekunda do par minuta)
7. Otvoriti web preglednik (Testirano na Google Chrome) te posjetiti adresu ```localhost``` 
8. Trebalo bi vam raditi

*Napomena* Frontend je rađen za rezoluciju 2560x1440, na nižima igleda čuno, ako možete molim vas stavite tu rezoluciju
___
## Opis projekta

~~InstantGrimoire~~ **MasterGrimoire** *(kasnije preimenovano)* je web aplikacija za olakšavanje baratanja informacijama o čarolijama za Društvenu igru uloga Dungeons & Dragons 5e. 
Omogućava pomoću korisničkog sučelja interakciju sa serverom i bazom podataka gdje se nalaze podaci o čarolijama, također se mogu podaci manipulirati, dodavati, filtrirati i vizualizirati.
___
## Opis strukture projekta

### Root
Dakle u root folderu se nalaze 5 stvari:
- .gitignore - Koristimo kako ne bi smo nepotrebno neke datoteke pratili
- README.MD - Ono što trenutačno čitate, tu pišem dokumentaciju, funkcionalnosti i slično
- docker-compose.yml - Ovo je file koji nam treba kako bi docker kontejneri mogli komunicirati jedni sa drugima, ovdje specifićno mi treba kako bi definirao backend i frontend servis, koji svaki ima svoj zasebni kontejner te kako da komuniciraju međusobno
- backend 
- frontend

### Backend
Unutar backenda se nalazi još jedan folder koji se zove jsons for testing, gdje sam ostavio python skriptu sa kojom sam povukao sve informacije o dosadašnjim čarolijama u igri D&D5e.
To sam ovdje stavio kako bi pokazao na koji način sam došao do all_spells.json.

Scrape.py neću objašnjavati pošto je izvan dometa ovoga kolegija te sam ga ostavio samo radi evidencije, all_spells.json doduše nam je potreban kako bi smo testirali funkciju importanja podataka iz datoteke.

Unutar database.sqlite se nalaze podaci o svim čarolijama koje aplikacija može vidjeti.

app.py je glavna aplikacija te ona poziva: 
- model.py - Definira schemu baze podataka, kreiram enumeratore unutar pythona pošto ih SQLite ne podržava taj tip podataka, također definiram setter metode kako bi se enforcealo pravilo enumeratora
- add_spell.py - Koristi se za CREATE funkcionalnost, doda određenu čaroliju za koju pošaljemo podatke u bazu.
- delete_spell.py - Koristi se za DELETE funkcionalnost, traži po imenu unutar baze podataka i izbriše taj zapis.
- get_spell.py - Koristi se za READ funkcionalnost, traži se po imenu čarolije unutar baze podataka, te vrati dictionary sa svim podacima.
- update_spell.py - Koristi se za UPDATE funckionalnost, traži se po imenu čarolije i prima bilo koje atribute koji damo, ako su ti atributi validni onda promjeni zapis.

Radi lakše preglednosti.

Unutar app.py koristim prijenavedene datoteke koje sam sam definirao te biblioteke: flask, flask_cors, pony.orm, workzeug.utils, os i json.

Ovdje imamo 7 različitih ruta definiranih i jednu pomočnu funkciju:
- '/spell', POST - 
- /spell/name, GET -
- /spells, GET -
- /sourcebooks, GET -
- /spell, PATCH -
- /upload-json, POST - 
- pomoćna funckija apply_filters - 


### Frontend
Ovdje imamo index.html, style.css te 5 .js datoteka.

index.html opisuje sadržaj front-enda te se sa style.css uređuje u polu-smislenu cjelinu.

Uglavnom se sastoji od ovih djelova:
- header - Sadrži naslov.
- form selection - Sadrži checkboxove za filtriranje po klasama(klase iz igre odnosno tipovi likova), javascript sluša za promjene te ako se promjeni filtrira po novim kriterijima
- filter options - Također kao prijašnji form selection samo sadrži različite tipove selekcije (id, knjiga, vrsta magije, level magije, trajanje i domet), te također ima gumb za resetirati sve filtre
- spell list - Ovaj dio sadrži prazni prostor koji popunjavamo sa listom čarolija koju ćemo pomoču javascripta dohvatiti sa back-enda. Također sadrži formu za upload .json-a za popunjavanje baze, te search po imenu i naposlijetku brojač koliko rezultata se prikazuje.
- spell detail - Ima 3 "taba", a to su Add, View i Edit. View je default te pokazuje placeholder data sve dok korisnik ne klikne na neku čaroliju sa liste te onda pokazuje informacije o njoj koje se dohvate iz baze. Dok je neki spell u view ako kliknemo na edit ćemo dobiti popunjenu formu sa svim informacijama o tom spellu te možemo lagano promjeniti, kliknuti submit i reloadat stranicu kako bi vidjeli promjene. I naposlijetku ako idemo na add dobijemo praznu formu za dodavanje novih spellova.
- add spell form - Forma spomenuta u Edit i Add tabovima u spell detail.
- footer - Sadrži osnovne podatke o meni, kolegiju te fakultetu.

Pošto frontend nije fokus ovog projekta, neću ići u detalje css koda, on ne dodaje funkcionalnsot.

Idemo na javascript:
- chartHandling - Ovdje vizualiziramo podatke, imamo 2 grafa, jedan prikazuje koliko ima spellova po levelima a drugi po skoli magije. 
- displayData - Ovdje imamo 2 bitne funkcije, resultsCounter koja mjeri koliko smo rezultata dobili i updatea broj, te display spells koja napravi listu spellova unutar HTMLa, osim što popuni njihove infomracije napravi i delete button koji je povezan sa imenom tog spella te koristi DELETE metodu ako se klikne.
- fetchData - Ova datoteka "gradi" url koji će se poslati na backend sa fetchspells funkcijom te prosljedi response u display spells. Također u getspelldetails po imenu zatražimo detalje o nekoj čaroliji te prema odgovoru updateamo tekst u htmlu, spell components ako su true se nadoda u string njihova oznaka, te klase se prikažu u listi tako da se prvo razdvoje pomoću string .trim() funkcije te se pokažu u listi, također ovdje imamo funkciju koja nađe sve knjige koje imamo u bazi te ih kreira kao opcije za filtriranje.
- filterHandling - Dakle prvo se uzmu kao konstante elementi htmla prema njihovom ID-u, zatim prođemo kroz sve filtre i maknemo prazne te čekamo promjene u formama za filtriranje, ako se nešto promjeni onda pozovemo fetchSpells funkciju sa svim filtrima trenutnim koji nisu prazni
- formHandling - Ovdje se mjenjaju "tabovi" opisanu u html djelu za add, view i edit spell. Također kada se klikne edit se froma updatea sa detaljima tog spella, a kad se klikne add se forma resetira. Nakon toga ovisno ako smo u edit ili add metoda se promjeni u POST ili PATCH, te na kraju imamo funkciju za import pomoću .jsona
___
## Funkcionalnosti web aplikacije

### Osnovne funkcionalnsoti (CRUD):
- CREATE 
  - Dodavanje spellova kroz add formu
- READ
  - Dohvaćanje osnovnih informacija svih spellova iz baze, te prikaz istih
  - Kliknom na spell sa liste, dohvaćanje i prihaz ostalih informacija
- UPDATE
  - Promjena spellova kroz edit formu
- DELETE
  - Brisanje spellova pomoću delete gumba

### Dodatne funkcionalnosti
- Filtriranje
  - Kako je teško pregledati npr. 575 spellova u listi, dodao sam nekoliko metoda filtriranja
  - Prema ID-u
  - Prema imenu, kako pišemo ime spella sve spellovi koji sadrže taj substring u imenu će se pokazivati
  - Prema knjizi iz koje su, ovdje se lista knjiga dinamicki updatea te uvijek sadrži sve knjige iz baze
  - Prema School of magic
  - Prema Levelu spella
  - Prema vremenu potrebnom za izvod
  - Prema dometu
  - Prema klasi za koju je spell
  - I naposlijetku bilo koja kombinacija prijespomenutog
- Vizualizacija
  - Sa strane uvijek imamo osnovnu vizualizaciju o raspodjeli spellova po levelu i skoli radi laganog pregleda podataka pomoću chart.js
- Import from file
  - Kako bi se lakše dodali spellovi koji su standardni ili neka grupa koristi, može se izabrati datoteka za upload, te ako je .json dobro formatiran unutar nekoliko trenutaka će se sve iz tog jsona dodat.
___
