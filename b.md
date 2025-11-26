- MUST only continue when have 98% of certainty
- MUST ask small questions untill clarify
- MUST understand the scenario and variables
- MUST understand the desired result
- MUST deliver the result

# Modificators

- WHEN modificators are set, follow the instructions

- `--3`: 
	- MUST generate three alternative solutions
	- IF is an subagent task
		- MUST clarify if it's not clear 
	- IF the solutions are editable
		- MUST open the first two options in `windsurf`
		- WHEN one close, open the third
		- MUST follow any instruction added directly in the file
		- MUST consider the last opened window, the best option
- `-b`:
	- MUST spawn sub-agents in background
	- MUST be able to chat while the sub-agents work in background

# Prompt Enhance

- MUST adapt the customer prompt to the format below
- MUST always have # Task section
- COULD have report

~~~
# Task 

- MUST create a task for each openspec change with tasks defined
- MUST start with openspec with completed tasks
- MUST review each proposal VS implementation
- MUST deliver report at root of change - ai_review.md
- SHALL try to run reviews in parallel, if not sequentially
- MUST never stop until all reviews are done 

# Report

- Max: 100 Lines
- Order by priority

- MUST analize each one
~~~~ 

# Log experiences

- MUST log every experience per session
- MUST create a dir {timestamp}_{context} to log a markdown notes
	- MUST create notes.md