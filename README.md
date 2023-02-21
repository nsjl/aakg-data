# CoTAK Dataset: **Co**mmonsense *T*emporal *A*ction *K*nowledge

A dataset resource consisting of short descriptions of action-describing sentences annotated with temporal commonsense knowledge. The dataset consists of instructions extracted from WikiHow, which are annotated with commonsense knowledge-based temporal labels indicating implicitly understood information about the actions described by the sentences, including approximately how long an action takes to perform and approximately how long its effects last for. For short duration actions labeled as taking seconds or minutes, which would be of relevance to automated task planning, e.g. in robotics applica-
tions, the dataset also provides scalar values to accurately label the temporal durations of how long actions take to perform. 

## Overview

A dataset annotating simple English-language sentences with temporal duration information, consisting of over 300K instances. 

### Coarse-grained - available under data/coarsegrained.

The action-describing sentences are annotated with:

- How long the action takes to perform or complete (which we denote \emph{perform duration}). 
- How long the duration of the action's effect last for (which we denote \emph{effect duration}).

### Fine-grained - available under data/finegrained.

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
title,description,minutes
How to Ask a Customer for Identification,Remind customers of the policy,2
...,...,...
```

## License

The data is available under a Creative Commons Zero v1.0 Universal license, which waives copyright interest and dedicates it to the world-wide public domain.
