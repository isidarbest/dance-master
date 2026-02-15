---
type: dance
specification:
  - dance technique
principle:
  - "[[Frame in zouk]]"
connected_with:
  - "[[Frame elasticity and flexibility]]"
---

## Cvičení na zjištění, které svaly potřebujeme na aktivaci rámu
Člověk A stojí na místě, má zavřené oči a uvolněné paže. Člověk B si stoupne k jeho boku a začne hýbat jeho rukou po kruhu kolem něj. V určitý moment (kdy si člověk A vybere) aktivuje co nejméně svalů, aby se pohyb ruky a její rotace rovnala rotaci v těle (jak kdybychom měli zasádrované rameno k tělu), tzn. tělo a ruka se pohybují současně. Člověk A zkouší střídat uvolnění a aktivace paže a přijít na to, jaké svaly k tomu používá. Zároveň pozorností projede i zbytek těla, jestli někde nemá zbytečnou aktivaci nebo zatnutí. 


# Connected notes 
## Connected technique %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance technique") AND contains(connected_with,this.file.link) 
SORT file.name DESC 
```
## Elements where we use this technique %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance element") AND contains(technique,this.file.link) 
SORT file.name DESC 
```
## Underlying principles %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance principle") AND contains(principle,this.file.link) 
SORT file.name DESC 
```

# Taught at %% fold %% 
```dataview
LIST
WHERE type = "event" AND contains(topic,this.file.link) AND !contains(file.name,"Template") OR type = "dance" AND contains(specification,"dance class") AND contains(topic,this.file.link) AND !contains(file.name,"Template")
SORT file.name DESC 
```