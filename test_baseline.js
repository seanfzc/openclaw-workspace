const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');

// Create a virtual DOM
const dom = new JSDOM(`
<!DOCTYPE html>
<html>
<body>
    <button id="print-baseline">Print</button>
    <form id="upload-baseline-form">
        <input type="file" id="baseline-file" accept=".pdf,.png,.jpg" required>
        <button type="submit">Upload</button>
    </form>
    <div id="baseline-upload-status" class="upload-status"></div>
    <div id="baseline-results" class="results-section hidden">
        <div id="gap-map"></div>
    </div>
</body>
</html>
`, { runScripts: 'dangerously', resources: 'usable' });

const window = dom.window;
const document = window.document;

// Mock global objects
global.window = window;
global.document = document;
global.navigator = window.navigator;
global.localStorage = window.localStorage;
global.sessionStorage = window.sessionStorage;
global.console = console;

// Mock fetch and api
global.fetch = async (url, options) => {
    console.log('Fetch called:', url, options);
    // Simulate responses for specific endpoints
    if (url.includes('/api/v1/scans') && options && options.method === 'POST') {
        // Upload scan endpoint
        return {
            ok: true,
            status: 200,
            json: async () => ({
                id: 'scan_test123',
                status: 'completed',
                uploadedAt: new Date().toISOString(),
                estimatedTime: 30,
                completedAt: new Date().toISOString(),
                ocrResults: [{ questionId: 'prob_001', text: 'Test OCR', confidence: 0.85 }],
                gapMap: { weakestPathways: [] }
            })
        };
    } else if (url.includes('/api/v1/scans/scan_test123')) {
        // Get scan endpoint
        return {
            ok: true,
            status: 200,
            json: async () => ({
                id: 'scan_test123',
                status: 'completed',
                uploadedAt: new Date().toISOString(),
                estimatedTime: 30,
                completedAt: new Date().toISOString(),
                ocrResults: [{ questionId: 'prob_001', text: 'Test OCR', confidence: 0.85 }],
                gapMap: { weakestPathways: [] }
            })
        };
    } else if (url.includes('/api/v1/analytics/baseline')) {
        // Baseline analytics endpoint
        return {
            ok: true,
            status: 200,
            json: async () => ({
                scanId: 'scan_test123',
                totalScore: 0.6,
                scoresByPathway: { 'before-after-change': 0.3 },
                gapMap: { weakestPathways: [] },
                completedAt: new Date().toISOString()
            })
        };
    } else {
        console.error('Unexpected fetch URL:', url);
        return { ok: false, status: 404 };
    }
};

// Mock api object (as defined in api.js)
global.api = {
    uploadScan: async (week, file) => {
        const formData = new FormData();
        formData.append('week', week);
        formData.append('file', file);
        const response = await fetch('/api/v1/scans', { method: 'POST', body: formData });
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return response.json();
    },
    getScan: async (scanId) => {
        const response = await fetch(`/api/v1/scans/${scanId}`);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return response.json();
    },
    getBaselineAnalytics: async () => {
        const response = await fetch('/api/v1/analytics/baseline');
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return response.json();
    },
    getProblemsPdf: (week) => `/api/v1/problems/${week}/pdf`
};

// Load baseline.js
const baselineScript = fs.readFileSync(path.join(__dirname, 'ATOM-SG Pilot/05-Backend/frontend/static/js/baseline.js'), 'utf8');
const scriptEl = document.createElement('script');
scriptEl.textContent = baselineScript;
document.head.appendChild(scriptEl);

// Wait for script to load
setTimeout(() => {
    console.log('Baseline script loaded');
    
    // Check if Baseline class is available
    if (window.Baseline) {
        console.log('Baseline class found');
        
        // Create instance
        const baseline = new window.Baseline();
        
        // Simulate file selection
        const file = new window.File(['%PDF dummy'], 'test.pdf', { type: 'application/pdf' });
        const dataTransfer = new window.DataTransfer();
        dataTransfer.items.add(file);
        document.getElementById('baseline-file').files = dataTransfer.files;
        
        // Trigger upload
        console.log('Triggering upload...');
        baseline.handleUpload().then(() => {
            console.log('Upload succeeded!');
            
            // Check if results section is visible
            const resultsSection = document.getElementById('baseline-results');
            if (resultsSection.classList.contains('hidden')) {
                console.error('Results section still hidden!');
                process.exit(1);
            } else {
                console.log('Results section visible - SUCCESS');
                process.exit(0);
            }
        }).catch(error => {
            console.error('Upload failed:', error);
            process.exit(1);
        });
    } else {
        console.error('Baseline class not found');
        process.exit(1);
    }
}, 1000);