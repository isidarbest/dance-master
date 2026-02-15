---
type: dance
specification:
  - dance principle
principle:
  - "[[Musicality in a dance]]"
---



# Connected notes  %% fold %% 
## Connected principles
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance principle") AND contains(principle,this.file.link) 
SORT file.name DESC 
```

## Connected technique
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance technique") AND contains(principle,this.file.link) 
SORT file.name DESC 
```

# Classes and workshops teaching this principle %% fold %% 
```dataview
LIST
WHERE contains(topic,this.file.link) 
SORT file.name DESC 
```