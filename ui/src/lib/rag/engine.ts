import fs from 'fs';
import path from 'path';
import { getProjectRoot } from '../progress';

const OLLAMA_BASE_URL = process.env.OLLAMA_URL || 'http://localhost:11434';
const OLLAMA_EMBED_URL = `${OLLAMA_BASE_URL}/api/embeddings`;
const EMBED_MODEL = 'mxbai-embed-large:latest';
const VECTOR_DB_PATH = path.join(process.cwd(), 'src/lib/rag/vectors.json');

interface KnowledgeChunk {
  id: string;
  content: string;
  source: string;
  embedding: number[];
}

export async function indexKnowledgeBase() {
  const root = getProjectRoot();
  const chunks: { content: string; source: string }[] = [];

  // Index Curriculum (only the 10 days we decided to keep)
  const paths = [
    { type: 'coding', dir: 'content/coding' },
    { type: 'aptitude', dir: 'content/aptitude' }
  ];

  for (const p of paths) {
    const fullDir = path.join(root, p.dir);
    if (!fs.existsSync(fullDir)) continue;
    
    const folders = fs.readdirSync(fullDir);
    for (const folder of folders) {
      const readme = path.join(fullDir, folder, 'README.md');
      if (fs.existsSync(readme)) {
        chunks.push({
          content: fs.readFileSync(readme, 'utf-8'),
          source: `${p.type}: ${folder}`
        });
      }
    }
  }

  const vectors: KnowledgeChunk[] = [];
  console.log(`Indexing ${chunks.length} chunks...`);

  for (let i = 0; i < chunks.length; i++) {
    const chunk = chunks[i];
    try {
      const res = await fetch(OLLAMA_EMBED_URL, {
        method: 'POST',
        body: JSON.stringify({ model: EMBED_MODEL, prompt: chunk.content })
      });
      const data = await res.json();
      
      if (data.embedding && Array.isArray(data.embedding)) {
        vectors.push({
          id: `chunk-${i}`,
          content: chunk.content,
          source: chunk.source,
          embedding: data.embedding
        });
        console.log(`[OK] Indexed ${chunk.source}`);
      } else {
        console.warn(`[WARN] No embedding for ${chunk.source}`);
      }
    } catch (e) {
      console.error(`[ERROR] Failed to embed ${chunk.source}:`, e);
    }
  }

  fs.writeFileSync(VECTOR_DB_PATH, JSON.stringify(vectors, null, 2));
  return vectors.length;
}

function cosineSimilarity(a: number[], b: number[]) {
  if (!a || !b || a.length !== b.length) return 0;
  const dotProduct = a.reduce((sum, val, i) => sum + val * b[i], 0);
  const magA = Math.sqrt(a.reduce((sum, val) => sum + val * val, 0));
  const magB = Math.sqrt(b.reduce((sum, val) => sum + val * val, 0));
  if (magA === 0 || magB === 0) return 0;
  return dotProduct / (magA * magB);
}

export async function searchKnowledge(query: string, limit = 3) {
  if (!fs.existsSync(VECTOR_DB_PATH)) {
    await indexKnowledgeBase();
  }

  const db: KnowledgeChunk[] = JSON.parse(fs.readFileSync(VECTOR_DB_PATH, 'utf-8'));
  
  const res = await fetch(OLLAMA_EMBED_URL, {
    method: 'POST',
    body: JSON.stringify({ model: EMBED_MODEL, prompt: query })
  });
  const queryEmbedding = (await res.json()).embedding;

  const results = db
    .filter(chunk => chunk.embedding && chunk.embedding.length > 0)
    .map(chunk => ({
      source: chunk.source,
      content: chunk.content,
      similarity: cosineSimilarity(queryEmbedding, chunk.embedding)
    }))
    .sort((a, b) => b.similarity - a.similarity)
    .slice(0, limit);

  return results;
}
