# Arkkitehtuurikuvaus

## Rakenne

Ohjelman alustava rakenne näyttää seuraavanlaiselta:

```mermaid
classDiagram
    UI --> Services
    Services --> Repositories
    Services --> Entities
    Repositories --> Entities
```
Pakkaus UI sisältää käyttöliittymän, services pelilogiikan ja repositories tietojen tallennuksesta vastaavan koodin. Entities sisältää sovelluksen tietokohteita.