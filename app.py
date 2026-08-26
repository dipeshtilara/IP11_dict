import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="AI Learning Hub: Python Dictionaries",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Design & Robust Theme Handling (Light & Dark Mode safe)
st.markdown("""
<style>
    /* Hide Streamlit default top bar and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stHeader"] {display: none;}
    
    /* Main Background & Fonts */
    .stApp {
        background-color: #F8F9FA !important;
        color: #2B2D42 !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Force all text in the main content area to be dark and readable */
    .stApp p, .stApp li, .stApp label, .stApp span, .stApp div, .stApp blockquote, .stApp td, .stApp th {
        color: #2B2D42 !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E9ECEF;
    }
    
    /* Force sidebar text to be dark and readable */
    section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p {
        color: #2B2D42 !important;
    }
    
    .css-1544g2n.e1fqcg364 {
        margin-top: -50px;
    }
    
    /* Headers styling */
    h1, h2, h3, h4, h5, h6 {
        color: #2B2D42 !important;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    h1 { font-size: 2.5rem; }
    h2 { font-size: 1.8rem; margin-top: 1.5rem; }
    
    /* Content Cards */
    .info-box {
        background-color: #FFFFFF !important;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 24px;
        border-left: 5px solid #6366F1;
    }
    .info-box h3, .info-box p {
        color: #2B2D42 !important;
    }
    
    /* NEW Dict Visualizer Layout */
    .dict-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 20px;
        margin-bottom: 30px;
        background: #FFFFFF !important;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    .dict-row {
        display: flex;
        align-items: center;
        background-color: #F8FAFC !important;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 12px 20px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .dict-row:hover {
        transform: translateX(5px);
        border-color: #6366F1;
        background-color: #F1F5F9 !important;
    }

    .key-badge {
        background-color: #4F46E5 !important;
        color: white !important;
        padding: 6px 14px;
        border-radius: 6px;
        font-weight: 600;
        font-family: monospace;
        font-size: 1rem;
        min-width: 120px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(79, 70, 229, 0.2);
    }
    
    .mapping-arrow {
        color: #94A3B8 !important;
        font-size: 1.5rem;
        margin: 0 20px;
        font-weight: bold;
    }
    
    .value-area {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        flex: 1;
    }
    
    .value-badge {
        background-color: #FFFFFF !important;
        color: #1E293B !important;
        border: 2px solid #CBD5E1;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 1rem;
    }
    
    .value-badge.scalar {
        border-color: #10B981;
        color: #047857 !important;
        background-color: #ECFDF5 !important;
    }
    
    /* Methods and Code styling */
    code {
        color: #E11D48 !important;
        background-color: #FFE4E6 !important;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 600;
    }
    .method-card {
        background-color: #F1F5F9 !important;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 4px solid #3B82F6;
    }
    .method-name {
        font-family: monospace;
        font-weight: bold;
        color: #0F172A !important;
        font-size: 1.1em;
    }
    .method-desc {
        color: #475569 !important;
        margin-top: 5px;
        font-size: 0.95em;
    }
    
    /* Custom Tabs - Pill Style */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        border-bottom: none !important;
        margin-bottom: 25px;
        flex-wrap: wrap;
    }
    .stTabs [data-baseweb="tab"] {
        height: auto;
        padding: 8px 24px;
        background-color: transparent !important;
        border: 1px solid #6366F1 !important;
        border-radius: 20px;
        font-weight: 500;
        font-size: 0.9rem;
        transition: all 0.2s ease;
    }
    .stTabs [data-baseweb="tab"] div, .stTabs [data-baseweb="tab"] span {
        color: #6366F1 !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #EEF2FF !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #6366F1 !important;
        border-color: #6366F1 !important;
        box-shadow: 0 4px 6px rgba(99, 102, 241, 0.2);
    }
    .stTabs [aria-selected="true"] div, .stTabs [aria-selected="true"] span {
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

# Main Navigation
st.sidebar.markdown("<h2 style='text-align: center; color: #6366F1; margin-bottom: 2rem;'>IP Dict XI</h2>", unsafe_allow_html=True)

nav_options = {
    "📚 Theory": "theory",
    "⚡ Visualizer": "visualizer",
    "💻 Code Lab": "codelab",
    "📝 Programs": "programs"
}
selected_page = st.sidebar.radio("Navigation", list(nav_options.keys()), label_visibility="collapsed")
page = nav_options[selected_page]

# Helper function to display dictionary visually
def render_dictionary(d, is_multi=False):
    html = '<div class="dict-container">'
    if not d:
        html += '<div style="color: #64748b; font-style: italic; padding: 20px; text-align: center;">Empty Dictionary {}</div>'
    for k, v in d.items():
        key_str = f'"{k}"' if isinstance(k, str) else str(k)
        html += f'<div class="dict-row"><div class="key-badge">{key_str}</div><div class="mapping-arrow">→</div><div class="value-area">'
        if is_multi and isinstance(v, list):
            if not v:
                 html += '<div class="value-badge scalar" style="color:#94A3B8; border-color:#CBD5E1; background:#F8FAFC;">Empty List []</div>'
            for item in v:
                item_str = f'"{item}"' if isinstance(item, str) else str(item)
                html += f'<div class="value-badge">{item_str}</div>'
        else:
            val_str = f'"{v}"' if isinstance(v, str) else str(v)
            html += f'<div class="value-badge scalar">{val_str}</div>'
        html += '</div></div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

# ----------------- THEORY MODULE -----------------
if page == "theory":
    st.title("Python Dictionaries (Unit 2)")
    tab_concepts, tab_props, tab_methods = st.tabs(["💡 Concepts", "⚙️ Properties", "🛠️ Methods"])
    
    with tab_concepts:
        st.markdown("""
        <div class="info-box">
            <h3>1. Conceptual Framework</h3>
            <p><strong>Definition:</strong> A dictionary is an <em>unordered</em>, <em>mutable</em>, and <em>indexed by keys</em> collection. Unlike lists, which use positional indices (0, 1, 2...), dictionaries use <strong>Key-Value pairs</strong>.</p>
            <p><strong>Mapping:</strong> It is often called a "Mapping" or "Associative Array" because it maps a unique Key to a specific Value.</p>
            <p><strong>Syntax:</strong> Defined using curly braces <code>{}</code>. Items are separated by commas, and keys are separated from values by colons <code>:</code>.</p>
        </div>
        """, unsafe_allow_html=True)
        st.code('my_dict = {"RollNo": 1, "Name": "Riya", "Marks": 95}', language="python")

    with tab_props:
        st.markdown('### Properties of Dictionaries')
        st.markdown("""
        | Feature | Rule |
        | :--- | :--- |
        | **Keys** | Must be **Unique** and **Immutable** (e.g., Strings, Numbers, or Tuples). |
        | **Values** | Can be of **any data type** and can be **Duplicated**. |
        | **Ordering** | **Unordered** (Though modern Python ≥3.7 maintains insertion order, they are logically accessed by key, not position). |
        | **Mutability** | The dictionary is **mutable**; you can add, remove, or change items after creation. |
        """)

    with tab_methods:
        st.markdown('### Essential Methods & Functions')
        methods_data = [
            {
                "name": "dict()", 
                "desc": "Constructor to create a new dictionary.",
                "code": "d = dict(name='Amit', age=16)\nprint(d)",
                "output": "{'name': 'Amit', 'age': 16}"
            },
            {
                "name": "len(d)", 
                "desc": "Returns the number of items in the dictionary.",
                "code": "d = {'a': 1, 'b': 2, 'c': 3}\nprint(len(d))",
                "output": "3"
            },
            {
                "name": "d.keys()", 
                "desc": "Returns a view object of all keys.",
                "code": "d = {'a': 1, 'b': 2}\nprint(list(d.keys()))",
                "output": "['a', 'b']"
            },
            {
                "name": "d.values()", 
                "desc": "Returns a view object of all values.",
                "code": "d = {'a': 1, 'b': 2}\nprint(list(d.values()))",
                "output": "[1, 2]"
            },
            {
                "name": "d.items()", 
                "desc": "Returns a view of (key, value) tuples.",
                "code": "d = {'a': 1, 'b': 2}\nprint(list(d.items()))",
                "output": "[('a', 1), ('b', 2)]"
            },
            {
                "name": "d.update(d2)", 
                "desc": "Merges dictionary d2 into d. Overwrites existing keys.",
                "code": "d = {'a': 1}\nd2 = {'b': 2, 'a': 3}\nd.update(d2)\nprint(d)",
                "output": "{'a': 3, 'b': 2}"
            },
            {
                "name": "d.get(key, default)", 
                "desc": "Safely fetches a value. Returns default if not found.",
                "code": "d = {'a': 1}\nprint(d.get('b', 0))",
                "output": "0"
            }
        ]
        
        for m in methods_data:
            st.markdown(f"""
            <div class="method-card">
                <span class="method-name">{m['name']}</span>
                <p class="method-desc">{m['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            with st.expander("Show Code Example"):
                st.code(m['code'], language="python")
                st.markdown(f"**Output:** `{m['output']}`")

# ----------------- VISUALIZER MODULE -----------------
elif page == "visualizer":
    # Embed the main dictionary operations visualizer (index.html)
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html_code = f.read()
        components.html(html_code, height=950, scrolling=True)
    else:
        st.error("Visualizer file 'index.html' not found!")

# ----------------- CODE LAB MODULE (Dictionary Only) -----------------
elif page == "codelab":
    st.title("💻 Python Dictionary Code Lab")
    st.subheader("Dictionary Loops & Traversal Stepper")
    
    st.markdown("""
    Instead of indices, standard dictionary traversal iterates through the **keys**. 
    You then access each corresponding value using `D[key]`.
    """)
    
    # Initialize variables for loop stepper in session_state
    emp_data = {"ID": 101, "Name": "Amit", "Salary": 45000}
    keys_list = list(emp_data.keys())
    
    if "loop_idx" not in st.session_state:
        st.session_state.loop_idx = -1
        st.session_state.stdout_log = []
        
    col_code, col_hud = st.columns([3, 2])
    
    with col_code:
        st.markdown("### Python Traversing Loop")
        
        # Displaying pseudo-code block with highlight
        loop_idx = st.session_state.loop_idx
        lines = [
            'emp = {"ID": 101, "Name": "Amit", "Salary": 45000}',
            'for key in emp:',
            '    print(key, "->", emp[key])'
        ]
        
        html_code = '<div style="font-family: monospace; background: #07080e; color: #cdd6f4; padding: 20px; border-radius: 12px; font-size: 14px; line-height: 1.8;">'
        for i, line in enumerate(lines):
            active = False
            if loop_idx == -1 and i == 0:
                active = True
            elif loop_idx >= 0 and loop_idx < len(keys_list) and i == 1:
                active = True
            elif loop_idx >= 0 and loop_idx < len(keys_list) and i == 2:
                active = True
                
            border = "border-left: 4px solid #6366F1; background: rgba(99,102,241,0.15);" if active else "border-left: 4px solid transparent;"
            html_code += f'<div style="padding: 2px 10px; margin-bottom: 2px; {border}">{line}</div>'
        html_code += '</div>'
        st.markdown(html_code, unsafe_allow_html=True)
        
        # Action controls
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("▶ Step Forward", use_container_width=True):
                if st.session_state.loop_idx < len(keys_list) - 1:
                    st.session_state.loop_idx += 1
                    cur_key = keys_list[st.session_state.loop_idx]
                    cur_val = emp_data[cur_key]
                    st.session_state.stdout_log.append(f"{cur_key} -> {cur_val}")
                else:
                    st.session_state.loop_idx = len(keys_list) # End state
        with col_btn2:
            if st.button("⟲ Reset Loop", use_container_width=True):
                st.session_state.loop_idx = -1
                st.session_state.stdout_log = []
                
    with col_hud:
        st.markdown("### Internal Loop Monitor")
        
        # Render the loop variables
        if st.session_state.loop_idx >= 0 and st.session_state.loop_idx < len(keys_list):
            active_key = keys_list[st.session_state.loop_idx]
            active_val = emp_data[active_key]
            
            st.markdown(f"""
            <div style="background: #FFFFFF; padding: 15px; border-radius: 12px; border: 1px solid #E2E8F0; margin-bottom: 15px;">
                <div style="font-size: 10px; font-weight: bold; color: #6366F1; text-transform: uppercase;">Current key binding</div>
                <div style="font-size: 24px; font-weight: 800; color: #EC4899; font-family: monospace;">"{active_key}"</div>
                <div style="font-size: 10px; font-weight: bold; color: #6366F1; text-transform: uppercase; margin-top: 10px;">Evaluation (emp[key])</div>
                <div style="font-size: 24px; font-weight: 800; color: #10B981; font-family: monospace;">{repr(active_val)}</div>
            </div>
            """, unsafe_allow_html=True)
        elif st.session_state.loop_idx >= len(keys_list):
            st.markdown("""
            <div style="background: rgba(16,185,129,0.1); border: 1px solid #10B981; padding: 25px; border-radius: 12px; text-align: center; color: #047857; font-weight: bold;">
                🎉 Loop Finished Successfully!
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background: #F1F5F9; border: 1px dashed #CBD5E1; padding: 25px; border-radius: 12px; text-align: center; color: #64748b; font-style: italic;">
                Loop not started. Click "Step Forward"
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### stdout Terminal")
        terminal_output = "\n".join(st.session_state.stdout_log) if st.session_state.stdout_log else "# Standard output is empty"
        st.markdown(f"""
        <div style="background-color: #030408; color: #10B981; padding: 12px; border-radius: 12px; font-family: monospace; font-size: 12px; min-height: 80px; whitespace: pre-wrap;">{terminal_output}</div>
        """, unsafe_allow_html=True)

    # Active Mapping Highlight
    st.markdown("---")
    st.markdown("### Dictionary Object in Memory")
    
    html = '<div class="dict-container">'
    for k, v in emp_data.items():
        is_pointer = (st.session_state.loop_idx >= 0 and st.session_state.loop_idx < len(keys_list) and keys_list[st.session_state.loop_idx] == k)
        row_bg = "background-color: rgba(99, 102, 241, 0.1) !important; border-color: #6366F1 !important;" if is_pointer else ""
        badge_bg = "background-color: #EC4899 !important; transform: scale(1.05);" if is_pointer else ""
        arrow_color = "color: #EC4899 !important;" if is_pointer else ""
        
        html += f'<div class="dict-row" style="{row_bg}">'
        html += f'<div class="key-badge" style="{badge_bg}">"{k}"</div>'
        html += f'<div class="mapping-arrow" style="{arrow_color}">→</div>'
        html += f'<div class="value-area"><div class="value-badge scalar">{v}</div></div>'
        html += '</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

# ----------------- PROGRAMS MODULE (Dictionary Only) -----------------
elif page == "programs":
    st.title("📝 CBSE Class XI Dictionary Programs")
    st.subheader("10 Key Dictionary Programs with Explanations & Output Screens")
    
    programs_data = {
        "1. Phonebook Lookup": {
            "title": "1. Phonebook Lookup",
            "level": "Beginner (Warm-up)",
            "task": "Create a dictionary of names and numbers. Retrieve a number based on search input safely without breaking the program.",
            "skill": "Dictionary Initialization and the .get() method",
            "code": """# Initialize a dictionary with key-value pairs
phonebook = {"Alice": "555-0101", "Bob": "555-0102", "Charlie": "555-0103"}

# The name we are looking for
search_name = "Bob"

# Use .get() to safely retrieve the phone number
number = phonebook.get(search_name, "Name not found")

print(f"{search_name}'s number is {number}")""",
            "explanation": [
                "phonebook = {...}: Create a dictionary mapping names to phone numbers.",
                "phonebook.get(...): Instead of phonebook['Bob'] (which raises KeyError if missing), we use .get() which returns fallback string if key is absent."
            ],
            "output": "Bob's number is 555-0102"
        },
        "2. Square Map": {
            "title": "2. Square Map",
            "level": "Beginner (Warm-up)",
            "task": "Generate a dictionary dynamically where the keys are integers from 1 to n, and the values are their squares.",
            "skill": "For Loops and Dictionary Assignment",
            "code": """n = 5
square_dict = {}

# Iterate from 1 up to n (inclusive)
for i in range(1, n + 1):
    # Add a new key-value pair
    square_dict[i] = i ** 2

print("Square Dictionary:", square_dict)""",
            "explanation": [
                "square_dict = {}: Start with an empty dictionary.",
                "for i in range(1, n + 1): Loop through integers starting at 1 up to n.",
                "square_dict[i] = i ** 2: Assign the square of i to the key i dynamically."
            ],
            "output": "Square Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"
        },
        "3. Key Deleter": {
            "title": "3. Key Deleter",
            "level": "Beginner (Warm-up)",
            "task": "Remove bananas from an inventory dictionary using pop() and capture the value it evaluated to.",
            "skill": "Modifying Dictionaries with .pop()",
            "code": """inventory = {"apples": 10, "bananas": 5, "oranges": 15}

# Remove 'bananas' and capture its value
removed_item = inventory.pop("bananas", "Item not found")

print(f"Removed bananas value: {removed_item}")
print("Updated inventory:", inventory)""",
            "explanation": [
                "inventory.pop('bananas', ...): Deletes key 'bananas' and returns value 5.",
                "If the key is missing, returns the default fallback value 'Item not found'."
            ],
            "output": "Removed bananas value: 5\nUpdated inventory: {'apples': 10, 'oranges': 15}"
        },
        "4. Inventory Price Check": {
            "title": "4. Inventory Price Check",
            "level": "Intermediate (Logic Building)",
            "task": "Check if an item exists; if yes, update its price; if no, add it as a new entry.",
            "skill": "Membership Operators (in) and Conditionals",
            "code": """stock = {"pen": 20, "pencil": 10, "eraser": 5}
item = "notebook"
new_price = 50

if item in stock:
    print(f"Updating '{item}' price.")
    stock[item] = new_price
else:
    print(f"Adding new item '{item}'.")
    stock[item] = new_price

print("Current Stock:", stock)""",
            "explanation": [
                "if item in stock: Checks if 'notebook' exists in the keys of stock.",
                "stock[item] = new_price: Overwrites the value if it exists, or inserts a new key-value pair if it doesn't."
            ],
            "output": "Adding new item 'notebook'.\nCurrent Stock: {'pen': 20, 'pencil': 10, 'eraser': 5, 'notebook': 50}"
        },
        "5. Dictionary Merger": {
            "title": "5. Dictionary Merger",
            "level": "Intermediate (Logic Building)",
            "task": "Merge two dictionaries, handling overlapping keys.",
            "skill": "The .update() method and .copy()",
            "code": """section_A = {"Alice": 85, "Bob": 90}
section_B = {"Charlie": 78, "Bob": 92}

# Copy section_A and update with section_B
merged = section_A.copy()
merged.update(section_B)

print("Merged Class Data:", merged)""",
            "explanation": [
                "merged = section_A.copy(): Copies section A to prevent mutating the original data.",
                "merged.update(section_B): Merges B's keys into the copy. Overlapping key 'Bob' is updated to B's value (92)."
            ],
            "output": "Merged Class Data: {'Alice': 85, 'Bob': 92, 'Charlie': 78}"
        },
        "6. Grade Tracker": {
            "title": "6. Grade Tracker",
            "level": "Intermediate (Logic Building)",
            "task": "Calculate the average marks of students stored in a dictionary.",
            "skill": "Reduction Operations (sum, len) on Values",
            "code": """marks = {"Amit": 85, "Bhavya": 92, "Chirag": 78}

total = sum(marks.values())
average = total / len(marks)

print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")""",
            "explanation": [
                "marks.values(): Returns a view of all values (marks) in the dictionary.",
                "sum(marks.values()): Sums all marks together.",
                "len(marks): Returns the number of items (keys) in the dictionary."
            ],
            "output": "Total Marks: 255\nAverage Marks: 85.00"
        },
        "7. Character Frequency Counter": {
            "title": "7. Character Frequency Counter",
            "level": "Advanced (Exam Focus)",
            "task": "Count the frequency of each character in a given string using a dictionary.",
            "skill": "Loops, Conditionals, and Dictionary Accumulators",
            "code": """text = "success"
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequencies:", freq)""",
            "explanation": [
                "for char in text: Iterates over each character in the string 'success'.",
                "if char in freq: If character key exists, increment its frequency value.",
                "else: If it's a new character, initialize its key in the dictionary with value 1."
            ],
            "output": "Character Frequencies: {'s': 3, 'u': 1, 'c': 2, 'e': 1}"
        },
        "8. Nested Student Database": {
            "title": "8. Nested Student Database",
            "level": "Advanced (Exam Focus)",
            "task": "Store and access student records where each student has their own dictionary of subject scores.",
            "skill": "Nested Dictionary Access",
            "code": """students = {
    "Roll_01": {"name": "Amit", "IP": 95, "Maths": 90},
    "Roll_02": {"name": "Bhavya", "IP": 98, "Maths": 95}
}

for roll, details in students.items():
    print(f"Roll No: {roll}")
    print(f"  Name: {details['name']}")
    print(f"  IP Score: {details['IP']}")""",
            "explanation": [
                "students is a dictionary where each value is another dictionary containing student attributes.",
                "details['name'] retrieves the value 'name' from the inner dictionary."
            ],
            "output": "Roll No: Roll_01\n  Name: Amit\n  IP Score: 95\nRoll No: Roll_02\n  Name: Bhavya\n  IP Score: 98"
        },
        "9. Value Finder": {
            "title": "9. Value Finder",
            "level": "Advanced (Exam Focus)",
            "task": "Find the student with the highest marks in a dictionary.",
            "skill": "Iterating and Tracking Extremum Values",
            "code": """marks = {"Amit": 85, "Bhavya": 98, "Chirag": 90}

max_student = ""
max_score = -1

for student, score in marks.items():
    if score > max_score:
        max_score = score
        max_student = student

print(f"Topper: {max_student} with {max_score} marks")""",
            "explanation": [
                "Iterates through the keys and values of the dictionary using marks.items().",
                "Compares each score against max_score, updating the topper's name and score whenever a higher value is found."
            ],
            "output": "Topper: Bhavya with 98 marks"
        },
        "10. Dictionary Key Sorter": {
            "title": "10. Dictionary Key Sorter",
            "level": "Advanced (Exam Focus)",
            "task": "Sort a dictionary by its keys alphabetically and print the sorted dictionary.",
            "skill": "Using sorted() on Keys",
            "code": """d = {"banana": 3, "apple": 5, "cherry": 2}

sorted_keys = sorted(d.keys())
sorted_dict = {}

for key in sorted_keys:
    sorted_dict[key] = d[key]

print("Sorted Dictionary:", sorted_dict)""",
            "explanation": [
                "sorted(d.keys()): Extracts all keys and returns them in a sorted list: ['apple', 'banana', 'cherry'].",
                "We iterate through this sorted list of keys and construct a new dictionary with elements in sorted order."
            ],
            "output": "Sorted Dictionary: {'apple': 5, 'banana': 3, 'cherry': 2}"
        }
    }
    
    # Left/Right Sidebar selection layout for programs
    selected_prog = st.sidebar.selectbox("Choose a program:", list(programs_data.keys()), key="prog_selector")
    prog = programs_data[selected_prog]
    
    st.markdown(f"## {prog['title']}")
    st.caption(f"Difficulty Level: **{prog['level']}** | Focus Skill: *{prog['skill']}*")
    
    st.markdown("### 📋 Program Objective / Task")
    st.write(prog["task"])
    
    st.markdown("### 🐍 Python Source Code")
    st.code(prog["code"], language="python")
    
    st.markdown("### 💡 Line-by-Line Explanation")
    for step in prog["explanation"]:
        st.markdown(f"- {step}", unsafe_allow_html=True)
        
    st.markdown("### 🖥️ Expected Output Screen")
    st.markdown(f"""
    <div style="background-color: #030408; color: #10B981; padding: 15px; border-radius: 12px; font-family: monospace; font-size: 13px; whitespace: pre-wrap;">{prog["output"]}</div>
    """, unsafe_allow_html=True)
