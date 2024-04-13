(function() {
    let interactions = [];

    function logInteraction(event, additionalDetails) {
        const baseDetails = {
            type: event.type,
            timestamp: new Date().toISOString(),
            details: {
                x: event.clientX || null,
                y: event.clientY || null,
                tag: event.target ? event.target.tagName : null,
                id: event.target ? event.target.id : null,
                key: event.key || null,
                button: event.button != undefined ? event.button : null,
                scrollDepth: window.scrollY || null,
                width: window.innerWidth || null,
                height: window.innerHeight || null,
                ...additionalDetails
            }
        };

        interactions.push(baseDetails);

        // Send batch if 100 interactions collected or periodically
        if (interactions.length >= 100) {
            sendBatch();
        }
    }

    // Generic event listener setup
    function setupListeners() {
        // Clicks and Taps
        document.addEventListener('click', logInteraction);
        document.addEventListener('touchend', logInteraction);

        // Hover and Mouse movements
        document.addEventListener('mouseover', logInteraction);
        document.addEventListener('mousemove', (event) => logInteraction(event, {throttle: true}));

        // Scroll
        window.addEventListener('scroll', () => logInteraction(event, {scrollDepth: window.scrollY}), { passive: true });

        // Form Interactions
        ['focusin', 'input', 'submit'].forEach(type => {
            document.addEventListener(type, (event) => {
                if (event.target.form) {
                    logInteraction(event, { formId: event.target.form.id, fieldId: event.target.id });
                }
            }, true);
        });

        // Navigation
        window.addEventListener('popstate', () => logInteraction(event, { url: window.location.href }));

        // Keyboard Events
        document.addEventListener('keypress', logInteraction);

        // Resize Events
        window.addEventListener('resize', () => logInteraction(event, { width: window.innerWidth, height: window.innerHeight }));
    }

    // Function to send batch of interactions to server
    function sendBatch() {
        fetch('/log-interactions/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(interactions)
        }).then(response => {
            if (response.ok) {
                console.log('Batch sent successfully.');
                interactions = []; // Clear after sending
            }
        }).catch(error => console.error('Error sending batch:', error));
    }

    // Helper function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    setupListeners();

    setInterval(sendBatch, 15000); // Adjust timing as needed
})();

