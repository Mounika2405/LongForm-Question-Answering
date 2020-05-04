# LongFormQA

### Overview of the Project

The task is to generate multi-sentence/long detailed answers to questions that require reasoning rather than just facts like in Factoid QA systems. We study this problem in the aftermath of the recent paper:  ELI5 that aims to build QA systems that can generate answers even detailed enough, ideally, to explain concepts to a “five-year old”. In this project, we reproduce the baseline scores closely while operating within our resource constraints.  We go further and propose two improvements to these baselines, that tacklesome of the principle issues in this task:

**Improvement 1**: Transformer with Pointer Generator to address the factual inaccuracies and OOV mishandling issues.
**Improvement 2**: Avoiding repetitions in answers with constrained multi head attention in the transformer decoder.


More details on these improvements are present in the report. We have adapted the 
[fairseq](https://github.com/pytorch/fairseq) codebase for our project and have followed the same preprocessing steps as specified here.

Dataset Link: 
Base Paper Implementation Link: 

### Runnning Improvement 1:

### Running Improvement 2:








