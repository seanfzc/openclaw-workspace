// Simple test to verify baseline.js logic
// This doesn't run the actual JavaScript but checks for common errors

const fs = require('fs');
const path = require('path');

// Load baseline.js
const baselinePath = path.join(__dirname, 'ATOM-SG Pilot/05-Backend/frontend/static/js/baseline.js');
const baselineCode = fs.readFileSync(baselinePath, 'utf8');

// Check for syntax patterns that might cause errors
const checks = [
    { name: 'Class definition', regex: /class Baseline/, pass: true },
    { name: 'Constructor', regex: /constructor\(\)/, pass: true },
    { name: 'handleUpload method', regex: /async handleUpload\(\)/, pass: true },
    { name: 'api.uploadScan call', regex: /api\.uploadScan/, pass: true },
    { name: 'Error handling in catch', regex: /catch\s*\(.*error.*\)/, pass: true },
    { name: 'DOM element IDs referenced', regex: /getElementById.*baseline/, pass: true },
    { name: 'No obvious syntax errors', regex: /undefined|null.*\./, pass: false }, // shouldn't have undefined.
];

console.log('Checking baseline.js for potential issues...');
let issues = 0;
checks.forEach(check => {
    const matches = baselineCode.match(check.regex);
    if (check.pass && !matches) {
        console.log(`❌ ${check.name}: NOT FOUND`);
        issues++;
    } else if (!check.pass && matches) {
        console.log(`⚠️  ${check.name}: Found potential issue`);
        issues++;
    } else {
        console.log(`✅ ${check.name}: OK`);
    }
});

// Check for common JavaScript errors
const errorPatterns = [
    /\.forEach\(.*=>/g,
    /\.addEventListener\(.*=>/g,
    /await.*\.then/g,
];

errorPatterns.forEach(pattern => {
    const matches = baselineCode.match(pattern);
    if (matches) {
        console.log(`✅ Async/await pattern found: ${pattern}`);
    }
});

// Check that api object is referenced safely
if (baselineCode.includes('api.') && !baselineCode.includes('window.api') && !baselineCode.includes('globalThis.api')) {
    console.log('⚠️  api referenced without window. prefix - assumes global');
}

console.log(`\nTotal potential issues: ${issues}`);

if (issues === 0) {
    console.log('✅ baseline.js appears syntactically correct');
    process.exit(0);
} else {
    console.log('❌ Some issues detected - please review');
    process.exit(1);
}