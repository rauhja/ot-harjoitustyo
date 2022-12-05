# Arkkitehtuurikuvaus

Arkkitehtuurikuvaus on alustava ja täydentyy myöhemmin.

## Rakenne

Sovellus rakentuu kahdesta eri pääkomponentista: ui ja services.

![](./kuvat/pakkauskaavio.png)

Ui sisältää kaiken graafisen käyttöliittymän toiminnallisuuden. Services sisältää kaksi luokkaa, joista toinen käsittelee näppäimistön tapahtumia ja toinen pelilogiikkaa.

## Käyttöliittymä

Käyttöliittymä koostuu kahdesta erillisestä näkymästä:

- Aloitusnäkymä, josta siirrytään pelaamaan
- Pelinäkymä, jossa pelataan peliä ja voidaan palata aloitusnäkymään back -painikkeella

## Sovelluslogiikka

Sovelluksen toiminnallisuus toteutuu luokissa GameLogic ja GameEvents, jotka toteuttavat pelissä tapahtuvat tapahtumat.

## Päätoiminnallisuudet

### Pelin aloitus

Käyttäjä näkee näkymässä tyhjän ruudukon, mihin syötetään täydentyy kirjaimet sekä vihjeet seuraavalla tavalla:

![](./kuvat/gameplay.png)

Kun käyttäjä painaa kirjainta näppäimistössään kutsuu GameEvents metodia add_letter GameLogic luokasta ja handle_letter metodia käyttöliittymästä antaen parametreiksi kirjaimen, kirjainten määrän ja ylärajan kirjaimien määrälle. Tämän jälkeen GameEvents kutsuu increase_letter_count funktiota.