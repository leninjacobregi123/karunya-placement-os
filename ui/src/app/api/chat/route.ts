import { NextResponse } from 'next/server';
import { searchKnowledge } from '@/lib/rag/engine';

const OLLAMA_BASE_URL = process.env.OLLAMA_URL || 'http://localhost:11434';
const OLLAMA_URL = `${OLLAMA_BASE_URL}/api/generate`;
const MODEL = 'llama3.2:latest';

export async function POST(request: Request) {
  const { message, context, history } = await request.json();

  // Perform RAG retrieval
  let retrievedContext = '';
  try {
    const searchResults = await searchKnowledge(message);
    retrievedContext = searchResults.map(r => `[Source: ${r.source}]\n${r.content}`).join('\n\n---\n\n');
  } catch (e) {
    console.error('RAG Search Error:', e);
  }

  const systemPrompt = `You are a placement preparation tutor for Karunya Placement OS (KPOS).
Your goal is to help students learn coding and aptitude.
Rules:
1. Never give the full answer immediately.
2. Provide small hints to guide the student.
3. If the student shares code, analyze it for bugs and complexity.
4. Be encouraging and patient.
5. Use the following retrieved knowledge and current lesson context to help the student:

CURRENT LESSON:
${context}

RETRIEVED KNOWLEDGE:
${retrievedContext}`;

  const prompt = `History: ${JSON.stringify(history)}
Student: ${message}
Tutor:`;

  try {
    const res = await fetch(OLLAMA_URL, {
      method: 'POST',
      body: JSON.stringify({
        model: MODEL,
        system: systemPrompt,
        prompt: prompt,
        stream: false,
      }),
    });

    const data = await res.json();
    return NextResponse.json({ response: data.response });
  } catch (e) {
    console.error('Ollama Error:', e);
    return NextResponse.json({ error: 'AI Tutor is offline' }, { status: 503 });
  }
}
