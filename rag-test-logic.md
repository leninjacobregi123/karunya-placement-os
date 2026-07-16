import fs from 'fs';
import path from 'path';

// Manual test script to show RAG results
async function testRAG(query: string) {
  console.log(`\n--- SEARCHING FOR: "${query}" ---`);
  
  const res = await fetch('http://localhost:3000/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message: query,
      context: "Current Day Context Placeholder",
      history: []
    })
  });
  
  const data = await res.json();
  console.log("AI RESPONSE PREVIEW:", data.response.substring(0, 150) + "...");
}

// We'll also test the raw retrieval to see SOURCES
import { searchKnowledge } from './ui/src/lib/rag/engine';

async function runSystematicTest() {
  const queries = [
    "What are prime numbers?",
    "How does a sliding window work?",
    "Tell me about divisibility rules for 6"
  ];

  for (const q of queries) {
    console.log(`\n[QUERY]: ${q}`);
    const results = await searchKnowledge(q, 2);
    results.forEach((r, i) => {
      console.log(`  Result ${i+1} (Score: ${r.similarity.toFixed(4)}):`);
      console.log(`  Source: ${r.source}`);
      console.log(`  Snippet: ${r.content.substring(0, 100).replace(/\n/g, ' ')}...`);
    });
  }
}

// Since we can't easily run TS scripts from root with imports, 
// I will create a temporary standalone JS test script that reads the vectors.json directly.
