import fs from 'fs';
import path from 'path';
import { getProjectRoot } from './progress';

export function loadRoadmap(pathName: string) {
  const root = getProjectRoot();
  const roadmapFile = path.join(root, 'config', `roadmap-${pathName}-30-days.json`);
  if (fs.existsSync(roadmapFile)) {
    return JSON.parse(fs.readFileSync(roadmapFile, 'utf-8'));
  }
  return null;
}

export function loadContent(pathName: string, slug: string) {
  const root = getProjectRoot();
  const contentDir = path.join(root, 'content', pathName === 'coding-dsa' ? 'coding' : 'aptitude', slug);
  
  if (!fs.existsSync(contentDir)) return null;

  const readmePath = path.join(contentDir, 'README.md');
  const quizPath = path.join(contentDir, 'quiz.json');
  
  const result: any = {
    slug,
    readme: fs.existsSync(readmePath) ? fs.readFileSync(readmePath, 'utf-8') : '',
    quiz: fs.existsSync(quizPath) ? JSON.parse(fs.readFileSync(quizPath, 'utf-8')) : null,
  };

  return result;
}
