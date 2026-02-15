---
type: dance element
specification:
  - headmovement
English:
Portuguese:
principle:
  - "[[Turns in dance]]"
technique:
  - "[[Turning on spot]]"
---
Followers have to learn to not listen their survival skill - always look where you are falling. In tilted turns and headmovements in general, the head is going in the opposite direction of "the fall". This is what makes it so hard to adapt the movement to the body. [^1]

### Možnosti ukončení tilted turns pro followerku: 
Všechny varianty začínají, jakmile její hlava prochází kolem jejího pravého ramene
- boční vlnou se zvednout do rovna (z levého ramene bez kroužku)
- udělat menší půl kroužek a skončit v rovné pozici z pravého ramene 
- dodělat celý kroužek, jen menší a může být dynamičtější (možnost přidat dva rychlé kroužky)
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
    type = "dance" 
    AND contains(elements,this.file.link) 
    AND !contains(file.name,"Template") 
    AND contains(specification,"exercise") 
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



# Connected notes
[^1]: [[Jade Rodrigues]] on Facebook 
