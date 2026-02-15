---
type: dance
specification:
  - combination
elements:
  - "[[Zarážka]]"
  - "[[Tilted turn]]"
  - "[[Balloon]]"
principle:
technique:
---

Zarážka s headmovementem, v momentě, kdy vymotávám ze zarážky, zvedám ruku nahoru, partnekra pokračuje balonem a tilted turn. Je potřeba vychytat správný moment, abychom followerce nezlomili ruku a zároveň abychom nezastavili energii, kterou už má nabranou.

Ideální příprava na [[Tornado]]

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
OR (
    type = "individual lesson" 
    AND contains(combinations,this.file.link) 
    AND !contains(file.name,"Template") 
)
SORT file.name DESC
```
