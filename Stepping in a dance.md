---
aliases:
  - Technika kroku
type: dance
specification:
  - dance technique
principle:
  - "[[Weight transfer and footwork]]"
connected_with:
  - "[[Slowing down]]"
---
*Chodidlo stojné nohy se odlepuje tehdy, kdy ho vezme tělo (kdy už to prostě jinak nejde)
Tohle platí především u hudby, která má tempo podobné tempu našeho kroku. Pokud je tempo pomalejší, tak se zdržujeme déle na stojné noze (jelikož nemůžeme zpomalit průběh kroku uprostřed). Pokud je to rychlejší, tak naopak z nohy odcházíme rychleji. Zároveň, pokud jdeme rychlejší krok, tak se dostaneme méně na paty.* [^1]


## Resources
https://amozouk.com/blog/6-tips-to-improve-your-brazilian-zouk-footwork?fbclid=IwAR3-VhIYzaN3nUvyI59UCyiRiJNHv4B-FzeDx0RnxWBGyUfXzu7t6NblYm0

[Ballet drills for strengthening your foot positions](https://youtu.be/U-nhYGYWO2Q?feature=shared)


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





[^1]: [[2023-02 Luděk technika kroku]]
