// Diagnostic script for baseline page issues
console.log('=== ATOM-SG Baseline Diagnostics ===');
console.log('URL:', window.location.href);
console.log('Hash:', window.location.hash);
console.log('Hash without #:', window.location.hash.substring(1));

// Check page elements
const baselinePage = document.getElementById('page-baseline');
console.log('page-baseline element:', baselinePage ? 'FOUND' : 'NOT FOUND');
if (baselinePage) {
  console.log('Has active class:', baselinePage.classList.contains('active'));
  console.log('All classes:', baselinePage.className);
}

// Check dashboard page
const dashboardPage = document.getElementById('page-dashboard');
console.log('page-dashboard element:', dashboardPage ? 'FOUND' : 'NOT FOUND');
if (dashboardPage) {
  console.log('Has active class:', dashboardPage.classList.contains('active'));
}

// Check navigation object
console.log('window.navigation:', window.navigation ? 'EXISTS' : 'UNDEFINED');
if (window.navigation) {
  console.log('navigation.currentPage:', window.navigation.currentPage);
}

// Check api object
console.log('window.api:', window.api ? 'EXISTS' : 'UNDEFINED');
console.log('global api variable:', typeof api !== 'undefined' ? 'EXISTS' : 'UNDEFINED');

// Check all scripts loaded
const scripts = document.querySelectorAll('script[src]');
console.log('Scripts loaded:', scripts.length);
scripts.forEach(s => console.log('  ', s.src));

// Check for errors (can't detect programmatically, but can check console)

console.log('=== End Diagnostics ===');

// If baseline page exists but not active, offer to fix
if (baselinePage && !baselinePage.classList.contains('active')) {
  console.log('\n⚠️  Baseline page is NOT active. Would you like to activate it?');
  console.log('Run this command:');
  console.log(`  document.getElementById('page-baseline').classList.add('active');`);
  console.log(`  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));`);
  console.log(`  document.getElementById('page-baseline').classList.add('active');`);
}

// If api not available
if (typeof api === 'undefined' && !window.api) {
  console.log('\n⚠️  API not available. Check if api.js loaded correctly.');
}