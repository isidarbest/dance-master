---
type: dance
specification:
  - dance technique
principle:
  - "[[Basic posture in dance]]"
  - "[[Flow in Zouk]]"
  - "[[Frame in zouk]]"
connected_with:
---

## Headmovements
We cannot start headmovement until we learn to walk with each other ([[Xandy Liberato]])[^1]

We don't have to lead the exact size of the movement of the head, because the head is influenced by the shoulders and chest. So always try to make it smaller. 

>try to find some good example on how to make it closer to people 

## Elements of headmovements  %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance element") AND contains(specification,"headmovement") 
SORT file.name ASC 
```

# Connected notes  %% fold %% 
[[Upper back backbend]]
## Connected technique %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance technique") AND contains(connected_with,this.file.link) 
SORT file.name DESC 
```
## Elements where we use this technique %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance element") AND contains(technique,this.file.link) 
SORT file.name DESC 
```
## Underlying principles %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance principle") AND contains(principle,this.file.link) 
SORT file.name DESC 
```
## Exercises practising this technique %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"exercise") AND contains(topic,this.file.link) 
SORT file.name DESC 
```

# Taught at %% fold %% 
```dataview
LIST
WHERE type = "event" AND contains(topic,this.file.link) AND !contains(file.name,"Template") OR type = "dance" AND contains(specification,"dance class") AND contains(topic,this.file.link) AND !contains(file.name,"Template")
SORT file.name DESC 
```



[^1]: [[2022-04 Zouk Bootcamp with Xandy#Headmovement]] 
