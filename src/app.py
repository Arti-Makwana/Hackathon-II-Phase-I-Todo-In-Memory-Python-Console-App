from manager import TodoManager

def main():
    manager = TodoManager()
    print("--- Professional Agentic Todo CLI (Phase III) ---")
    
    while True:
        cmd = input("\nCommands: add, list, done, delete, search, filter, exit: ").lower().strip()
        
        if cmd == "add":
            t = input("Title: ")
            d = input("Description: ")
            p = input("Priority (Low, Medium, High) [Medium]: ").strip().capitalize() or "Medium"
            c = input("Category [General]: ").strip().capitalize() or "General"
            # NEW: Ask for Due Date
            date = input("Due Date (YYYY-MM-DD) [N/A]: ").strip() or "N/A"
            
            manager.add_task(t, d, p, c, date)
            print(f"Task saved for {date}!")
        elif cmd == "edit":
            try:
                tid = int(input("Task ID to edit: "))
                print("(Leave blank to keep current value)")
                new_title = input("New Title: ").strip()
                new_date = input("New Due Date: ").strip()
                
                if manager.edit_task(tid, title=new_title, due_date=new_date):
                    print("Task updated successfully!")
                else:
                    print("Task ID not found.")
            except ValueError:
                print("Please enter a valid number for the ID.")
            
        elif cmd == "list":
            tasks = manager.get_all_tasks()
            display_tasks(tasks, "All Tasks")

        elif cmd == "filter":
            # NEW: Filter logic
            cat = input("Enter category to view: ").strip()
            results = manager.get_tasks_by_category(cat)
            display_tasks(results, f"Category: {cat.capitalize()}")
                
        elif cmd == "search":
            query = input("Search for: ").strip()
            results = manager.search_tasks(query)
            display_tasks(results, f"Search results for '{query}'")
                
        elif cmd == "done":
            try:
                tid = int(input("Task ID to toggle: "))
                if manager.toggle_complete(tid): print("Status updated!")
                else: print("ID not found.")
            except ValueError: print("Enter a valid number.")
                
        elif cmd == "delete":
            try:
                tid = int(input("Task ID to delete: "))
                if manager.delete_task(tid): print("Task deleted!")
                else: print("ID not found.")
            except ValueError: print("Enter a valid number.")
                
        elif cmd == "exit":
            print("Goodbye!")
            break

# A helper function to keep the 'list' code clean and pretty
def display_tasks(tasks, title):
    if not tasks:
        print(f"\n--- {title}: No tasks found ---")
        return
    print(f"\n--- {title} ---")
    # Add 'Due' to the header
    print(f"{'ID':<3} | {'Stat':<4} | {'Prio':<7} | {'Cat':<10} | {'Due':<12} | {'Task'}")
    print("-" * 70)
    for t in tasks:
        status = "[X]" if t["completed"] else "[ ]"
        prio = t.get("priority", "Medium")
        cat = t.get("category", "General")
        due = t.get("due_date", "N/A")
        print(f"{t['id']:<3} | {status:<4} | {prio:<7} | {cat:<10} | {due:<12} | {t['title']}")

if __name__ == "__main__":
    main()