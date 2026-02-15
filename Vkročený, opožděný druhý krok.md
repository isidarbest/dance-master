---
type: dance
specification:
  - dance technique
principle:
  - "[[Weight transfer and footwork]]"
connected_with:
  - "[[Turning on spot]]"
  - "[[Stepping in a dance|Stepping in a dance]]"
---
⏯ [Video principu a na co se používá](https://youtu.be/q0djFNTpJKg) (ze [[2025-11 Zoukmania s Moni a Hančou (celý měsíc)]])


Základ je stejný do druhého kroku. Leader vede partnerku do laterálového otevření a následně druhý krok vkročí mezi její nohy. Nejlépe tak, aby měli kontakt L v levé noze a F v pravé na stehnu. Je to opožděný krok, který L vytváří až následně, když už prošla noha followerky.

Jakým způsobem jdeme třetí krok potom odliší, jaký prvek můžeme jít.

Využíváme pro prvky: 
- [[Vkročená změna směru]]
	- třetí krok jde zpátky do linie, ze které jsme vyšli. Naše tělo nenechá partnerku odlepit její levou nohu od podlahy tím, že jde zpátky do původního směru.
- [[Pião]]
	- třetí krok jde kolem partnerky v kruhu, tím rozjedeme rotaci
- [[Contrabalance]]
	- stejně jako Piao, ale nenecháme partnerce prostor na krok - držíme ji pořád v její ose. Energie točky ji tím pádem pošle na jednu nohu.
	- případně varianty různého stylingu a kreativity [jako například na tomto videu](https://youtu.be/1ydDqWdFKPY?si=SX8XXmrjwfDwh9rm&t=36)
- [[Viradinha#Overrotated viradinha]]
	- přeneseme více váhu do druhého kroku, přeneseme se přes tento krok a u toho otevíráme hrudníkem do viradinhy. Snažíme se delší dobu držet váhu na druhém kroku, abychom měli dostatek času ji přetočit.

Postup učení viz [[Vkročená změna směru#Postup učení]].
# Connected notes  %% fold %% 
## Connected technique %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance technique") AND contains(connected_with,this.file.link) 
SORT file.name DESC 
```
## Elements and combinations using this technique %% fold %% 
```dataview
LIST
WHERE (
  type = "dance element"
  AND contains(technique, this.file.link)
  AND !contains(file.name, "Template")
) OR (
  type = "dance"
  AND contains(specification, "combination")
  AND contains(technique, this.file.link)
  AND !contains(file.name, "Template")
)
SORT type DESC
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