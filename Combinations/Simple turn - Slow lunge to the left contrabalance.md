---
type: dance
specification:
  - combination
elements:
  - "[[Simple turn]]"
  - "[[Slow lunge to the left]]"
---

Můžeme tréninkově zastavit mezi druhým a třetím krokem točky, kde L dává F ruku na záda a připravuje energii rotace. Zde *vyzkoušíme*, jestli L vedou opravdu po kruhu a jestli F neuvolňují lopatku a nevysazují rameno. 

**Chceme, aby Followerky:**
- nespěchaly do prvního kroku, už třetí krok točky nás připravuje do tohoto prvku. Zůstávat pocitově pořád vzadu
- držely svoje tělo rovně, není těžké si to splést s navedení do vlny

**Chceme, aby Leadeři:**
- navázali na pohyb followerky, neměla by cítit žádné zastavení rotace. Využíváme předešlé rotace do dalšího pohybu
- přípravu provádíme většinou přejitím na pravou stranu followerky (z pohledu L)

## Možné vstupy 
- po [[Simple turn]]
- [[Soltinho#Soltinho wifi|Soltinho wifi]] ukončení
- z [[Open to the right]]
	- zde je pro F nejnáročnější čekat na vstup do prvního kroku dostatečně dlouho

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
