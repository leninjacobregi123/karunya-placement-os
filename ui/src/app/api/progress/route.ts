import { NextResponse } from 'next/server';
import { loadProgress, saveProgress } from '@/lib/progress';

export async function GET() {
  const progress = loadProgress();
  return NextResponse.json(progress);
}

export async function POST(request: Request) {
  const body = await request.json();
  saveProgress(body);
  return NextResponse.json({ success: true });
}
