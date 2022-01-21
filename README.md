# File Reading and Data Manipulation

# Description

In this project I'm practising extracting data from a .txt file and data manipulation in Python.  
I'll be also practising my TDD skills whilst working on this project.

## Client Requirements

You are supply files with extracts from a book. There are a few request from the reviewing team:

> Find keywords in file  
> How many times these are repeated in each file

Text 1 - "Today is a sunny day, I like it when it's sunny like this."

|      Input      |   Output   |
| :-------------: | :--------: |
| Text 1, "sunny" | "sunny: 2" |

> Find capitalized words in sentences in each file  
> Return the word and the sentence where the word was found.

Text 2 - "I live in Chesham, it is a lovely town. In Chesham there are lovely coffee shops like the Tavern."

| Input  |
| :----: |
| Text 2 |

**Output:**

```
{
    "capitalized_words": {

        "Sentence": "I live in Chesham, it is a lovely town.",
        "Words": ["I", "Chesham"],
    },
    {
        "Sentence": "In Chesham there are lovely coffee shops like the Tavern.",
        "Words": ["In", "Chesham", "Tavern"],
    }
}
```

> The ideal lenght of a sentence is 20 words.  
> Find sentences where the length is higher that 20 words.  
> Return the word count and the sentence.

Text 3 - "I live in Chesham, it is a lovely town and in Chesham there are lovely coffee shops like the Tavern that serve delicious food and drinks."

| Input  |
| :----: |
| Text 3 |

**Output:**

```
{
    "very_long_sentences": {
        "sentence": "I live in Chesham, it is a lovely town and in Chesham there are lovely coffee shops like the Tavern that serve delicious food and drinks.",
        "word_count": 26,
    },
}
```

# Technologies

- Python 3.8
- Pytest 5.4
