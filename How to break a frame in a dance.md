---
type: dance
specification:
  - dance technique
principle:
  - "[[Frame in zouk]]"
connected_with:
---
## Basic options for leader to break the frame [^1] 
1) Using the inertia of the body (for example in [[Dance/Elements/Open to the right]]). When it would be too hard to keep the frame in the moment, so instead the frame relaxes. 
2) Changing the angle of the hands
3) Bringing hands into the "empty zone" - the center of the body of the follower

[^1]: [[Lui and Larrisa headmovement Masterclass]]


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
WHERE type = "event" AND contains(topic,this.file.link) AND !contains(file.name,"Template") OR type = "dance" AND contains(specification,"dance class") AND contains(topic,this.file.link) AND !contains(file.name,"Template")
SORT file.name DESC 
```