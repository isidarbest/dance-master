---
type: dance
specification:
  - dance principle
principle:
technique:
  - "[[Musicality layers of a dancer]]"
---


Brenda: Some songs give more attention into how we feel and some into how we move. [^1]

In general it is most often seen as how you decide to move your body (with your partner) to interpret some music. 

1. dancing in the beats
   your dance is expressing everything that is in the music. It is the "obvious" choice
2. dancing on the beats
   looking at the song from above and deciding what you express. You understand the music you hear and your dance is adding something extra to it, not always "visible" in the music. You are expressing the music in your own "words". So you follow and respect the message of the song, but adding something to it. 

You don't want to seperate them, you want to be great at both.

# Rhytmical changes
## Emphasise one

### 1) quick- sloooow
Making the steps before the one all quick and then prolonging the one for twice the time
[Like in this video](https://www.facebook.com/watch/?v=817114566851246) at 3:53


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
WHERE contains(topic,this.file.link) 
SORT file.name DESC 
```
# Exercises 
```dataview
TABLE teacher, created
WHERE type = "dance" AND contains(specification,"exercise") AND contains(tags,"musicality")
SORT teacher DESC 
```

[^1]: [[2023-09 Bali Zouk embodiment retreat and traveling#Workshop where everyone teaches]]