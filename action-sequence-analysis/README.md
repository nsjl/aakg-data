# CoTAK Dataset Update: Occurrence Type Annotations

## Overview
In this update, we enhance the **Commonsense Temporal Action Knowledge (CoTAK)** dataset by introducing a new temporal attribute: **occurrence type**. This attribute classifies actions based on whether they typically occur once or are repeated over time. The goal of this addition is to improve the temporal commonsense understanding of actions, supporting better reasoning in task planning and sequence prediction.

## Occurrence Type Classification
Each action in the dataset has been categorized into one of the following:
- **Singular:** Actions that typically happen only once or rarely (e.g., "bake a cake").
- **Periodic:** Actions that typically occur regularly or often (e.g., "water the plants").
- **Unknown:** Actions that are difficult to classify due to subjectivity or ambiguity.

To generate these annotations, we used **GPT-4o** to classify sentences based on their occurrence type. The annotation quality was validated through **manual verification** on a random sample of annotations, confirming a high level of accuracy, except for highly subjective cases.

## Annotation Prompt
The following prompt was used to guide GPT-4o in classifying the sentences:

```plaintext
You are given a sentence. Classify whether the sentence describes something that a person does regularly or often, e.g. brush their teeth, walk a dog, take a shower etc. If so, answer yes, otherwise answer no.
```

### Example Classifications

```markdown
| Sentence                          | Classification |
|-----------------------------------|---------------|
| Bake a cake                       | Singular      |
| Water the plants                  | Periodic      |
| Attend a surprise party           | Singular      |
| Brush your teeth                   | Periodic      |
| Read a random book                 | Unknown      |
```

## Accessing the Data
The updated dataset is integrated with the main CoTAK dataset.
