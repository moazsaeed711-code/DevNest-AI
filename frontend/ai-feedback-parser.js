/**
 * DevNest AI Feedback Parser
 * Automatically parses AI feedback text and applies CSS classes for colored headers
 */

function parseAndStyleAIFeedback(feedbackText) {
    // Split feedback into sections
    let styledHTML = feedbackText;
    
    // Define section patterns and their corresponding CSS classes
    const sections = [
        {
            pattern: /WHAT YOUR CODE DOES:/gi,
            replacement: '<h2 class="feedback-section-what">WHAT YOUR CODE DOES:</h2>',
            cssClass: 'feedback-section-what'
        },
        {
            pattern: /GOOD PRACTICES FOUND:/gi,
            replacement: '<h2 class="feedback-section-good">GOOD PRACTICES FOUND:</h2>',
            cssClass: 'feedback-section-good'
        },
        {
            pattern: /ISSUES TO FIX:/gi,
            replacement: '<h2 class="feedback-section-issues">ISSUES TO FIX:</h2>',
            cssClass: 'feedback-section-issues'
        },
        {
            pattern: /CRITICAL ERRORS:/gi,
            replacement: '<h3 class="feedback-section-critical">CRITICAL ERRORS:</h3>',
            cssClass: 'feedback-section-critical'
        },
        {
            pattern: /STYLE IMPROVEMENTS:/gi,
            replacement: '<h3 class="feedback-section-style">STYLE IMPROVEMENTS:</h3>',
            cssClass: 'feedback-section-style'
        },
        {
            pattern: /LEARNING TIPS:/gi,
            replacement: '<h2 class="feedback-section-tips">LEARNING TIPS:</h2>',
            cssClass: 'feedback-section-tips'
        },
        {
            pattern: /KEY TAKEAWAY:/gi,
            replacement: '<h2 class="feedback-section-takeaway">KEY TAKEAWAY:</h2>',
            cssClass: 'feedback-section-takeaway'
        }
    ];
    
    // Replace headers with styled versions
    sections.forEach(section => {
        styledHTML = styledHTML.replace(section.pattern, section.replacement);
    });
    
    // Style code blocks (Before/After examples)
    styledHTML = styledHTML.replace(/Before:\s*\n\s*(.+?)(?=\n\s*After:|\n\n)/gis, (match, code) => {
        return `<div class="code-example code-example-before">
                    <div class="code-example-label">Before:</div>
                    <pre><code>${escapeHTML(code.trim())}</code></pre>
                </div>`;
    });
    
    styledHTML = styledHTML.replace(/After:\s*\n\s*(.+?)(?=\n\n|\n-|$)/gis, (match, code) => {
        return `<div class="code-example code-example-after">
                    <div class="code-example-label">After:</div>
                    <pre><code>${escapeHTML(code.trim())}</code></pre>
                </div>`;
    });
    
    // Convert markdown-style code blocks to HTML
    styledHTML = styledHTML.replace(/```python\n([\s\S]*?)```/g, (match, code) => {
        return `<pre><code>${escapeHTML(code.trim())}</code></pre>`;
    });
    
    // Convert inline code
    styledHTML = styledHTML.replace(/`([^`]+)`/g, '<code>$1</code>');
    
    // Convert newlines to <br> tags (preserve spacing)
    styledHTML = styledHTML.replace(/\n\n/g, '</p><p>');
    styledHTML = styledHTML.replace(/\n/g, '<br>');
    
    // Wrap in container
    return `<div class="ai-feedback-container"><p>${styledHTML}</p></div>`;
}

/**
 * Helper function to escape HTML entities
 */
function escapeHTML(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Alternative: Simple class-based styling without HTML parsing
 * Use this if you want to keep the text as-is and just add classes
 */
function wrapAIFeedbackWithClasses(feedbackText) {
    // Wrap the entire feedback in a container
    const container = document.createElement('div');
    container.className = 'ai-feedback-container';
    
    // Split into lines and process each
    const lines = feedbackText.split('\n');
    let currentSection = null;
    let html = '';
    
    lines.forEach(line => {
        const trimmedLine = line.trim();
        
        // Check if this is a header
        if (trimmedLine.includes('WHAT YOUR CODE DOES:')) {
            html += `<div class="feedback-section"><h2 class="feedback-section-what">${trimmedLine}</h2>`;
            currentSection = 'what';
        } else if (trimmedLine.includes('GOOD PRACTICES FOUND:')) {
            html += `</div><div class="feedback-section"><h2 class="feedback-section-good">${trimmedLine}</h2>`;
            currentSection = 'good';
        } else if (trimmedLine.includes('ISSUES TO FIX:')) {
            html += `</div><div class="feedback-section"><h2 class="feedback-section-issues">${trimmedLine}</h2>`;
            currentSection = 'issues';
        } else if (trimmedLine.includes('CRITICAL ERRORS:')) {
            html += `<h3 class="feedback-section-critical">${trimmedLine}</h3>`;
            currentSection = 'critical';
        } else if (trimmedLine.includes('STYLE IMPROVEMENTS:')) {
            html += `<h3 class="feedback-section-style">${trimmedLine}</h3>`;
            currentSection = 'style';
        } else if (trimmedLine.includes('LEARNING TIPS:')) {
            html += `</div><div class="feedback-section"><h2 class="feedback-section-tips">${trimmedLine}</h2>`;
            currentSection = 'tips';
        } else if (trimmedLine.includes('KEY TAKEAWAY:')) {
            html += `</div><div class="feedback-section"><h2 class="feedback-section-takeaway">${trimmedLine}</h2>`;
            currentSection = 'takeaway';
        } else {
            // Regular content line
            if (trimmedLine) {
                html += `<p>${escapeHTML(trimmedLine)}</p>`;
            } else {
                html += '<br>';
            }
        }
    });
    
    html += '</div>'; // Close last section
    container.innerHTML = html;
    
    return container;
}

/**
 * Usage Example:
 * 
 * // When you receive AI feedback from the backend:
 * fetch('/api/ai-explain', {
 *     method: 'POST',
 *     headers: { 'Content-Type': 'application/json' },
 *     body: JSON.stringify({ code: userCode })
 * })
 * .then(res => res.json())
 * .then(data => {
 *     const styledFeedback = parseAndStyleAIFeedback(data.explanation);
 *     document.getElementById('ai-feedback-display').innerHTML = styledFeedback;
 * });
 */

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        parseAndStyleAIFeedback,
        wrapAIFeedbackWithClasses,
        escapeHTML
    };
}
