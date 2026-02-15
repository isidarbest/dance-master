---
type: dance
specification:
  - dance principle
principle:
technique:
---
Grounding is a technique that helps you to feel safe, free, open and relax and things can happen naturally and we don't have to make them happen. [^1]

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

# Classes, workshops and exercises teaching this principle %% fold %% 
```dataview
LIST
WHERE contains(topic,this.file.link) 
SORT file.name DESC 
```

[^1]: [[Brenda]] on [[2025-04 Castle of Miracles]]
