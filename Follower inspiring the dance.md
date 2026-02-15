---
type: dance
specification:
  - dance technique
principle:
  - "[[Dance adaptibility]]"
  - "[[Dance communication]]"
connected_with:
  - "[[Following in zouk]]"
---


# Connected notes 
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
WHERE type = "dance" AND contains(specification,"dance principle") AND contains(technique,this.file.link) 
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
WHERE (
  type = "event"
  AND contains(topic, this.file.link)
  AND !contains(file.name, "Template")
) OR (
  type = "dance"
  AND contains(specification, "dance class")
  AND contains(topic, this.file.link)
  AND !contains(file.name, "Template")
) OR (
  type = "individual lesson"
  AND contains(topic, this.file.link)
  AND !contains(file.name, "Template")
)
SORT file.name DESC
```