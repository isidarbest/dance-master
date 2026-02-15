---
type: dance
specification:
  - dance principle
principle:
---

Dancing is like speaking language. Sometimes two people don't speak the same language but they want to try to understand each other. One can learn from the second one. Or they don't have to want to understand each other. **If both people want, they can always understand each other in dance**.  [^1]


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

# Classes and workshops teaching this principle
```dataview
LIST
WHERE type = "event" AND contains(topic,this.file.link) 
SORT file.name DESC 
```





[^1]: [[2023-06 Bremen Val and Vanessa teachers course]]