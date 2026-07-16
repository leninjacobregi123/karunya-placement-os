import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';
import { getProjectRoot } from '@/lib/progress';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const pathName = searchParams.get('pathName');
  const slug = searchParams.get('slug');

  if (!pathName || !slug) {
    return NextResponse.json({ error: 'Missing parameters' }, { status: 400 });
  }

  const root = getProjectRoot();
  const starterFile = path.join(
    root, 
    'content', 
    pathName === 'coding-dsa' ? 'coding' : 'aptitude', 
    slug, 
    'code', 
    'starter.py'
  );

  if (!fs.existsSync(starterFile)) {
    return NextResponse.json({ code: '# No starter code found for this topic.' });
  }

  const code = fs.readFileSync(starterFile, 'utf-8');
  return NextResponse.json({ code });
}

export async function POST(request: Request) {
  const body = await request.json();
  const { pathName, slug, code } = body;

  if (!pathName || !slug || code === undefined) {
    return NextResponse.json({ error: 'Missing parameters' }, { status: 400 });
  }

  const root = getProjectRoot();
  const starterFile = path.join(
    root, 
    'content', 
    pathName === 'coding-dsa' ? 'coding' : 'aptitude', 
    slug, 
    'code', 
    'starter.py'
  );

  try {
    // Ensure the code directory exists
    const codeDir = path.dirname(starterFile);
    if (!fs.existsSync(codeDir)) {
      fs.mkdirSync(codeDir, { recursive: true });
    }
    
    fs.writeFileSync(starterFile, code, 'utf-8');
    return NextResponse.json({ success: true });
  } catch (e) {
    console.error('Error saving code:', e);
    return NextResponse.json({ error: 'Failed to save code' }, { status: 500 });
  }
}
