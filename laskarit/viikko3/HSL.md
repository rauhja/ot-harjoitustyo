sequenceDiagram
    Main->>Laitehallinto: HKLLaitehallinto()
    Main->>rautatietori: Lataajalaite()
    Main->>ratikka6: Lukijalaite()
    Main->>bussi244: Lukijalaite()
    Main->>Laitehallinto: laitehallinto.lisaa_lataaja(rautatietori)
    Main->>Laitehallinto: laitehallinto.lisaa_lukija(ratikka6)
    Main->>Laitehallinto: laitehallinto.lisaa_lukija(bussi244)
    Main->>lippu_luukku: Kioski()
    Main->>lippu_luukku: lippu_luukku.osta_matkakortti("Kalle")
    lippu_luukku->>kallen_kortti: uusi_kortti = Matkakortti("kallen_kortti")
    kallen_kortti->>Main: kallen_kortti
    Main->>rautatietori: rautatietori.lataa_arvoa(kallen_kortti, 3)
    rautatietori->>kallen_kortti: rautatietori.kasvata_arvoa(kallen_kortti, 3)
    kallen_kortti->>kallen_kortti: kasvata_arvoa(3)
    Main->>ratikka6: ratikka6.osta_lippu(kallen_kortti, 0)
    ratikka6->>kallen_kortti: kallen_kortti.arvo()
    kallen_kortti->>ratikka6: 3
    ratikka6->>kallen_kortti: kallen_kortti.vahenna_arvoa(hinta)
    ratikka6->>Main: True
    Main->>bussi244: bussi244.osta_lippu(kallen_kortti, 2)
    bussi244->>kallen_kortti: kallen_kortti.arvo()
    kallen_kortti->>bussi244: 1.5
    bussi244->>Main: False