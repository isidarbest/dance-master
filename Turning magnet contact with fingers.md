---
type: dance
specification:
  - dance technique
principle:
connected_with:
  - "[[Following in zouk]]"
---
Something we are using in many figures when we need to rotate with our hands and in the same time not loose contact. Both roles stretch their fingers and try to keep the contact as magnet (which is mainly followers role).

# Connected notes 
## Connected technique %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance technique") AND contains(connected_with,this.file.link) 
SORT file.name DESC 
```

## Underlying principles %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance principle") AND contains(principle,this.file.link) 
SORT file.name DESC 
```

# Taught at %% fold %% 
```dataview
LIST
WHERE type = "event" AND contains(topic,this.file.link) AND !contains(file.name,"Template") OR type = "dance" AND contains(specification,"dance class") AND contains(topic,this.file.link) AND !contains(file.name,"Template")
SORT file.name DESC 
```