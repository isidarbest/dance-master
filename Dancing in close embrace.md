---
aliases:
  - Blízké držení
type: dance
specification:
  - dance technique
principle:
  - "[[Dance connection]]"
  - "[[Dance communication]]"
  - "[[Intimity in dance]]"
connected_with:
  - "[[Sliding touch]]"
---

> [!NOTE] Leading to close embrace should always be an invitation!


## Close embrace beginners
- First just make them to try how it is to dance in close embrace. Change partners a lot. Then ask for whom was any experience uncomfortable.
- Talk about how to get to and out of the close embrace
 *In any point during a day we can feel differently and it is very important to be true to ourselves. When someone doesn't wan to get closer to you it doesn't have to be caused by you (eventhough it can and always try to smell nice). It can be just their state of body, how their day is or anything else.*
- L try to invite their partners into close embrace, F are choosing, how close they wanna go (see also [[Social Dance Handbook#Consent]])

## Leading into close embrace
Easiest figures where we can get to close embrace (most comfortable is when leader is adjusting his position)
- [[Basic step]] when follower is going front, leader shortens his steps
- Standing on spot

**Make sure that:** 
- you are standing in between each other feet (every feet has its own lane)
- your body is a turned a little bit to the left - so your tools are facing away from the follower
- you are standing straight and not hunched over or bent
## Non-verbal communication of close embrace
### How does leader know that follower wants to get close?
- she is using [[Sliding touch]] when getting closer
- he feels like she wants to hug him
### How can follower let leader know she doesn't want to get close?
From softest to the most obvious. 
1. Changing her steps so she does not get close (usually smaller steps, more controlled)
2. Activating her frame more than usual
3. Placing her hands in front of leaders shoulders so she can push back - only if they feel stronger pull from the leader

If non of these work - then be verbal or stop the dance.

> [!warning] Be careful
> If it should be working, follower has to relax again once the position is gone (once she is in the position she wishes to be in) to let leader know that this is what she wanted.


## Figury vhodné na close embrace
[[Lateral mirror]]
[[Pião]]

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

