#!/usr/bin/env python3.10
import json
import re
from pathlib import Path

def extract_topics_from_text(text):
    """Extract potential topic phrases from text."""
    topics = set()
    # Look for headings (all caps lines)
    lines = text.split('\n')
    for line in lines:
        stripped = line.strip()
        if stripped.isupper() and 3 < len(stripped) < 50:
            # Remove non-alphabetic
            clean = re.sub(r'[^A-Z\s]', '', stripped)
            if len(clean) > 3:
                topics.add(clean.title())
        # Common math phrases
        math_phrases = ['numbers to', 'addition and subtraction', 'within', 
                       'place value', 'counting', 'word problems', 'shapes',
                       'measurement', 'time', 'money', 'graph', 'pattern']
        lower = stripped.lower()
        for phrase in math_phrases:
            if phrase in lower:
                topics.add(phrase.title())
    return list(topics)

def extract_topics_from_filename(filename):
    """Extract topics from filename."""
    # Example: "2021 P1 Maths Quiz1 Henry Park.pdf"
    name = filename.replace('.pdf', '').replace('.txt', '')
    parts = name.split()
    topics = []
    for part in parts:
        if part.isdigit():
            continue
        if part in ['P1', 'Maths', 'Quiz', 'Test', 'Review', 'Assessment', 'Mini', 'Term']:
            continue
        if len(part) > 2 and not part.lower() in ['and', 'the', 'for', 'with']:
            topics.append(part)
    return topics

def main():
    txt_files = list(Path('.').glob('*.txt'))
    nodes = []
    edges = []
    hyperedges = []
    
    # Map topic label to node id
    topic_to_id = {}
    next_id = 1
    
    for txt in txt_files:
        # File node
        file_id = f"file_{txt.stem}"
        nodes.append({
            "id": file_id,
            "label": txt.stem,
            "type": "file",
            "source_file": str(txt.with_suffix('.pdf')),
            "source_location": "L1",
            "confidence": "HIGH"
        })
        
        # Read text
        text = txt.read_text(encoding='utf-8', errors='ignore')
        # Extract topics
        filename_topics = extract_topics_from_filename(txt.stem)
        text_topics = extract_topics_from_text(text)
        all_topics = list(set(filename_topics + text_topics))
        
        # Create topic nodes and edges
        for topic in all_topics:
            if not topic or len(topic) < 2:
                continue
            # Clean topic
            clean_topic = re.sub(r'[^A-Za-z0-9\s]', '', topic).strip()
            if len(clean_topic) < 2:
                continue
            if clean_topic not in topic_to_id:
                topic_id = f"topic_{next_id}"
                topic_to_id[clean_topic] = topic_id
                next_id += 1
                nodes.append({
                    "id": topic_id,
                    "label": clean_topic,
                    "type": "concept",
                    "source_file": str(txt.with_suffix('.pdf')),
                    "source_location": "L1",
                    "confidence": "MEDIUM"
                })
            else:
                topic_id = topic_to_id[clean_topic]
            
            # Edge from file to topic
            edges.append({
                "source": file_id,
                "target": topic_id,
                "relation": "contains",
                "confidence": "MEDIUM",
                "source_file": str(txt.with_suffix('.pdf')),
                "source_location": "L1"
            })
        
        # Hyperedge for this file's topics
        if all_topics:
            hyperedges.append({
                "id": f"hyper_{txt.stem}",
                "label": f"Topics in {txt.stem}",
                "nodes": [topic_to_id[t] for t in all_topics if t in topic_to_id],
                "confidence": "MEDIUM",
                "source_file": str(txt.with_suffix('.pdf'))
            })
    
    # Add similarity edges between topics that co-occur in same files
    # For simplicity, connect topics that appear together in at least 2 files
    from collections import defaultdict
    topic_files = defaultdict(set)
    for edge in edges:
        if edge['relation'] == 'contains':
            topic_files[edge['target']].add(edge['source'])
    
    for topic1, files1 in topic_files.items():
        for topic2, files2 in topic_files.items():
            if topic1 >= topic2:
                continue
            common = files1.intersection(files2)
            if len(common) >= 1:
                edges.append({
                    "source": topic1,
                    "target": topic2,
                    "relation": "co_occurs_with",
                    "confidence": "LOW",
                    "source_file": "multiple",
                    "source_location": "L1"
                })
    
    result = {
        "nodes": nodes,
        "edges": edges,
        "hyperedges": hyperedges,
        "input_tokens": 0,
        "output_tokens": 0
    }
    
    with open('.graphify_semantic.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"Created {len(nodes)} nodes, {len(edges)} edges, {len(hyperedges)} hyperedges")
    print("Saved to .graphify_semantic.json")

if __name__ == '__main__':
    main()