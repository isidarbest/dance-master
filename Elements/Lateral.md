---
type: dance element
specification:
Portuguese: Lateral, Corredor
technique:
  - "[[Sliding touch]]"
---

[[Gui Prada]] nazývá lateral mirror prvek, kde se točíme oba dva stejným směrem a děláme laterálové kroky při změně držení. (tančí to v [tomto demu](https://youtu.be/oS3AUerO5Fk?si=-XyoHqkE9xvrLjBy&t=78)) ^f41cad

## Lateral basic
- ukázat oddělené kroky dámský/pánský laterál **(nejdřív učit bez pánských přešlapů)**
- naučit se open lateral
- vysvětlit klouzavé držení
- směřovat hrudníky do středu 
- udržovat stejnou vzdálenost rukou, stejný kruh

Později je možné přidat překroky pro leadery.

### Pohledy na rotaci hrudníku followerky
1. Nos vždy směruje na partnera, hrudník se otáčí zároveň s nosem. 
2. Představa provázku, který spojuje naše hrudníky a má jen určitou fixní vzdálenost. Je taky možné partnerku fyzicky chytnout za střed jejího trička na hrudníku. 
3. Hrudník vždy směřuje do středu rámu. 
4. Hrudník se točí mnohem méně než kyčle. 
5. Hrudník se vždy snaží, aby tělu bylo pohodlně. Když jdeš nejdelší možný krok (tam, kam vede energie), tak v určitý moment se začne rám deformovat, pokud se hrudník neotočí. 
### Holding hands %% fold %% 
![[Holding hands#Open posture (lateral)]]


# Typy laterálu basic podle vzdáleností

## Vzdálené držení (klasický)

## Vedení v basic vzdálenosti až v blízkém
- We are holding in [[Holding hands#Basic embrace|Basic embrace]] and doing the same lateral
- Leader needs to rotate the chest a lot
- We can either hold very box-like frame or we can stretch it little bit into diagonal (making it less symetrical)
# Typy laterálu podle krokování 

![[Lateral mirror#Lateral mirror]]
## Lateral reverse
Otočení směru kroků partnerky. 
# Typ lateralu podle vzájemné pozice

## Lateral behind the back
- leader vede followerku za svými zády
- leader si buď může přehodit nohy a pak jde pánský lateral nebo nepřehazovat nohy a pak jde dámský laterál od druhé nohy (tato varianta je příjemnější vést s jednou rukou)
## Shadow mirror lateral 
[Video prvku](https://youtu.be/iVY-SiQkOIM?si=Fsfjx62OS0PZhyM2&t=31)
- shadow pozice
- stejná logika jako u normální pozice, jen zezadu 
- stejně jako u mirror laterálu můžeme jít buď každý ve své lajně nebo oba ve stejné lajně. 
- Když jdeme ve stejné lajně
	- L jde ve stejné lajně a směru jako partnerka, třetí krok musí zarovnat do lajny, aby vyšli oba dozadu  
	- L zůstává více na středu, druhým krokem vkročí, ale třetí nemusí dostávat do lajny followerky. Je trochu náročnější v tom, že vedeme partnerku směr, který sami nejdeme

## Lateral Soltinho %% fold %% 

# Ukončení 
### Lateral ukončení z [[Dance/Elements/Open to the right]]
[[Dance/Elements/Open to the right]] + [[Simple turn]]
### Lateral Basic ukončení (vkročený)
Když je F na levé straně L pustí pravou ruku a vkročí do kroku partnerky > [[Basic step]]

# Kombinace
```dataview
LIST
WHERE type = "dance" AND contains(specification,"combination") AND contains(elements,this.file.link)
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