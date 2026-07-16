'use client';

import { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import Editor from '@monaco-editor/react';
import { 
  BookOpen, 
  CheckCircle, 
  ChevronRight, 
  Code, 
  Layout, 
  MessageSquare, 
  Settings, 
  Star,
  Terminal,
  Clock,
  HelpCircle,
  SkipForward,
  Play,
  Save,
  Maximize2
} from 'lucide-react';

export default function Dashboard() {
  const [progress, setProgress] = useState<any>(null);
  const [roadmap, setRoadmap] = useState<any[]>([]);
  const [currentDay, setCurrentDay] = useState<number>(1);
  const [currentPath, setCurrentPath] = useState<string>('full');
  const [content, setContent] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [view, setView] = useState<'lesson' | 'editor'>('lesson');
  const [userCode, setUserCode] = useState<string>('');
  const [consoleOutput, setConsoleOutput] = useState<string>('');
  const [isRunning, setIsRunning] = useState(false);

  // Resizing state
  const [sidebarWidth, setSidebarWidth] = useState(280);
  const [tutorWidth, setTutorWidth] = useState(320);
  const [consoleHeight, setConsoleHeight] = useState(200);
  const [resizing, setResizing] = useState<'sidebar' | 'tutor' | 'console' | null>(null);

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!resizing) return;
      if (resizing === 'sidebar') {
        setSidebarWidth(Math.max(150, Math.min(500, e.clientX)));
      } else if (resizing === 'tutor') {
        setTutorWidth(Math.max(200, Math.min(600, window.innerWidth - e.clientX)));
      } else if (resizing === 'console') {
        setConsoleHeight(Math.max(100, Math.min(600, window.innerHeight - e.clientY)));
      }
    };

    const handleMouseUp = () => setResizing(null);

    if (resizing) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
      document.body.style.cursor = resizing === 'console' ? 'row-resize' : 'col-resize';
    }

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
      document.body.style.cursor = 'default';
    };
  }, [resizing]);

  useEffect(() => {
    fetchInitialData();
  }, []);

  useEffect(() => {
    if (progress) {
      fetchRoadmap(progress.selected_path || 'full');
      setCurrentPath(progress.selected_path || 'full');
      setCurrentDay(progress.current_day || 1);
    }
  }, [progress]);

  useEffect(() => {
    if (roadmap.length > 0) {
      loadDayContent(currentDay);
    }
  }, [currentDay, roadmap]);

  const fetchInitialData = async () => {
    try {
      const res = await fetch('/api/progress');
      const data = await res.json();
      setProgress(data);
    } catch (e) {
      console.error('Failed to fetch progress');
    } finally {
      setLoading(false);
    }
  };

  const createProfile = async (selectedPath: string) => {
    const newProfile = {
      student_id: `local-${Date.now()}`,
      name: '',
      selected_path: selectedPath,
      current_day: 1,
      days_completed_coding: [],
      days_completed_aptitude: [],
      scores: {},
      weak_topics: [],
      streak: 0,
      last_active_day: null,
      created_at: new Date().toISOString(),
    };

    try {
      await fetch('/api/progress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newProfile),
      });
      setProgress(newProfile);
    } catch (e) {
      console.error('Failed to create profile');
    }
  };

  const fetchRoadmap = async (path: string) => {
    try {
      const res = await fetch(`/api/roadmap/${path}`);
      const data = await res.json();
      // Limit to 10 days as per user request
      setRoadmap(data.slice(0, 10));
    } catch (e) {
      console.error('Failed to fetch roadmap');
    }
  };

  const loadDayContent = async (day: number) => {
    const entry = roadmap.find(e => e.sequence === day);
    if (!entry) return;

    const slug = currentPath === 'aptitude-reasoning' ? entry.aptitude_reasoning.slug : 
                 (entry.coding_dsa ? entry.coding_dsa.slug : entry.aptitude_reasoning.slug);
    
    const pathName = currentPath === 'full' ? 'coding-dsa' : currentPath;

    try {
      const res = await fetch(`/api/content/${pathName}/${slug}`);
      const data = await res.json();
      setContent(data);

      // Fetch starter code if it's a coding track
      if (currentPath !== 'aptitude-reasoning' && entry.coding_dsa) {
        const codeRes = await fetch(`/api/code?pathName=coding-dsa&slug=${slug}`);
        const codeData = await codeRes.json();
        setUserCode(codeData.code);
      }
    } catch (e) {
      console.error('Failed to fetch content');
      setContent(null);
    }
  };

  const handleSaveCode = async () => {
    const entry = roadmap.find(e => e.sequence === currentDay);
    if (!entry || !entry.coding_dsa) return;

    try {
      await fetch('/api/code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          pathName: 'coding-dsa',
          slug: entry.coding_dsa.slug,
          code: userCode
        })
      });
    } catch (e) {
      console.error('Failed to save code');
    }
  };

  const handleComplete = async () => {
    const entry = roadmap.find(e => e.sequence === currentDay);
    if (!entry) return;

    const pathName = currentPath === 'full' ? 'coding-dsa' : currentPath;
    
    try {
      const res = await fetch('/api/action', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          action: 'complete',
          day: currentDay,
          pathName
        })
      });
      const data = await res.json();
      if (data.success) {
        setProgress(data.progress);
        if (currentDay < 10) setCurrentDay(currentDay + 1);
      }
    } catch (e) {
      alert('Failed to complete day');
    }
  };

  const handleTestRun = async () => {
    const entry = roadmap.find(e => e.sequence === currentDay);
    if (!entry) return;

    const slug = currentPath === 'aptitude-reasoning' ? entry.aptitude_reasoning.slug : 
                 (entry.coding_dsa ? entry.coding_dsa.slug : entry.aptitude_reasoning.slug);
    const pathName = currentPath === 'full' ? 'coding-dsa' : currentPath;

    try {
      setIsRunning(true);
      setConsoleOutput('Running tests...\n');
      
      // Save first
      await handleSaveCode();

      const res = await fetch('/api/action', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          action: 'test',
          pathName,
          slug
        })
      });
      const data = await res.json();
      setConsoleOutput(data.output || (data.success ? 'All tests passed! ✅' : 'Tests failed with no output. ❌'));
      setView('editor'); // Switch to editor to see the console
    } catch (e) {
      setConsoleOutput('Error: Failed to connect to execution engine.');
    } finally {
      setIsRunning(false);
    }
  };

  const [messages, setMessages] = useState<any[]>([
    { role: 'tutor', text: 'Welcome back! Ready to start today\'s session?' }
  ]);
  const [input, setInput] = useState('');
  const [isChatting, setIsChatting] = useState(false);

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isChatting) return;

    const userMsg = input.trim();
    setInput('');
    setMessages(prev => [...prev, { role: 'user', text: userMsg }]);
    setIsChatting(true);

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userMsg,
          context: content?.readme || 'No context available',
          history: messages.slice(-5)
        })
      });
      const data = await res.json();
      setMessages(prev => [...prev, { role: 'tutor', text: data.response || data.error }]);
    } catch (e) {
      setMessages(prev => [...prev, { role: 'tutor', text: 'Sorry, I am having trouble connecting to my brain.' }]);
    } finally {
      setIsChatting(false);
    }
  };

  if (loading && !progress) return <div className="flex h-screen items-center justify-center bg-black text-blue-500 font-mono">Initializing KPOS Engine...</div>;

  if (!loading && !progress) {
    return (
      <div className="flex h-screen items-center justify-center bg-[#0d1117] text-[#c9d1d9] font-mono">
        <div className="max-w-md w-full mx-auto text-center space-y-6 p-8">
          <Terminal className="mx-auto text-blue-500" size={40} />
          <h1 className="text-xl font-bold text-white">Welcome to KPOS</h1>
          <p className="text-[#8b949e] text-sm">
            No profile found on this machine yet. Pick a track to start your 30-day placement prep.
          </p>
          <div className="space-y-3">
            <button
              onClick={() => createProfile('coding-dsa')}
              className="w-full flex items-center gap-3 p-4 rounded-lg bg-[#161b22] border border-[#30363d] hover:border-blue-500 transition-colors text-left"
            >
              <Code className="text-blue-500 shrink-0" size={20} />
              <div>
                <div className="text-sm font-bold text-white">Coding + DSA</div>
                <div className="text-xs text-[#8b949e]">Python, arrays, algorithms — 30 min/day</div>
              </div>
            </button>
            <button
              onClick={() => createProfile('aptitude-reasoning')}
              className="w-full flex items-center gap-3 p-4 rounded-lg bg-[#161b22] border border-[#30363d] hover:border-blue-500 transition-colors text-left"
            >
              <BookOpen className="text-blue-500 shrink-0" size={20} />
              <div>
                <div className="text-sm font-bold text-white">Aptitude + Reasoning</div>
                <div className="text-xs text-[#8b949e]">Percentages, ratios, logic — 30 min/day</div>
              </div>
            </button>
            <button
              onClick={() => createProfile('full')}
              className="w-full flex items-center gap-3 p-4 rounded-lg bg-[#161b22] border border-[#30363d] hover:border-blue-500 transition-colors text-left"
            >
              <Layout className="text-blue-500 shrink-0" size={20} />
              <div>
                <div className="text-sm font-bold text-white">Full Mode</div>
                <div className="text-xs text-[#8b949e]">Both tracks combined — 60 min/day</div>
              </div>
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className={`flex h-screen bg-[#0d1117] text-[#c9d1d9] overflow-hidden font-mono text-sm ${resizing ? 'select-none' : ''}`}>
      {/* Sidebar - Roadmap Navigator */}
      <div 
        style={{ width: `${sidebarWidth}px`, minWidth: `${sidebarWidth}px` }}
        className="bg-[#161b22] border-r border-[#30363d] flex flex-col relative"
      >
        <div className="p-4 border-b border-[#30363d] flex items-center gap-2">
          <Terminal className="text-blue-500" size={20} />
          <h1 className="font-bold text-base">KPOS Dashboard</h1>
        </div>
        <div className="flex-1 overflow-y-auto p-2 space-y-1">
          {roadmap.map((entry) => (
            <div 
              key={entry.sequence}
              onClick={() => setCurrentDay(entry.sequence)}
              className={`p-3 rounded-md flex items-center gap-3 cursor-pointer transition-colors ${
                currentDay === entry.sequence ? 'bg-[#1f2937] border-l-2 border-blue-500 text-white' : 'hover:bg-[#21262d] text-gray-400'
              }`}
            >
              <div className={`w-6 h-6 rounded-full flex items-center justify-center text-[10px] ${
                progress?.days_completed_coding?.some((d: any) => d.day === entry.sequence) ? 'bg-green-900 text-green-400 border border-green-700' : 'bg-[#30363d] text-gray-500'
              }`}>
                {entry.sequence}
              </div>
              <div className="truncate flex-1">
                <p className="text-xs font-semibold">{currentPath === 'full' ? 'Day ' + entry.sequence : (entry.coding_dsa?.topic || entry.aptitude_reasoning?.topic)}</p>
                {currentPath === 'full' && (
                  <p className="text-[10px] opacity-60 truncate">
                    {entry.coding_dsa?.topic}
                  </p>
                )}
              </div>
            </div>
          ))}
        </div>
        <div className="p-4 border-t border-[#30363d] bg-[#0d1117]">
          <div className="flex justify-between items-center mb-2">
            <span className="text-[10px] text-gray-500">STREAK</span>
            <span className="text-orange-500 flex items-center gap-1"><Star size={12} /> {progress?.streak || 0}</span>
          </div>
          <div className="w-full bg-[#30363d] h-1.5 rounded-full">
            <div 
              className="bg-blue-500 h-1.5 rounded-full transition-all duration-500" 
              style={{ width: `${(progress?.days_completed_coding?.length / 10) * 100}%` }}
            ></div>
          </div>
        </div>
      </div>

      {/* Sidebar Resizer */}
      <div 
        onMouseDown={() => setResizing('sidebar')}
        className={`w-1 hover:w-1.5 transition-all bg-transparent hover:bg-blue-500/50 cursor-col-resize z-10 ${resizing === 'sidebar' ? 'bg-blue-500 w-1.5' : ''}`}
      />

      {/* Main Content Area - Classroom */}
      <div className="flex-1 flex flex-col bg-[#0d1117] overflow-hidden">
        <header className="h-14 border-b border-[#30363d] flex items-center justify-between px-6">
          <div className="flex items-center gap-4">
            <span className="text-gray-500 text-xs">Day {currentDay}</span>
            <ChevronRight size={14} className="text-gray-600" />
            <div className="flex bg-[#161b22] rounded p-0.5 border border-[#30363d]">
              <button 
                onClick={() => setView('lesson')}
                className={`flex items-center gap-2 px-3 py-1 rounded text-[10px] font-bold transition-colors ${view === 'lesson' ? 'bg-[#30363d] text-white' : 'text-gray-500 hover:text-gray-300'}`}
              >
                <BookOpen size={12} /> LESSON
              </button>
              <button 
                onClick={() => setView('editor')}
                className={`flex items-center gap-2 px-3 py-1 rounded text-[10px] font-bold transition-colors ${view === 'editor' ? 'bg-[#30363d] text-white' : 'text-gray-500 hover:text-gray-300'}`}
              >
                <Code size={12} /> EDITOR
              </button>
            </div>
          </div>
          <div className="flex items-center gap-3">
             <button 
               onClick={handleSaveCode}
               className="flex items-center gap-2 px-3 py-1.5 bg-[#21262d] hover:bg-[#30363d] rounded text-[10px] border border-[#30363d] text-gray-300"
             >
               <Save size={12} /> SAVE
             </button>
             <button 
               onClick={handleComplete}
               className="flex items-center gap-2 px-3 py-1.5 bg-blue-600 hover:bg-blue-500 rounded text-[10px] text-white font-bold"
             >
               <CheckCircle size={12} /> COMPLETE
             </button>
          </div>
        </header>
        
        <main className="flex-1 overflow-hidden flex flex-col">
          {view === 'lesson' ? (
            <div className="flex-1 overflow-y-auto p-8 custom-markdown">
              {content ? (
                <div className="max-w-3xl mx-auto prose prose-invert">
                  <ReactMarkdown 
                    components={{
                      h1: ({node, ...props}) => <h1 className="text-2xl font-bold mb-6 text-white border-b border-[#30363d] pb-2" {...props} />,
                      h2: ({node, ...props}) => <h2 className="text-xl font-bold mt-8 mb-4 text-white" {...props} />,
                      p: ({node, ...props}) => <p className="mb-4 leading-relaxed text-gray-300" {...props} />,
                      ul: ({node, ...props}) => <ul className="list-disc ml-5 mb-4 space-y-2 text-gray-300" {...props} />,
                      code: ({node, ...props}) => <code className="bg-[#21262d] px-1.5 py-0.5 rounded text-blue-400" {...props} />,
                      pre: ({node, ...props}) => <pre className="bg-[#161b22] p-4 rounded-lg border border-[#30363d] overflow-x-auto mb-6" {...props} />,
                    }}
                  >
                    {content.readme}
                  </ReactMarkdown>
                  
                  {content.quiz && (
                    <div className="mt-12 p-6 bg-[#161b22] border border-[#30363d] rounded-lg">
                      <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
                        <HelpCircle className="text-blue-500" /> Daily Quiz
                      </h3>
                      <div className="space-y-6">
                        {content.quiz.questions?.map((q: any, i: number) => (
                          <div key={i} className="space-y-3">
                            <p className="font-medium text-sm">{i + 1}. {q.question || q.q}</p>
                            <div className="grid grid-cols-1 gap-2">
                              {q.choices.map((choice: string, ci: number) => (
                                <button 
                                  key={ci}
                                  className="text-left p-3 rounded bg-[#21262d] border border-[#30363d] hover:border-blue-500 transition-colors text-xs"
                                >
                                  {choice}
                                </button>
                              ))}
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              ) : (
                <div className="flex flex-col items-center justify-center h-full text-gray-500">
                   <BookOpen size={48} className="mb-4 opacity-20" />
                   <p>Content Pending...</p>
                </div>
              )}
            </div>
          ) : (
            <div className="flex-1 flex flex-col overflow-hidden">
              <div className="flex-1">
                <Editor
                  height="100%"
                  defaultLanguage="python"
                  theme="vs-dark"
                  value={userCode}
                  onChange={(val) => setUserCode(val || '')}
                  options={{
                    fontSize: 14,
                    fontFamily: 'JetBrains Mono',
                    minimap: { enabled: false },
                    scrollBeyondLastLine: false,
                    padding: { top: 20 },
                  }}
                />
              </div>

              {/* Console Resizer */}
              <div 
                onMouseDown={() => setResizing('console')}
                className={`h-1 hover:h-1.5 transition-all bg-transparent hover:bg-blue-500/50 cursor-row-resize z-10 ${resizing === 'console' ? 'bg-blue-500 h-1.5' : ''}`}
              />

              <div 
                style={{ height: `${consoleHeight}px` }}
                className="border-t border-[#30363d] bg-[#0d1117] flex flex-col"
              >
                <div className="flex items-center justify-between px-4 py-2 bg-[#161b22] border-b border-[#30363d]">
                  <span className="text-[10px] font-bold text-gray-500 flex items-center gap-2 uppercase">
                    <Terminal size={12} /> Output Console
                  </span>
                  <button 
                    onClick={() => setConsoleOutput('')}
                    className="text-[10px] text-gray-500 hover:text-white"
                  >
                    CLEAR
                  </button>
                </div>
                <div className="flex-1 p-4 font-mono text-xs overflow-y-auto whitespace-pre-wrap text-gray-400">
                  {consoleOutput || 'Click "RUN CODE" to see results...'}
                </div>
              </div>
            </div>
          )}
        </main>
      </div>

      {/* Tutor Resizer */}
      <div 
        onMouseDown={() => setResizing('tutor')}
        className={`w-1 hover:w-1.5 transition-all bg-transparent hover:bg-blue-500/50 cursor-col-resize z-10 ${resizing === 'tutor' ? 'bg-blue-500 w-1.5' : ''}`}
      />

      {/* Right Panel - AI Tutor & Activity */}
      <div 
        style={{ width: `${tutorWidth}px`, minWidth: `${tutorWidth}px` }}
        className="bg-[#161b22] border-l border-[#30363d] flex flex-col"
      >
        <div className="p-4 border-b border-[#30363d] flex items-center gap-2">
          <MessageSquare className="text-blue-500" size={18} />
          <h2 className="font-bold uppercase text-xs tracking-wider text-gray-400">AI Tutor</h2>
        </div>
        <div className="flex-1 p-4 overflow-y-auto flex flex-col gap-4">
          {messages.map((msg, i) => (
            <div key={i} className={`${msg.role === 'user' ? 'bg-[#1f2937] border-blue-900 self-end' : 'bg-[#21262d] border-[#30363d] self-start'} p-3 rounded-lg border text-xs max-w-[90%]`}>
              <p className={`${msg.role === 'user' ? 'text-blue-300' : 'text-blue-400'} font-bold mb-1 uppercase tracking-tighter`}>
                {msg.role === 'user' ? 'You' : 'Tutor'}
              </p>
              <p className="leading-relaxed whitespace-pre-wrap">{msg.text}</p>
            </div>
          ))}
          {isChatting && (
            <div className="bg-[#21262d] border-[#30363d] p-3 rounded-lg border text-xs self-start animate-pulse">
              <p className="text-blue-400 font-bold mb-1 uppercase tracking-tighter">Tutor</p>
              <p>Thinking...</p>
            </div>
          )}
        </div>
        <div className="p-4 border-t border-[#30363d] bg-[#0d1117] space-y-3">
          <div className="flex gap-2">
            <button 
              onClick={handleTestRun}
              className="flex-1 flex items-center justify-center gap-2 py-2 bg-[#238636] hover:bg-[#2ea043] rounded text-white text-xs font-bold transition-colors"
            >
              <Code size={14} /> RUN CODE
            </button>
            <button className="px-3 py-2 bg-[#21262d] hover:bg-[#30363d] rounded border border-[#30363d] text-gray-300">
              <HelpCircle size={14} />
            </button>
          </div>
          <form onSubmit={handleSendMessage} className="relative">
            <input 
              type="text" 
              value={input}
              onChange={(e) => setInput(e.target.value)}
              disabled={isChatting}
              placeholder={isChatting ? "Waiting for tutor..." : "Ask for a hint..."} 
              className="w-full bg-[#161b22] border border-[#30363d] rounded p-2 pl-3 text-xs focus:outline-none focus:border-blue-500 transition-colors disabled:opacity-50"
            />
          </form>
        </div>
      </div>
    </div>
  );
}
