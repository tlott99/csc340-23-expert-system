# csc340-23-expert-system

## Requirements

The program tries to guess an item by asking two questions. The first question will take a single string answer and the second question will be yes/no.

If the program can't find the answer, it asks the user what the answer is and stores the answer to the internal knowledge base (kb). 

Implementation details:
* The kb is stored as a map where the key is the reponse to the first question concatenated with a hyphen then concatenate with a 0 or 1 base on the reponse to the second question.
* The value associate with the key is the answer.
* Example: 
```
What is the color of the fruit?
Yellow

Is it round?
Yes

What you have there is a lemon.
```

The program would have got the answer from the kb that loos like this:
```
{
    "yellow-1" : {
        "name" : "lemon"
    }
}
```

If there is no answer, the scenario would go like this:
```
What is the color of the fruit?
Yellow

Is it round?
No

I'm stumped. What is it?
Banana
```
It would then be added to the kb as:
```
{
    "yellow-1" : {
        "name" : "lemon"
    },
    "yellow-0" : {
        "name" : "banana"
    }
}
```


