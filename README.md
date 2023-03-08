# CoTAK Dataset: **Co**mmonsense *T*emporal *A*ction *K*nowledge

A dataset resource consisting of short descriptions of action-describing sentences annotated with temporal commonsense knowledge. The dataset consists of instructions extracted from WikiHow, which are annotated with commonsense knowledge-based temporal labels indicating implicitly understood information about the actions described by the sentences, including approximately how long an action takes to perform and approximately how long its effects last for. For short duration actions labeled as taking seconds or minutes, which would be of relevance to automated task planning, e.g. in robotics applications, the dataset also provides scalar values to label the temporal durations of how long actions take to perform. 

## Overview

A dataset annotating simple English-language sentences with temporal duration information, consisting of over 300K instances. 

### Coarse-grained - available under [data/coarsegrained](data/coarsegrained).

The action-describing sentences are annotated with:

- How long the action takes to perform or complete (which we denote **perform duration**). 
- How long the duration of the action's effect last for (which we denote **effect duration**).

### Fine-grained - available under [data/finegrained](data/finegrained).

For data annoated as taking seconds or minutes in the coarse-grained dataset, the action-describing sentences are annoated with the number of seconds/minutes needed to perform the action.

## Data Format

Both segments of the dataset are available in JSON and CSV:

- Coarse-grained data is available as JSON: a list of JSON objects representing action sequences in the form:

```json
{     
   "id": "How to Ask a Customer for Identification1",
   "title": "How to Ask a Customer for Identification",
   "len": 10,
   "actions": [{
      "description": "Remind customers of the policy.",
      "perform": {
         "period": "minutes",
         "confidence": 2
      },
      "effect": {
         "period": "minutes",
         "confidence": 3
      }
   },
   ...
   ]
}
```

Where **id** is unique identifier of the action sequence, **title** is the sequence title, **len** is the number of actions and each action has a short text description, and perform and effect duration annotations as shown in the example.

- Fine-grained data is available in CSV format (separate files for seconds and minutes):

```csv
title,action,minutes
How to Ask a Customer for Identification,Remind customers of the policy,1-10mins
...,...,...
```

## Coarse-grained dataset trained models

BERT (Bidirectional Encoder Representations from Transformers) is a powerful language model developed by Google that is capable of understanding the context of words in a sentence. We have used BERT to train several models for the coarse-grained dataset, which can be accessed through the links provided. In this case, our models have been trained to predict the perform duration of an action or the effect duration of an action, based on the description of that action in text in the form of the WikiHow-style descriptions on which they were trained. 

---
[https://huggingface.co/mrfriedpotato/perform](https://huggingface.co/mrfriedpotato/perform)
- This model is trained to predict how long an action takes to perform from the textual description of the action only. For example "Heat the oven".
---
[https://huggingface.co/mrfriedpotato/perform_t](https://huggingface.co/mrfriedpotato/perform_t)
- This model is trained to predict how long an action takes to perform from the textual description of the action only. For example "How to clean the house. Take out the trash".
---
[https://huggingface.co/mrfriedpotato/effect](https://huggingface.co/mrfriedpotato/effect)
- This model is trained to predict how long an action's effects last for from a how-to-style title followed by action description, for example "Take out the trash".
---
[https://huggingface.co/mrfriedpotato/effect_t](https://huggingface.co/mrfriedpotato/effect_t)
- This model is trained to predict how long an action's effects last for from a how-to-style title followed by action description, for example "How to bake a Pizza. Heat the oven".
---

## License

The data is available under a Creative Commons Zero v1.0 Universal license, which waives copyright interest and dedicates it to the world-wide public domain.

## Acknowledgements

Our work is partially derived from information extracted from [WikiHow](https://www.wikihow.com/), which is used under the terms of the Creative Commons [Attribution-NonCommercial-ShareAlike 3.0 license](https://creativecommons.org/licenses/by-nc-sa/3.0/).

## Disclaimer

The dataset and trained machine learning models described above are provided on an "as is" basis and without warranties or guarantees of any kind.
