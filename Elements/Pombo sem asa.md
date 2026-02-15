---
type: dance element
specification:
  - headmovement
English: wingless pigeon
Portuguese: Pombo sem asa
---
[[2025-04-29]] [[Shanie]] told me about it in Prague.

It is basically [[Toalha]] stepping in linear way for the follower. She completes the circle while the rotation of her body stops. 


# Kombinace s tímto prvkem %% fold %% 
```dataview
LIST
WHERE type = "dance" AND contains(specification,"combination") AND contains(elements,this.file.link) AND !contains(file.name,"Template")
SORT file.name DESC 
```

# Učili jsme na
```dataview
LIST
WHERE type = "event" AND contains(elements,this.file.link) AND !contains(file.name,"Template") OR type = "class" AND contains(elements,this.file.link) AND !contains(file.name,"Template")
SORT file.name DESC 
```