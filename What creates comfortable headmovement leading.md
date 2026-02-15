---
type: dance
specification:
  - dance technique
principle:
  - "[[Frame in zouk]]"
connected_with:
  - "[[Headmovements]]"
  - "[[Leading in zouk]]"
  - "[[Frame activation]]"
  - "[[Frame elasticity and flexibility]]"
  - "[[Reactive frame]]"
  - "[[Connection of frame and body in leading]]"
up:
  - "[[Headmovements]]"
---

**Using our chest for leading the movement**
The movement of the body should come from the same place as the followers movement, only our head is staying upright. Movement of the body of leader can become smaller and smaller with time as the body learns to adapt to the movement and be more clear. 

**Adaptation ([[Reactive frame]])**
- the way leader is capable of adapting to followers:
	- range of motion 
	- irregularities 
	- tension/softness/relaxation level/tone of muscle
- receiving the body weight of follower with reactive frame instead of fixed

**[[Connection of frame and body in leading]]**
If the leading comes only from the frame it will always feel stiff and less comfortable for the follower. 

**Using legs to create and slow down the movement**
Especially when we receive the follower in the end of movement, it is very important that we use our knees to soften the movement. 

**Grounding**

**Support**

**Clarity of size and direction**


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
WHERE type = "dance" AND contains(specification,"dance principle") AND contains(principle,this.file.link) 
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