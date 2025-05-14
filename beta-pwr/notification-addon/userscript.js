// ==UserScript==
// @name         Beta Power DApp
// @version      0.2
// @description  YouTube DApp for age voting and ad feedback with Google OAuth
// @match        https://*.youtube.com/*
// @grant        GM_xmlhttpRequest
// @connect      accounts.google.com
// ==/UserScript==

(function() {
    'use strict';
    console.log("Beta Power DApp loaded");

    // OAuth configuration
    const CLIENT_ID = 'YOUR_CLIENT_ID'; // Replace with Google Cloud Console client ID
    const REDIRECT_URI = 'https://youtube.com'; // Adjust as needed
    const OAUTH_URL = `https://accounts.google.com/o/oauth2/v2/auth?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=code&scope=https://www.googleapis.com/auth/youtube.readonly`;

    // Inject auth button listener
    document.addEventListener('click', function(e) {
        if (e.target.id === 'auth-button') {
            window.location.href = OAUTH_URL; // Redirect to Google OAuth
        } else if (e.target.className.includes('beta-vote')) {
            // Handle age voting
            console.log("Vote recorded: ", e.target.value);
            // TODO: Call vote.py API via backend.py
        }
    });

    // Handle OAuth callback (parse code from URL)
    const urlParams = new URLSearchParams(window.location.search);
    const authCode = urlParams.get('code');
    if (authCode) {
        // Exchange code for tokens (placeholder for backend call)
        console.log("Auth code received: ", authCode);
        // TODO: Send authCode to backend.py for token exchange
    }
})();




