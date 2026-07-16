import { NextResponse } from 'next/server';
import { loadRoadmap } from '@/lib/curriculum';

export async function GET(
  request: Request,
  { params }: { params: Promise<{ path: string }> }
) {
  const { path } = await params;
  const roadmap = loadRoadmap(path);
  if (!roadmap) {
    return NextResponse.json({ error: 'Roadmap not found' }, { status: 404 });
  }
  return NextResponse.json(roadmap);
}
