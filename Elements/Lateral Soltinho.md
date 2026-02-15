---
type: dance element
specification:
  - dance element
English:
Portuguese:
principle:
technique:
---
🔗 [Video prvku](https://youtube.com/shorts/ktNMIhvE_3M?feature=share)

[[Viradinha - Side hip bump odstrčení#Pokračování leader turn under arm + turn follower]]
Leader vede levou rukou partnerčinu pravou a mění si strany. Partnerka je před partnerem.

### Jak učit 
Ukázat, do čeho se budeme dostávat. Začínáme [[Soltinho]]

🟢 Cvičení, kdy partnerka stojí na místě. Drží se L levá, F pravá. 
Leader jde směrem za partnerku, na jednu stranu po její pravé straně, na druhou stranu po její levé straně (aby se jí jednou omotala ruka kolem těla a podruhé šla mimo). Jediný úkol partnerky je uvolnit paži, ale aktivovat lopatku, aby nikdy nevylezla ze svého místa a otočit se, až jí to zatáhne na zádech u lopatky. 
Druhý stage zvedneme ruku do výšky ramen a děláme to stejné. 

Vyzkoušet si kroky bez držení (L od pravé, F od levé) z pozice Soltinha. 
- L dělá follower lateral od pravé nohy

Vyzkoušet i s vedením. Důležité aspekty
- L nevede pomocí ruky, jediný pohyb je nahoru, aby partnerka mohla projít. Vede pomocí své pozice vůči partnerce, tím vytvoří napětí, které ji otočí a nepustí do Soltinho kroku 
- partnerky mají tendenci se přitahovat rukou hlavně v levé pozici
### Normální ukončení
V momentě, kdy jde partnerka do prava, tak nejdu tak daleko od ní, ale do normální soltinhové vzdálenosti. Tím pádem jí "povolím" udělat překrok do jiné strany.
### Cool ukončení 
Na straně, kdy leader vychází pravou nohou podejde svoji ruku a zlstane pořád natočený stejným směrem. Následně musí vést partnerku přípravu + točku ze soltinha. 

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

# Lekce od ostatních lektorů s tímto prvkem
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