#!/usr/bin/env python3
import json

# Load the graph data
with open('knowledge_graph.json', 'r') as f:
    graph_data = json.load(f)

# Read the original HTML template
with open('syllabus_graph.html', 'r') as f:
    html_template = f.read()

# Replace the async loadGraphData function with embedded data
embed_script = f'''
        // Embedded graph data
        let graphData = {json.dumps(graph_data, indent=2)};
        
        async function loadGraphData() {{
            // Use embedded data directly
            initGraph();
        }}
'''

# Replace from "// Graph data will be loaded here" to "async function loadGraphData() {"
# Find the section to replace
lines = html_template.split('\n')
new_lines = []
in_replace_section = False
replaced = False

for i, line in enumerate(lines):
    if '// Graph data will be loaded here' in line:
        new_lines.append(line)
        # Skip until we find the async function
        in_replace_section = True
    elif in_replace_section and 'async function loadGraphData()' in line:
        # Add our embedded version instead
        new_lines.append(embed_script)
        replaced = True
        # Skip the original function
        skip = True
        while skip and i < len(lines):
            i += 1
            if lines[i].strip() == '}' and lines[i-1].strip() == '}':
                skip = False
        continue
    elif not replaced:
        new_lines.append(line)

if not replaced:
    # Fallback: simpler replacement
    html_template = html_template.replace(
        '        // Graph data will be loaded here\n        let graphData = {\n            nodes: [],\n            edges: []\n        };',
        f'        // Embedded graph data\n        let graphData = {json.dumps(graph_data, indent=8)};'
    )
    html_template = html_template.replace(
        '        // Load the graph data\n        async function loadGraphData() {\n            try {\n                const response = await fetch(\'knowledge_graph.json\');\n                const data = await response.json();\n                graphData = data;\n                initGraph();\n            } catch (error) {\n                console.error(\'Error loading graph data:\', error);\n                // Fallback to minimal data\n                graphData = {\n                    nodes: [{id: \'error\', label: \'Error loading data\', type: \'error\'}],\n                    edges: []\n                };\n                initGraph();\n            }\n        }',
        '        async function loadGraphData() {\n            // Use embedded data\n            initGraph();\n        }'
    )
else:
    html_template = '\n'.join(new_lines)

# Write new file
with open('syllabus_graph_embedded.html', 'w') as f:
    f.write(html_template)

print('Created syllabus_graph_embedded.html with embedded data')
print('Open this file in your browser to avoid CORS issues')