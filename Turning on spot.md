---
type: dance
specification:
  - dance technique
principle:
  - "[[Turns in dance]]"
connected_with:
---



# Connected notes  %% fold %% 
## Connected technique %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance technique") AND contains(connected_with,this.file.link) 
SORT file.name DESC 
```
## Elements and combinations using this technique %% fold %% 
```dataview
LIST
WHERE (
  type = "dance"
  AND contains(specification, "dance element")
  AND contains(technique, this.file.link)
  AND !contains(file.name, "Template")
) OR (
  type = "dance"
  AND contains(specification, "combination")
  AND contains(technique, this.file.link)
  AND !contains(file.name, "Template")
)
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

# ss

When turning in spot, we often use footwork when we:
1) Move one foot to the direction of the turn
2) Replace the original place of first foot with second foot
![[Pasted image 20240112111003.png|300]]
![[Pasted image 20240112111014.png|310]]

Second option is to use the Paddle footwork (like we are going on a scooter or skateboard) [^1]

[^1]: [[Lui and Larrisa headmovement Masterclass]]