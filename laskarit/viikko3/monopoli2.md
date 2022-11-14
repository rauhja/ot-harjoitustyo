classDiagram
    Nopat -- Pelaaja : 2
    Pelaaja -- Pelilauta : 2-8
    Pelilauta -- Ruutu : 40
    Pelaaja -- Pelinappula : 2-8
    Pelinappula -- Ruutu : 2-8
    Ruutu -- Sattuma
    Ruutu -- Vankila
    Ruutu -- Yhteismaa
    Ruutu -- Aloitusruutu
    Ruutu -- Asema
    Ruutu -- Laitos
    Ruutu -- Katu
    Sattuma -- Tapahtuma
    Yhteismaa -- Tapahtuma
    Vankila -- Tapahtuma
    Aloitusruutu -- Tapahtuma
    Asema -- Tapahtuma
    Laitos -- Tapahtuma
    Katu -- Tapahtuma
    Yhteismaa -- Kortti
    Sattuma -- Kortti
    Kortti -- Tapahtuma
    Katu -- Rakennus : 0-4