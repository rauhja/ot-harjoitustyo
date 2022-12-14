# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on sanapeli, jossa pelaaja yrittää arvata annettua viisikirjaimista sanaa. Sovellukseen 
on mahdollista luoda oma käyttäjätunnus, jolloin sovellus tallentaa tilastoja pelikerroista. 

## Käyttäjät

Sovellusta voi pelata joko luomalla käyttäjätunnuksen tai ilman. Luomalla käyttäjätunnuksen 
sovellus pitää kirjaa pelatuista peleistä ja arvattujen sanojen määrästä.

## Käyttöliittymäluonnos

Sovellus koostuu viidestä eri näkymästä

![](./kuvat/kayttoliittyma_hahmotelma.jpg)

Sovellus aukeaa aloitusnäkymään, josta on mahdollisuus siirtyä kirjautumiseen, rekisteröitymiseen tai pelaamaan peliä. Kirjautumisen jälkeen sovellus siirtyy kirjautuneen käyttäjän näkymään.

## Perusversion tarjoama toiminnallisuus

### Pelin toiminnallisuus

- Käyttäjä yrittää arvata annettua sanaa
  - Viisi yritystä arvata sana
  - Jos kirjain on oikein ja oikealla paikalla, muuttuu se vihreäksi
  - Jos kirjain on oikein, mutta on väärällä paikalla, muuttuu se keltaiseksi

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
- Käyttäjätunnuksen tulee olla uniikki
  - Salasanan täytyy olla yli 6 merkkiä ja sisältää:
  - Vähintään yksi iso kirjain
  - Vähintään yksi numero
  
- Käyttäjä voi kirjautua sisään tunnuksella ja salasanalla
  - Jos käyttäjätunnus tai salasana on väärin, järjestelmä ilmoittaa siitä

- Käyttäjä voi pelata peliä myös ilman kirjautumista

### Kirjautumisen jälkeen

- Käyttäjä voi pelata peliä
- Käyttäjän peleistä tallentuu tilastoja

## Jatkokehitysideoita

Perusversion jälkeen sovellukseen voisi lisätä seuraavia ominaisuuksia:

- Käyttäjä voi valita pelin arvattavien sanojen kielen.
- Peli tarkistaisi onko syötetty arvo oikeasti sana.
- Enemmän pelin tilastointia.
- Käyttäjä voi valita pelin vaikeustason, muokkaamalla arvauskertojen määrää.
