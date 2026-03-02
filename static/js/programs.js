const PROGRAM_DATA = {
    "1. Phonebook Lookup": {
        "title": '1. Phonebook Lookup',
        "level": "Phase 1: Easy (Warm-up)",
        "task": "Create a dictionary of names and numbers. Retrieve a number based on user input safely without breaking the program.",
        "skill": "Dictionary Initialization and the .get() method",
        "code": `# Initialize a dictionary with key-value pairs
phonebook = {"Alice": "555-0101", "Bob": "555-0102", "Charlie": "555-0103"}

# The name we are looking for (this could be from input())
search_name = "Bob"

# Use .get() to safely retrieve the phone number
# If "Bob" is not in the dictionary, it returns the default string
number = phonebook.get(search_name, "Name not found")

print(f"{search_name}'s number is {number}")`,
        "explanation": [
            "<code>phonebook = {...}</code>: We create a collection mapping string names (keys) to string phone numbers (values).",
            "<code>search_name = \"Bob\"</code>: We store the key we want to look up in a variable.",
            "<code>phonebook.get(...)</code>: Instead of using <code>phonebook[\"Bob\"]</code> (which crashes the program with a KeyError if Bob doesn't exist), we use the safe <code>.get()</code> method.",
            "The second argument <code>\"Name not found\"</code> is a fallback value. If the key is missing from the dictionary, it gracefully returns this fallback instead of crashing."
        ]
    },
    "2. Square Map": {
        "title": '2. Square Map',
        "level": "Phase 1: Easy (Warm-up)",
        "task": "Generate a dictionary dynamically where the keys are integers from 1 to *n*, and the values are their mathematical squares. (E.g. {2: 4, 3: 9}).",
        "skill": "For Loops and Dictionary Assignment",
        "code": `n = 5
square_dict = {}

# Iterate over a sequence of numbers from 1 up to n (inclusive)
for i in range(1, n + 1):
    # Add a new key-value pair to the dictionary
    square_dict[i] = i ** 2

print("Square Dictionary:", square_dict)`,
        "explanation": [
            "<code>square_dict = {}</code>: We start with an empty dictionary that we will populate dynamically.",
            "<code>for i in range(1, n + 1):</code>: Loop through integers starting at 1. We use <code>n + 1</code> because the range() function stops exactly one step *before* its upper limit.",
            "<code>square_dict[i] = i ** 2</code>: On each loop iteration, we create a new entry. The key is simply <code>i</code> (e.g. 1, 2, 3), and we set its corresponding value to <code>i</code> raised to the power of 2 (represented by the <code>**</code> operator)."
        ]
    },
    "3. Key Deleter": {
        "title": '3. Key Deleter',
        "level": "Phase 1: Easy (Warm-up)",
        "task": "Write a program to remove a specific item from an inventory dictionary using the `.pop()` method, isolating the removed value.",
        "skill": "Modifying Dictionaries with .pop()",
        "code": `inventory = {"apples": 10, "bananas": 5, "oranges": 15}
print("Original:", inventory)

# Remove 'bananas' by its key and capture the value it evaluated to
removed_item = inventory.pop("bananas", "Item not found")

print(f"Removed '{removed_item}' bananas.")
print("Updated inventory:", inventory)`,
        "explanation": [
            "<code>removed_item = inventory.pop(...)</code>: The <code>.pop()</code> method takes a key and completely deletes that key-value pair from the dictionary.",
            "Unlike the <code>del</code> keyword, <code>.pop()</code> *returns* the value that was deleted before wiping it from memory. Here, it returns the integer <code>5</code>, which we immediately store in the <code>removed_item</code> variable.",
            "We provide a fallback string <code>\"Item not found\"</code> as the second argument, acting as a safety net in case we try to pop a key that doesn't exist."
        ]
    },
    "4. Inventory Updater": {
        "title": '4. Inventory Updater',
        "level": "Phase 2: Medium (Logic Building)",
        "task": "Check if an item exists in a stock dictionary; if it does, update its existing price; if it doesn't, add it as an entirely new entry.",
        "skill": "Membership Operators (in) and Conditionals",
        "code": `stock = {"pen": 20, "pencil": 10, "eraser": 5}
item_to_update = "notebook"
new_price = 50

# Check if the key exists in our dictionary
if item_to_update in stock:
    print(f"Updating '{item_to_update}' price.")
    stock[item_to_update] = new_price
else:
    print(f"Adding new item: '{item_to_update}'.")
    stock[item_to_update] = new_price

print("Current Stock:", stock)`,
        "explanation": [
            "<code>if item_to_update in stock:</code>: We use the <code>in</code> membership operator. When used on a dictionary, it automatically checks if the string exists specifically in the dictionary's *keys* (not values).",
            "If it exists (True), the program flows into the <code>if</code> block and overwrites the existing value.",
            "If it does not exist (False), the program flows into the <code>else</code> block. Notice that the syntax <code>stock[item_to_update] = new_price</code> is used in both branches! That's because the assignment operator behaves contextually: it *updates* if the key exists, but *creates* a new pair if the key is missing."
        ]
    },
    "5. Dictionary Merger": {
        "title": '5. Dictionary Merger',
        "level": "Phase 2: Medium (Logic Building)",
        "task": "Take two separate dictionaries (e.g. data for two different classes) and merge them perfectly into one, elegantly handling overlapping keys.",
        "skill": "The .update() method and .copy()",
        "code": `section_A = {"Alice": 85, "Bob": 90}
section_B = {"Charlie": 78, "Bob": 92} # Note: 'Bob' exists in both subsets

# Copy section A so we don't accidentally modify the original data
merged_sections = section_A.copy()

# Add all key-value pairs from B into our new dictionary
merged_sections.update(section_B) 

# Bob's score will be 92 from section_B, because overlapping 
# keys from the inserted dictionary always overwrite older ones.
print("Merged:", merged_sections)`,
        "explanation": [
            "<code>section_A.copy()</code>: We create a brand new dictionary in memory that replicates the exact structure of <code>section_A</code>. If we didn't do this, we would be altering the original Section A dictionary data.",
            "<code>merged_sections.update(section_B)</code>: The <code>.update()</code> command takes a second dictionary and automatically loops through it, injecting every single key-value pair into the existing dictionary.",
            "Because dictionary keys must be rigidly distinct/unique, Python handles duplicates (like <code>\"Bob\"</code>) by allowing the newest data (from <code>section_B</code>) to overwrite and crush the older data."
        ]
    },
    "6. Reverse Search": {
        "title": '6. Reverse Search',
        "level": "Phase 2: Medium (Logic Building)",
        "task": "Given a specific value, find and print the corresponding 'Key' that maps to it by looping through `.items()`.",
        "skill": "Looping through dict.items() and early exit breaks",
        "code": `student_marks = {"Alice": 85, "Bob": 92, "Charlie": 78}
target_score = 92
found_student = None

# Unpack both the key and the value simultaneously during the loop
for name, mark in student_marks.items():
    if mark == target_score:
        found_student = name
        break # Exit the loop immediately since we found what we need

if found_student:
    print(f"The student with {target_score} marks is {found_student}.")
else:
    print("No student found.")`,
        "explanation": [
            "<code>student_marks.items()</code>: Normally, running a <code>for</code> loop over a dictionary only loops through its keys. Adding <code>.items()</code> provides access to both the key and value as a grouped pair on every iteration.",
            "<code>for name, mark in ...</code>: We capture the two pieces of information unpacking them into two clearly named variables to work with.",
            "<code>if mark == target_score</code>: Instead of searching by key (which dictionaries are optimized for), we do a 'reverse search' by manually testing every value against our target integer.",
            "<code>break</code>: Once our condition matches, we store the student's name and immediately escape the loop to save processing time, assuming scores are perfectly unique."
        ]
    },
    "7. Maximum Value Finder": {
        "title": '7. Maximum Value Finder',
        "level": "Phase 2: Medium (Logic Building)",
        "task": "Identify the student with the absolute highest marks by evaluating the entire dictionary sequentially.",
        "skill": "Tracking maximum values through iteration",
        "code": `student_marks = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}

highest_student = ""
max_marks = -1 # Start with an impossibly low score to ensure the first actual score crushes it

for name, marks in student_marks.items():
    # If the current student's marks are strictly greater than our current maximum...
    if marks > max_marks:
        max_marks = marks          # Update our mental 'high score'
        highest_student = name     # Remember the name that achieved it

print(f"Top ranker is {highest_student} with {max_marks} marks.")`,
        "explanation": [
            "<code>max_marks = -1</code>: We initialize a tracking variable. We intentionally set it lower than any possible actual score. This guarantees that the very first student in the loop will automatically become the 'highest' initially.",
            "<code>if marks > max_marks:</code>: During iterations, we compare the current student's score against our tracked high score.",
            "If it's higher, we completely overwrite <code>max_marks</code> with the new value, and overwrite <code>highest_student</code> with the new key. By the time the loop finishes its cycle, we are guaranteed to be holding the highest values found."
        ]
    },
    "8. Frequency Counter": {
        "title": '8. Frequency Counter',
        "level": "Phase 3: Advanced (Combining Concepts)",
        "task": "Take a string of raw text and generate a dictionary that dynamically counts exactly how many times each specific word appears.",
        "skill": "String splitting and cumulative dictionary updates",
        "code": `text = "apple banana apple orange banana apple"

# Break the long string into a list of isolated words (separated by spaces)
words = text.split() 

frequency = {}

for word in words:
    if word in frequency:
        # If the word is already a key in our dictionary, increment its count
        frequency[word] += 1
    else:
        # If it's the first time seeing this word, create a new key and set it to 1
        frequency[word] = 1

print("Word Frequencies:", frequency)`,
        "explanation": [
            "<code>words = text.split()</code>: Before we can count words, we must isolate them. <code>split()</code> converts our string into an iterable List object: <code>['apple', 'banana', ...]</code>",
            "<code>for word in words:</code>: We begin cycling through every string in our list sequentially.",
            "<code>if word in frequency:</code>: This is the core logic. We check if the dictionary already has an entry for this word. If it does, we use the <code>+= 1</code> operator to increment its existing integer value by 1.",
            "<code>else: frequency[word] = 1</code>: If the dictionary does not have an entry for this word (because it's the first time we've encountered it), we generate a brand new key-value pair, assigning it a starting value of 1."
        ]
    },
    "9. Nested Student Record": {
        "title": '9. Nested Student Record',
        "level": "Phase 3: Advanced (Combining Concepts)",
        "task": "Store complex multidimensional data (Age, Grade, City) for multiple students using dictionaries nested completely inside other dictionaries, mapping ID to Profile.",
        "skill": "Multidimensional Keys and formatting nested data",
        "code": `# The main dictionary uses Student IDs as Keys, and entire dictionaries as Values
students = {
    "S101": {"Name": "Alice", "Age": 16, "Grade": "11th", "City": "Delhi"},
    "S102": {"Name": "Bob", "Age": 17, "Grade": "12th", "City": "Mumbai"}
}

student_id = "S101"
print(f"Details for {student_id}:")

# We chain square brackets to dig deeper. 
# Step 1: Access the dictionary mapped to S101
# Step 2: Access the specific string mapped to "Name" within that nested dictionary
print("Name:", students[student_id]["Name"])
print("City:", students[student_id]["City"])`,
        "explanation": [
            "<code>students = {...}</code>: dictionaries are incredibly flexible because their values do not have to be simple integers or strings. A value can be complex data structure, including an entirely separate dictionary.",
            "<code>students[student_id]</code>: When we query the dictionary with a key like <code>\"S101\"</code>, it returns an entire dictionary object (<code>{\"Name\": \"Alice\", ...}</code>).",
            "<code>students[student_id][\"Name\"]</code>: Because the first part of the expression resolves into a dictionary, we can immediately chain a *second* set of square brackets <code>[\"Name\"]</code> to pull out a specific value from that inner sub-dictionary."
        ]
    },
    "10. Character Categorizer": {
        "title": '10. Character Categorizer',
        "level": "Phase 3: Advanced (Combining Concepts)",
        "task": "Take a raw sentence and dynamically generate a dictionary with two distinct keys: 'vowels' and 'consonants', mapping to dynamic Lists containing the categorized alphabet characters.",
        "skill": "Mapping Keys to Lists and using .append()",
        "code": `sentence = "python programming"
vowels = "aeiou"

# Initialize dictionary with keys mapped to empty List objects
categorized = {"vowels": [], "consonants": []}

for char in sentence.lower():
    if char.isalpha(): # Ensure it's a letter (ignoring spaces or punctuation)
        if char in vowels:
            # We access the list mapped to 'vowels', then call the list method .append()
            categorized["vowels"].append(char)
        else:
            # Otherwise, append it to the consonant list
            categorized["consonants"].append(char)

print("Categorized characters:", categorized)`,
        "explanation": [
            "<code>categorized = {\"vowels\": []...}</code>: Just like the previous example nested dictionaries as values, this example demonstrates using flexible List structures <code>[]</code> as values.",
            "<code>for char in sentence.lower()</code>: We normalize the sentence to completely lowercase to make our string comparisons simpler, and loop through every character (including spaces).",
            "<code>if char.isalpha()</code>: A safety check to ensure we only process letters, ignoring spaces, numbers, or periods.",
            "<code>categorized[\"vowels\"].append(char)</code>: If a letter is a vowel, we target the list sitting at the <code>\"vowels\"</code> key, and use standard List operations like <code>.append()</code> to push the string character directly into it."
        ]
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const listContainer = document.getElementById('program-list-container');
    const placeholder = document.getElementById('prog-placeholder');
    const contentArea = document.getElementById('prog-content');

    // Content nodes
    const titleNode = document.getElementById('prog-title');
    const levelNode = document.getElementById('prog-level');
    const taskNode = document.getElementById('prog-task');
    const skillNode = document.getElementById('prog-skill');
    const codeNode = document.getElementById('prog-code');
    const explNode = document.getElementById('prog-explanation');

    let activeLink = null;

    Object.keys(PROGRAM_DATA).forEach(key => {
        const prog = PROGRAM_DATA[key];

        // Create Sidebar Link
        const link = document.createElement('a');
        link.href = '#';
        link.textContent = prog.title;
        // Apply identical styling to the requested plain text Streamlit version
        link.style.cssText = `
            text-decoration: none; 
            color: #475569; 
            padding: 8px 10px; 
            border-radius: 6px;
            font-size: 0.95rem;
            transition: all 0.2s ease;
            display: block;
        `;

        link.addEventListener('mouseenter', () => {
            if (link !== activeLink) {
                link.style.color = '#4F46E5';
                link.style.backgroundColor = '#F8FAFC';
            }
        });
        link.addEventListener('mouseleave', () => {
            if (link !== activeLink) {
                link.style.color = '#475569';
                link.style.backgroundColor = 'transparent';
            }
        });

        link.addEventListener('click', (e) => {
            e.preventDefault();

            // Handle Active Styling Swap
            if (activeLink) {
                activeLink.style.color = '#475569';
                activeLink.style.fontWeight = 'normal';
                activeLink.style.backgroundColor = 'transparent';
            }
            link.style.color = '#4F46E5';
            link.style.fontWeight = '700';
            link.style.backgroundColor = '#EEF2FF';
            activeLink = link;

            // Hide Placeholder, Show Content
            placeholder.style.display = 'none';
            contentArea.style.display = 'block';

            // Inject Data
            titleNode.textContent = prog.title;
            levelNode.textContent = prog.level;

            // Use innerHTML for task/skill because they might have bold tags from python dict
            taskNode.innerHTML = prog.task;
            skillNode.innerHTML = prog.skill;

            // Code block
            codeNode.textContent = prog.code;

            // Logic breakdown (Array of strings)
            explNode.innerHTML = '';
            const ol = document.createElement('ol');
            ol.style.paddingLeft = '20px';
            ol.style.color = '#334155';
            ol.style.lineHeight = '1.6';

            prog.explanation.forEach(step => {
                const li = document.createElement('li');
                li.style.marginBottom = '10px';
                li.innerHTML = step;
                ol.appendChild(li);
            });
            explNode.appendChild(ol);
        });

        listContainer.appendChild(link);
    });
});
