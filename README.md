# Word Guess Game

Tämä sovellus on peli, jossa käyttäjä yrittää arvata viisi kirjaimista sanaa viidellä yrityksellä. 

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

## Asennus

### Asenna riippuvuudet komennolla

```bash
poetry install
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