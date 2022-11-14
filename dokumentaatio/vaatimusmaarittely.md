#Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on sanapeli, jossa pelaaja yrittää arvata annettua viisikirjaimista sanaa. Sovellukseen 
on mahdollista luoda oma käyttäjätunnus, jolloin sovellus tallentaa tilastoja pelikerroista. 

## Käyttäjät

Sovellusta voi pelata joko luomalla käyttäjätunnuksen tai ilman. Luomalla käyttäjätunnuksen 
sovellus pitää kirjaa arvatuista sanoista ja montako arvausyritystä siihen kului.

## Käyttöliittymäluonnos

![](./kuvat/kayttoliittyma-hahmotelma.jpg)

## Perusversion tarjoama toiminnallisuus

### Pelin toiminnallisuus

- Käyttäjä yrittää arvata annettua sanaa
  - Viisi yritystä arvata sanaa
  - Jos kirjain on oikein ja oikealla paikalla, muuttuu se vihreäksi
  - Jos kirjain on oikein, mutta on väärällä paikalla, muuttuu se keltaiseksi

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen tulee olla uniikki
  - Salasanan täytyy olla yli 8 merkkiä ja sisältää:
    - Vähintään yksi iso kirjain
    - Vähintään yksi numero
  
- Käyttäjä voi kirjautua sisään tunnuksella ja salasanalla
  - Jos käyttäjätunnus tai salasana on väärin, järjestelmä ilmoittaa siitä

- Käyttäjä voi pelata peliä myös ilman kirjautumista

### Kirjautumisen jälkeen

- Käyttäjä voi pelata peliä

- Käyttäjän peleistä tallentuu tilastoja
