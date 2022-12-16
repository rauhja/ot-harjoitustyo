# Word Guess Game

Tämä sovellus on jäljitelmä suureen suosioon nouseesta New York Timesin Wordle pelistä, missä käyttäjä yrittää arvata satunnaista viisi kirjaimista sanaa. Käyttäjä voi myös luoda oman käyttäjätunnuksen ja näin kerätä tilastoja peleistään. 

Sovellus on tehty Helsingin yliopiston Ohjelmistotekniikan kurssin harjoitustyönä.

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Testausdokumentti](dokumentaatio/testaus.md)
- [Viikko 5 release](https://github.com/rauhja/ot-harjoitustyo/releases/tag/Viikko5)
- [Viikko 6 release](https://github.com/rauhja/ot-harjoitustyo/releases/tag/Viikko6)
- [Loppupalautus](https://github.com/rauhja/ot-harjoitustyo/releases/tag/Loppupalautus)

## Asennus

### Asenna riippuvuudet komennolla

```bash
poetry install
```
### Alusta ohjelma

```bash
poetry run invoke build
```

### Käynnistä ohjelma

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman käynnistys

```bash
poetry run invoke start
```

## Testaus

```bash
poetry run invoke test
```

## Testikattavuusraportti

```bash
poetry run invoke coverage-report
```
Kattavuutta voi tarkastella htmlcov -kansiosta löytävästä index.html tiedostosta

## Pylint

```bash
poetry run invoke lint
```

## Lähdeviite

Sovelluksessa käytettävä sanalista ladattu:
https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt