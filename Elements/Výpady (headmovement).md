---
type: dance element
specification:
  - headmovement
English:
Portuguese:
---

## Followerky kroky 
Druhý krok k noze, třetí krok od nohy (společně s hlavou).
Točí se s nohami u sebe. 

## Pokračovací výpady 
Učili [[Val and Vanessa]] na [[2019-03 Krakow zouk delight with Val and Vanessa]].

Při výpadu napravo partner nezamče svoje tělo, povolí svůj rám, aby povolil partnerce udělat celý kroužek. Svůj rám odpojí od partnerky, aby změna jeho pozice ji neovlivnila. Přechází před ni a teprve až je na správné pozici (výchozí pozice klasického výpadu), tak svůj rám znovu aktivuje a vede další výpad. 
Je velmi důležité, aby se nepřerušil flow balónu a aby partner respektoval rychlost cestování hlavy partnerky. 

## Výpady s counterlabance (s [[Slow lunge to the left]])
Dělali jsme na [[Kristýna Danielová - individual lesson#33. Lekce 2025-10-31 fold]]

Nejdřív zvládnutí [[Slow lunge to the left#Cambre]]. Velmi stejný princip vedení a následování, akorát leader vede naklopení. Z jeho roviny ramen partnerka rozumí, jestli je to rovné cambre nebo naklopení. 

Dá se přetáčet na obě strany, když točíme na naši pravou, je to náročnější jak navést, tak následovat. 

# Kombinace s tímto prvkem %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"combination") AND contains(elements,this.file.link) AND !contains(file.name,"Template")
SORT file.name DESC 
```

# Učili jsme na
```dataview
LIST
WHERE (
    contains(type,"event") 
    AND contains(elements,this.file.link) 
    AND !contains(file.name,"Template") 
    AND contains(teacher,link("Ondřej Král"))
)
OR (
    type = "dance" 
    AND contains(elements,this.file.link) 
    AND !contains(file.name,"Template") 
    AND contains(specification,"dance class") 
    AND contains(teacher,link("Ondřej Král"))
)
SORT file.name DESC
```