---
type: dance element
specification:
English:
Portuguese:
principle:
technique:
  - "[[Vkročený, opožděný druhý krok]]"
---
## Vkročená změna směru
⏯ [Video prvku](https://youtu.be/cE2B5RNMAxE) ([[2025-11 Zouk Flow s Niki#2. Lekce 2025-11-19]])

> [!NOTE] Pozn. 
> Stejný vstup můžeme použít do [[Pião]], akorát začít točit víc. Tento prvek bychom proto měli jít hodně lineárně (otočka o 180 stupňů).

**Pro Followerky**
- je to krok [[Lateral]], proto se snažit druhý krok jít co nejvíc rovně (ale také tak musí být veden)
- usazovat váhu v bočním kroku

**Pro Leadery:**
- vkročený krok by měl být zhruba v půlce jejího kroku a co nejdál, abychom měli stejné centrum rotace
- třetí krok, který obkročujeme by měl vést energií dozadu
- pozor na moc rotační energii při vedení bočního kroku - F to pak bude vést spíš dokola kolem nás než lineární změnu směru (vchod do [[Pião]])
### Postup učení 
Vše v rytmu *Slow-Slow*

🟢 Basic pozice, leader vede pouze otevření do bočního kroku (jako otevření do Viradinha, skončíme hrudníky na sebe). 
- důležité, abychom usadili váhu na otevřenou stranu (L pravá, F levá)
- loopujeme tam a zpátky 
- leader zvolí pravidelný rytmus a občas zastaví v otevřené pozici (aby partnerka nic neočekávala a usadila váhu)

🟢 Začátek stejný, v otevřené pozici si leader může zvolit pokračovat pivot do stejné strany
- pro F se z toho stane krok dopředu mimo leadera 
- leader jde zadem a mimo partnerku
- jdeme jen jeden krok a pak se vracíme zpět do otevřené pozice
- zase můžeme zastavovat

🟢 V momentě, kdy partnerka dělá boční krok, tak L vkročí do prostoru mezi jejími nohami
- snaží se udělat co nejdelší krok (aby se dotkla stehna)
- časově krok dělá chvíli potom, co ona svůj krok umístí (jinak do sebe kopnou nebo ona ho musí překračovat)
- potom, co vkročí, tak jde zase zpět do basic pozice

🟢 Třetí krokem obkročí partnerku a pokračuje basic dozadu a může loopovat


# Kombinace s tímto prvkem %% fold %% 
```dataview
LIST
WHERE 
	type = "dance" 
	AND contains(specification,"combination") 
	AND contains(elements,this.file.link) 
	AND !contains(file.name,"Template")
SORT file.name DESC 
```

# Učili jsme na %% fold %% 
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
OR (
    type = "individual lesson" 
    AND contains(elements,this.file.link) 
    AND !contains(file.name,"Template") 
)
SORT file.name DESC
```

# Lekce od ostatních lektorů s tímto prvkem %% fold %% 
```dataview
LIST
WHERE (
    contains(type,"event") 
    AND contains(elements,this.file.link) 
    AND !contains(file.name,"Template") 
    AND !contains(teacher,link("Ondřej Král"))
)
OR (
    type = "dance" 
    AND contains(elements,this.file.link) 
    AND !contains(file.name,"Template") 
    AND contains(specification,"dance class") 
    AND !contains(teacher,link("Ondřej Král"))
)
SORT file.name DESC
```