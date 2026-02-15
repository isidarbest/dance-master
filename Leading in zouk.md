---
type: dance
specification:
  - dance technique
principle:
  - "[[Principles of leading and following]]"
  - "[[Dance adaptibility]]"
connected_with:
  - "[[Frame elasticity and flexibility]]"
---

We never try to force as leader. We try to convince. Not by force but by ourselves moving differently with our body (example when he started to move fluently in front of Vanessa and she started moving subconciously)[^1]


- Leader never has to carry the follower 

# Connected notes  %% fold %% 
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

[^1]: [[2023-06 Bremen Val and Vanessa teachers course]]