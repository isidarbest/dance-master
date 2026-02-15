---
type: dance
specification:
  - dance principle
principle:
technique:
  - "[[Following in zouk]]"
  - "[[Leading in zouk]]"
---
> [!example] Example: Leader Carrying vs. Active Following
> Imagine helping a child jump onto a high curb. If you try to lift them without their help, it's heavy and uncoordinated. But if the child bends their knees with you and **uses your upward impulse to jump**, the movement becomes smooth and shared.


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
WHERE type = "event" AND contains(topic,this.file.link) 
SORT file.name DESC 
```