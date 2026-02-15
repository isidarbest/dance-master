---
type: dance
specification:
  - dance technique
principle:
  - "[[Principles of leading and following]]"
connected_with:
  - "[[Following through the frame]]"
  - "[[Momentum-Based Following]]"
---
Follower should react in a way of [[Relaxed action]]. 

If the follower is [[Non-reactivity|non-reactive]], it helps to create relaxed actions. Sentence, that can help the mind and body can be *I don’t need to move until I feel a clear impulse.*

## Basic rules follower should follow 
1. Respecting her / his own body
2. Respecting the direction of leading 
3. Respecting the size of energy giver to her body by the size of movement

## Relaxed following
1. Follower is standing in relaxed posture (minimal tension needed to be standing in healthy posture)
2. Lead is starting the preparation of movement 
3. The follower begins sensing information through the preparation—tension naturally starts to build as energy accumulates.
4. The follower consciously relaxes to let the information complete its flow—without letting the tension spread into emotional reactivity or the upper body.
5. Leading energy gets so high that it gets easier to move than to stand
6. [[Relaxed action]], the follower moves with clarity, honoring the direction and energy of the lead without adding excess effort. Using the inertia of the energy while keeping her body integrity and activity. 

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
  type = "dance element"
  AND contains(technique, this.file.link)
  AND !contains(file.name, "Template")
) OR (
  type = "dance"
  AND contains(specification, "combination")
  AND contains(technique, this.file.link)
  AND !contains(file.name, "Template")
)
SORT type DESC
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