document.addEventListener('DOMContentLoaded', () => {

    // --- Single Value Logic ---
    let currentDict = {
        "Name": "Riya",
        "RollNo": 1,
        "Status": "Active"
    };

    const container = document.getElementById('visualizer-container');
    const syntaxDisplay = document.getElementById('python-syntax-display');
    const keyInput = document.getElementById('vis-key-input');
    const valInput = document.getElementById('vis-value-input');
    const delKeyInput = document.getElementById('vis-del-key-input');
    const addBtn = document.getElementById('vis-add-btn');
    const delBtn = document.getElementById('vis-del-btn');
    const resetBtn = document.getElementById('vis-reset-btn');

    function renderDictionary() {
        container.innerHTML = '';
        const keys = Object.keys(currentDict);

        let syntaxItems = keys.map(k => {
            let v = currentDict[k];
            let kStr = `"${k}"`; // Simple wrap for keys
            let vStr = typeof v === 'string' ? `"${v}"` : v;
            return `${kStr}: ${vStr}`;
        });
        syntaxDisplay.textContent = `my_dict = {${syntaxItems.join(', ')}}`;

        if (keys.length === 0) {
            container.innerHTML = '<div style="color: #64748b; font-style: italic; text-align: center; padding: 20px;">Dictionary is currently empty {}</div>';
            return;
        }

        keys.forEach(k => {
            const v = currentDict[k];
            const row = document.createElement('div');
            row.className = 'dict-row';

            const kStr = `"${k}"`;
            const keyBadge = document.createElement('div');
            keyBadge.className = 'key-badge';
            keyBadge.textContent = kStr;

            const arrow = document.createElement('div');
            arrow.className = 'mapping-arrow';
            arrow.textContent = '→';

            const valArea = document.createElement('div');
            valArea.className = 'value-area';

            const valBadge = document.createElement('div');
            valBadge.className = 'value-badge scalar';

            let vStr = typeof v === 'string' ? `"${v}"` : String(v);
            valBadge.textContent = vStr;
            valArea.appendChild(valBadge);

            row.appendChild(keyBadge);
            row.appendChild(arrow);
            row.appendChild(valArea);
            container.appendChild(row);
        });
    }

    addBtn.addEventListener('click', () => {
        let k = keyInput.value.trim();
        let vRaw = valInput.value.trim();
        if (!k) { alert("A dictionary key cannot be empty!"); return; }

        let v;
        if (vRaw === "true" || vRaw === "True") v = true;
        else if (vRaw === "false" || vRaw === "False") v = false;
        else if (!isNaN(vRaw) && vRaw !== "") v = Number(vRaw);
        else v = vRaw; // default string

        currentDict[k] = v;
        keyInput.value = ''; valInput.value = ''; keyInput.focus();
        renderDictionary();
    });

    delBtn.addEventListener('click', () => {
        let k = delKeyInput.value.trim();
        if (k in currentDict) {
            delete currentDict[k];
            delKeyInput.value = '';
            renderDictionary();
        } else {
            alert(`KeyError: '${k}' not found in dictionary.`);
        }
    });

    resetBtn.addEventListener('click', () => {
        currentDict = { "Name": "Riya", "RollNo": 1, "Status": "Active" };
        renderDictionary();
    });

    renderDictionary();


    // --- Multi Value Logic ---
    let multiDict = {
        "Amit": [85, 90, 88],
        "Bhavya": [92, 95, 98],
        "Chirag": [78, 80, 75]
    };

    const multiContainer = document.getElementById('visualizer-multi-container');
    const multiSyntaxDisplay = document.getElementById('python-multi-syntax-display');
    const multiKeySelect = document.getElementById('vis-multi-key-select');
    const multiValInput = document.getElementById('vis-multi-val-input');
    const multiAppendBtn = document.getElementById('vis-multi-append-btn');
    const multiNewKeyInput = document.getElementById('vis-multi-new-key-input');
    const multiAddKeyBtn = document.getElementById('vis-multi-add-key-btn');
    const multiResetBtn = document.getElementById('vis-multi-reset-btn');

    function renderMultiDictionary() {
        multiContainer.innerHTML = '';
        multiKeySelect.innerHTML = '';
        const keys = Object.keys(multiDict);

        let syntaxItems = keys.map(k => {
            let listStr = `[${multiDict[k].join(', ')}]`;
            return `"${k}": ${listStr}`;
        });
        multiSyntaxDisplay.textContent = `my_dict = {${syntaxItems.join(', ')}}`;

        if (keys.length === 0) {
            multiContainer.innerHTML = '<div style="color: #64748b; font-style: italic; text-align: center; padding: 20px;">Dictionary is currently empty {}</div>';
            return;
        }

        keys.forEach(k => {
            // Update Select Dropdown
            const option = document.createElement('option');
            option.value = k;
            option.textContent = k;
            multiKeySelect.appendChild(option);

            // Render Row
            const vList = multiDict[k];
            const row = document.createElement('div');
            row.className = 'dict-row';

            const keyBadge = document.createElement('div');
            keyBadge.className = 'key-badge';
            keyBadge.style.backgroundColor = '#10B981';
            keyBadge.textContent = `"${k}"`;

            const arrow = document.createElement('div');
            arrow.className = 'mapping-arrow';
            arrow.textContent = '→';

            const valArea = document.createElement('div');
            valArea.className = 'value-area';

            if (vList.length === 0) {
                const emptyBadge = document.createElement('div');
                emptyBadge.className = 'value-badge scalar';
                emptyBadge.style.color = '#94A3B8';
                emptyBadge.style.borderColor = '#CBD5E1';
                emptyBadge.style.backgroundColor = '#F8FAFC';
                emptyBadge.textContent = 'Empty List []';
                valArea.appendChild(emptyBadge);
            } else {
                vList.forEach(item => {
                    const valBadge = document.createElement('div');
                    valBadge.className = 'value-badge';
                    valBadge.textContent = typeof item === 'string' ? `"${item}"` : String(item);
                    valArea.appendChild(valBadge);
                });
            }

            row.appendChild(keyBadge);
            row.appendChild(arrow);
            row.appendChild(valArea);
            multiContainer.appendChild(row);
        });
    }

    multiAppendBtn.addEventListener('click', () => {
        const k = multiKeySelect.value;
        const vRaw = multiValInput.value.trim();
        if (!k || !vRaw) return;

        let v = isNaN(vRaw) ? vRaw : Number(vRaw);
        multiDict[k].push(v);
        multiValInput.value = '';
        renderMultiDictionary();
    });

    multiAddKeyBtn.addEventListener('click', () => {
        const k = multiNewKeyInput.value.trim();
        if (!k) return;
        if (!(k in multiDict)) {
            multiDict[k] = [];
        }
        multiNewKeyInput.value = '';
        renderMultiDictionary();
    });

    multiResetBtn.addEventListener('click', () => {
        multiDict = {
            "Amit": [85, 90, 88],
            "Bhavya": [92, 95, 98],
            "Chirag": [78, 80, 75]
        };
        renderMultiDictionary();
    });

    renderMultiDictionary();
});
