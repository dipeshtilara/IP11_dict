document.addEventListener('DOMContentLoaded', () => {

    // Mock Data reflecting the python target loop
    const empData = {
        "ID": 101,
        "Name": "Amit",
        "Salary": 45000
    };

    const keysList = Object.keys(empData);
    let loopIndex = -1;

    // DOM Nodes
    const visualizerContent = document.getElementById('codelab-visualizer-content');
    const btnStep = document.getElementById('btn-step');
    const btnReset = document.getElementById('btn-reset');

    // Core rendering function
    function renderState() {
        if (loopIndex === -1) {
            visualizerContent.innerHTML = `<h4 style='color: #64748b; text-align:center; padding: 40px 0; font-weight: 500;'>Loop not started. Click 'Step Forward'</h4>`;
            return;
        }

        const currentKey = keysList[loopIndex];
        const currentVal = empData[currentKey];

        let html = `
            <div style="margin-bottom: 15px;">
                <strong style="color: #1E293B;">Iteration:</strong> <code style="background-color: transparent; color: inherit; padding: 0;">${loopIndex + 1}</code> of <code style="background-color: transparent; color: inherit; padding: 0;">${keysList.length}</code>
            </div>
            
            <div style="margin-bottom: 15px;">
                <strong style="color: #1E293B;">Current <code>key</code> variable:</strong> 
                <span style='background:#F1F5F9; padding:6px 10px; border-radius:5px; font-weight:bold; color:#E11D48; font-family: monospace; font-size: 1.05rem;'>"${currentKey}"</span>
            </div>
            
            <div style="margin-bottom: 25px;">
                <strong style="color: #1E293B;">Accessing Value <code>emp[key]</code>:</strong> 
                <span style='background:#F1F5F9; padding:6px 10px; border-radius:5px; font-weight:bold; color:#0F172A; font-family: monospace; font-size: 1.05rem;'>
                    ${typeof currentVal === 'string' ? `"${currentVal}"` : currentVal}
                </span>
            </div>
            
            <hr style="border: none; border-top: 1px solid #E2E8F0; margin: 20px 0;">
            
            <div style="margin-bottom: 10px;"><strong style="color: #1E293B;">Console Output:</strong></div>
            <div class="code-block" style="padding: 15px;">
                <span style="color: #a9b1d6; font-family: monospace; font-size: 0.95rem;">> ${currentKey} : ${currentVal}</span>
            </div>
        `;

        visualizerContent.innerHTML = html;

        // Retrigger fade animation
        visualizerContent.style.animation = "none";
        visualizerContent.offsetHeight; /* trigger reflow */
        visualizerContent.style.animation = "fadeIn 0.3s ease-in-out";
    }

    // Events
    btnStep.addEventListener('click', () => {
        if (loopIndex < keysList.length - 1) {
            loopIndex++;
        } else {
            loopIndex = -1; // Reset back to -1 when hitting the end
        }
        renderState();
    });

    btnReset.addEventListener('click', () => {
        loopIndex = -1;
        renderState();
    });

    // Initial UI Setup
    renderState();
});
