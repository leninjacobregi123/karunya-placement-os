import { NextResponse } from 'next/server';
import { indexKnowledgeBase } from '@/lib/rag/engine';

export async function POST() {
  try {
    const count = await indexKnowledgeBase();
    return NextResponse.json({ success: true, count });
  } catch (e) {
    console.error('Indexing error:', e);
    return NextResponse.json({ error: 'Failed to index knowledge base' }, { status: 500 });
  }
}
