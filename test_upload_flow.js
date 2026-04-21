const fs = require('fs');
const vm = require('vm');

// Create a mock DOM environment
const mockWindow = {
    console: {
        log: (...args) => console.log('[MOCK LOG]', ...args),
        error: (...args) => console.error('[MOCK ERROR]', ...args),
        warn: (...args) => console.warn('[MOCK WARN]', ...args)
    },
    document: {
        getElementById: (id) => {
            const elements = {
                'print-baseline': { addEventListener: () => {} },
                'upload-baseline-form': { 
                    addEventListener: () => {},
                    querySelector: () => ({ disabled: false })
                },
                'baseline-file': { files: [] },
                'baseline-upload-status': { textContent: '', className: '' },
                'baseline-results': { classList: { contains: () => false, remove: () => {} }, style: {} },
                'gap-map': { innerHTML: '' }
            };
            return elements[id] || { addEventListener: () => {} };
        },
        createElement: () => ({ appendChild: () => {} }),
        head: { appendChild: () => {} },
        addEventListener: (event, cb) => {
            if (event === 'DOMContentLoaded') setTimeout(cb, 0);
        }
    },
    window: {},
    navigator: {},
    localStorage: { getItem: () => null, setItem: () => {} },
    sessionStorage: { getItem: () => null, setItem: () => {} },
    File: function(content, name, options) {
        this.name = name;
        this.type = options.type;
    },
    DataTransfer: function() {
        this.items = { add: () => {} };
    },
    FormData: function() {
        this.append = () => {};
    },
    CustomEvent: function(type, detail) {
        this.type = type;
        this.detail = detail.detail;
    },
    fetch: async (url, options) => {
        console.log(`[MOCK FETCH] ${options?.method || 'GET'} ${url}`);
        if (url.includes('/api/v1/scans') && options?.method === 'POST') {
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
        } else if (url.includes('/api/v1/scans/')) {
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
        }
        return { ok: false, status: 404 };
    },
    addEventListener: (event, cb) => {
        if (event === 'pageLoad') {
            // Store callback for later triggering
            mockWindow.pageLoadCallbacks = mockWindow.pageLoadCallbacks || [];
            mockWindow.pageLoadCallbacks.push(cb);
        }
    },
    dispatchEvent: (event) => {
        if (event.type === 'pageLoad' && mockWindow.pageLoadCallbacks) {
            mockWindow.pageLoadCallbacks.forEach(cb => cb(event));
        }
    },
    history: { pushState: () => {} },
    location: { hash: '#baseline' }
};

// Make window refer to itself
mockWindow.window = mockWindow;
mockWindow.navigation = { currentPage: 'baseline' };

// Load api.js
const apiCode = fs.readFileSync('./ATOM-SG Pilot/05-Backend/frontend/static/js/api.js', 'utf8');
const apiContext = vm.createContext(mockWindow);
const apiScript = new vm.Script(apiCode);
apiScript.runInContext(apiContext);

// Load baseline.js
const baselineCode = fs.readFileSync('./ATOM-SG Pilot/05-Backend/frontend/static/js/baseline.js', 'utf8');
const baselineScript = new vm.Script(baselineCode);
baselineScript.runInContext(apiContext);

// Wait for next tick for DOMContentLoaded
setImmediate(() => {
    console.log('Scripts loaded');
    
    // Check if Baseline class is defined
    if (apiContext.Baseline) {
        console.log('Baseline class found');
        
        // Create instance
        const baseline = new apiContext.Baseline();
        console.log('Baseline instance created');
        
        // Simulate file selection
        const mockFile = new apiContext.File(['%PDF'], 'test.pdf', { type: 'application/pdf' });
        apiContext.document.getElementById('baseline-file').files = [mockFile];
        
        // Trigger upload
        console.log('Starting upload test...');
        baseline.handleUpload().then(() => {
            console.log('✅ Upload test PASSED');
            process.exit(0);
        }).catch(err => {
            console.error('❌ Upload test FAILED:', err);
            process.exit(1);
        });
    } else {
        console.error('Baseline class not found');
        process.exit(1);
    }
});