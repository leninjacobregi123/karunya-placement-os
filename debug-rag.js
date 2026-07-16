const fs = require('fs');
const path = require('path');

const VECTOR_DB_PATH = path.join(__dirname, 'ui/src/lib/rag/vectors.json');
const OLLAMA_EMBED_URL = 'http://localhost:11434/api/embeddings';
const EMBED_MODEL = 'mxbai-embed-large:latest';

function cosineSimilarity(a, b) {
  if (!a || !b || a.length !== b.length) return 0;
  const dotProduct = a.reduce((sum, val, i) => sum + val * b[i], 0);
  const magA = Math.sqrt(a.reduce((sum, val) => sum + val * val, 0));
  const magB = Math.sqrt(b.reduce((sum, val) => sum + val * val, 0));
  if (magA === 0 || magB === 0) return 0;
  return dotProduct / (magA * magB);
}

async function testRetrieval(query) {
  const db = JSON.parse(fs.readFileSync(VECTOR_DB_PATH, 'utf-8'));
  
  const res = await fetch(OLLAMA_EMBED_URL, {
    method: 'POST',
    body: JSON.stringify({ model: EMBED_MODEL, prompt: query })
  });
  const data = await res.json();
  const queryEmbedding = data.embedding;

  const results = db
    .filter(chunk => chunk.embedding && chunk.embedding.length > 0)
    .map(chunk => ({
      source: chunk.source,
      content: chunk.content,
      similarity: cosineSimilarity(queryEmbedding, chunk.embedding)
    }))
    .sort((a, b) => b.similarity - a.similarity)
    .slice(0, 2);

  console.log(`\nQUERY: "${query}"`);
  results.forEach((r, i) => {
    console.log(`  [MATCH ${i+1}] Score: ${r.similarity.toFixed(4)} | Source: ${r.source}`);
    console.log(`  Snippet: ${r.content.substring(0, 150).replace(/\n/g, ' ')}...`);
  });
}

async function run() {
  console.log("=== KPOS RAG SYSTEMATIC AUDIT ===");
  await testRetrieval("What is the divisibility rule for 11?");
  await testRetrieval("How to count frequencies in a list?");
  await testRetrieval("Can you explain how sliding window works?");
}

run();
