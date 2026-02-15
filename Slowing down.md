---
type: dance
notetoolbar: dance
specification:
  - dance technique
principle:
  - "[[Weight transfer and footwork]]"
connected_with:
  - "[[Stepping in a dance|Stepping in a dance]]"
  - "[[Momentum-Based Following]]"
aliases:
  - zpomalování
---
Zpomalování je nejjednodušší v každém druhém kroku, kde provádíme nějakou změnu směru. Jelikož v tom momentě přirozeně tělo zpomaluje a má větší možnost se zklidnit a usadit váhu na kyčel. 

Dá se trénovat v basic stepu solo i v páru.

Vycházíme L dozadu, v basicu dopředu absorbujeme energii v druhém kroku a do třetího kroku vycházíme s minimální energií. Můžeme propojit i se zpomalením v druhém kroku. 

Je možné jít stejnou krokovou sestavu a ve druhé a třetím kroku pouze absorbovat, abychom levou vyšli na jedničku dozadu dlouhý krok (náročnější). Pak je potřeba zase přenést váhu na pravou.

To stejné můžou pokročilejší tanečníci zkusit ve [[Viradinha]]. 

# Connected notes  %% fold %% 
## Connected technique %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance technique") AND contains(connected_with,this.file.link) 
SORT file.name DESC 
```
## Elements and combination using this technique %% fold %% 
```dataview
LIST
WHERE (
  type = "dance"
  AND contains(specification, "dance element")
  AND contains(technique, this.file.link)
  AND !contains(file.name, "Template")
) OR (
  type = "dance"
  AND contains(specification, "combination")
  AND contains(technique, this.file.link)
  AND !contains(file.name, "Template")
)
SORT file.name DESC
```
## Underlying principles %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance principle") AND contains(technique,this.file.link) 
SORT file.name DESC 
```
## Exercises practising this technique %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"exercise") AND contains(topic,this.file.link) 
SORT file.name DESC 
```

# Taught at %% fold %% 
```dataview
LIST
WHERE (
  type = "event"
  AND contains(topic, this.file.link)
  AND !contains(file.name, "Template")
) OR (
  type = "dance"
  AND contains(specification, "dance class")
  AND contains(topic, this.file.link)
  AND !contains(file.name, "Template")
) OR (
  type = "individual lesson"
  AND contains(topic, this.file.link)
  AND !contains(file.name, "Template")
)
SORT file.name DESC
```