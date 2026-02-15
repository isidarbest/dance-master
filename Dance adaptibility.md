---
type: dance
specification:
  - dance principle
principle:
technique:
  - "[[Following in zouk]]"
  - "[[Leading in zouk]]"
  - "[[Reactive frame]]"
  - "[[Follower inspiring the dance]]"
---
This is very important topic for leaders especially when they want [[Follower inspiring the dance|to be inspired by follower]]. Body of leader is not lead by the follower in that moment, his role is to adapt to her body in a way that feels most compatible and comfortable for both of them.


# Connected notes 
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