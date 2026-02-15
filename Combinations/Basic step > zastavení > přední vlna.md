---
type: dance
specification:
  - combination
elements:
  - "[[Basic step]]"
  - "[[Front Wave]]"
technique:
  - "[[Slowing down]]"
---
Před učením je potřeba probrat techniku [[Slowing down|zpomalování]]. 

V basic stepu na 5 krok zpomalujeme, 6 zavíráme hrudník partnerce. Na 1 vycházíme hrudníkem k ní a zároveň L přenáší váhu na levou nohu. S dokončením vlny do sedu přenášíme váhu na pravou nohu. 

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
