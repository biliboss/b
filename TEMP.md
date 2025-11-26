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


Testing Convention: docs/TESTING.md

spec: safe-leads-journey
tests/e2e/conftest.py
tests/e2e/helpers.py
tests/e2e/test_safe_leads_user_filter_leads_and_list_saved_filters.py

- Avalie se os testes seguem as convenções
- Senti falta do teste no testcontainers postgres, e não na base de teste local - avalie e ajuste a convenção, e depois o teste
- Avalie, é preciso atualizar a proposal change,com a jornada abaixo - atualize e implementa na sequencia


#### Extraction Journey

- User submits search request with filters
- User receive leads result
- User Extract a certain amount of leads as CSV

specs-involved: safe-leads-search, safe-leads-filters, safe-leads-extraction


-b



--3


We already started the implementation, sync the tasks
app/features/safe_leads/extraction
app/features/safe_leads/extraction_service.py
app/features/safe_leads/router.py


This safe-leads-journey, shouldn't have the requirements of 2 E2E tests? We already have one of the journeys - tests/e2e/test_safe_leads_user_filter_leads_and_list_saved_filters.py


safe-leads-journey

- Apresente um resumo do que vai ser feito safe-leads-extraction, para que eu aprove e você delegue o desenvolvimento para um background agent 


- Eu quero um prompt que 
- ajuste a spec da change @search-journey-user-flow, para safe-leads-journey
- E que adicione a new change proposal to add-leads-extraction, which define the spec safe-leads-extraction. O cliente pode a partir de um filtro pertir para exportar o arquivo. Ai na lista de filtros salvos, os que foram importados poderão ser visualizados. O exportar deve gerar um csv no google cloud