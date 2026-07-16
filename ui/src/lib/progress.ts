import fs from 'fs';
import path from 'path';
import os from 'os';

const KPOS_DIR = path.join(os.homedir(), '.kpos');
const PROGRESS_FILE = path.join(KPOS_DIR, 'student.json');

export interface StudentProgress {
  student_id: string;
  name: string;
  selected_path: string;
  current_day: number;
  days_completed_coding: any[];
  days_completed_aptitude: any[];
  scores: Record<string, any>;
  weak_topics: string[];
  streak: number;
  last_active_day: string | null;
  created_at: string;
}

export function ensureKposDir() {
  if (!fs.existsSync(KPOS_DIR)) {
    fs.mkdirSync(KPOS_DIR, { recursive: true });
  }
}

export function loadProgress(): StudentProgress | null {
  ensureKposDir();
  if (fs.existsSync(PROGRESS_FILE)) {
    try {
      const data = fs.readFileSync(PROGRESS_FILE, 'utf-8');
      return JSON.parse(data);
    } catch (e) {
      console.error('Error loading progress:', e);
      return null;
    }
  }
  return null;
}

export function saveProgress(progress: StudentProgress) {
  ensureKposDir();
  fs.writeFileSync(PROGRESS_FILE, JSON.stringify(progress, null, 2), 'utf-8');
}

export function getProjectRoot() {
  // Assuming the UI is in /root/ui/ and we need access to /root/config/
  return path.join(process.cwd(), '..');
}
