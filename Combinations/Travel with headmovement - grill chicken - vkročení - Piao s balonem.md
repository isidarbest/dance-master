---
type: dance
specification:
  - combination
elements:
  - "[[Travel]]"
  - "[[Balloon]]"
  - "[[Grill Chicken]]"
  - "[[Pião]]"
principle:
  - "[[Flow in Zouk]]"
technique:
  - "[[Headmovements]]"
---


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
OR (
    type = "individual lesson" 
    AND contains(combinations,this.file.link) 
    AND !contains(file.name,"Template") 
)
SORT file.name DESC
```
