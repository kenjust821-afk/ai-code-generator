import React, { useEffect, useState } from 'react';
import Editor from '@monaco-editor/react';
import { Copy, Check } from 'lucide-react';
import '../styles/CodeEditor.css';

interface CodeEditorProps {
  code: string;
  language: string;
}

const CodeEditor: React.FC<CodeEditorProps> = ({ code, language }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="code-editor-wrapper">
      <div className="editor-toolbar">
        <span className="language-label">{language}</span>
        <button
          onClick={handleCopy}
          className="copy-button"
          title="Copy to clipboard"
        >
          {copied ? (
            <>
              <Check size={18} /> Copied!
            </>
          ) : (
            <>
              <Copy size={18} /> Copy
            </>
          )}
        </button>
      </div>
      <Editor
        height="100%"
        language={getMonacoLanguage(language)}
        value={code}
        options={{
          readOnly: true,
          minimap: { enabled: false },
          fontSize: 14,
          fontFamily: "'Fira Code', monospace",
          scrollBeyondLastLine: false,
          wordWrap: 'on',
        }}
        theme="vs-dark"
      />
    </div>
  );
};

function getMonacoLanguage(language: string): string {
  const languageMap: Record<string, string> = {
    python: 'python',
    javascript: 'javascript',
    typescript: 'typescript',
    java: 'java',
    cpp: 'cpp',
    csharp: 'csharp',
    go: 'go',
    rust: 'rust',
    php: 'php',
    ruby: 'ruby',
    kotlin: 'kotlin',
    swift: 'swift',
    html: 'html',
    css: 'css',
    sql: 'sql',
  };
  return languageMap[language.toLowerCase()] || 'plaintext';
}

export default CodeEditor;
