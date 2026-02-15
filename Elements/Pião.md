---
Portuguese: Pião
English: Spinning top
type: dance element
specification:
principle:
  - "[[Turns in dance]]"
technique:
  - "[[Vkročený, opožděný druhý krok]]"
---
## Teaching Pião
V pozici, kdy máme oba dva pravou nohu jako centrum děláme koloběžku. 

Upravit, aby nepřenášeli tolik váhu na vnější nohu.

Upravit, aby vnější nohou chodili víc po směru točení dopředu kolem partnera. 


Přechod - musíme udělat jeden tum čik čik na místě a pak začít točit (zastavit lineární pohyb).
- točení doprava je přirozenější 
- máme jako centrum L pravá noha, F taky pravá
- druhá noha koloběžkuje
	- nepřenášet váhu na vnější nohu moc (stejně jako na koloběžce), jen se odrazit a jít zpět do středu, tělou celou dobu zůstává co nejvíc nad střední nohou
- ideální je dělat sudý počet kroků (6, 12), nebo-li sudý počet taktů 

když se točíme do leva, tak se změní střed -  centrum L levá a F pravá
### Procvičování 
- leader se pustí a partnerky se snaží držet kontakt převážně tím, že noha ve středu se nikam nehýbe

## Popis krokování od [[Michal Chromčák]]
Popisu kroky lambady z frente tras. 
1) prava noha leadera centrem toceni (napr Pablo) (pocit vic jako zabalim levou, vkrocim pravou do partnerky)
	- 1 vpred 
	- 2 vzad (na puvodnim miste) 
	- 3 diagonalne vlevo vzad 
	- 5 lehce vzad vuci puvodnimu mistu, ale s tim, ze tu nohu nechavam partnerce v ceste, aby vznikl kontakt stehny. Velikost kroku 3 urcuje, jak moc vzad jde krok 5 
	- 6 vpred (jakoby kolem partnerky se snazit jit - zabalovat) 
	- 7 na puvodnim miste kroku 5 
2) stahuju pravou nohu do vecka k leve 
	- 1 vpred 
	- 2 vzad (na puvodnim miste) 
	- 3 diagonalne vlevo vzad 
	- 5 stahnu paty k sobe do vecka 
	- 6 stranou, ale porad s umyslem za partnerku 
	- 7 paty k sobe do vecka 
3) vicemene paralelni postaveni 
	- 1 vpred 
	- 2 vzad (na puvodnim miste) 
	- 3 diagonalne vlevo vzad 
	- 5 vzad vuci puvodnimu mistu, kontakt stehny nevznika. 
	- 6 vpred (jakoby kolem partnerky se snazit jit - zabalovat) 
	- 7 klidne muze cestovat vic do prostoru (nedavam nikdy nohy k sobe a nemam kontakt stehny)

# Variations

## Reverse returning to leader 
Seen [[2026-01-05]] on [[2026-01 Organic Flow Marathon Warsaw]] on [[Manu]]

Using the rotation of the Piao, releasing follower into an outside turn with left hand on 4 beats but directly pulling arm back towards the center of the circle and continuing with Piao again. 

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