---
type: dance
specification:
  - dance principle
principle:
technique:
---

Dance creativity is not about training one movement for hours and then execute it perfectly. I see it more as training some general technique over and over until you can just completely relax our of your head, you can trust your body and "go with the flow". Do what body feels on the music. 

## Jednoduché cvičení k rozvíjení kreativity a muzikality leadera
- vyjadřovat hudbu jen pomocí 
	- lateral 
	- piao
	- krokové točky
- za celou písničku netančit žádnou točku

- říkat STOP, tehdy musí leader co nejplynuleji zastavit a vrátit se na začátek prvku, který tančil, pozpátku (revertovat směr)


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

