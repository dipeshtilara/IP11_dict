import streamlit as st
import time

st.set_page_config(
    page_title="AI Learning Hub: Dictionaries",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Design & Robust Theme Handling (Light & Dark Mode safe)
st.markdown("""
<style>
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
    
    /* Methods and Code */
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
    
    /* Custom Button */
    .stButton>button {
        background-color: #6366F1 !important;
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        transition: background-color 0.2s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #4F46E5 !important;
        color: white !important;
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
    
    /* New Programs Module Styles */
    .white-card {
        background-color: #FFFFFF !important;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        border: 1px solid #E2E8F0;
        height: 100%;
    }
    .white-card div, .white-card span, .white-card p {
        color: #2B2D42 !important;
    }
    
    .program-title {
        color: #4F46E5 !important;
        font-weight: 800;
        font-size: 2rem;
        margin-bottom: 0px;
        margin-top: -10px;
    }
    
    .program-desc {
        color: #EC4899 !important;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 30px;
    }
    
    .library-header {
        color: #4F46E5 !important;
        font-weight: 800;
        font-size: 1.5rem;
        margin-bottom: 25px;
    }
    
    .level-heading {
        font-size: 0.8rem;
        font-weight: bold;
        color: #1E293B !important;
        letter-spacing: 1px;
        margin-top: 25px;
        margin-bottom: 15px;
        text-transform: uppercase;
    }

    /* Subtle buttons for library */
    .stButton > button.lib-btn {
        background: transparent !important;
        color: #475569 !important;
        border: none;
        box-shadow: none;
        text-align: left;
        padding: 5px 0;
        font-weight: 500;
        justify-content: flex-start;
    }
    .stButton > button.lib-btn:hover {
        color: #4F46E5 !important;
        background: transparent !important;
    }
    .stButton > button.lib-btn-active {
        color: #4F46E5 !important;
        font-weight: 700;
        background: transparent !important;
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
