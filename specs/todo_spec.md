# Phase 1: In-Memory Todo App
Build a console app with these features:
1. Add Task (Title, Description)
2. List all Tasks (Show ID and Status)
3. Mark Task as Complete (by ID)
4. Delete Task (by ID)

Storage: Store tasks in a Python List (no database yet).
Status: Phase 1 Basic Logic Complete - [2026-01-06]
## Phase 2: JSON Persistence
- Requirement: Tasks must be saved to a `tasks.json` file automatically.
- Requirement: When the app starts, it must load existing tasks from the file.
- Requirement: If the file doesn't exist, start with an empty list.
## Phase 3: Advanced Task Metadata
- **Priority**: Every task must have a priority level (Low, Medium, High).
- **Defaulting**: If no priority is given, default to "Medium".
- **Visuals**: Display the priority in the list view (e.g., [H], [M], [L]).
- **Validation**: Ensure the user can only enter valid priority levels.
## Phase 4: Search Functionality
- **Requirement**: User can search for tasks by a keyword.
- **Scope**: The search should look for the keyword within task titles.
- **Display**: Show all matching tasks in the same table format as the list view.
## Phase 4: Search & Discovery
- **Keyword Search**: User can find tasks by searching titles or descriptions.
- **Filter by Priority**: User can view only tasks of a specific priority (e.g., only "High").
- **Case-Insensitivity**: Searching "MILK" should find "milk".