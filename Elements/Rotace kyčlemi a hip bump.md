---
type: dance element
specification:
English:
Portuguese:
---
⭐ [Video prvku](https://youtube.com/shorts/TbQ-uBtwbd8?feature=share)

Společné principy pro obě role: 
- rotace probíhá na jedné noze, jakmile se začneme rotovat, tak se obě nohy dostanou do kontaktu. Ta, na které se nerotujeme se pokrčí v koleni, špičkou se dotýká stojné nohy
- kolena směřují tam, kam špičky
- rotujeme pouze od kyčlí dolů (hodně podobný pocit jako v tangovém ochu)

## Z basic držení 
## Z [[Elastico]]

# Kombinace
```dataview
LIST
WHERE type = "dance" AND contains(specification,"combination") AND contains(elements,this.file.link) AND !contains(file.name,"Template")
SORT file.name DESC 
```

# Učili jsme na %% fold %% 
```dataview
LIST
WHERE type = "event" AND contains(elements,this.file.link) AND !contains(file.name,"Template") OR type = "dance" AND contains(specification,"dance class") AND contains(elements,this.file.link) AND !contains(file.name,"Template")
SORT file.name DESC 
```