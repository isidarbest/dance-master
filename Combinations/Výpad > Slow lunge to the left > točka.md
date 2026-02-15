---
type: dance
specification:
  - combination
elements:
  - "[[Slow lunge to the left]]"
  - "[[Výpady (headmovement)]]"
---

## Možnosti headmovementu v točce pro followerky 
Změna hlavy přichází ve stejnou dobu, co followerka přitahuje nohu pod sebe.

1. narovnání 
2. stejně jako výpady - držení tvaru po celou dobu točky a změna tvaru až po dokončení točky
3. vložený balon ([[Tornado]])
# Učili jsme na %% fold %% 
```dataview
LIST
WHERE (
    contains(type,"event") 
    AND contains(combinations,this.file.link) 
    AND !contains(file.name,"Template") 
    AND contains(teacher,link("Ondřej Král"))
)
OR (
    type = "dance" 
    AND contains(combinations,this.file.link) 
    AND !contains(file.name,"Template") 
    AND contains(specification,"dance class") 
    AND contains(teacher,link("Ondřej Král"))
)
SORT file.name DESC
```
