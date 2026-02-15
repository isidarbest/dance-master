---
type: dance element
specification:
  - dance element
English:
Portuguese:
principle:
technique:
---

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

