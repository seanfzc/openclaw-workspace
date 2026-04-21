#!/usr/bin/env python3
"""
Validate that P6 question files contain all required v4.1 schema fields.
"""

import re
import yaml
from pathlib import Path

# Required fields for v4.1 schema
REQUIRED_FIELDS = {
    'core': ['question_id', 'source_file', 'logic_family', 'grade_level', 
             '2026_syllabus_check', 'paper_type', 'date_extracted', 'pilot_phase'],
    'paper_1': ['calculator_required', 'time_target_seconds', 'mental_math_required',
                'speed_accuracy_balance'],
    'red_herring': ['has_red_herring_data', 'distractor_density'],
    'nodes': ['primary', 'secondary', 'tertiary', 'vertical_evolution'],
    'vertical_evolution': ['forward', 'backward'],
    'validation': ['manual_review_required', 'confidence_score', 'syllabus_2026_alignment']
}

def extract_yaml_frontmatter(filepath):
    """Extract YAML frontmatter from markdown file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Match YAML frontmatter between --- delimiters
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    
    yaml_content = match.group(1)
    try:
        data = yaml.safe_load(yaml_content)
        return data
    except yaml.YAMLError as e:
        print(f"  YAML parsing error: {e}")
        return None

def validate_field_present(data, field_path, filepath):
    """Check if a field path exists in data."""
    current = data
    path_parts = field_path.split('.')
    
    for part in path_parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            print(f"  ❌ Missing: {field_path}")
            return False
    
    # Check if field has content
    if current is None or current == "":
        print(f"  ⚠️  Empty: {field_path}")
        return False
    
    return True

def validate_file(filepath):
    """Validate a single question file."""
    print(f"\nValidating: {filepath.name}")
    print("-"*40)
    
    data = extract_yaml_frontmatter(filepath)
    if not data:
        print("  ❌ No valid YAML frontmatter found")
        return False
    
    all_valid = True
    
    # Check core fields
    print("  Core fields:")
    for field in REQUIRED_FIELDS['core']:
        if not validate_field_present(data, field, filepath):
            all_valid = False
    
    # Check paper_1 fields (nested under paper_1_requirements)
    print("  Paper 1 fields:")
    for field in REQUIRED_FIELDS['paper_1']:
        if not validate_field_present(data, f'paper_1_requirements.{field}', filepath):
            all_valid = False
    
    # Check red_herring fields (nested)
    print("  Red herring fields:")
    for field in REQUIRED_FIELDS['red_herring']:
        if not validate_field_present(data, f'red_herring_analysis.{field}', filepath):
            all_valid = False
    
    # Check nodes fields
    print("  Node fields:")
    for field in REQUIRED_FIELDS['nodes']:
        if not validate_field_present(data, f'nodes.{field}', filepath):
            all_valid = False
    
    # Check vertical_evolution subfields
    print("  Vertical evolution fields:")
    for field in REQUIRED_FIELDS['vertical_evolution']:
        if not validate_field_present(data, f'nodes.vertical_evolution.{field}', filepath):
            all_valid = False
    
    # Check validation fields
    print("  Validation fields:")
    for field in REQUIRED_FIELDS['validation']:
        if not validate_field_present(data, f'validation.{field}', filepath):
            all_valid = False
    
    # Additional checks
    print("  Additional checks:")
    
    # Check time_target_seconds is numeric and <90
    try:
        time_target = data.get('paper_1_requirements', {}).get('time_target_seconds')
        if time_target:
            if int(time_target) > 90:
                print(f"  ⚠️  Time target {time_target}s > 90s (Paper 1 max)")
            elif int(time_target) < 30:
                print(f"  ⚠️  Time target {time_target}s < 30s (very short)")
        else:
            print("  ❌ No time_target_seconds")
            all_valid = False
    except:
        print("  ❌ Invalid time_target_seconds format")
        all_valid = False
    
    # Check distractor_density is 1-5
    try:
        density = data.get('complexity_scores', {}).get('distractor_density')
        if density:
            if not (1 <= int(density) <= 5):
                print(f"  ⚠️  Distractor density {density} not in 1-5 range")
        else:
            print("  ❌ No distractor_density")
            all_valid = False
    except:
        print("  ❌ Invalid distractor_density format")
        all_valid = False
    
    # Check backward links exist
    backward_links = data.get('nodes', {}).get('vertical_evolution', {}).get('backward', [])
    if not backward_links:
        print("  ⚠️  No backward links to P1 (should have at least one)")
        all_valid = False
    else:
        print(f"  ✓ Backward links: {len(backward_links)} P1 connections")
    
    # Check logic_traps exist
    logic_traps = data.get('logic_traps', [])
    if not logic_traps:
        print("  ⚠️  No logic traps identified")
    else:
        print(f"  ✓ Logic traps: {len(logic_traps)} identified")
    
    return all_valid

def main():
    """Main validation function."""
    p6_dir = Path("/Users/zcaeth/.openclaw/workspace/P6_Pilot_Validation")
    
    print("="*80)
    print("SCHEMA v4.1 VALIDATION CHECK")
    print("="*80)
    print("Checking required fields for Paper 1 Revolution compliance")
    print()
    
    # Find all P6 question files
    question_files = list(p6_dir.glob("P6_Rosyth_Q*.md"))
    
    if not question_files:
        print("No P6 question files found")
        return
    
    print(f"Found {len(question_files)} question files")
    print()
    
    validation_results = {}
    for filepath in sorted(question_files):
        is_valid = validate_file(filepath)
        validation_results[filepath.name] = is_valid
        print()
    
    # Summary
    print("="*80)
    print("VALIDATION SUMMARY")
    print("="*80)
    
    valid_count = sum(1 for result in validation_results.values() if result)
    total_count = len(validation_results)
    
    print(f"Valid files: {valid_count}/{total_count}")
    
    for filename, is_valid in validation_results.items():
        status = "✅ PASS" if is_valid else "❌ FAIL"
        print(f"  {filename}: {status}")
    
    if valid_count == total_count:
        print("\n✅ ALL FILES COMPLY WITH SCHEMA v4.1 REQUIREMENTS")
        print("Ready for independent verification")
    else:
        print("\n❌ SOME FILES FAIL VALIDATION")
        print("Please check missing fields before verification")

if __name__ == "__main__":
    main()