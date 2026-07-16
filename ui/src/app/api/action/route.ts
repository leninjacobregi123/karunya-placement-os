import { NextResponse } from 'next/server';
import { spawn } from 'child_process';
import path from 'path';
import { getProjectRoot, loadProgress, saveProgress } from '@/lib/progress';

export async function POST(request: Request) {
  const body = await request.json();
  const { action, day, pathName, slug } = body;

  if (action === 'test') {
    return handleTest(pathName, slug);
  } else if (action === 'complete') {
    return handleComplete(pathName, day);
  }

  return NextResponse.json({ error: 'Unknown action' }, { status: 400 });
}

async function handleTest(pathName: string, slug: string): Promise<NextResponse> {
  const root = getProjectRoot();
  const contentDir = path.join(root, 'content', pathName === 'coding-dsa' ? 'coding' : 'aptitude', slug, 'code');
  
  return new Promise<NextResponse>((resolve) => {
    const pythonProcess = spawn('python3', ['-m', 'unittest', 'discover', '-p', 'test_*.py'], {
      cwd: contentDir
    });

    let output = '';
    pythonProcess.stdout.on('data', (data) => { output += data.toString(); });
    pythonProcess.stderr.on('data', (data) => { output += data.toString(); });

    pythonProcess.on('close', (code) => {
      resolve(NextResponse.json({ 
        success: code === 0, 
        output 
      }));
    });
  });
}

function handleComplete(pathName: string, day: number): NextResponse {
  const progress = loadProgress();
  if (!progress) return NextResponse.json({ error: 'No progress found' }, { status: 404 });

  const listKey = pathName.includes('coding') ? 'days_completed_coding' : 'days_completed_aptitude';
  
  const currentList = (progress as any)[listKey] || [];
  if (!currentList.some((d: any) => d.day === day)) {
    currentList.push({
      day,
      completed_at: new Date().toISOString()
    });
    (progress as any)[listKey] = currentList;
  }

  if (day + 1 > progress.current_day) {
    progress.current_day = day + 1;
  }

  saveProgress(progress);
  return NextResponse.json({ success: true, progress });
}
