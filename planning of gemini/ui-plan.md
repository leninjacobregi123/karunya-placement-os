 # KPOS Web UI Implementation Plan (Next.js)
    ## Objective
    To build a modern Web UI for KPOS using a Full TypeScript (Next.js) architecture.
    
    ## Architecture
     - Next.js (App Router) for both Frontend and API.
     - Re-implements Python tracking logic in TypeScript to read/write `~/.kpos/student.json`.
     - Uses Node.js `child_process` to execute local Python tests when needed.
  
   ## Features
    1. **Left Pane:** Roadmap Navigator (reads `config/`).
    2. **Center Pane:** Classroom (Markdown renderer, interactive quizzes, Monaco editor).
    3. **Right Pane:** AI Tutor (chat interface).
   
    ## Phases
    1. Initialize Next.js project.
    2. Build TS utilities for progress tracking.
    3. Build API routes for content and progress.
    4. Implement UI components and Monaco editor.
    5. Integration testing.
