import streamlit as st
import time

st.set_page_config(
    page_title="AI Learning Hub: Dictionaries",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Design
st.markdown("""
<style>
    /* Main Background & Fonts */
    .stApp {
        background-color: #F8F9FA;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E9ECEF;
    }
    .css-1544g2n.e1fqcg364 {
        margin-top: -50px;
    }
    
    /* Headers */
    h1, h2, h3, h4 {
        color: #2B2D42;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    h1 { font-size: 2.5rem; }
    h2 { font-size: 1.8rem; margin-top: 1.5rem; }
    
    /* Content Cards */
    .info-box {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 24px;
        border-left: 5px solid #6366F1;
    }
    
    /* NEW Dict Visualizer Layout */
    .dict-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 20px;
        margin-bottom: 30px;
        background: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    .dict-row {
        display: flex;
        align-items: center;
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 12px 20px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .dict-row:hover {
        transform: translateX(5px);
        border-color: #6366F1;
        background-color: #F1F5F9;
    }

    .key-badge {
        background-color: #4F46E5;
        color: white;
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
        color: #94A3B8;
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
        background-color: #FFFFFF;
        color: #1E293B;
        border: 2px solid #CBD5E1;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 1rem;
    }
    
    .value-badge.scalar {
        border-color: #10B981;
        color: #047857;
        background-color: #ECFDF5;
    }
    
    /* Methods and Code */
    code {
        color: #E11D48 !important;
        background-color: #FFE4E6 !important;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 600;
    }
    .method-card {
        background-color: #F1F5F9;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 4px solid #3B82F6;
    }
    .method-name {
        font-family: monospace;
        font-weight: bold;
        color: #0F172A;
        font-size: 1.1em;
    }
    .method-desc {
        color: #475569;
        margin-top: 5px;
        font-size: 0.95em;
    }
    
    /* Custom Button */
    .stButton>button {
        background-color: #6366F1;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        transition: background-color 0.2s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #4F46E5;
        color: white;
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
        background-color: transparent;
        border: 1px solid #6366F1 !important;
        border-radius: 20px;
        font-weight: 500;
        font-size: 0.9rem;
        color: #6366F1 !important;
        transition: all 0.2s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #EEF2FF;
    }
    .stTabs [aria-selected="true"] {
        color: #FFFFFF !important;
        background-color: #6366F1 !important;
        border-color: #6366F1 !important;
        box-shadow: 0 4px 6px rgba(99, 102, 241, 0.2);
    }
    /* New Programs Module Styles */
    .white-card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        border: 1px solid #E2E8F0;
        height: 100%;
    }
    
    .program-title {
        color: #4F46E5;
        font-weight: 800;
        font-size: 2rem;
        margin-bottom: 0px;
        margin-top: -10px;
    }
    
    .program-desc {
        color: #EC4899;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 30px;
    }
    
    .library-header {
        color: #4F46E5;
        font-weight: 800;
        font-size: 1.5rem;
        margin-bottom: 25px;
    }
    
    .level-heading {
        font-size: 0.8rem;
        font-weight: bold;
        color: #1E293B;
        letter-spacing: 1px;
        margin-top: 25px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* Subtle buttons for library */
    .stButton > button.lib-btn {
        background: transparent;
        color: #475569;
        border: none;
        box-shadow: none;
        text-align: left;
        padding: 5px 0;
        font-weight: 500;
        justify-content: flex-start;
    }
    .stButton > button.lib-btn:hover {
        color: #4F46E5;
        background: transparent;
    }
    .stButton > button.lib-btn-active {
        color: #4F46E5;
        font-weight: 700;
        background: transparent;
        border: none;
        box-shadow: none;
        text-align: left;
        padding: 5px 0;
        justify-content: flex-start;
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

# Session State for Visualizer Dictionaries
if 'demo_dict_single' not in st.session_state:
    st.session_state.demo_dict_single = {"RollNo": 1, "Name": "Riya", "Marks": 95}
if 'demo_dict_multi' not in st.session_state:
    st.session_state.demo_dict_multi = {
        "Amit": [85, 90, 88],
        "Bhavya": [92, 95, 98],
        "Chirag": [78, 80, 75]
    }
if 'loop_index' not in st.session_state:
    st.session_state.loop_index = -1

# Helper function to display dictionary visually
def render_dictionary(d, is_multi=False):
    html = '<div class="dict-container">'
    if not d:
        html += '<div style="color: #64748b; font-style: italic; padding: 20px; text-align: center;">Empty Dictionary {}</div>'
    for k, v in d.items():
        key_str = f'"{k}"' if isinstance(k, str) else str(k)
        
        html += f'<div class="dict-row"><div class="key-badge">{key_str}</div><div class="mapping-arrow">→</div><div class="value-area">'
        
        # Handle multiple values (lists) vs scalar values
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
    
    # Create horizontal tabs matching the reference style
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
        # Styled Table for Properties
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
                "code": "d = {'a': 1}\nprint(d.get('b', 'Not Found'))",
                "output": "Not Found"
            },
            {
                "name": "del d[key]", 
                "desc": "Removes a specific key-value pair.",
                "code": "d = {'a': 1, 'b': 2}\ndel d['a']\nprint(d)",
                "output": "{'b': 2}"
            },
            {
                "name": "d.clear()", 
                "desc": "Removes all elements, leaving an empty dictionary.",
                "code": "d = {'a': 1, 'b': 2}\nd.clear()\nprint(d)",
                "output": "{}"
            }
        ]
        
        for method in methods_data:
            with st.expander(f"🛠️ {method['name']}"):
                st.markdown(f"**{method['desc']}**")
                col_code, col_out = st.columns(2)
                with col_code:
                    st.markdown("`Code Example:`")
                    st.code(method['code'], language="python")
                with col_out:
                    st.markdown("`Expected Output:`")
                    st.code(method['output'], language="plaintext")

# ----------------- VISUALIZER MODULE -----------------
elif page == "visualizer":
    st.title("Interactive Dictionary Visualizer")
    
    tab1, tab2 = st.tabs(["📌 Single Value per Key", "📚 Multiple Values per Key"])
    
    with tab1:
        st.markdown("""
        <p style="color: #475569; font-size: 1.1rem; margin-top: 10px;">
        <strong>Example 1:</strong> A standard dictionary mapping a unique key (String/Int) to a single scalar value. Used often for records like a student's profile.
        </p>
        """, unsafe_allow_html=True)
        
        # The Visual Representation (Single)
        render_dictionary(st.session_state.demo_dict_single, is_multi=False)
        
        st.markdown("### Operations Lab (Single Values)")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### Add / Update `emp[Key] = Value`")
            with st.container(border=True):
                new_key = st.text_input("Key (String)", placeholder="e.g. Dept", key="s_k")
                new_val = st.text_input("Value", placeholder="e.g. IT", key="s_v")
                if st.button("Set Key-Value", key="s_btn1"):
                    if new_key:
                        try:
                            parsed_val = int(new_val)
                        except:
                            try:
                                parsed_val = float(new_val)
                            except:
                                parsed_val = new_val
                        st.session_state.demo_dict_single[new_key] = parsed_val
                        st.rerun()
                    else:
                        st.warning("Please provide a Key.")
                        
        with col2:
            st.markdown("#### Delete `del emp[Key]`")
            with st.container(border=True):
                if st.session_state.demo_dict_single:
                    del_key = st.selectbox("Select Key", options=list(st.session_state.demo_dict_single.keys()), key="s_d_k")
                    if st.button("Delete Key", type="primary", key="s_btn2"):
                        del st.session_state.demo_dict_single[del_key]
                        st.rerun()
                else:
                    st.info("Dictionary is empty.")
                    
        with col3:
            st.markdown("#### Safe Fetch `emp.get(Key)`")
            with st.container(border=True):
                get_key = st.text_input("Query Key", placeholder="e.g. Salary", key="s_g_k")
                if st.button("Get Value", key="s_btn3"):
                    if get_key:
                        val = st.session_state.demo_dict_single.get(get_key, "Not Found (None)")
                        st.success(f"Result: {val}")
                    else:
                        st.warning("Enter a Key to query.")
        
        if st.button("Reset Default Single Dictionary"):
            st.session_state.demo_dict_single = {"RollNo": 1, "Name": "Riya", "Marks": 95}
            st.rerun()

    with tab2:
        st.markdown("""
        <p style="color: #475569; font-size: 1.1rem; margin-top: 10px;">
        <strong>Example 2:</strong> A complex dictionary mapping a unique key to a <strong>List</strong> of values. Used often for datasets, like mapping a student name to all of their test scores.
        </p>
        """, unsafe_allow_html=True)
        
        # The Visual Representation (Multi)
        render_dictionary(st.session_state.demo_dict_multi, is_multi=True)
        
        st.markdown("### Operations Lab (Multiple Values)")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Append Value `scores[Key].append(Val)`")
            with st.container(border=True):
                multi_key = st.selectbox("Select Student", options=list(st.session_state.demo_dict_multi.keys()) if st.session_state.demo_dict_multi else ["None"], key="m_k")
                new_score = st.number_input("New Score to Append", min_value=0, max_value=100, value=90)
                if st.button("Append Score"):
                    if multi_key != "None":
                        st.session_state.demo_dict_multi[multi_key].append(new_score)
                        st.rerun()
                    
        with col2:
            st.markdown("#### Add New Student (Key with empty list)")
            with st.container(border=True):
                new_student = st.text_input("New Student Name", placeholder="e.g. Divya")
                if st.button("Add Student"):
                    if new_student:
                        st.session_state.demo_dict_multi[new_student] = []
                        st.rerun()
                    else:
                        st.warning("Enter a name.")
                        
        if st.button("Reset Default Multi Dictionary"):
            st.session_state.demo_dict_multi = {"Amit": [85, 90, 88], "Bhavya": [92, 95, 98], "Chirag": [78, 80, 75]}
            st.rerun()


# ----------------- CODE LAB MODULE -----------------
elif page == "codelab":
    st.title("Dictionary Traversing (Loops)")
    
    st.markdown("""
    <div class="info-box">
        Instead of position indices, standard dictionary traversal iterates through the <strong>Keys</strong>. 
        You then use each key to access its corresponding value.
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
emp = {"ID": 101, "Name": "Amit", "Salary": 45000}

# Traversing through a loop
for key in emp:
    print(key, ":", emp[key])
    """, language="python")
    
    st.markdown("### Step-by-Step Loop Execution")
    
    loop_emp = {"ID": 101, "Name": "Amit", "Salary": 45000}
    keys_list = list(loop_emp.keys())
    
    col_vis, col_ctrl = st.columns([2, 1])
    
    with col_ctrl:
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("▶ Step Forward in Loop"):
            if st.session_state.loop_index < len(keys_list) - 1:
                st.session_state.loop_index += 1
            else:
                st.session_state.loop_index = -1 # Reset
            st.rerun()
            
        if st.button("🔄 Reset Loop"):
            st.session_state.loop_index = -1
            st.rerun()
            
    with col_vis:
        with st.container(border=True):
            if st.session_state.loop_index == -1:
                st.markdown("<h4 style='color: #64748b; text-align:center'>Loop not started. Click 'Step Forward'</h4>", unsafe_allow_html=True)
            else:
                current_key = keys_list[st.session_state.loop_index]
                current_val = loop_emp[current_key]
                
                st.markdown(f"**Iteration:** `{st.session_state.loop_index + 1}` of `{len(keys_list)}`")
                st.markdown(f"**Current `key` variable:** <span style='background:#F1F5F9; padding:5px; border-radius:5px; font-weight:bold; color:#E11D48'>\"{current_key}\"</span>", unsafe_allow_html=True)
                st.markdown(f"**Accessing Value `emp[key]`:** <span style='background:#F1F5F9; padding:5px; border-radius:5px; font-weight:bold; color:#0F172A'>\"{current_val}\" (or {current_val})</span>", unsafe_allow_html=True)
                
                st.markdown("---")
                st.markdown("**Console Output:**")
                st.code(f"{current_key} : {current_val}")

# ----------------- PROGRAMS MODULE -----------------
elif page == "programs":
    
    # --- Program Data Definition ---
    PROGRAM_DATA = {
        "1. Phonebook Lookup": {
            "title": '1. Phonebook Lookup',
            "level": "Phase 1: Easy (Warm-up)",
            "task": "Create a dictionary of names and numbers. Retrieve a number based on user input safely without breaking the program.",
            "skill": "Dictionary Initialization and the .get() method",
            "code": '''# Initialize a dictionary with key-value pairs
phonebook = {"Alice": "555-0101", "Bob": "555-0102", "Charlie": "555-0103"}

# The name we are looking for (this could be from input())
search_name = "Bob"

# Use .get() to safely retrieve the phone number
# If "Bob" is not in the dictionary, it returns the default string
number = phonebook.get(search_name, "Name not found")

print(f"{search_name}'s number is {number}")''',
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
            "code": '''n = 5
square_dict = {}

# Iterate over a sequence of numbers from 1 up to n (inclusive)
for i in range(1, n + 1):
    # Add a new key-value pair to the dictionary
    square_dict[i] = i ** 2

print("Square Dictionary:", square_dict)''',
            "explanation": [
                "<code>square_dict = {}</code>: We start with an empty dictionary that we will populate dynamically.",
                "<code>for i in range(1, n + 1):</code>: Loop through integers starting at 1. We use <code>n + 1</code> because the range() function stops exactly one step *before* its upper limit.",
                "<code>square_dict[i] = i ** 2</code>: On each loop iteration, we create a new entry. The key is simply <code>i</code> (e.g. 1, 2, 3), and we set its corresponding value to <code>i</code> raised to the power of 2 (represented by the <code>**</code> operator).",
            ]
        },
        "3. Key Deleter": {
            "title": '3. Key Deleter',
            "level": "Phase 1: Easy (Warm-up)",
            "task": "Write a program to remove a specific item from an inventory dictionary using the `.pop()` method, isolating the removed value.",
            "skill": "Modifying Dictionaries with .pop()",
            "code": '''inventory = {"apples": 10, "bananas": 5, "oranges": 15}
print("Original:", inventory)

# Remove 'bananas' by its key and capture the value it evaluated to
removed_item = inventory.pop("bananas", "Item not found")

print(f"Removed '{removed_item}' bananas.")
print("Updated inventory:", inventory)''',
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
            "code": '''stock = {"pen": 20, "pencil": 10, "eraser": 5}
item_to_update = "notebook"
new_price = 50

# Check if the key exists in our dictionary
if item_to_update in stock:
    print(f"Updating '{item_to_update}' price.")
    stock[item_to_update] = new_price
else:
    print(f"Adding new item: '{item_to_update}'.")
    stock[item_to_update] = new_price

print("Current Stock:", stock)''',
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
            "code": '''section_A = {"Alice": 85, "Bob": 90}
section_B = {"Charlie": 78, "Bob": 92} # Note: 'Bob' exists in both subsets

# Copy section A so we don't accidentally modify the original data
merged_sections = section_A.copy()

# Add all key-value pairs from B into our new dictionary
merged_sections.update(section_B) 

# Bob's score will be 92 from section_B, because overlapping 
# keys from the inserted dictionary always overwrite older ones.
print("Merged:", merged_sections)''',
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
            "code": '''student_marks = {"Alice": 85, "Bob": 92, "Charlie": 78}
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
    print("No student found.")''',
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
            "code": '''student_marks = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}

highest_student = ""
max_marks = -1 # Start with an impossibly low score to ensure the first actual score crushes it

for name, marks in student_marks.items():
    # If the current student's marks are strictly greater than our current maximum...
    if marks > max_marks:
        max_marks = marks          # Update our mental 'high score'
        highest_student = name     # Remember the name that achieved it

print(f"Top ranker is {highest_student} with {max_marks} marks.")''',
            "explanation": [
                "<code>max_marks = -1</code>: We initialize a tracking variable. We intentionally set it lower than any possible actual score. This guarantees that the very first student in the loop will automatically become the 'highest' initially.",
                "<code>if marks > max_marks:</code>: During iterations, we compare the current student's score against our tracked high score.",
                "If it's higher, we completely overwrite <code>max_marks</code> with the new value, and overwrite <code>highest_student</code> with the new key. By the time the loop finishes its cycle, we are guaranteed to be holding the highest values found.",
            ]
        },
        "8. Frequency Counter": {
            "title": '8. Frequency Counter',
            "level": "Phase 3: Advanced (Combining Concepts)",
            "task": "Take a string of raw text and generate a dictionary that dynamically counts exactly how many times each specific word appears.",
            "skill": "String splitting and cumulative dictionary updates",
            "code": '''text = "apple banana apple orange banana apple"

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

print("Word Frequencies:", frequency)''',
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
            "code": '''# The main dictionary uses Student IDs as Keys, and entire dictionaries as Values
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
print("City:", students[student_id]["City"])''',
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
            "code": '''sentence = "python programming"
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

print("Categorized characters:", categorized)''',
            "explanation": [
                "<code>categorized = {\"vowels\": []...}</code>: Just like the previous example nested dictionaries as values, this example demonstrates using flexible List structures <code>[]</code> as values.",
                "<code>for char in sentence.lower()</code>: We normalize the sentence to completely lowercase to make our string comparisons simpler, and loop through every character (including spaces).",
                "<code>if char.isalpha()</code>: A safety check to ensure we only process letters, ignoring spaces, numbers, or periods.",
                "<code>categorized[\"vowels\"].append(char)</code>: If a letter is a vowel, we target the list sitting at the <code>\"vowels\"</code> key, and use standard List operations like <code>.append()</code> to push the string character directly into it."
            ]
        }
    }

    # Initialize session state for tracking selected program
    st.session_state.setdefault("active_program", "1. Phonebook Lookup")
    
    # --- Two-Column Layout ---
    col_nav, col_content = st.columns([1, 2.8])
    
    with col_nav:
        # Wrap library in white card
        st.markdown("<div class='white-card'>", unsafe_allow_html=True)
        st.markdown("<div class='library-header'>Program Library</div>", unsafe_allow_html=True)
        
        # Categorize keys
        level1_keys = [k for k in PROGRAM_DATA.keys() if "Phase 1" in PROGRAM_DATA[k]['level']]
        level2_keys = [k for k in PROGRAM_DATA.keys() if "Phase 2" in PROGRAM_DATA[k]['level']]
        level3_keys = [k for k in PROGRAM_DATA.keys() if "Phase 3" in PROGRAM_DATA[k]['level']]
        
        # Helper to render styled menu
        def render_menu(title, keys):
            st.markdown(f"<div class='level-heading'>LEVEL {title}</div>", unsafe_allow_html=True)
            for i, key in enumerate(keys):
                # Clean up string for the menu, removing the 'Phase X: ' prefix if present
                clean_name = key
                if "Phonebook" in key: clean_name = "1. Phonebook Lookup"
                if "Square" in key: clean_name = "2. Square Map"
                if "Deleter" in key: clean_name = "3. Key Deleter"
                if "Updater" in key: clean_name = "4. Inventory Updater"
                if "Merger" in key: clean_name = "5. Dictionary Merger"
                if "Reverse" in key: clean_name = "6. Reverse Search"
                if "Maximum" in key: clean_name = "7. Maximum Value Finder"
                if "Frequency" in key: clean_name = "8. Frequency Counter"
                if "Nested" in key: clean_name = "9. Nested Student Record"
                if "Categorizer" in key: clean_name = "10. Character Categorizer"

                # We use use_container_width and custom classes to restyle standard buttons
                if st.session_state.active_program == key:
                    st.button(f"{clean_name}", key=f"btn_{key}", use_container_width=True, type="primary")
                else:
                    if st.button(f"{clean_name}", key=f"btn_{key}", use_container_width=True, type="secondary"):
                        st.session_state.active_program = key
                        st.rerun()
        
        # Note: We inject CSS targets to match the plain text link style requested
        st.markdown("""
        <style>
        div[data-testid="column"]:nth-of-type(1) div[data-testid="stButton"] > button {
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            justify-content: flex-start !important;
            padding: 5px 0 !important;
            text-decoration: none !important;
            border-radius: 0 !important;
        }
        
        div[data-testid="column"]:nth-of-type(1) div[data-testid="stButton"] > button[kind="primary"] {
            color: #4F46E5 !important; 
            font-weight: 700 !important; 
        }
        div[data-testid="column"]:nth-of-type(1) div[data-testid="stButton"] > button[kind="primary"]:hover { 
            color: #312E81 !important; 
            background-color: transparent !important;
        }
        
        div[data-testid="column"]:nth-of-type(1) div[data-testid="stButton"] > button[kind="secondary"] {
            color: #475569 !important; 
            font-weight: normal !important; 
            font-size: 0.95rem !important;
        }
        div[data-testid="column"]:nth-of-type(1) div[data-testid="stButton"] > button[kind="secondary"]:hover { 
            color: #4F46E5 !important; 
            background-color: transparent !important;
        }
        </style>
        """, unsafe_allow_html=True)

        render_menu("1: BASIC", level1_keys)
        render_menu("2: MEDIUM", level2_keys)
        render_menu("3: ADVANCED", level3_keys)
        
        st.markdown("</div>", unsafe_allow_html=True) # End white card

    with col_content:
        # Retrieve the currently active program's data
        data = PROGRAM_DATA[st.session_state.active_program]
        
        st.markdown("<div class='white-card'>", unsafe_allow_html=True)
        
        st.markdown(f"<div class='program-title'>{data['title']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='program-desc'>{data['level']}</div>", unsafe_allow_html=True)
        
        # Step 1: The Task Definition Block
        st.markdown(f"""
        <div style="background-color: #f8fafc; border-left: 4px solid #EC4899; padding: 20px; border-radius: 8px; margin-bottom: 30px;">
            <p style="margin-bottom: 8px; font-weight: 700; color: #1E293B;">📋 The Task</p>
            <p style="font-size: 1.05rem; color: #334155;">{data['task']}</p>
            <p style="font-size: 0.85rem; color: #64748b; margin-top: 15px; margin-bottom: 0;"><strong>Target Skill:</strong> {data['skill']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Step 2: The Code Block (mimicking a terminal)
        st.markdown("<p style='font-size: 1.15rem; font-weight: 800; color: #1E293B; margin-bottom: 15px;'>🐍 Python Solution</p>", unsafe_allow_html=True)
        
        # Streamlit standard code block with terminal aesthetic wrapper
        st.markdown("""
        <div style="background-color: #1a1b26; border-radius: 10px 10px 0 0; padding: 10px 15px; display: flex; gap: 8px;">
            <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #ff5f56;"></div>
            <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #ffbd2e;"></div>
            <div style="width: 12px; height: 12px; border-radius: 50%; background-color: #27c93f;"></div>
        </div>
        """, unsafe_allow_html=True)
        # Margin tweak to attach code seamlessly to the terminal header
        st.markdown("<div style='margin-top: -16px;'>", unsafe_allow_html=True)
        st.code(data['code'], language="python")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Step 3: What is happening here? (The line-by-line explanation)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background-color: #FFFFFF; border: 1px solid #f1f5f9; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); padding: 25px; border-radius: 12px; margin-bottom: 20px;">
            <p style='font-size: 1.15rem; font-weight: 800; color: #1E293B; margin-bottom: 15px;'>🧠 What is happening here?</p>
            <ol style='color: #475569; font-size: 1.05rem; line-height: 1.8; padding-left: 20px;'>
        """, unsafe_allow_html=True)
        
        exp_list_html = ""
        for exp in data['explanation']:
            exp_list_html += f"<li style='margin-bottom: 12px;'>{exp}</li>"
            
        st.markdown(exp_list_html + "</ol></div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True) # End white card
