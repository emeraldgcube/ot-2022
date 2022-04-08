#### OT 2022 Repositorio

Jatketaan viime vuonna kesken jäänyttä tetris-projektia kurssin vetäjän (Matti Luukkainen) siunauksella

# Tetris

Tetris on klassinen peli, jossa pinotaan eri muotoisia palikoita pelikentälle, tavoitteena saada virheettömiä rivejä aikaiseksi. 

## Python-versio

Sovellus on testattu Python-versiolla 3.8.

## Käyttö 

1. Asenna riippuvuudet ajamalla komentoriviltä `poetry install`
2. Käynnistä peli komennolla `poetry run invoke start`

## Testit

1. Aja komento `poetry run pytest` src-kansiossa

## Testikattavuus

Testikattavuusraportin voi generoida komennoilla:

```bash
poetry run invoke coveragereport
```

Raportti generoituu _htmlcov_-hakemistoon.

## Pylint

.pylintrc-tiedoston määräämät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```



## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmäärittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Sekvenssikaavio](./dokumentaatio/kuvat/sekvenssikaaviotetris.jpg)

