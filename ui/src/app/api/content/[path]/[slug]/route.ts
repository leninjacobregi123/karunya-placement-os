import { NextResponse } from 'next/server';
import { loadContent } from '@/lib/curriculum';

export async function GET(
  request: Request,
  { params }: { params: Promise<{ path: string; slug: string }> }
) {
  const { path, slug } = await params;
  const content = loadContent(path, slug);
  if (!content) {
    return NextResponse.json({ error: 'Content not found' }, { status: 404 });
  }
  return NextResponse.json(content);
}
