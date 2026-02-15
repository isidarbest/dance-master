---
type: dance
specification:
  - dance technique
principle:
  - "[[Frame in zouk]]"
connected_with:
  - "[[Momentum-Based Following]]"
---
In the full stretch of elastic moment, it should feel like two ropes connected and gently pulled apart—firm, responsive, and ready to move, but never rigid.
If you lock your elbows, then it will feel like two sticks. 

Elastic moment is a combination of maximum distance in your arms together with the size of your step and how far you move your body center between your legs. Your weight in elastic moment should always be at least in the middle, otherwise it will not be comfortable for you and you won't make proper step.


## Connected principles
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance principle") AND contains(technique,this.file.link) 
SORT file.name DESC 
```

## Connected technique
```dataview
LIST
WHERE type = "dance" AND contains(specification,"dance technique") AND contains(connected_with,this.file.link) 
SORT file.name DESC 
```

# Lekce/workshopy s tímto tématem
```dataview
LIST
WHERE type = "event" AND contains(topic,this.file.link) AND !contains(file.name,"Template") OR type = "dance" AND contains(specification,"dance class") AND contains(topic,this.file.link) AND !contains(file.name,"Template")
SORT file.name DESC 
```