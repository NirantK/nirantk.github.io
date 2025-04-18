# WhatsApp Analyzer Web App TODO

## Phase 1: Basic Setup
- [ ] Set up FastHTML project structure
  - [ ] Create main.py with basic FastHTML setup
  - [ ] Add necessary dependencies to requirements.txt
  - [ ] Update README.md with setup instructions

## Phase 2: File Upload Implementation
- [ ] Create file upload form
  - [ ] Add file input with .txt extension validation
  - [ ] Add form submission handler
  - [ ] Implement secure file storage in temp directory
  - [ ] Add file size validation (max 10MB)

## Phase 3: Analysis Options
- [ ] Create analysis options form
  - [ ] Window days input (default: 60)
  - [ ] Exclude/Include contacts toggle
  - [ ] Analysis type selector (single/multiple/score)
  - [ ] Decay days input for scoring (default: 90)
  - [ ] Reference messages input for scoring (default: 5)

## Phase 4: Results Display
- [ ] Create results page
  - [ ] Display analysis results in a table
  - [ ] Add download results as CSV option
  - [ ] Add error handling and user feedback
  - [ ] Implement loading state during analysis

## Phase 5: UI/UX Improvements
- [ ] Add responsive design
  - [ ] Mobile-friendly layout
  - [ ] Progress indicators
  - [ ] Input validation feedback
- [ ] Add help tooltips for options
- [ ] Add example file download

## Phase 6: Security & Optimization
- [ ] Implement file cleanup
  - [ ] Auto-delete uploaded files after analysis
  - [ ] Add rate limiting for uploads
- [ ] Add input sanitization
- [ ] Add error logging 